from django.views import View
from django.shortcuts import render

from .forms import LoanForm, UserLoanForm


class LoanApplicationView(View):
    loan_form = LoanForm()
    user_loan_form = UserLoanForm()
    template_name = "loans/loan_application.html"
    
    def get(self, request, *args, **kwargs):
        context = {
            'loan_form': self.loan_form,
            'user_loan_form': self.user_loan_form,
            'status': '0',
        }
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        loan_form = LoanForm(data=request.POST)
        user_loan_form = UserLoanForm(data=request.POST)
        context = {
            'loan_form': loan_form,
            'user_loan_form': user_loan_form,
            'status': '0',
        } 
        if user_loan_form.is_valid() and loan_form.is_valid():
            user_loan = user_loan_form.save()
            loan_form = loan_form.save(commit=False)
            loan_form.user_loan = user_loan
            loan_form.save()
            context['status'] = '1'
        return render(request, self.template_name, context)
