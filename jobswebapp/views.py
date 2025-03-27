from datetime import date, timedelta
import json

from django.shortcuts import render
from .models import Job

# Create your views here.
def index(request):
    from_date = date.today() - timedelta(days=2) #change delta accordandly
    job_list = Job.objects.filter(date_posted__gte=from_date)
    #print(job_list[0])
    json_list = json.dumps(list(job_list.values()), default=str)
    #print(json_list)
    return render(request, "jobswebapp/index.html", {"jobs":job_list, "json_data":json_list})
