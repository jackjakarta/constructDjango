from django.contrib import admin
from .models import NewsletterSub, FinishedBuilding, Employee

# Register your models here.
admin.site.register(NewsletterSub)
admin.site.register(FinishedBuilding)
admin.site.register(Employee)
