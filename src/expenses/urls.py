# filepath: /expense_tracker/expenses/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/expenses', views.get_expenses, name='get_expenses'),
    path('api/expenses/add', views.add_expense, name='add_expense'),
    path('delete/<int:id>', views.delete_expense, name='delete_expense'),
    path('edit/<int:id>', views.edit_expense, name='edit_expense'),  # New edit path
]