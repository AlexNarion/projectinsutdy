from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from datetime import datetime
from .filters import ProductFilter
from .forms import ProductForm



class ProductsList(ListView):
    model = Product
    ordering = 'name'
    template_name = 'products.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        context['filterset'] = self.filterset
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product'


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        form.save()
        return HttpResponseRedirect('/products/')

    form = ProductForm()
    return render(request, 'product_edit.html', {'form': form})








