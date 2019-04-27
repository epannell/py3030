from django.urls import path
from rules import views

urlpatterns = [
    path('rules/', views.RuleList.as_view(), name="rule-list"),
]