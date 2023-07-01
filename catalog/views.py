from django.shortcuts import render
from django.views.generic import TemplateView

from catalog.models import Product, Contact


class IndexView(TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()
        return context_data

# def index(request):
#     # Convert QuerySet to List
#     # list_products = list(Product.objects.all())
#     # Print last five records
#     # if len(list_products) >= 5:
#     #     for product in list_products[-5:]:
#     #         print(product)
#     # else:
#     #     for product in list_products:
#     #         print(product)
#
#     # Get all products from catalog
#     products = Product.objects.all()
#
#     context = {
#         'object_list': products,
#     }
#
#     return render(request, 'catalog/index.html', context)

def contacts(request):
    data = Contact.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html',{"contacts": data})


