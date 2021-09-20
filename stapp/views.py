from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import StudentRegistration
from .models import profile
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
# This function will add and show the data..
def add_show(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data["name"]
            eml = form.cleaned_data["email"]
            pwd = form.cleaned_data["password"]
            marks = form.cleaned_data["marks"]
            reg = profile(name=nm, email=eml, password=pwd, marks=marks)
            reg.save()

            messages.success(request, "Student data inserted successfully...!")
            
            # form.save()
            form = StudentRegistration()

    else:
        form = StudentRegistration()
        # messages.error(request, "Error. Message not sent.")
    data = profile.objects.all()


    return render(request, 'stapp/addandshow.html', {'form':form, 'data':data})

#This fumction will delete the data...

def delete_data(request, id):
    if request.method == "POST":
        pi = profile.objects.get(pk=id)
        pi.delete()
        messages.success(request, "Student data deleted successfully...!")
        return HttpResponseRedirect('/')
    messages.error(request, "Error. Message not sent.")

# This function will update the student data...

def update_data(request, id):
    if request.method == "POST":
        pi = profile.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = profile.objects.get(pk=id)
        form = StudentRegistration(instance=pi)
    return render(request, 'stapp/updatestudent.html', {'form':form})