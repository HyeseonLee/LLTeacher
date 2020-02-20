from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.utils import timezone

class GeneralChemistry2(models.Model):
    objects = models.Manager()
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
    time = models.DateTimeField(default=timezone.now)
    # 정렬기준이 필요한거 같아서 자료입력시간만 추가했어요
    def __str__(self):
        return str(self.time)
    


class LawAndEconomics(models.Model):
    objects = models.Manager()
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
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.time)


class WebProgramming(models.Model):
    objects = models.Manager()
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
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.time)

class PhysicsExperiment(models.Model):
    objects = models.Manager()
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
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.time)
