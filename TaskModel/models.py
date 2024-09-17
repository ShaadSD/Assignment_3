from django.db import models
from TaskCategory.models import Taskcategory
import datetime
class Taskmodel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.CharField(max_length=500)
    task_assign_date = models.DateTimeField(default=datetime.date.today)
    is_completed = models.BooleanField(default=False)
    taskmodel = models.ManyToManyField(Taskcategory)

    def __str__(self):
        return self.taskTitle
