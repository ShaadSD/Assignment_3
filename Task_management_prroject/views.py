from django.shortcuts import render

from TaskModel.models import Taskmodel
def home(request):
    data=Taskmodel.objects.prefetch_related('taskmodel').all()
    return render(request,'home.html',{'data':data})