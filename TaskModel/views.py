from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_model(request):
    if request.method=='POST':
        model_form= forms.TaskMod(request.POST)
        if model_form.is_valid():
            model_form.save()
            return redirect('add_model')
    else:
        model_form= forms.TaskMod()
    return render(request,'add_model.html',{'form':model_form})

def edit_model(request,id):
    model=models.Taskmodel.objects.get(pk=id)
    model_form=forms.TaskMod(instance=model)
    if request.method=='POST':
        model_form=forms.TaskMod(request.POST,instance=model)
        if model_form.is_valid():
            model_form.save()
            return redirect('homepage')
    return render(request,'add_model.html',{'form':model_form})

def delete_model(request,id):
    model = models.Taskmodel.objects.get(pk=id) 
    model.delete()
    return redirect('homepage')