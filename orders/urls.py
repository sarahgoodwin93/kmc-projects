from django.urls import path
from . import views
from .views import OrderView

urlpatterns = [
    path('', views.OrderView, name='orders'),
    path('remove/<item_id>/', views.remove_from_order, name='remove_from_order'),  # noqa
    path('order_success/<order_number>', views.order_success, name='order_success'),  # noqa
]