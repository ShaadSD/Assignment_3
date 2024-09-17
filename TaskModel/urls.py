from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_model,name='add_model'),
    path('edit/<int:id>', views.edit_model, name='edit_model'),
    path('delete/<int:id>', views.delete_model, name='delete_model'),
    
]