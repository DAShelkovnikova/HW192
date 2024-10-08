from catalog.apps import CatalogConfig
from django.urls import path
from catalog.views import home
from catalog.views import contact

app_name = CatalogConfig.name
urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contact, name='contacts')
]
