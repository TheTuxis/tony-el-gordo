import datetime

from django.contrib import admin
from django.contrib.admin import SimpleListFilter

from .models import Loan, UserLoan


class DateCreateFilter(SimpleListFilter):
    title = 'Solicitado'
    parameter_name = 'date_create'

    def lookups(self, request, model_admin):
        return [('HOY', 'Hoy'), ('ESTE MES', 'Del Mes')]

    def queryset(self, request, queryset):
        today = datetime.datetime.now()
        if self.value() == 'HOY':
            return queryset.filter(
                start_date__day=today.day,
                start_date__month=today.month,
                start_date__year=today.year
            )
        elif self.value() == 'ESTE MES':
            return queryset.filter(
                start_date__month=today.month,
                start_date__year=today.year
            )


class LoanDetailInline(admin.TabularInline):
    readonly_fields = (
        'date_create',
        'amount',
        'status',
    )
    model = Loan
    extra = 0


class LoanAdmin(admin.ModelAdmin):
    list_display = (
        'user_loan', 'date_create',
        'amount', 'get_status_display'
    )
    search_field = (
        'user_loan__legal_number', 'user_loan__last_name',
        'user_loan__first_name'
    )
    list_filter = (DateCreateFilter, 'status')


admin.site.register(Loan, LoanAdmin)


class UserLoanAdmin(admin.ModelAdmin):
    list_display = (
        'legal_number', 'first_name',
        'last_name', 'gender',
        'mail'
    )
    search_field = (
        'legal_number', 'last_name',
        'first_name'
    )
    inlines = (LoanDetailInline, )



admin.site.register(UserLoan, UserLoanAdmin)
