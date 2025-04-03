from datetime import date, timedelta
import json

from django.shortcuts import render, redirect
from .models import Job

# Create your views here.
def index(request):
    from_date = date.today() - timedelta(days=2) #change delta accordandly
    job_list = Job.objects.filter(date_posted__gte=from_date, location__contains="Seattle")
    json_list = json.dumps(list(job_list.values()), default=str)
    return render(request, "jobswebapp/index.html", {"jobs":job_list, "json_data":json_list})

def jobsinlocation(request, location):
    location_converter = {'fresno':'Fresno, CA','bakersfield':'Bakersfield, CA', 'seattle':'Seattle, WA'}
    if location not in ['fresno','bakersfield','seattle']:
        return redirect("/jobs/")
    else:
        location = location_converter[location]

    from_date = date.today() - timedelta(days=8) #change delta accordandly
    job_list = Job.objects.filter(date_posted__gte=from_date, location=location)
    json_list = json.dumps(list(job_list.values()), default=str)
    return render(request, "jobswebapp/index.html", {"jobs":job_list, "json_data":json_list})

def HealthCheckBackend(request):
    raise Exception("Make Response code 500")
    return redirect("/jobs/")