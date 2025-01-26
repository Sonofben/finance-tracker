from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import RecurringTransaction, BillReminder, SavingsGoal
from .serializers import (
    RecurringTransactionSerializer,
    BillReminderSerializer,
    SavingsGoalSerializer
)

# Recurring Subscriptions View
class RecurringTransactionViewSet(viewsets.ModelViewSet):
    serializer_class = RecurringTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return RecurringTransaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Bill Reminders View
class BillReminderViewSet(viewsets.ModelViewSet):
    serializer_class = BillReminderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BillReminder.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Savings Goals View
class SavingsGoalViewSet(viewsets.ModelViewSet):
    serializer_class = SavingsGoalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SavingsGoal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)