
from django.views.generic.list import ListView
from .models import MultiplicationTable


class MultiplicationTableListView(ListView):
    template_name = 'multiplication_table/multiplication_table.html'
    model = MultiplicationTable
    context_object_name = 'multiplication_records'

    def get_queryset(self):
        numbers = range(1, 11)
        return [MultiplicationTable(number=num) for num in numbers]
