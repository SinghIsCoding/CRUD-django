from django.urls import path
from . import views

urlpatterns = [
    path('', views.insertdata, name='home'),
    path('delete/<int:id>/', views.delete_data, name="deletedata"),
    path('<int:id>/', views.update_data, name="updatedata"),
]
