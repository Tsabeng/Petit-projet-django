from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

class Band(models.Model):
    def __str__(self):
        return f'{self.name}'
    class Genre(models.TextChoices):
        HIP_HOP='HH'
        SYNTH_POP='SP'
        ALTERNATIVE_ROCK='AR'
        MBOLE='MB'
        RAP='RAP'
        BENSKIN='BK'
        MAKOSA='MK'

    name=models.fields.CharField(max_length=100)
    genre=models.fields.CharField(choices=Genre.choices,max_length=5)
    biography=models.fields.CharField(max_length=1000)
    year_formed=models.fields.IntegerField(
        validators=[MinValueValidator(1900),MaxValueValidator(2025)]
    )
    active=models.fields.BooleanField(default=True)
    official_homepage=models.fields.URLField(null=True, blank=True)
    

class Listing(models.Model):
    def __str__(self):
        return f'{self.title}'
    class Types(models.TextChoices):
        DISQUES='RECORDS'
        VETEMENTS='CLOTHING'
        AFFICHES='POSTERS'
        DIVERS='MISECELLANEOUS'
        TICKET='TICKET'

    title=models.fields.CharField(max_length=100)
    description=models.fields.CharField(max_length=200)
    sold=models.fields.BooleanField(default=False)
    year=models.fields.IntegerField (
        validators=[MinValueValidator(1900),MaxValueValidator(2025)],
        null=True
    )
    type = models.fields.CharField(choices=Types.choices,max_length=14)
    band = models.ForeignKey(Band,null=True,blank=True, on_delete=models.SET_NULL)


