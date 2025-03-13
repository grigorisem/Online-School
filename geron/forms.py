from django import forms
from .models import Membership
import datetime

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['parent_name', 'child_name', 'start_date', 'membership_type']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'style': 'display: block;'}),  # для выбора даты
        }

    # Убираем price из формы, чтобы оно рассчитывалось на сервере
    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')
        if start_date > datetime.date.today():
            raise forms.ValidationError("Вы не можете выбрать дату из будущего.")
        return start_date
