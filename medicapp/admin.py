from django.contrib import admin
from .models import *

@admin.register(User)
class ShowUser(admin.ModelAdmin):
    list_display = ("first_name","last_name","email","password","UserImage","date_joined")
    list_filter = ("date_joined",)
    search_fields = ("first_name","last_name","email")
    list_editable = ("password",)
    list_per_page = 3
    list_display_links = ("first_name","last_name")

@admin.register(Country)
class ShowCountry(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_per_page = 3

@admin.register(State)
class ShowState(admin.ModelAdmin):
    list_display = ("country","name")
    list_filter = ("country",)
    search_fields = ("name",)
    list_per_page = 3
    list_display_links = ("name",)

@admin.register(City)
class ShowCity(admin.ModelAdmin):
    list_display = ("state","name")
    list_filter = ("state",)
    search_fields = ("name",)
    list_per_page = 3
    list_display_links = ("name",)

@admin.register(DoctorSpecialization)
class ShowDoctorSpecialization(admin.ModelAdmin):
    list_display = ("name","description","SpecialityImage")
    search_fields = ("name","description")
    list_per_page = 3
    list_display_links = ("name",)

@admin.register(Doctor)
class ShowDoctor(admin.ModelAdmin):
    list_display = ( "user","specialization","experience_years","qualification","consultation_fees","phone","address","city","state",
                    "country","available_from","available_to","bio","DoctorsImage","created_at")
    list_filter = ("specialization","country","state","city","created_at")
    search_fields = ("user__first_name","user__last_name","qualification","phone","city__name",)
    list_editable = ("consultation_fees","available_from","available_to",)
    list_per_page = 3
    list_display_links = ("user",)

@admin.register(PatientProfile)
class ShowPatientProfile(admin.ModelAdmin):
    list_display = ("user","dob","gender","blood_group","address","phone_no","PatientImage")
    list_filter = ("gender","blood_group")
    search_fields = ("user__first_name","user__last_name","phone_no",)
    list_editable = ("phone_no",)
    list_per_page = 3
    list_display_links = ("user",)

@admin.register(Appointment)
class ShowAppointment(admin.ModelAdmin):
    list_display = ("patient","doctor","appointment_date","time_slot","symptoms","status","created_at")
    list_filter = ("status","appointment_date")
    search_fields = ("patient__first_name","doctor__user__first_name",)
    list_editable = ("status",)
    list_per_page = 3
    list_display_links = ("patient",)

@admin.register(Prescription)
class ShowPrescription(admin.ModelAdmin):
    list_display = ("appointment","doctor_notes","medicines","next_visit_date","created_at")
    list_filter = ("created_at",)
    search_fields = ("doctor_notes","medicines")
    list_per_page = 3
    list_display_links = ("appointment",)

@admin.register(Payment)
class ShowPayment(admin.ModelAdmin):
    list_display = ("user","appointment","amount","payment_method","status","payment_date")
    list_filter = ("payment_method","status","payment_date")
    search_fields = ("user__first_name","user__last_name")
    list_editable = ("status",)
    list_per_page = 3
    list_display_links = ("user",)

@admin.register(Review)
class ShowReview(admin.ModelAdmin):
    list_display = ("user","doctor","rating","comment","created_at")
    list_filter = ("rating","created_at")
    search_fields = ("user__first_name","doctor__user__first_name","comment",)
    list_editable = ("rating",)
    list_per_page = 3
    list_display_links = ("user",)

@admin.register(ContactUs)
class ShowContactUs(admin.ModelAdmin):
    list_display = (
        "name","email","phone",
        "message","created_at"
    )
    list_filter = ("created_at",)
    search_fields = ("name","email","phone")
    list_per_page = 3
    list_display_links = ("name",)