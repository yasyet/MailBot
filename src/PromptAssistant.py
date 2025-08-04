
# This script automatically replaces variables from a prompt with the prospects data.

# Importing necessary libraries
import Libraries.FileService as fservice
import Libraries.SheetService as sservice
from Libraries.SheetService import Contact
import pyperclip

# Generating prompt function
def generatePrompt(contact: Contact):
    prompt = f"""Anweisung: Du bist ein Experte für B2B-Vertriebstexte. Deine Aufgabe ist es, eine hochgradig personalisierte Kaltakquise-E-Mail zu verfassen. Die E-Mail muss kurz, prägnant und überzeugend sein und auf den unten stehenden Informationen basieren.
Kontext über mich (den Absender):
Mein Unternehmen: Nexlead
Meine Dienstleistung: Ich übernehme die Kaltakquise für SaaS-Firmen. Mein Prozess ist:
Lead-Generierung: Ich finde und verifiziere hunderte idealer Kunden.
Outreach: Ich kontaktiere sie mit personalisierten E-Mails und Follow-ups.
Terminbuchung: Ich analysiere die Antworten und buche qualifizierte Meetings direkt in den Kalender meiner Kunden.
Mein Nutzenversprechen (USP): Meine Kunden bekommen eine planbare Sales-Pipeline und mehr Umsatz, sparen sich aber die hohen Kosten (ca. 60-80k €/Jahr) und den Aufwand für den Aufbau eines eigenen Vertriebsteams (SDR-Team). Ich spare dem Gründer wertvolle Zeit.
Typischer Schmerzpunkt meiner Kunden: Gründer von SaaS-Firmen (besonders in der Wachstumsphase) haben keine Zeit für systematischen Vertrieb, da sie alles selbst machen (der "Chief Everything Officer"). Sie stehen unter Druck, planbaren Umsatz zu generieren, haben aber oft keine Lust auf oder Angst vor Kaltakquise.
Suche wenn möglich detaillierten Schmerzpunkte die personalisiert and die Firma angepasst sind
Variable Informationen (für jede E-Mail neu ausfüllen):
Unternehmen des Empfängers: {contact.Company}
Name des Ansprechpartners: {contact.FirstName} {contact.LastName}
Persönlicher Anknüpfungspunkt: Mach sie selber. Sie soll höchst personalisiert sein. Mach eine kurze recherche zu kürzlichen Signalen der Firma.
Mein Name: Yasin Holzenkämpfer
Mein LinkedIn-Profil: Gerade nicht verfügbar lass es frei
Deine Aufgabe:
Schreibe jetzt die vollständige E-Mail. Halte dich exakt an diese Struktur und Tonalität:
Betreff: Wähle einen kurzen, direkten Betreff wie "Planbare Neukunden für [Unternehmen des Empfängers]" oder formuliere einen, der direkt auf den persönlichen Anknüpfungspunkt Bezug nimmt.
Anrede: Beginne mit "Hallo [Name des Ansprechpartners],".
Einleitung (1-2 Sätze): Starte direkt mit dem persönlichen Anknüpfungspunkt. Formuliere ihn als authentische, positive Beobachtung. Zeige, dass dies keine Massen-E-Mail ist.
Übergang zum Problem (1-2 Sätze): Baue eine Brücke von deiner Einleitung zum typischen Schmerzpunkt. Sprich die Zeitknappheit oder die Doppelrolle des Gründers ("Chief Everything Officer") an.
Lösung (2-3 Sätze): Stelle "Nexlead" als logische Lösung vor. Beschreibe kurz den 3-Stufen-Prozess (Leads finden, Outreach machen, Termine buchen).
Nutzen (1 Satz): Fasse das Endergebnis zusammen: eine messbare Sales-Pipeline ohne die Kosten und den Aufwand eines Inhouse-Teams.
Call to Action (1 Satz): Stelle eine einfache, zeitlich begrenzte Frage, um die Hürde für eine Antwort zu senken. ("Hätten Sie nächste Woche 15 Minuten Zeit für ein kurzes Gespräch?").
Abschluss: Beende mit "Beste Grüße" und meiner Signatur.
Die E-Mail muss professionell, aber menschlich klingen und darf nicht länger als ca. 150 Wörter sein.
"""

    return prompt.strip()

# Opening the csv file and converting it to contacts
csv_file_path = fservice.askOpenFile()
contacts = sservice.convertCSVPathToContacts(csv_file_path)

# Keeps asking the user for a index or he enters 'exit' to stop the program
while True:
    index = input("Enter the index of the contact to generate a prompt (or 'exit' to stop): ")
    if index.lower() == 'exit':
        break
    try:
        index = int(index)
        if 0 <= index < len(contacts):
            contact = contacts[index]
            prompt = generatePrompt(contact)
            print(f"Generated prompt for {contact.FirstName} {contact.LastName}:\n")
            print("Prompt copied to clipboard.")
            pyperclip.copy(prompt)  # Copy the prompt to clipboard
        else:
            print("Index out of range. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid index or 'exit'.")