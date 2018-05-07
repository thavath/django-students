from __future__ import unicode_literals
from django.db import models

class Student(models.Model):

    english_name = models.CharField(max_length=200)
    khmer_name = models.CharField(max_length=200, blank=True)
    japanese_name = models.CharField(max_length=200, blank=True)
    nationality = models.CharField(max_length=50)
    place_of_birth = models.CharField(max_length=200)
    card_id = models.CharField(max_length=100, blank=True)
    khmer_salary = models.FloatField(max_length=10, blank=True)
    education = models.CharField(max_length=200, blank=True)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    age = models.PositiveIntegerField(default=False)
    GENDER = (
            ('Male','Male'),
            ('Female','Female'),
        )
    genders = models.CharField(max_length=200,choices=GENDER)
    state_of_healt = models.CharField(max_length=20, blank=True)
    blood_type = models.CharField(max_length=20, blank=True)
    vision = models.CharField(max_length=50, blank=True)
    interest = models.CharField(max_length=50, blank=True)
    year_of_experience = models.IntegerField(default=0)
    MARRIED = (
            ('Yes','Yes'),
            ('No','No'),
    )
    married = models.CharField(max_length=50, choices=MARRIED)
    position = models.CharField(max_length=50, blank=True)
    behavior = models.CharField(max_length=50)
    went_to_japan = models.CharField(max_length=50, choices=MARRIED)
    japanese_conversation = models.CharField(max_length=50, choices=MARRIED)
    height = models.CharField(max_length=50, blank=True)
    weight = models.CharField(max_length=50, blank=True)
    current_address = models.CharField(max_length=200)
    last_peroid_of_study = models.DateField(auto_now=False, auto_now_add=False)
    school_name= models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    REASON = (
        ('','')
        )
    reason = models.TextField(max_length=255)
    arrang_money = models.TextField(max_length=255)
    sending_company = models.CharField(max_length=200)
    LEVEL = (
        ('level','level'),
        ('N5','N5'),
        ('N4','N4'),
        ('N3','N3'),
        ('N2','N2'),
        ('N1','N1'),
        )
    japanese_level = models.CharField(max_length=50, choices=LEVEL)
    field_of_work = models.CharField(max_length=50)
    date_go_japan = models.DateField(auto_now_add=False, auto_now=False)
    prefecture = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    admin = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.english_name
