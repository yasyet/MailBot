# --//[ESSENTIAL IMPORTS]\\--
from typing import Tuple

# --//[TEMPLATE API]\\--
def get_initial_email_template(variant: int) -> Tuple[str, str]:
    if variant == 1:
        return initial_email_variant_one
    elif variant == 2:
        return initial_email_variant_two
    elif variant == 3:
        return initial_email_variant_three
    elif variant == 4:
        return initial_email_variant_four
    elif variant == 5:
        return initial_email_variant_five
    else:
        raise ValueError("Invalid template number.")
    
def get_follow_up_one_template(variant: int) -> Tuple[str, str]:
    if variant == 1:
        return follow_up_one_variant_one
    elif variant == 2:
        return follow_up_one_variant_two
    elif variant == 3:
        return follow_up_one_variant_three
    elif variant == 4:
        return follow_up_one_variant_four
    elif variant == 5:
        return follow_up_one_variant_five
    else:
        raise ValueError("Invalid variant number.")
    
def get_follow_up_two_template(variant: int) -> Tuple[str, str]:
    if variant == 1:
        return follow_up_two_variant_one
    elif variant == 2:
        return follow_up_two_variant_two
    elif variant == 3:
        return follow_up_two_variant_three
    elif variant == 4:
        return follow_up_two_variant_four
    elif variant == 5:
        return follow_up_two_variant_five
    else:
        raise ValueError("Invalid variant number.")

