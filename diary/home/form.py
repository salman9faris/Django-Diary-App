from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import DateInput

from .models import Diaryy


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class Diaryform(forms.ModelForm):
    diary = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "write something....",
                "class": "new-class-name two",
                "rows": 20,
                "cols": 100
            }
        ))
    YEARS = [x for x in range(2020, 2010, -1)]
    date = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))

    class Meta:
        model = Diaryy
        fields = [
            "date",
            "title",
            "diary"
        ]
