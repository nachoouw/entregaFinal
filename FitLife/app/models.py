from django.db import models


class PlanEntreno(models.Model):
    Entrenamiento = models.IntegerField(help_text="Tipo Entrenamiento")
    Valor =  models.FloatField()
    DuracionDias = models.IntegerField(help_text="Duración en días")
    Objetivo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Objetivo
