from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    terms_of_service = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name
