from django import forms
from . import models

class CreateContact(forms.ModelForm):
    TYPE_CHOICES = [
        ('Web Design', 'Web Design'),
        ('Dashboard', 'Dashboard'),
        ('Mobile App', 'Mobile App'),
        ('Mockup', 'Mockup'),
        ('Desktop App', 'Desktop App'),
        ('Ui kit', 'Ui kit'),
    ]
    project_type = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=TYPE_CHOICES)

    BUDGET_SELECTS = [
        ('50k', '₦50k'),
        ('100k', '₦100k'),
        ('150k to ₦300k', '₦150k to ₦300k'),
        ('350k to ₦500k', '₦350k to ₦500k'),
        ('More than ₦550k', 'More than ₦550k'),
    ]
    budget_range = forms.ChoiceField(widget=forms.RadioSelect, choices=BUDGET_SELECTS)

    DEADLINE_SELECTS = [
        ('1 week', '1 week'),
        ('2 week', '2 week'),
        ('3 week', '3 week'),
        ('4 week', '4 week'),
        ('5 week', '5 week'),
    ]
    deadline = forms.ChoiceField(widget=forms.RadioSelect, choices=DEADLINE_SELECTS)

    class Meta:
        model = models.Contact
        fields = ['project_type','budget_range','deadline','fullname','email','phone','message']

        