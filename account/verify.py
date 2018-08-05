from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils import six
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode


class AccountActivation(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.profile.verified)


account_activation = AccountActivation()


def send_activation_email(request, user):
    current_site = get_current_site(request)
    subject = 'Activate Your TuitionBD Account'
    token = account_activation.make_token(user)
    message = render_to_string('account/account_activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': force_text(urlsafe_base64_encode(force_bytes(user.pk))),
        'token': token,
    })
    email = EmailMessage(subject, message, to=[user.email])
    email.send()
    return token


def activate(uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64).decode())
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation.check_token(user, token):
        user.is_active = True
        user.profile.verified = True
        user.save()

    return user
