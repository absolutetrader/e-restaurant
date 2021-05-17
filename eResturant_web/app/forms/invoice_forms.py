from django import forms
from django.conf import settings
from django.forms import ValidationError
from app.models.invoice_model import InVoice


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = InVoice
        fields = [
            'booking'
        ]
        labels = {
            'booking': 'Table number'
        }
