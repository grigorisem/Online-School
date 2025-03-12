from django import forms
from .models import Membership

class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['parent_name', 'child_name', 'start_date', 'membership_type']

    price = forms.DecimalField(max_digits=10, decimal_places=2, required=False, disabled=True)

    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')
        if start_date > datetime.date.today():
            raise forms.ValidationError("Вы не можете выбрать дату из будущего.")
        return start_date
