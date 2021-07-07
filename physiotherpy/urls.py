
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Accounts.urls')),
    path('',include('MyAdmin.urls')),
    path('', include('Patient.urls')),
    path('', include('Clinic.urls')),
    path('', include('Physiotherapist.urls')),
    path('',include('Game.urls')),
    path('',include('ExeercisePlan.urls')),
    path('', include('Session.urls')),
    path('',include('Favourite.urls')),
    path('',include('Observation.urls')),
    path('', include('Scores.urls'))

]

