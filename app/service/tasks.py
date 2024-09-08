from celery import shared_task

from .email import send_activate_email_message


@shared_task
def send_activate_email_message_task(email):
    """
    1. Задача обрабатывается в представлении: UserRegisterView
    2. Отправка письма подтверждения осуществляется через функцию: send_activate_email_message
    """
    return send_activate_email_message(email)
