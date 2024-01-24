
from django.urls import path
from .views import MultiplicationTableListView

urlpatterns = [
    path('', MultiplicationTableListView.as_view(), name='multiplication_table/multiplication_table.html'),
]
