from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import Site
from django.utils.http import urlsafe_base64_encode
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes
from django.shortcuts import get_object_or_404

from app.user.models import User


def send_activate_email_message(email):
    """
    Функция отправки письма с подтверждением для аккаунта
    """
    user = get_object_or_404(User, email=email)
    current_site = Site.objects.get_current().domain
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    activation_url = reverse_lazy('activate', kwargs={
        'uid64': uid, 'token': token})
    subject = f'Активируйте свой аккаунт!'
    message = render_to_string('email/activate_email_send.html', {
        'activation_url': f'http://{current_site}{activation_url}',
    })
    return user.email_user(subject, message)
