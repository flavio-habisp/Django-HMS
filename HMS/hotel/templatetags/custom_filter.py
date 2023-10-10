from django import template
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def add_days(date_str, days):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    new_date = date_obj + timedelta(days=int(days))
    return new_date.strftime('%b %d')