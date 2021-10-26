from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import(
   CreateView, DetailView, ListView, UpdateView, DeleteView
) 

from .forms import VentaForm
from .models import Venta

# Create your views here.
class VentaCreateView(CreateView):
    template_name = 'venta/venta_create.html'
    form_class = VentaForm
    queryset = Venta.objects.all() # <blog>/<modelname>_list.html
    #success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class VentaListView(ListView):
    template_name = 'venta/venta_list.html'
    queryset = Venta.objects.all() # <blog>/<modelname>_list.html


class VentaDetailView(DetailView):
    template_name = 'venta/venta_detail.html'
    #queryset = Cotizazion.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Venta, id=id_)


class VentaUpdateView(UpdateView):
    template_name = 'venta/venta_create.html'
    form_class = VentaForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Venta, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class VentaDeleteView(DeleteView):
    template_name = 'venta/venta_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Venta, id=id_)

    def get_success_url(self):
        return reverse('venta:venta_list')
