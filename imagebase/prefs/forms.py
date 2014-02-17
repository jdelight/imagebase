from django.forms import ModelForm

from .models import ImagebaseSettings

class SettingsForm(ModelForm):

    class Meta:
        model = ImagebaseSettings

