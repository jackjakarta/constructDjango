from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives


def send_register_user_email(user):
    context = {
        "first_name": user.first_name,
        "last_name": user.last_name,
    }

    template = get_template("email/email.html")
    content = template.render(context)

    mail = EmailMultiAlternatives(
        subject="Your account has been registered.",
        body=content,
        to=[user.email],
    )
    mail.content_subtype = "html"
    mail.send()
