from django import forms

from .models import Loan, UserLoan


class LoanForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LoanForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Loan
        fields = (
            'amount',
        )
        exclude = ('status', 'user_loan', 'date_create', )
        widgets = {
            'amount': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }
    
    def clean_amount(self):
        if self.cleaned_data['amount'] <= 0:
            raise forms.ValidationError('Monto invalido.')
        else:
            return self.cleaned_data['amount']


class UserLoanForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserLoanForm, self).__init__(*args, **kwargs)

    class Meta:
        model = UserLoan
        fields = (
            'legal_number', 'first_name', 'last_name', 'gender', 'mail'
        )
        widgets = {
            'legal_number': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control'
            }),
            'mail': forms.TextInput(attrs={
                'class': 'form-control'
            }),

        }

    def clean_legal_number(self):
        legal_number = self.cleaned_data['legal_number']
        if len(legal_number) < 8:
            raise forms.ValidationError('Ingrese un dni valido.')
        else:
            try:
                int(legal_number.replace('.', ''))
                return legal_number
            except:
                raise forms.ValidationError('Ingrese un dni valido.')
