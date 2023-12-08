from django.contrib import admin
from .models import NewsletterSub, FinishedBuilding, Employee, PartnerCompany

# Register your models here.
admin.site.register(NewsletterSub)
admin.site.register(FinishedBuilding)
admin.site.register(Employee)
admin.site.register(PartnerCompany)
