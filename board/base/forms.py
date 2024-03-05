from django.forms import ModelForm, DateInput
from .models import User, Meeting
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__' #creates form based on the model
        exclude = ['host','participants'] #excludes them from the form,not the model
        widgets = {
            'date': DateInput(attrs={'class': 'datepicker'}),
        }
