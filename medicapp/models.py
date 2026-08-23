from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to="Users")
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def UserImage(self):
        return mark_safe('<img src={} width="100px">'.format(self.profile_image.url))

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class DoctorSpecialization(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="Speciality")

    def __str__(self):
        return self.name

    def SpecialityImage(self):
        return mark_safe('<img src={} width="100px">'.format(self.image.url))

class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    specialization = models.ForeignKey(DoctorSpecialization, on_delete=models.CASCADE)
    experience_years = models.IntegerField()
    qualification = models.CharField(max_length=200)
    consultation_fees = models.FloatField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    available_from = models.TimeField()
    available_to = models.TimeField()
    bio = models.TextField()
    image = models.ImageField(upload_to="Doctors")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.specialization}"

    def DoctorsImage(self):
        return mark_safe('<img src={} width="100px">'.format(self.image.url))

class PatientProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'),('Female', 'Female'),('Other', 'Other'),])
    blood_group = models.CharField(max_length=5, choices=[('A+', 'A+'),('A-', 'A-'),('B+', 'B+'),('B-', 'B-'),('AB+', 'AB+'),('AB-', 'AB-'),('O+', 'O+'),('O-', 'O-'),])
    address = models.TextField()
    phone_no = models.CharField(max_length=15)
    image = models.ImageField(upload_to="Patients")

    def PatientImage(self):
        return mark_safe('<img src={} width="100px">'.format(self.image.url))

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateField()
    time_slot = models.TimeField()
    symptoms = models.TextField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'),('confirmed', 'Confirmed'),('completed', 'Completed'),('cancelled', 'Cancelled'),])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} / {self.doctor}"

class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    doctor_notes = models.TextField()
    medicines = models.TextField()
    next_visit_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_method = models.CharField(max_length=20, choices=[('credit_card', 'Credit Card'),('debit_card', 'Debit Card'),('paypal', 'PayPal'),('other', 'Other'),])
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'),('completed', 'Completed'),('failed', 'Failed'),])
    payment_date = models.DateField()

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

