from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView
from pytils.translit import slugify

from catalog.models import Product, Contact, Blog


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


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'date_created', 'preview')
    success_url = reverse_lazy('catalog:blog_list')

    def form_valid(self, form):
        if form.is_valid:
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()

        return super().form_valid(form)

class BlogListView(ListView):
    model = Blog

    # def query(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     return queryset

