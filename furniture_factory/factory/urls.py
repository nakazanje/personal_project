from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('workshops/', views.WorkshopListView.as_view(), name='workshop_list'),
    path('orders/', views.OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('workshops/<int:workshop_id>/', views.workshop_detail, name='workshop_detail'),
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
]



