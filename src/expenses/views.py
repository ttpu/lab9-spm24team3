# filepath: /expense_tracker/expenses/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Expense
from django.views.decorators.csrf import csrf_exempt
import json
from .forms import ExpenseForm
import logging



logger = logging.getLogger(__name__)


def index(request):
    expenses = Expense.objects.all()
    return render(request, 'index.html', {'expenses': expenses})

def get_expenses(request):
    expenses = list(Expense.objects.values())
    return JsonResponse({'expenses': expenses})

@csrf_exempt
def add_expense(request):
    if request.method == 'POST':
        try:
            logger.debug(f"Request body: {request.body}")
            data = json.loads(request.body)
            expense = Expense.objects.create(
                date=data['date'],
                title=data['title'],
                category=data['category'],
                amount=data['amount']
            )
            return JsonResponse({'id': expense.id})
        except json.JSONDecodeError:
            return HttpResponseBadRequest("Invalid JSON")
        except KeyError as e:
            return HttpResponseBadRequest(f"Missing key: {e}")



# @csrf_exempt
# def delete_expense(request, id):
#     # Support POST method override for DELETE
#     method = request.POST.get('_method', request.method)

#     if method == 'DELETE':
#         try:
#             expense = Expense.objects.get(id=id)
#             expense.delete()
#             return JsonResponse({'status': 'success'})
#         except Expense.DoesNotExist:
#             return JsonResponse({'status': 'error', 'message': 'Expense not found'}, status=404)
#     else:
#         return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)

def delete_expense(request, id):
    if request.method == 'POST':  # Ensure it's a POST request for deletion
        if request.POST.get('_method') == 'DELETE':

            try:
                expense = Expense.objects.get(id=id)
                expense.delete()
            except Expense.DoesNotExist:
                pass  # Optionally handle the error
        return redirect('index')


def edit_expense(request, id):
    expense = get_object_or_404(Expense, id=id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'edit_expense.html', {'form': form})