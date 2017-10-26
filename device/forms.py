from django import forms
from device.models import Device

class CreateDeviceForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Device
        fields = ('name', )