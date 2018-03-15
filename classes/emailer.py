#!/usr/bin/env python3

class Emailer:

    def __init__(self, sender, recipient, subject, message, outgoingServer, outgoingPort, senderPw):
        self.sender         = sender
        self.recipient      = recipient
        self.subject        = subject
        self.message        = message
        self.outgoingServer = outgoingServer
        self.outgoingPort   = outgoingPort
        self.senderPw       = senderPw

        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText

        msg            = MIMEMultipart()
        msg['From']    = sender
        msg['To']      = ", ".join(recipient)
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP_SSL(outgoingServer, outgoingPort)
        server.login(sender, senderPw)
        text = msg.as_string()
        server.sendmail(sender, recipient, text)
        server.quit()
