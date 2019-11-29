"""
Forms for the test application B4
"""
from opal.core import forms
from b4 import models

class AddPatientForm(forms.SubrecordForm):
    model              = models.Demographics
    template_name      = 'pages/add_patient.html'
    form_template_name = 'forms/add_patient.html'

    def save(self, *a, **k):
        """
        Delete the episode created by default.
        """
        patient, episode = super().save(*a, **k)
        episode.delete()
        return patient, None
