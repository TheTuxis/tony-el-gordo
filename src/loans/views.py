from django.views import View
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

from .models import Loan
from .forms import LoanForm, UserLoanForm
from .api.API import get_autorization_api


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
            val_res = get_autorization_api(
                user_loan.legal_number,
                user_loan.gender,
                user_loan.mail
            )
            print(val_res)
            if val_res['approved'] and val_res['error']:
                validation = 'A'
                context['status'] = '1'
            else:
                validation = 'R'
                context['status'] = '2'
            loan_form.status = validation
            loan_form.save()
        else:
            context = {
                'loan_form': loan_form,
                'user_loan_form': user_loan_form,
                'status': '0',
            }
        return render(request, self.template_name, context)


@login_required
@permission_required('loans.can_change')
def application_admin(request):
    template = 'loans/table.html'
    loan_list = Loan.objects.all() 
    context = {
        'loan_list': loan_list,
    }
    return render(
        request,
        template,
        context,
    )
