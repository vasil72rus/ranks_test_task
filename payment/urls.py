from django.contrib import admin
from django.urls import path
from pay_system.views import create_checkout_session, ItemDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buy/<int:id>', create_checkout_session, name='buy_id'),
    path('item/<int:pk>', ItemDetailView.as_view(), name='item_id'),
]
