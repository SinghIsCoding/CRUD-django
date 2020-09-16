from django.shortcuts import render
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
from .models import User

# This will add new data into the database
def insertdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pas = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pas)
            reg.save()
            fm = StudentRegistration()
    else:
       fm = StudentRegistration() 
    stud = User.objects.all()
    return render(request, 'home.html',{'form': fm, 'stu': stud})

# This will delete data from the database
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/') 

# This will update data from the database
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else :
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'update.html', {'form': fm})
