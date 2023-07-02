from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import IndexView, contacts, BlogListView, BlogCreateView, \
    BlogDetailView, BlogUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_view'),
    path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='blog_edit'),
]