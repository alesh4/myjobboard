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
    location_converter = {'fresno':'Fresno, CA','bakersfield':'Bakersfield, CA', 'seattle':'Seattle, WA', 'houston':'Houston, TX'}
    if location not in ['fresno','bakersfield','seattle','houston']:
        return redirect("/jobs/")

    latest_only = request.GET.get('lo',None)
    from_date = date.today() - timedelta(days=2) #change delta accordandly
    job_list = Job.objects.filter(location__contains=location)
    latest_only = False if latest_only in ['False','f','false','0'] else True
    if latest_only:
        job_list = job_list & Job.objects.filter(date_posted__gte=from_date)

    json_list = json.dumps(list(job_list.values()), default=str)
    return render(request, "jobswebapp/index.html", {"jobs":job_list, "json_data":json_list})

def HealthCheckBackend(request):
    # used to check if my logger was set correctly. it appears it is. this method should not be called for now
    raise Exception("Make Response code 500")
    return redirect("/jobs/")