# -*- coding: utf-8 -*-

from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives
from item.models import SendNewsletterAfterActivating
import smtplib
import threading


NBR_RECIPIENTS_BY_TIME = 50


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
        while len(self.recipient_list[i:i+NBR_RECIPIENTS_BY_TIME]) > 0:
            msg.bcc = self.recipient_list[i:i+NBR_RECIPIENTS_BY_TIME]
            try:
                msg.send(self.fail_silently)
            except smtplib.SMTPDataError:
                print("***********************************************")
                print("daily_excessed")
            i += NBR_RECIPIENTS_BY_TIME
        if self.args_tuple and self.args_tuple[0] is False:
            SendNewsletterAfterActivating.objects.filter(item_id=self.args_tuple[1]).delete()
