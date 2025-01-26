from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RecurringTransactionViewSet,
    BillReminderViewSet,
    SavingsGoalViewSet
)

router = DefaultRouter()
router.register(r'subscriptions', RecurringTransactionViewSet, basename='subscription')
router.register(r'bills', BillReminderViewSet, basename='bill')
router.register(r'savings-goals', SavingsGoalViewSet, basename='savings-goal')

urlpatterns = [
    path('', include(router.urls)),
]