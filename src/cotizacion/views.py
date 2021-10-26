from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import(
   CreateView, DetailView, ListView, UpdateView, DeleteView
) 

from .forms import CotizacionForm
from .models import Cotizacion

# Create your views here.
class CotizacionCreateView(CreateView):
    template_name = 'cotizacion/cotizacion_create.html'
    form_class = CotizacionForm
    queryset = Cotizacion.objects.all() # <blog>/<modelname>_list.html
    #success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class CotizacionListView(ListView):
    template_name = 'cotizacion/cotizacion_list.html'
    queryset = Cotizacion.objects.all() # <blog>/<modelname>_list.html


class CotizacionDetailView(DetailView):
    template_name = 'cotizacion/cotizacion_detail.html'
    #queryset = Cotizazion.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Cotizacion, id=id_)


class CotizacionUpdateView(UpdateView):
    template_name = 'cotizacion/cotizacion_create.html'
    form_class = CotizacionForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Cotizacion, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class CotizacionDeleteView(DeleteView):
    template_name = 'cotizacion/cotizacion_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Cotizacion, id=id_)

    def get_success_url(self):
        return reverse('cotizacion:cotizacion_list')
