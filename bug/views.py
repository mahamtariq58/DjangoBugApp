from django.shortcuts import render, redirect 
from .models import Bug
from .forms import BugForm
from django.views import generic
from django.utils import timezone
from .models import Bug

# generic views
class IndexView(generic.ListView):

    template_name = "bug/index.html"
    context_object_name = "bugs"
    
    def get_queryset(self):
        return Bug.objects.filter(report_date__lte=timezone.now()).order_by("-report_date")[:]
    
class DetailView(generic.DetailView):

    model = Bug 
    template_name = "bug/detail.html" 

def register_bug(request):
    if request.method =="POST":
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bug:index')
    else:
        form = BugForm()
    return render (request,'bug/bug_form.html',{'form': form})        