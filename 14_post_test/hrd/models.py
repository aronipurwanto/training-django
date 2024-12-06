from django.db import models

class Department(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.code})"

class Employee(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    date_of_birth = models.DateTimeField()
    place_of_birth = models.CharField(max_length=255)
    RELIGION_CHOICES = (
        ('Islam', 'Islam'),
        ('Kristen', 'Kristen'),
        ('Katholik', 'Katholik'),
        ('Hindu', 'Hindu'),
        ('Budha', 'Budha'),
    )
    religion = models.CharField(max_length=20, choices=RELIGION_CHOICES)
    GENDER_CHOICES = (
        ('Pria', 'Pria'),
        ('Wanita', 'Wanita'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.name} - {self.department}"