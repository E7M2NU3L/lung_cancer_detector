from django.db import models

class CovidModel(models.Model):
    image_url = models.CharField(
        max_length = 2250,
        blank = True
    )
    author = models.CharField(
        max_length = 100
    )
    description = models.CharField(
        max_length = 4000,
        blank = True
    )
    output = models.CharField(
        max_length = 100,
        blank = True
    )

    def __str__(self) -> str:
        return super().__str__()
    
class LungCancerModel(models.Model):
    GENDER_CHOICES = [("M", "Male"), ("F", "Female")]
    LUNG_CANCER_CHOICES = [("YES", "Yes"), ("NO", "No")]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField()
    smoking = models.IntegerField()
    yellow_fingers = models.IntegerField()
    anxiety = models.IntegerField()
    peer_pressure = models.IntegerField()
    chronic_disease = models.IntegerField()
    fatigue = models.IntegerField()
    allergy = models.IntegerField()
    wheezing = models.IntegerField()
    alcohol_consuming = models.IntegerField()
    coughing = models.IntegerField()
    shortness_of_breath = models.IntegerField()
    swallowing_difficulty = models.IntegerField()
    chest_pain = models.IntegerField()
    lung_cancer = models.CharField(max_length=3, choices=LUNG_CANCER_CHOICES)  # Target variable

    def __str__(self):
        return f"{self.gender} - {self.age} - {self.lung_cancer}"

class LungCancerCtModel(models.Model):
    image_url = models.CharField(
        max_length = 2250,
        blank = True
    )
    author = models.CharField(
        max_length = 100
    )
    description = models.CharField(
        max_length = 4000,
        blank = True
    )
    output = models.CharField(
        max_length = 100,
        blank = True
    )

    def __str__(self) -> str:
        return super().__str__()