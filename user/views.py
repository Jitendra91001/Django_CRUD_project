from django.shortcuts import render,HttpResponseRedirect
from .forms import studentRagistration
from .models import student

# Create your views here.

# create a function of show the data
def home(request):
    if request.method=='POST':
        fm=studentRagistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            res=student(name=nm,email=em,password=pw)
            res.save()
            fm=studentRagistration()
    else:
        fm=studentRagistration()
    stud=student.objects.all()
    return render(request,'curd/index.html',{'forms':fm,'stu':stud})   

# create a function of update data
def dataupdate(request,id):
    if request.method=='POST':
        pi=student.objects.get(pk=id)
        fm=studentRagistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = student.objects.get(pk=id)
        fm=studentRagistration(instance=pi)
    return render(request,'curd/update.html',{'forms':fm})
# create a function of deleat data
def datadelete(request,id):
    if request.method=='POST':
        pi=student.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

