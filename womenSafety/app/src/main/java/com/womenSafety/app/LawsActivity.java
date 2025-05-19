package com.womenSafety.app;

import android.os.Bundle;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

public class LawsActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_laws);

        TextView lawsTextView = findViewById(R.id.laws_text);
        lawsTextView.setText("Important Women and Girl Child Safety Laws in India:\n\n" +
    "1. Nirbhaya Act, 2013\n" +
    "Strengthened punishments for crimes like rape and acid attacks. Introduced fast-track courts for speedy justice. Empowered victims with better police accountability.\n\n" +

    "2. Criminal Law (Amendment) Act, 2018\n" +
    "Mandates death penalty for rape of girls below 12 years. Reduces time for investigation and trial. Enhances punishments for gang rape.\n\n" +

    "3. Protection of Women from Domestic Violence Act, 2005\n" +
    "Covers physical, emotional, sexual, and financial abuse. Provides immediate relief like protection orders and shelter. Empowers women to seek help without delay.\n\n" +

    "4. Sexual Harassment of Women at Workplace Act, 2013\n" +
    "Protects women from harassment at the workplace. Makes Internal Complaints Committees mandatory. Covers both organized and unorganized sectors.\n\n" +

    "5. Section 498A IPC - Cruelty by Husband or Relatives\n" +
    "Addresses domestic cruelty by husband or in-laws. Includes harassment for dowry. Considered a non-bailable offense to protect the victim.\n\n" +

    "6. Section 354 IPC - Assault on Women\n" +
    "Covers assault with intent to outrage modesty. Includes stalking, voyeurism, and physical attacks. Punishable with imprisonment and fine.\n\n" +

    "7. Section 375 IPC - Rape\n" +
    "Defines rape and outlines different circumstances under which it occurs. Includes marital rape under certain conditions. Punishable with rigorous imprisonment.\n\n" +

    "8. Section 509 IPC - Insulting Modesty of a Woman\n" +
    "Covers verbal abuse, gestures, and acts intended to insult a woman's modesty. Applies to both public and private scenarios. Punishable with imprisonment and fine.\n\n" +

    "9. POCSO Act, 2012 (Protection of Children from Sexual Offences)\n" +
    "Specifically protects minors below 18 years. Covers abuse, harassment, and child pornography. Ensures child-friendly legal procedures.\n\n" +

    "10. Child Marriage Restraint Act / Prohibition of Child Marriage Act, 2006\n" +
    "Prohibits marriage of girls below 18. Makes child marriage voidable at the option of the minor. Punishable for guardians and parties involved.\n\n" +

    "11. Immoral Traffic (Prevention) Act, 1956\n" +
    "Targets human trafficking and sexual exploitation. Provides rescue and rehabilitation of victims. Criminalizes running or managing brothels.\n\n" +

    "12. Medical Termination of Pregnancy (Amendment) Act, 2021\n" +
    "Allows safe and legal abortion up to 24 weeks for special categories. Ensures privacy and consent. Empowers women with reproductive rights.\n\n" +

    "13. Indecent Representation of Women (Prohibition) Act, 1986\n" +
    "Prohibits derogatory depiction of women in ads, publications, or media. Penalizes those involved in printing, publishing, or distributing such content.\n\n" +

    "14. Dowry Prohibition Act, 1961\n" +
    "Makes giving or taking dowry a punishable offense. Applies before, during, or after marriage. Aimed at protecting women from harassment or death due to dowry.\n\n" +

    "15. The Equal Remuneration Act, 1976\n" +
    "Ensures equal pay for equal work for men and women. Prohibits discrimination during recruitment and service conditions.\n\n" +

    "Note: Awareness of these laws is the first step toward safety and empowerment.");

    }
}
