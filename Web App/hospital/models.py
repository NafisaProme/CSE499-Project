from django.contrib.auth.models import User
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gen = models.CharField(max_length=6)
    email = models.EmailField(unique=True)
    phn = models.IntegerField()
    password = models.CharField(max_length=100)
    is_doctor = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        user, created = User.objects.get_or_create(username=self.email, email=self.email)
        if created:
            user.set_password(self.password)
            user.save()

        super(Person, self).save(*args, **kwargs)


class Patient(Person):
    address = models.CharField(max_length=200, default='Dhaka')

class Doctor(Person):
    image = models.ImageField(default='static/images/ai.jpg', upload_to='static/images/doctor_images')
    degree = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    keyword = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.is_doctor = True
        super(Doctor, self).save(*args, **kwargs)

class Appointment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()

    def __str__(self):
        return f"{self.patient.name} with {self.doctor.name}"
