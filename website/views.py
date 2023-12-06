from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives, send_mail
from decouple import config
from .forms import SignUpForm, BookingForm
from .models import NewsletterSub
import requests


def home(request):
    return render(request, "home.html", {})


def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect("home")
        else:
            messages.success(request, "There was a problem logging you in. Please try again...")
            return redirect("login")
    else:
        return render(request, "login.html")


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect("home")


def register(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have registered !")
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {
            "form": form
        })

    return render(request, "register.html", {
        "form": form
    })


def about(request):
    return render(request, "about.html", {})


def team(request):
    return render(request, "team.html", {})


def projects(request):
    return render(request, "projects.html", {})


def services(request):
    return render(request, "services.html", {})


def pricing(request):
    return render(request, "pricing.html", {})


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]

        # Send Email
        send_mail(
            subject=f"{name} - {subject}",
            message=f"From: {email}\n\n{message}",
            from_email=email,
            recipient_list=["alex.termure@yahoo.com"]
        )

        return render(request, "contact.html", {
            "name": name,
        })
    else:
        return render(request, "contact.html", {})


def send_newsletter(request):
    if request.user.is_staff:
        sub_emails = NewsletterSub.objects.all()
        emails_list = [x.email for x in sub_emails]

        context = {
            "first_name": "John",
            "last_name": "McDonald",
        }

        template = get_template("email/email.html")
        content = template.render(context)
        mail = EmailMultiAlternatives(
            subject="Newsletter from WebApp",
            body=content,
            to=emails_list
        )
        mail.content_subtype = "html"
        mail.send()

        messages.success(request, "Newsletter sent successfully!")
        return redirect("home")

    else:
        messages.success(request, "You don't have the permissions to access this feature!")
        return redirect("home")


def booking(request):
    if request.method == "GET":
        form = BookingForm()
    else:
        form = BookingForm(request.POST)
        if form.is_valid():
            # Define the data you want to send in the POST request (if any)
            data = {
                "name": form.cleaned_data["name"],
                "email": form.cleaned_data["email"],
                "date": form.cleaned_data["date"],
                "time": form.cleaned_data["time"],
                "location": form.cleaned_data["location"],
            }
            # Define the Zapier Webhook URL
            zapier_webhook_url = config("ZAPIER_WEB_HOOK_URL")

            # Make the POST request
            response = requests.post(zapier_webhook_url, json=data)

            if response.status_code == 200:
                # html_message = "You're booking request has sent successfully!"
                print(JsonResponse({'success': True}))
                return redirect("home")
            else:
                print(JsonResponse({'success': False, 'error_message': 'Failed to trigger Zapier'}))
                return redirect("booking")

    return render(request, "booking.html", {
        "form": form
    })
