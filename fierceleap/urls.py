from django.urls import path
from .views import contact_view 
from .views import index_view

urlpatterns = [
    path('', index_view, name='index'),  # Renders the index.html file
    path('contact/', contact_view, name='contact'),
]
