from django.urls import path
from . import views
from .views import *

urlpatterns = [
path('Clinic/Patient/<int:patient_id>',views.ClinicDetailsByPat,name='ClinicDetailsByPatient'),
path('Clinic/<int:pk>',clinic_detail.as_view(),name='clinic_detail'),
path('Clinic',ClinicList.as_view(),name='clinic_list'),
]