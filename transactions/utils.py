# transactions/utils.py
from django.utils import timezone
from transactions.models import Budget, Transaction

def check_budget_alerts():
    for budget in Budget.objects.all():
        spent = Transaction.objects.filter(
            user=budget.user,
            category=budget.category,
            date__range=[budget.start_date, budget.end_date]
        ).aggregate(total=models.Sum('amount'))['total'] or 0

        percentage = (spent / budget.limit) * 100
        if percentage >= budget.alert_threshold:
            # Implement email/SMS notification
            pass