from django.shortcuts import render,redirect

from .models import *

from .forms import *
# Create your views here.

def home(request):
    task=Task.objects.all()
    form=TaskForm
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'home.html',{'task':task,'form':form})


def edit(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form})





def deleteTask(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html',{'task':task})