from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Workshop, Order
workshops = [
    {'id': 1, 'name': 'Деревообработка', 'workers': 10, 'description': 'Обработка дерева для мебели'},
    {'id': 2, 'name': 'Сборка мебели', 'workers': 15, 'description': 'Сборка готовых изделий'},
]

orders = [
    {'id': 1, 'name': 'Стол из дуба', 'workshop_ids': [1], 'status': 'В процессе'},
    {'id': 2, 'name': 'Комплект мебели', 'workshop_ids': [1, 2], 'status': 'Готов'},
]

class WorkshopListView(ListView):
    model = Workshop
    template_name = 'factory/workshop_list.html'
    context_object_name = 'workshops'


class OrderListView(ListView):
    model = Order
    template_name = 'factory/order_list.html'
    context_object_name = 'orders'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'factory/order_detail.html'

def home(request):
    return render(request, 'factory/home.html')

def workshop_detail(request, workshop_id):
    workshop = get_object_or_404(Workshop, pk=workshop_id)
    return render(request, 'factory/workshop_detail.html', {
        'workshop': workshop
    })


def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    related_workshops = order.workshops.all()
    return render(request, 'factory/order_detail.html', {
        'order': order,
        'related_workshops': related_workshops
    })

