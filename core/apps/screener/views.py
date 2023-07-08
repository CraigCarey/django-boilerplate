from django.shortcuts import render
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

from .filters import ProductUniversalFilter
from .models import Product
from .tables import ProductHTMxTable


def home(request):
    return render(request, 'screener/home.html')


class PandasHTMxTableView(SingleTableMixin, FilterView):
    table_class = ProductHTMxTable
    queryset = Product.objects.all()
    filterset_class = ProductUniversalFilter
    paginate_by = 10

    def get_template_names(self):
        template_name = 'products/product_table_htmx_pandas.html'

        return template_name
