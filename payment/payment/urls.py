from django.contrib import admin
from django.urls import path
from pay_system.views import buy_item, ItemDetailView, buy_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:id>', buy_item, name='buy_id'),
    path('item/<int:pk>', ItemDetailView.as_view(), name='item_id'),
    path('order/<int:id>', buy_order, name='order_id'),
]
