from.models import Leasing
from backend.celery import app
import datetime
from backend.utils import send_email
from django.conf import settings
from .models import Client
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.template.loader import get_template
from django.utils.translation import ugettext as _
from settings_db.models import SettingsDb
from django.core.mail import EmailMultiAlternatives
from sociallink.views import get_list_social_links
from backend.utils import send_email, get_list_social_links_images


@app.task
def create_leasing_entries():
    now = datetime.datetime.now()
    try:
        next_month_treated = now.replace(month=now.month + 1)
    except ValueError:
        if now.month == 12:
            next_month_treated = now.replace(year=now.year + 1, month=1)
        else:
            next_month_treated = now.replace(month=now.month + 1, day=1)
    current_month = format(now, '%m/%Y')
    for leasing in Leasing.objects.filter(is_active=True, month_treated=current_month):
        Leasing.objects.create(
            client=leasing.client,
            end_at=leasing.end_at,
            item=leasing.item,
            month_treated=format(next_month_treated, '%m/%Y'),
            payment_day=leasing.payment_day,
            price=leasing.price,
            start_at=leasing.start_at
        )


@app.task
def email_de_rappel_de_paiement(is_test=False, to_emails_test=["kechkarayoub@gmail.com"]):
    reminder_email_data = SettingsDb.get_reminder_email_data()
    context = {
        "backend_url": settings.BACKEND_URL_ROOT,
        "environment": settings.ENVIRONMENT,
        "logo_url": settings.BACKEND_URL_ROOT + static("contact/images/logo.jpg"),
        "message_1": reminder_email_data['message_1'],
        "message_2": reminder_email_data['message_2'],
        "message_3": reminder_email_data['message_3'],
        "footer_1": reminder_email_data['footer_1'],
        "footer_2": reminder_email_data['footer_2'],
        "site_name": SettingsDb.get_site_name(),
        "site_url_root": settings.SITE_URL_ROOT,
        "social_links": get_list_social_links(),
        "social_links_images": get_list_social_links_images(),
    }
    html_content = get_template('client/payment_reminder_email.html').render(context)
    text_content = get_template('client/payment_reminder_email.txt').render(context)
    if is_test:
        clients_emails = to_emails_test if len(to_emails_test) else ["kechkarayoub@gmail.com"]
    else:
        clients_emails = [
            client['email'] for client in Client.objects.filter(is_active=True, type="locataire").values('email')
        ]
    msg = EmailMultiAlternatives(
        reminder_email_data['object'], text_content, settings.EMAIL_HOST_USER, clients_emails[0:1],
        bcc=clients_emails[1:],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.content_subtype = 'html'
    msg.mixed_subtype = 'related'
    msg.send()
    # send_email("Test celery", "Celery work perfectly", settings.EMAIL_HOST_USER, "kechkarayoub@gmail.com")
