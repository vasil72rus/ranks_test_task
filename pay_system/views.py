from django.shortcuts import render, redirect
import stripe
from .models import Item
from django.views.generic.detail import DetailView

stripe.api_key = 'sk_test_51L0OOEFm5dxVGPkG4wckZO1rl5YdWY1nseIwLC1CGMiEWoxiv0kWpwLYSoUEaQAaVofeMX2PnpynhuM7ksG3gmLB009oBI0Jly'


def create_checkout_session(request, id):
    item = Item.objects.get(pk=id)
    print(item)
    session = stripe.checkout.Session.create(
    line_items=[{
        'price_data': {
        'currency': 'rub',
        'product_data': {
            'name': item.name,
            'description': item.description
        },
        'unit_amount': item.price*100,
        },
        'quantity': 1
    }],
    mode='payment',
    success_url='http://127.0.0.1:8000/item/{}'.format(id),
    cancel_url='http://127.0.0.1:8000/item/{}'.format(id),
    )

    return redirect(session.url, code=303)


class ItemDetailView(DetailView):
    template_name = "item_detail.html"
    model = Item