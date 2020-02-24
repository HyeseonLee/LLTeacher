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
    lectureName = models.CharField(max_length=200, default="일반화학2")
    professorName = models.CharField(max_length=50, default="민선준")
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
    def save(self, *args, **kwargs):
        super(GeneralChemistry2, self).save(*args, **kwargs)
    


class LawAndEconomics(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default =1, on_delete = models.CASCADE)
    lectureName = models.CharField(max_length=200, default="법과경제학")
    professorName = models.CharField(max_length=50, default="김용규")
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
    def save(self, *args, **kwargs):
        super(LawAndEconomics, self).save(*args, **kwargs)


class WebProgramming(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default =1, on_delete = models.CASCADE)
    lectureName = models.CharField(max_length=200, default="웹프로그래밍")
    professorName = models.CharField(max_length=50, default="최기환")
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

    def save(self, *args, **kwargs):
        super(WebProgramming, self).save(*args, **kwargs)

class PhysicsExperiment(models.Model):
    objects = models.Manager()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default =1, on_delete = models.CASCADE)
    lectureName = models.CharField(max_length=200, default="일반물리학실험")
    professorName = models.CharField(max_length=50, default="오혜근")
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

    def save(self, *args, **kwargs):
        super(PhysicsExperiment, self).save(*args, **kwargs)
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
