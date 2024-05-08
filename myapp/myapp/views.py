from django.http import HttpResponse
import datetime
from django.shortcuts import render

def home(request):
    isActive=True
    if request.method == 'POST':
        check=request.POST.get('check')
        print(check )
        if check is None:isActive=False
        else:isActive=True
    
    date=datetime.datetime.now()
    
    name="Sanjeev Kumar Yadav"
    list_of_skills=[
       	    'Cloud Platform: AWS',
        	'Operating System: Linux, Windows and MacOS',
        	'Ticketing Tool: Freshdesk, Autotask', 
        	'Bug Tracking: Jira',
       	    'CRM: Zoho',
       	    'Database: SQL'

    ]
    student={
        'student_name':'Sanjeev Kumar Yadav',
        'student_college':'Satya college of engineering and technology',
        'student_place':'New Delhi'

    }
    # return HttpResponse("<h1>Hello this is index page </h1>" +str(date))
    data={
        'date':date,
        'isActive':isActive,
        'name':name,
        'list_of_skills':list_of_skills,
        'student_data':student
    }
    return render(request,"home.html",data)


def about(request):
    # return HttpResponse("<h1>This is about page</h1>")
    return render(request,"about.html",{})

def services(request):
    # return HttpResponse("<h1>This is services page</h1>")
    return render(request,"services.html",{})

def contact(request):
    # return HttpResponse("<h1>This is services page</h1>")
    return render(request,"contact.html",{})