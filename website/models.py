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


class FinishedBuilding(MyModel):
    class Meta:
        db_table = "finished_buildings"

    name = models.CharField(max_length=200, null=False)
    location = models.CharField(max_length=100, null=False)
    building_type = models.CharField(max_length=100)
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
