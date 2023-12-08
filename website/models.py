from django.db import models


class MyModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class NewsletterSub(MyModel):
    class Meta:
        db_table = "newsletter_subs"

    email = models.EmailField(unique=True, null=False)

    def __str__(self):
        return self.email


class PartnerCompany(MyModel):
    class Meta:
        db_table = "partner_companies"

    name = models.CharField('Company Name', max_length=200, null=False)
    address = models.CharField('Company Address', max_length=250, blank=True)
    zip_code = models.CharField('Company Zip Code', max_length=250, blank=True)
    city = models.CharField('Company City', max_length=250, blank=True)
    website = models.URLField('Company Website', blank=True)
    email = models.EmailField('Company Email', max_length=150, blank=True)
    phone = models.CharField('Company Contact', max_length=250, blank=True)

    def __str__(self):
        return self.name


class FinishedBuilding(MyModel):
    class Meta:
        db_table = "finished_buildings"

    name = models.CharField(max_length=200, null=False)
    location = models.CharField(max_length=100, null=False)
    building_type = models.CharField(max_length=100)
    partner_company = models.ForeignKey(PartnerCompany, blank=True, null=True, on_delete=models.SET_NULL)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    def __str__(self):
        return self.name


class Employee(MyModel):
    class Meta:
        db_table = "employees"

    first_name = models.CharField(max_length=200, null=False)
    last_name = models.CharField(max_length=200, null=False)
    position = models.CharField(max_length=50, null=False)
    employment_type = models.CharField(max_length=50, choices=[("Full-Time", "Full-Time"), ("Part-Time", "Part-Time"),
                                                               ("Contract", "Contract")])
    phone_number = models.CharField(max_length=25, unique=True, null=False)
    email = models.EmailField(unique=True, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