# --//[INITIAL EMAIL TEMPLATES]\\--
def initial_email_variant_one(sender_name: str, recipient_name: str, company_name: str, discovery_method: str, linkedin_profile_link: str) -> Tuple[str, str]:
    """
    Initial email template 1/5.
    Args:
        sender_name (str): The name of the sender (e.g., "Yasin Holzenkaempfer").
        recipient_name (str): The last name of the recipient.
        company_name (str): The name of the recipient's company.
        discovery_method (str): How you became aware of the person/company.
        linkedin_profile_link (str): Your LinkedIn profile URL.
    Returns:
        Tuple[str, str]: A tuple containing the subject and the HTML body of the email.
    """
    subject = f"Ihr Vertrieb: Von neuen Leads zur vollen Pipeline ({company_name})"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
        .footer {{ font-size: 0.9em; color: #777; margin-top: 20px; border-top: 1px solid #eee; padding-top: 10px; }}
    </style>
    </head>
    <body>
    <div class="container">
        <p>Sehr geehrte/r Herr/Frau {recipient_name},</p>
        <p>Ich bin auf Sie aufmerksam geworden, weil {discovery_method}.</p>
        <p>Mein Name ist {sender_name}. Ich bin darauf spezialisiert, deutschen B2B-Unternehmen wie Ihrem dabei zu helfen, nicht nur qualifizierte Leads zu finden, sondern diese auch direkt in gebuchte Termine für Ihren Vertrieb zu verwandeln. Kurz gesagt: Ich baue Ihre <strong>Vertriebspipeline komplett auf</strong>, von der ersten Kontaktaufnahme bis zum fixen Gespräch.</p>
        <p>Ich bin überzeugt, dass ich Ihnen innerhalb von 72 Stunden nicht nur eine Liste mit potenziellen Neukunden liefern, sondern auch die ersten Schritte zur Terminbuchung für Sie einleiten kann.</p>
        <p>Um den Wert meiner Arbeit zu demonstrieren, würde ich Ihnen gerne eine <strong>kostenlose und unverbindliche Probe von 10 Kontakten</strong> aus Ihrer Zielbranche erstellen und kurz erläutern, wie ich daraus Termine für Sie generiere.</p>
        <p>Wäre ein 15-minütiges Gespräch dazu nächste Woche für Sie interessant?</p>
        <p>Mit freundlichen Grüßen,</p>
        <p>{sender_name}<br>
        <a href="{linkedin_profile_link}">Mein LinkedIn-Profil</a></p>
    </div>
    </body>
    </html>
    """
    return subject, body

def initial_email_variant_two(sender_name: str, recipient_name: str, discovery_method: str, linkedin_profile_link: str) -> Tuple[str, str]:
    """
    Initial email template 2/5.
    Args:
        sender_name (str): The name of the sender (e.g., "Yasin Holzenkaempfer").
        recipient_name (str): The last name of the recipient.
        discovery_method (str): How you became aware of the person/company.
        linkedin_profile_link (str): Your LinkedIn profile URL.
    Returns:
        Tuple[str, str]: A tuple containing the subject and the HTML body of the email.
    """
    subject = f"Neue Kunden, fix & fertig: Eine Frage an {recipient_name}"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
        .footer {{ font-size: 0.9em; color: #777; margin-top: 20px; border-top: 1px solid #eee; padding-top: 10px; }}
    </style>
    </head>
    <body>
    <div class="container">
        <p>Guten Tag Herr/Frau {recipient_name},</p>
        <p>{discovery_method}.</p>
        <p>Mein Name ist {sender_name} und ich unterstütze B2B-Unternehmen dabei, ihre Neukundengewinnung zu optimieren – und zwar vom ersten Kontakt bis zum fertigen Termin in Ihrem Kalender. Sie erhalten nicht nur Leads, sondern <strong>fertige Vertriebschancen</strong>.</p>
        <p>Ich kann Ihnen innerhalb von 72 Stunden eine qualifizierte Lead-Liste zur Verfügung stellen und zeige Ihnen gerne, wie ich für Sie die <strong>Terminbuchung übernehme</strong>.</p>
        <p>Um Ihnen zu zeigen, wie das funktioniert, biete ich Ihnen gerne eine kostenlose Probe von <strong>10 passenden Kontakten</strong> aus Ihrer Branche an.</p>
        <p>Haben Sie nächste Woche 15 Minuten Zeit für einen kurzen Austausch, wie wir Ihre Pipeline füllen können?</p>
        <p>Herzliche Grüße,</p>
        <p>{sender_name}<br>
        <a href="{linkedin_profile_link}">Mein LinkedIn-Profil</a></p>
    </div>
    </body>
    </html>
    """
    return subject, body

def initial_email_variant_three(sender_name: str, recipient_name: str, discovery_method: str, linkedin_profile_link: str) -> Tuple[str, str]:
    """
    Initial email template 3/5.
    Args:
        sender_name (str): The name of the sender (e.g., "Yasin Holzenkaempfer").
        recipient_name (str): The last name of the recipient.
        discovery_method (str): How you became aware of the person/company.
        linkedin_profile_link (str): Your LinkedIn profile URL.
    Returns:
        Tuple[str, str]: A tuple containing the subject and the HTML body of the email.
    """
    subject = f"Direkte Termine für Ihren Vertrieb durch Lead-Spezialist {sender_name}"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
        .footer {{ font-size: 0.9em; color: #777; margin-top: 20px; border-top: 1px solid #eee; padding-top: 10px; }}
    </style>
    </head>
    <body>
    <div class="container">
        <p>Hallo Herr/Frau {recipient_name},</p>
        <p>{discovery_method}.</p>
        <p>Mein Name ist {sender_name}. Ich helfe Unternehmen im deutschen Mittelstand dabei, ihre Vertriebspipeline mit hochwertigen B2B-Leads zu füllen <strong>und direkt qualifizierte Termine für sie zu buchen</strong>. Sie können sich auf das Verkaufsgespräch konzentrieren, den Rest erledige ich.</p>
        <p>Ich bin zuversichtlich, Ihnen innerhalb von 72 Stunden eine Liste mit potenziellen Neukunden bereitstellen zu können und Ihnen den Prozess der <strong>Terminvereinbarung</strong> zu erläutern.</p>
        <p>Damit Sie sich von der Qualität meiner Arbeit überzeugen können, erstelle ich Ihnen gerne eine <strong>kostenlose und unverbindliche Liste mit 10 relevanten Kontakten</strong>.</p>
        <p>Würden Sie diese gerne nächste Woche in einem kurzen Gespräch dazu besprechen, wie ich Ihnen die Termine bringe?</p>
        <p>Beste Grüße,</p>
        <p>{sender_name}<br>
        <a href="{linkedin_profile_link}">Mein LinkedIn-Profil</a></p>
    </div>
    </body>
    </html>
    """
    return subject, body

def initial_email_variant_four(sender_name: str, recipient_name: str, company_name: str, discovery_method: str, linkedin_profile_link: str) -> Tuple[str, str]:
    """
    Initial email template 4/5.
    Args:
        sender_name (str): The name of the sender (e.g., "Yasin Holzenkaempfer").
        recipient_name (str): The last name of the recipient.
        company_name (str): The name of the recipient's company.
        discovery_method (str): How you became aware of the person/company.
        linkedin_profile_link (str): Your LinkedIn profile URL.
    Returns:
        Tuple[str, str]: A tuple containing the subject and the HTML body of the email.
    """
    subject = f"So füllen Sie Ihren Kalender mit Neukundenterminen – {company_name}"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
        .footer {{ font-size: 0.9em; color: #777; margin-top: 20px; border-top: 1px solid #eee; padding-top: 10px; }}
    </style>
    </head>
    <body>
    <div class="container">
        <p>Sehr geehrte/r Herr/Frau {recipient_name},</p>
        <p>{discovery_method}.</p>
        <p>Als Spezialist für B2B-Lead-Generierung unterstütze ich deutsche Unternehmen dabei, kontinuierlich neue Geschäftskontakte zu gewinnen und diese <strong>direkt in Ihren Vertriebskalender zu buchen</strong>. Mein Service umfasst die komplette Strecke vom ersten Kontakt bis zum vereinbarten Termin.</p>
        <p>Ich kann Ihnen versichern, dass ich Ihnen innerhalb von 72 Stunden eine maßgeschneiderte Liste mit potenziellen Neukunden liefern und Ihnen erklären kann, wie ich die <strong>Terminfindung für Sie übernehme</strong>.</p>
        <p>Um Ihnen einen Eindruck zu verschaffen, biete ich Ihnen eine kostenlose Testliste von <strong>10 Kontakten</strong> aus Ihrem Zielmarkt an.</p>
        <p>Lassen Sie uns kurz telefonieren, um das zu besprechen – vielleicht nächste Woche für 15 Minuten?</p>
        <p>Mit freundlichen Grüßen,</p>
        <p>{sender_name}<br>
        <a href="{linkedin_profile_link}">Mein LinkedIn-Profil</a></p>
    </div>
    </body>
    </html>
    """
    return subject, body

def initial_email_variant_five(sender_name: str, recipient_name: str, company_name: str, discovery_method: str, linkedin_profile_link: str) -> Tuple[str, str]:
    """
    Initial email template 5/5.
    Args:
        sender_name (str): The name of the sender (e.g., "Yasin Holzenkaempfer").
        recipient_name (str): The last name of the recipient.
        company_name (str): The name of the recipient's company.
        discovery_method (str): How you became aware of the person/company.
        linkedin_profile_link (str): Your LinkedIn profile URL.
    Returns:
        Tuple[str, str]: A tuple containing the subject and the HTML body of the email.
    """
    subject = f"Wie {company_name} mehr Termine mit qualifizierten Leads erhalten könnte"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
        .footer {{ font-size: 0.9em; color: #777; margin-top: 20px; border-top: 1px solid #eee; padding-top: 10px; }}
    </style>
    </head>
    <body>
    <div class="container">
        <p>Guten Tag Herr/Frau {recipient_name},</p>
        <p>{discovery_method}.</p>
        <p>Mein Name ist {sender_name}. Ich konzentriere mich darauf, deutschen B2B-Unternehmen wie Ihrem dabei zu helfen, systematisch neue Leads zu generieren <strong>und daraus direkt qualifizierte Termine für Ihr Vertriebsteam zu buchen</strong>. Sie erhalten von mir nicht nur Daten, sondern messbare Ergebnisse in Ihrem Kalender.</p>
        <p>Ich bin überzeugt, Ihnen innerhalb von nur 72 Stunden eine Liste mit qualifizierten Neukundenkontakten bereitstellen und Ihnen den gesamten Prozess der <strong>Terminbuchung für Sie abnehmen</strong> zu können.</p>
        <p>Um Ihnen dies zu beweisen, biete ich Ihnen an, eine <strong>kostenlose und völlig unverbindliche Testliste von 10 relevanten Kontakten</strong> für Sie zu erstellen.</p>
        <p>Gibt es nächste Woche eine kurze Gelegenheit (ca. 15 Minuten), um dies zu erörtern?</p>
        <p>Viele Grüße,</p>
        <p>{sender_name}<br>
        <a href="{linkedin_profile_link}">Mein LinkedIn-Profil</a></p>
    </div>
    </body>
    </html>
    """
    return subject, body


# --//[FOLLOW UP ONE EMAIL TEMPLATES]\\--
def follow_up_one_variant_one(sender_name: str, recipient_name: str, company_name: str, initial_send_date: str, linkedin_profile_link: str) -> Tuple[str, str]:
    """
    Follow-up 1, variant 1/5.
    Args:
        sender_name (str): The name of the sender (e.g., "Yasin Holzenkaempfer").
        recipient_name (str): The last name of the recipient.
        company_name (str): The name of the recipient's company.
        initial_send_date (str): The date the initial email was sent.
        linkedin_profile_link (str): Your LinkedIn profile URL.
    Returns:
        Tuple[str, str]: A tuple containing the subject and the HTML body of the email.
    """
    subject = f"AW: Ihr Vertrieb: Von neuen Leads zur vollen Pipeline ({company_name})"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
        .footer {{ font-size: 0.9em; color: #777; margin-top: 20px; border-top: 1px solid #eee; padding-top: 10px; }}
    </style>
    </head>
    <body>
    <div class="container">
        <p>Sehr geehrte/r Herr/Frau {recipient_name},</p>
        <p>ich wollte nur kurz nachfragen, ob meine letzte E-Mail vom {initial_send_date} bei Ihnen angekommen ist.</p>
        <p>Ich hatte Ihnen angeboten, eine kostenlose Probe von 10 Kontakten für Ihr Unternehmen zu erstellen und kurz zu zeigen, wie ich diese Leads direkt in <strong>fertige Termine für Sie umwandle</strong>.</p>
        <p>Haben Sie vielleicht doch 15 Minuten Zeit, um das kurz zu besprechen?</p>
        <p>Mit freundlichen Grüßen,</p>
        <p>{sender_name}<br>
        <a href="{linkedin_profile_link}">Mein LinkedIn-Profil</a></p>
    </div>
    </body>
    </html>
    """
    return subject, body

def follow_up_one_variant_two(sender_name: str, recipient_name: str, company_name: str, linkedin_profile_link: str) -> Tuple[str, str]:
    """
    Follow-up 1, variant 2/5.
    Args:
        sender_name (str): The name of the sender (e.g., "Yasin Holzenkaempfer").
        recipient_name (str): The last name of the recipient.
        company_name (str): The name of the recipient's company.
        linkedin_profile_link (str): Your LinkedIn profile URL.
    Returns:
        Tuple[str, str]: A tuple containing the subject and the HTML body of the email.
    """
    subject = f"Kurze Nachfrage – Termine & Leads für {company_name}"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
        .footer {{ font-size: 0.9em; color: #777; margin-top: 20px; border-top: 1px solid #eee; padding-top: 10px; }}
    </style>
    </head>
    <body>
    <div class="container">
        <p>Guten Tag Herr/Frau {recipient_name},</p>
        <p>ich schließe gerade meine E-Mails für heute ab und wollte mich noch einmal melden.</p>
        <p>Ich hatte Ihnen ja das Angebot gemacht, Ihnen 10 kostenlose Leads aus Ihrer Zielgruppe zukommen zu lassen und Ihnen zu zeigen, wie ich diese direkt in <strong>Termine in Ihrem Kalender</strong> verwandle. Vielleicht ist meine letzte E-Mail im Posteingang untergegangen.</p>
        <p>Gibt es nächste Woche einen passenden Zeitpunkt für ein kurzes Telefonat dazu?</p>
        <p>Herzliche Grüße,</p>
        <p>{sender_name}<br>
        <a href="{linkedin_profile_link}">Mein LinkedIn-Profil</a></p>
    </div>
    </body>
    </html>
    """
    return subject, body

def follow_up_one_variant_three(sender_name: str, recipient_name: str, linkedin_profile_link: str) -> Tuple[str, str]:
    """
    Follow-up 1, variant 3/5.
    Args:
        sender_name (str): The name of the sender (e.g., "Yasin Holzenkaempfer").
        recipient_name (str): The last name of the recipient.
        linkedin_profile_link (str): Your LinkedIn profile URL.
    Returns:
        Tuple[str, str]: A tuple containing the subject and the HTML body of the email.
    """
    subject = f"AW: Neue Kunden, fix & fertig: Eine Frage an {recipient_name}"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
        .footer {{ font-size: 0.9em; color: #777; margin-top: 20px; border-top: 1px solid #eee; padding-top: 10px; }}
    </style>
    </head>
    <body>
    <div class="container">
        <p>Hallo Herr/Frau {recipient_name},</p>
        <p>ich habe Ihnen letzte Woche eine E-Mail bezüglich der Möglichkeit geschickt, Ihre Vertriebspipeline mit qualifizierten Leads zu füllen und <strong>direkt Termine für Sie zu buchen</strong>.</p>
        <p>Vielleicht ist es gerade nicht der richtige Zeitpunkt, aber ich wollte sicherstellen, dass Sie mein Angebot für eine kostenlose Testliste von 10 Kontakten gesehen haben und verstanden haben, dass ich Ihnen die <strong>komplette Arbeit der Terminbuchung</strong> abnehme.</p>
        <p>Lassen Sie mich wissen, ob Sie Interesse haben, mehr darüber zu erfahren.</p>
        <p>Beste Grüße,</p>
        <p>{sender_name}<br>
        <a href="{linkedin_profile_link}">Mein LinkedIn-Profil</a></p>
    </div>
    </body>
    </html>
    """
    return subject, body

def follow_up_one_variant_four(sender_name: str, recipient_name: str, company_name: str, linkedin_profile_link: str) -> Tuple[str, str]:
    """
    Follow-up 1, variant 4/5.
    Args:
        sender_name (str): The name of the sender (e.g., "Yasin Holzenkaempfer").
        recipient_name (str): The last name of the recipient.
        company_name (str): The name of the recipient's company.
        linkedin_profile_link (str): Your LinkedIn profile URL.
    Returns:
        Tuple[str, str]: A tuple containing the subject and the HTML body of the email.
    """
    subject = f"Nur eine kurze Erinnerung – {company_name} & gebuchte Termine"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
        .footer {{ font-size: 0.9em; color: #777; margin-top: 20px; border-top: 1px solid #eee; padding-top: 10px; }}
    </style>
    </head>
    <body>
    <div class="container">
        <p>Sehr geehrte/r Herr/Frau {recipient_name},</p>
        <p>dies ist eine kurze Erinnerung an meine vorherige E-Mail.</p>
        <p>Ich hatte Ihnen angeboten, Ihnen als Demonstration meiner Arbeit 10 kostenlose und relevante B2B-Leads für Ihr Unternehmen zu liefern und Ihnen den Weg zu <strong>fertigen Terminen</strong> aufzuzeigen.</p>
        <p>Würden Sie das gerne in einem kurzen 15-minütigen Gespräch erläutern?</p>
        <p>Mit freundlichen Grüßen,</p>
        <p>{sender_name}<br>
        <a href="{linkedin_profile_link}">Mein LinkedIn-Profil</a></p>
    </div>
    </body>
    </html>
    """
    return subject, body

def follow_up_one_variant_five(sender_name: str, recipient_name: str, linkedin_profile_link: str) -> Tuple[str, str]:
    """
    Follow-up 1, variant 5/5.
    Args:
        sender_name (str): The name of the sender (e.g., "Yasin Holzenkaempfer").
        recipient_name (str): The last name of the recipient.
        linkedin_profile_link (str): Your LinkedIn profile URL.
    Returns:
        Tuple[str, str]: A tuple containing the subject and the HTML body of the email.
    """
    subject = "Ihr Feedback zu meinem Angebot für volle Kalender"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
        .footer {{ font-size: 0.9em; color: #777; margin-top: 20px; border-top: 1px solid #eee; padding-top: 10px; }}
    </style>
    </head>
    <body>
    <div class="container">
        <p>Guten Tag Herr/Frau {recipient_name},</p>
        <p>ich hoffe, diese E-Mail erreicht Sie gut. Ich wollte mich erkundigen, ob Sie Zeit hatten, meine letzte Nachricht zu lesen.</p>
        <p>Mein Angebot, Ihnen 10 kostenlose Leads zu liefern und diese <strong>direkt in konkrete Termine</strong> für Sie zu verwandeln, ist weiterhin gültig und soll Ihnen den Start erleichtern.</p>
        <p>Ich stehe gerne für ein kurzes Gespräch zur Verfügung, um dies näher zu erläutern.</p>
        <p>Viele Grüße,</p>
        <p>{sender_name}<br>
        <a href="{linkedin_profile_link}">Mein LinkedIn-Profil</a></p>
    </div>
    </body>
    </html>
    """
    return subject, body


# --//[FOLLOW UP TWO EMAIL TEMPLATES]\\--
def follow_up_two_variant_one(sender_name: str, recipient_name: str, company_name: str, linkedin_profile_link: str) -> Tuple[str, str]:
    """
    Follow-up 2, variant 1/5.
    Args:
        sender_name (str): The name of the sender (e.g., "Yasin Holzenkaempfer").
        recipient_name (str): The last name of the recipient.
        company_name (str): The name of the recipient's company.
        linkedin_profile_link (str): Your LinkedIn profile URL.
    Returns:
        Tuple[str, str]: A tuple containing the subject and the HTML body of the email.
    """
    subject = f"Letzte Nachfrage: Termine & Leads für {company_name}"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
        .footer {{ font-size: 0.9em; color: #777; margin-top: 20px; border-top: 1px solid #eee; padding-top: 10px; }}
    </style>
    </head>
    <body>
    <div class="container">
        <p>Sehr geehrte/r Herr/Frau {recipient_name},</p>
        <p>ich habe Ihnen nun zweimal bezüglich der Generierung von B2B-Leads und der <strong>direkten Terminbuchung</strong> für Ihr Unternehmen geschrieben.</p>
        <p>Ich verstehe, dass Ihr Posteingang voll sein kann. Mein Angebot, Ihnen 10 kostenlose Leads als Beweis meiner Expertise zu liefern und Ihnen zu zeigen, wie ich <strong>Ihren Kalender fülle</strong>, steht weiterhin.</p>
        <p>Wenn das Thema für Sie aktuell ist, lassen Sie mich es wissen. Wenn nicht, nehme ich an, dass kein Bedarf besteht und werde Sie nicht weiter kontaktieren.</p>
        <p>Mit freundlichen Grüßen,</p>
        <p>{sender_name}<br>
        <a href="{linkedin_profile_link}">Mein LinkedIn-Profil</a></p>
    </div>
    </body>
    </html>
    """
    return subject, body

def follow_up_two_variant_two(sender_name: str, recipient_name: str, linkedin_profile_link: str) -> Tuple[str, str]:
    """
    Follow-up 2, variant 2/5.
    Args:
        sender_name (str): The name of the sender (e.g., "Yasin Holzenkaempfer").
        recipient_name (str): The last name of the recipient.
        linkedin_profile_link (str): Your LinkedIn profile URL.
    Returns:
        Tuple[str, str]: A tuple containing the subject and the HTML body of the email.
    """
    subject = "Schnelle Frage – Gebuchte B2B-Termine"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
        .footer {{ font-size: 0.9em; color: #777; margin-top: 20px; border-top: 1px solid #eee; padding-top: 10px; }}
    </style>
    </head>
    <body>
    <div class="container">
        <p>Guten Tag Herr/Frau {recipient_name},</p>
        <p>ich wollte sicherstellen, dass meine vorherigen E-Mails nicht im Spam gelandet sind.</p>
        <p>Kurz gesagt: Ich helfe B2B-Unternehmen, ihre Vertriebspipeline mit qualifizierten Leads zu füllen <strong>und buche direkt die Termine für sie ein</strong>. Als Einstieg biete ich 10 kostenlose Test-Leads an.</p>
        <p>Ist das etwas, das für Sie interessant sein könnte oder kann ich das Thema abhaken?</p>
        <p>Herzliche Grüße,</p>
        <p>{sender_name}<br>
        <a href="{linkedin_profile_link}">Mein LinkedIn-Profil</a></p>
    </div>
    </body>
    </html>
    """
    return subject, body

def follow_up_two_variant_three(sender_name: str, recipient_name: str, company_name: str, linkedin_profile_link: str) -> Tuple[str, str]:
    """
    Follow-up 2, variant 3/5.
    Args:
        sender_name (str): The name of the sender (e.g., "Yasin Holzenkaempfer").
        recipient_name (str): The last name of the recipient.
        company_name (str): The name of the recipient's company.
        linkedin_profile_link (str): Your LinkedIn profile URL.
    Returns:
        Tuple[str, str]: A tuple containing the subject and the HTML body of the email.
    """
    subject = f"AW: AW: Ihr Vertrieb: Von neuen Leads zur vollen Pipeline ({company_name})"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
        .footer {{ font-size: 0.9em; color: #777; margin-top: 20px; border-top: 1px solid #eee; padding-top: 10px; }}
    </style>
    </head>
    <body>
    <div class="container">
        <p>Hallo Herr/Frau {recipient_name},</p>
        <p>ich schreibe Ihnen ein letztes Mal bezüglich meines Angebots, Ihnen 10 kostenlose Leads für Ihr Unternehmen zu erstellen und Ihnen dabei die <strong>komplette Terminfindung abzunehmen</strong>.</p>
        <p>Ich möchte nicht aufdringlich sein, aber ich bin davon überzeugt, Ihnen einen echten Mehrwert bieten zu können, indem Sie sich auf das Wesentliche konzentrieren können: den Verkauf.</p>
        <p>Sollte derzeit kein Bedarf bestehen, ist das natürlich völlig in Ordnung. Eine kurze Rückmeldung wäre hilfreich, damit ich weiß, wo ich stehe.</p>
        <p>Beste Grüße,</p>
        <p>{sender_name}<br>
        <a href="{linkedin_profile_link}">Mein LinkedIn-Profil</a></p>
    </div>
    </body>
    </html>
    """
    return subject, body

def follow_up_two_variant_four(sender_name: str, recipient_name: str, company_name: str, linkedin_profile_link: str) -> Tuple[str, str]:
    """
    Follow-up 2, variant 4/5.
    Args:
        sender_name (str): The name of the sender (e.g., "Yasin Holzenkaempfer").
        recipient_name (str): The last name of the recipient.
        company_name (str): The name of the recipient's company.
        linkedin_profile_link (str): Your LinkedIn profile URL.
    Returns:
        Tuple[str, str]: A tuple containing the subject and the HTML body of the email.
    """
    subject = f"Letzte Chance für kostenlose Leads & Termine – {company_name}"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
        .footer {{ font-size: 0.9em; color: #777; margin-top: 20px; border-top: 1px solid #eee; padding-top: 10px; }}
    </style>
    </head>
    <body>
    <div class="container">
        <p>Sehr geehrte/r Herr/Frau {recipient_name},</p>
        <p>dies ist meine letzte E-Mail zu meinem Angebot, Ihnen 10 kostenlose B2B-Leads zu liefern und diese <strong>direkt in Ihren Vertriebskalender zu bringen</strong>.</p>
        <p>Ich möchte Ihnen die Möglichkeit geben, von meiner Expertise zu profitieren, ohne jedes Risiko einzugehen.</p>
        <p>Falls Sie derzeit keine Notwendigkeit für frische Leads und vorgebuchte Termine sehen, respektiere ich das selbstverständlich.</p>
        <p>Viele Grüße,</p>
        <p>{sender_name}<br>
        <a href="{linkedin_profile_link}">Mein LinkedIn-Profil</a></p>
    </div>
    </body>
    </html>
    """
    return subject, body

def follow_up_two_variant_five(sender_name: str, recipient_name: str, company_name: str, linkedin_profile_link: str) -> Tuple[str, str]:
    """
    Follow-up 2, variant 5/5.
    Args:
        sender_name (str): The name of the sender (e.g., "Yasin Holzenkaempfer").
        recipient_name (str): The last name of the recipient.
        company_name (str): The name of the recipient's company.
        linkedin_profile_link (str): Your LinkedIn profile URL.
    Returns:
        Tuple[str, str]: A tuple containing the subject and the HTML body of the email.
    """
    subject = f"Keine Antwort ist auch eine Antwort? (Volle Kalender für {company_name})"
    body = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        .container {{ max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 5px; }}
        .footer {{ font-size: 0.9em; color: #777; margin-top: 20px; border-top: 1px solid #eee; padding-top: 10px; }}
    </style>
    </head>
    <body>
    <div class="container">
        <p>Guten Tag Herr/Frau {recipient_name},</p>
        <p>ich habe Ihnen in den letzten Tagen zweimal geschrieben, aber bisher keine Rückmeldung erhalten. Das ist völlig in Ordnung, aber ich wollte mich noch einmal melden, falls meine Nachrichten untergegangen sind.</p>
        <p>Mein Angebot, 10 kostenlose Leads für Ihr Unternehmen zu generieren und diese <strong>direkt in konkrete Termine</strong> zu verwandeln, steht noch. Es ist eine risikofreie Möglichkeit, den Wert meiner Arbeit zu testen.</p>
        <p>Wenn kein Interesse besteht, geben Sie mir gerne kurz Bescheid. Andernfalls freue ich mich, von Ihnen zu hören!</p>
        <p>Mit freundlichen Grüßen,</p>
        <p>{sender_name}<br>
        <a href="{linkedin_profile_link}">Mein LinkedIn-Profil</a></p>
    </div>
    </body>
    </html>
    """
    return subject, body