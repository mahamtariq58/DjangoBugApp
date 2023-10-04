from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bug

# Create your views here.
# funtion  to register bug into database

def index(request):

    # retreive data from database
    bugs= Bug.objects.all()

    data = {
        'bugs': bugs,
    }
    
    return render(request, 'bug/index.html',data)


def register_bug(request):

    if request.method == 'POST':

        bug_description =request.POST['bug_description']
        bug_type = request.POST['bug_type']
        report_date = request.POST['report_date']
        status = request.POST['status']

     #bug object to save in database
        bug =Bug(
            bug_description=bug_description,
            bug_type=bug_type,
            report_date=report_date,
            status=status
        )   
        bug.save ()


        # redirect to index page when bug is registered
        return redirect(index)
    
    # render the bug registreation form
    return render (request, 'bug_register.html')