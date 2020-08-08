from django import forms
from .models import *

class ReservationProblem(forms.ModelForm):
    class Meta:
        model = Reservation
        fields =['name', 'phone', 'descriptionProblem']

class AddService(forms.ModelForm):
    class Meta:
        model = ServicProvider
        fields = '__all__'
        exclude = [ 'user', 'publishAt' ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']