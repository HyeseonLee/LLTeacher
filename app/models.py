from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User  
from django.db.models.signals import post_save  
from django.dispatch import receiver

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
    class ReadonlyMeta:
        readonly = ["professorName"]
    


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

## 회원가입 필요 모델 추가해요

class Profile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):  
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):  
    instance.profile.save()
