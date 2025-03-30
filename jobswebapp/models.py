from django.db import models

# Create your models here.
class Job(models.Model):
    site = models.CharField(max_length=25, null=True)
    job_url = models.CharField(max_length=500, null=True)
    job_url_direct = models.CharField(max_length=500, null=True)
    title = models.CharField(max_length=255, null=True)
    company = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    date_posted = models.DateField(null=True)
    job_type = models.CharField(max_length=10, null=True)
    #salary_source =
    min_amount = models.IntegerField()
    max_amount = models.IntegerField()
    is_remote = models.BooleanField(default=False, null=True)
    job_level = models.CharField(max_length=255, null=True)
    job_function = models.CharField(max_length=255, null=True)
    description = models.TextField()
    company_url =  models.CharField(max_length=500, null=True)
    company_logo = models.CharField(max_length=255, null=True)
    company_description = models.TextField()
    #applied = 