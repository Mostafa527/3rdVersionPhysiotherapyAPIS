from django.db import models
from Physiotherapist.models import Physiotherapist
from Patient.models import Patient
class Favorite(models.Model):
    Physio_Favorite=models.ForeignKey(Physiotherapist,related_name='Physio_Fav',on_delete=models.CASCADE)
    Patient_Favorite=models.ForeignKey(Patient,related_name='Patient_Fav',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)