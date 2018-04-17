from django.db import models


class UserLoan(models.Model):
    GENDER_CHOICES = (
        ('M', 'Mascúlino'),
        ('F', 'Femenino')
    )
    legal_number = models.CharField('DNI', max_length=8)
    first_name = models.CharField(
        'Nombre', max_length=30, null=True, blank=True
    )
    last_name = models.CharField(
        'Apellido', max_length=30, null=True, blank=True
    )
    gender = models.CharField(
        max_length=2, choices=GENDER_CHOICES
    )
    mail = models.EmailField('Email', max_length=254)

    def __str__(self):
        return '{0}, {1}'.format(
            self.last_name,
            self.first_name
        )


class Loan(models.Model):
    STATUS_CHOICES = (
        ('A', 'Aprobado'),
        ('R', 'Rechazado')
    )
    user_loan = models.ForeignKey(
        UserLoan, on_delete=models.CASCADE
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
    )
    date_create = models.DateTimeField(
        'Fecha Solicitud', auto_now_add=True
    )
    amount = models.DecimalField(
        'Monto Solicitado', max_digits=10, decimal_places=2
    )

    def __str__(self):
        return '{0}, {1}: {2}'.format(
            self.user_loan, self.date_create, self.get_status_display()
        )
                        
