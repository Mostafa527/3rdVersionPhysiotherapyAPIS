from django.db import models
from ExeercisePlan.models import Exercise_Plan
class Session(models.Model):
    DateOfCreation=models.DateTimeField(blank=False)
    Description=models.CharField(max_length=300)
    Session_Plan=models.ForeignKey(Exercise_Plan,related_name='session_plan',on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)