from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_category(request):
    if request.method=='POST':
        category_form= forms.TaskCate(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
    else:
        category_form= forms.TaskCate()
    return render(request,'add_category.html',{'form':category_form})

def edit_category(request,id):
    category=models.Taskcategory.objects.get(pk=id)
    category_form=forms.TaskCate(instance=category)
    if request.method=='POST':
        category_form=forms.TaskCate(request.POST,instance=category)
        if category_form.is_valid():
            category_form.save()
            return redirect('homepage')
    return render(request,'add_category.html',{'form': category_form})

def delete_category(request,id):
    category = models.Taskcategory.objects.get(pk=id) 
    category.delete()
    return redirect('homepage')
    category = models.Taskcategory.objects.get(pk=0) 