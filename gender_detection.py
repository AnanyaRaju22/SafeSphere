from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os
import cvlib as cv
import pyttsx3
import time
import csv
from datetime import datetime

# Load model
model = load_model(r'D:\Emergency\Women-Safety-App\gender_detection.h5')

# Log file path
log_file = 'gender_detection_log.csv'

# Create the file with headers if it doesn't exist
if not os.path.exists(log_file):
    with open(log_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp', 'Gender', 'Confidence'])

# Initialize TTS engine
engine = pyttsx3.init()

# Initialize tracking variables
gender_start_time = None
last_gender = None
last_announcement_time = 0
danger_start_time = None
last_danger_announcement_time = 0

# Open webcam
webcam = cv2.VideoCapture(0)

# Classes
classes = ['men', 'women']

# Main loop
while webcam.isOpened():
    men_count = 0
    women_count = 0
    status, frame = webcam.read()
    if not status:
        break

    face, confidence = cv.detect_face(frame)

    # Loop through detected faces
    for idx, f in enumerate(face):
        (startX, startY) = f[0], f[1]
        (endX, endY) = f[2], f[3]

        face_crop = np.copy(frame[startY:endY, startX:endX])
        if face_crop.shape[0] < 10 or face_crop.shape[1] < 10:
            continue

        face_crop = cv2.resize(face_crop, (96, 96))
        face_crop = face_crop.astype("float") / 255.0
        face_crop = img_to_array(face_crop)
        face_crop = np.expand_dims(face_crop, axis=0)

        conf = model.predict(face_crop)[0]
        idx = np.argmax(conf)
        label = classes[idx]

        if label == 'men':
            men_count += 1
        else:
            women_count += 1

        predicted_gender = label
        current_time = time.time()

        if predicted_gender == last_gender:
            if gender_start_time is None:
                gender_start_time = current_time
        else:
            last_gender = predicted_gender
            gender_start_time = current_time
        gender_duration = current_time - gender_start_time if gender_start_time else 0

        if predicted_gender == "women":
            if last_announcement_time == 0:
                engine.say("Lone Woman detected")
                engine.runAndWait()
                last_announcement_time = current_time
            elif gender_duration >= 5 and current_time - last_announcement_time >= 5:
                engine.say("Lone Woman detected")
                engine.runAndWait()
                last_announcement_time = current_time

        label_display = "{}: {:.2f}%".format(label, conf[idx] * 100)

        # Log gender prediction
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, label, f"{conf[idx] * 100:.2f}"])

        # Draw bounding box and label
        Y = startY - 10 if startY - 10 > 10 else startY + 10
        if label == 'women':
            box_color = (0, 255, 0)
            text_color = (0, 255, 0)
        else:
            box_color = (255, 0, 0)
            text_color = (255, 0, 0)

        cv2.rectangle(frame, (startX, startY), (endX, endY), box_color, 2)
        cv2.putText(frame, label_display, (startX, Y), cv2.FONT_HERSHEY_SIMPLEX,
                    0.7, text_color, 2)

    # ✅ Danger condition check (moved outside face loop)
    current_time = time.time()
    if women_count == 1 and men_count >= 2:
        if danger_start_time is None:
            danger_start_time = current_time
        danger_duration = current_time - danger_start_time

        if danger_duration >= 2 and current_time - last_danger_announcement_time >= 2:
            engine.say("Potential danger")
            engine.runAndWait()
            last_danger_announcement_time = current_time
    else:
        danger_start_time = None

    # Draw gender count
    count_text = f"Men: {men_count}  Women: {women_count}"
    cv2.putText(frame, count_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 0), 2)

    # Show output
    cv2.imshow("gender detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release
webcam.release()
cv2.destroyAllWindows()
