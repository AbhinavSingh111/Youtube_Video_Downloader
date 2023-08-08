from django.contrib import admin
from django.urls import path
from download_window import views


urlpatterns = [
    path("", views.index, name='home'),
    # path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    # path("contact", views.contact, name='contact'),
    # path('audio', views.process_video, name='process_video'),
    # path('handle-form-submission/', views.handle_form_submission, name='handle_form_submission')
]