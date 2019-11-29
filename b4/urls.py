"""
Urls file for an opal application
"""
from django.conf.urls import include, url
from django.urls import path
from opal.views import IndexView
from opal.urls import urlpatterns as opatterns

from django.contrib import admin
admin.autodiscover()

from b4 import forms, views

urlpatterns = [
    url(r'^$', IndexView.as_view()),
    path('forms/add-patient/', forms.AddPatientForm.as_view(), name='add-patient'),
    url(r'^create-new-episode', views.CreateEpisodeView.as_view(), name='create-new-episode'),
]

urlpatterns += opatterns
