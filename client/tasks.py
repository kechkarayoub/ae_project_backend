from.models import Leasing
from backend.celery import app
import datetime


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