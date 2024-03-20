
from django.contrib import admin
from django.urls import path
from hospital_app import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('nav/', views.Nav, name='nav'),
    path('', views.Index, name='home'),
    path('admin_login/', views.Login, name='login'),
    path('logout/', views.Logout_admin, name='logout'),
    path('view_doctor/', views.View_doctor, name='view_doctor'),
    path('add_doctor/', views.Add_doctor, name='add_doctor'),
    path('delete_doctor(?P<int:pid>)', views.Delete_Doctor, name='delete_doctor'),
    path('view_patient/', views.View_patient, name='view_patient'),
    path('add_patient/', views.Add_patient, name='add_patient'),
    path('delete_patient(?P<int:pid>)', views.Delete_Patient, name='delete_patient'),
    path('view_appointment/', views.View_Appointment, name='view_appointment'),
    path('add_appointment/', views.Add_Appointment, name='add_appointment'),
    path('delete_appointment(?P<int:pid>)', views.Delete_Appointent, name='delete_appointment'),
  
]
