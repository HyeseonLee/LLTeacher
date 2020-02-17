from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings

class GeneralChemistry2(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default =1, on_delete = models.CASCADE)
    lectureName = models.CharField(max_length=200)
    professorName = models.CharField(max_length=50)
    SEME_FIELD_CHOICES=[
        ('19년도 2학기', '19년도 2학기'),
        ('19년도 1학기', '19년도 1학기'),
        ('18년도 2학기', '18년도 2학기'),
        ('18년도 2학기', '18년도 1학기'),
    ]
    seme = models.CharField(max_length=10, choices=SEME_FIELD_CHOICES)
    score = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)], default=[0])
    text = models.TextField(max_length=300)
