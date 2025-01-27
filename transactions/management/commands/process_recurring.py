# transactions/management/commands/process_recurring.py
from django.core.management.base import BaseCommand
from django.utils import timezone
from transactions.models import RecurringTransaction, Transaction
from dateutil.relativedelta import relativedelta

class Command(BaseCommand):
    help = 'Process recurring transactions'

    def handle(self, *args, **options):
        today = timezone.now().date()
        recurring_txns = RecurringTransaction.objects.filter(
            next_payment_date__lte=today,
            is_active=True
        )

        for txn in recurring_txns:
            Transaction.objects.create(
                user=txn.user,
                amount=txn.amount,
                category=txn.category,
                type='expense',
                description=f"Recurring: {txn.category}"
            )
            # Update next payment date
            txn.next_payment_date += relativedelta(**{txn.frequency: 1})
            txn.save()