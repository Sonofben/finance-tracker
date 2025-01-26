from rest_framework import serializers
from .models import Transaction, RecurringTransaction, BillReminder, SavingsGoal

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'category', 'type', 'date', 'description']

class RecurringTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecurringTransaction
        fields = ['id', 'amount', 'category', 'frequency', 'next_payment_date', 'is_active']

class BillReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillReminder
        fields = ['id', 'name', 'amount', 'due_date', 'is_paid', 'transaction']

class SavingsGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsGoal
        fields = ['id', 'name', 'target_amount', 'current_amount', 'target_date', 'is_completed']