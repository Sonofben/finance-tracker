from django.contrib import admin
from .models import (
    Transaction,
    Budget,
    UserProfile,  # Now defined!
    RecurringTransaction,
    BillReminder,
    SavingsGoal
)

admin.site.register(Transaction)
admin.site.register(Budget)
admin.site.register(UserProfile)
admin.site.register(RecurringTransaction)
admin.site.register(BillReminder)
admin.site.register(SavingsGoal)