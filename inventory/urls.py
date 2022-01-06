from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import re_path, include
from inventory.views import InventoryList


app_name = 'inventory'

urlpatterns = [
    re_path(r'^$', InventoryList.as_view(), name='inventory_list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
