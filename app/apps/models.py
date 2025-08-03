from django.db import models
from django.forms import ValidationError


# Create your models here.
class Voting(models.Model):
    total_votes = models.PositiveSmallIntegerField(
        null=True,
        verbose_name=("Total de votos"),
        )
    valid_votes = models.PositiveSmallIntegerField(
        null=True, 
        verbose_name=("Votos válidos")
        )
    null_votes = models.PositiveSmallIntegerField(
        null=True, 
        verbose_name=("Votos Nulos")
        )
    blank_votes = models.PositiveSmallIntegerField(
        null=True, 
        verbose_name=("Votos Brancos")
        )

    class Meta:
        verbose_name_plural = ("1.0 -  Voting")
        verbose_name = ("Voting")

    def __str__(self):
        return str(self.total_votes)
    
    def clean(self):
        super().clean()
        total_calculated = self.valid_votes + self.null_votes + self.blank_votes
        if total_calculated != self.total_votes:
            raise ValidationError(
                ("A soma de votos válidos, nulos e brancos não pode ser diferente que o total de votos")
            )


