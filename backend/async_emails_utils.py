# -*- coding: utf-8 -*-

from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from item.models import SendNewsletterAfterActivating
import smtplib
import threading


NBR_RECIPIENTS_BY_TIME = 50


def send_python_email(host_user, host_password, msg, recipients_list):

    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login(host_user, host_password)
    mail.sendmail(host_user, recipients_list, msg.as_string())
    mail.quit()


class EmailThread(threading.Thread):
    def __init__(self, subject, body, from_email, recipient_list, fail_silently, html, images, args_tuple):
        self.subject = subject
        self.body = body
        self.recipient_list = recipient_list
        self.from_email = from_email
        self.fail_silently = fail_silently
        self.html = html
        self.images = images
        self.args_tuple = args_tuple
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMultiAlternatives(self.subject, self.body, self.from_email, bcc=self.recipient_list)
        if self.html:
            msg.attach_alternative(self.html, "text/html")
            msg.content_subtype = 'html'
            msg.mixed_subtype = 'related'
            if self.images:
                for image in self.images:
                    # Create an inline attachment
                    ext = '.' + image.image.url.split('.')[-1]
                    image = MIMEImage(image.image.read(), _subtype=ext)
                    image.add_header('Content-ID', '<{}>'.format(image.image_filename))
                    msg.attach(image)
        i = 0
        recipients_list_ = self.recipient_list[i:i+NBR_RECIPIENTS_BY_TIME]
        while len(recipients_list_) > 0:
            recipients_list_ = self.recipient_list[i:i + NBR_RECIPIENTS_BY_TIME]
            msg.bcc = recipients_list_
            try:
                msg.send(self.fail_silently)
            except smtplib.SMTPDataError:
                print("SMTPDataError.......................")
                print("recipients_list_:")
                print(str(recipients_list_))
                is_ok = False
                msg2 = MIMEMultipart('alternative')
                msg2['Subject'] = self.subject
                msg2['From'] = self.from_email
                msg2['bcc'] = ", ".join(recipients_list_)
                part1 = MIMEText(self.body, 'plain')
                part2 = MIMEText(self.html, 'html')
                msg2.attach(part1)
                msg2.attach(part2)
                msg2.content_subtype = 'html'
                msg2.mixed_subtype = 'related'
                if self.images:
                    for image in self.images:
                        ext = '.' + image.image.url.split('.')[-1]
                        image = MIMEImage(image.image.read(), _subtype=ext)
                        image.add_header('Content-ID', '<{}>'.format(image.image_filename))
                        msg2.attach(image)
                for added_email_account in settings.ADDED_EMAILS_ACCOUNTS:
                    print("is_ok: "+str(is_ok))
                    if is_ok:
                        break
                    try:
                        send_python_email(
                            added_email_account['host_user'], added_email_account['host_password'], msg2,
                            recipients_list_
                        )
                        is_ok = True
                    except Exception as e:
                        # for the repr
                        print("the repr: ")
                        print(repr(e))
                        # for just the message, or str(e), since print calls str under the hood
                        print("just the message, or str(e): ")
                        print(e)
                        # the arguments that the exception has been called with.
                        # the first one is usually the message. (OSError is different, though)
                        print("the arguments that the exception has been called with: ")
                        print(e.args)
            i += NBR_RECIPIENTS_BY_TIME
        if self.args_tuple and self.args_tuple[0] is False:
            SendNewsletterAfterActivating.objects.filter(item_id=self.args_tuple[1]).delete()
