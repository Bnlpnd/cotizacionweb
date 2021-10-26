from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import(
    CreateView, DetailView, ListView, UpdateView, DeleteView
)

from .forms import ModeloForm
from .models import Modelo

class ModeloCreateView(CreateView):
    template_name = 'modelo/modelo_create.html'
    form_class = ModeloForm
    queryset = Modelo.objects.all() # <blog>/<modelname>_list.html
    #success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ModeloListView(ListView):
    template_name = 'modelo/modelo_list.html'
    queryset = Modelo.objects.all() # <blog>/<modelname>_list.html


class ModeloDetailView(DetailView):
    template_name = 'modelo/modelo_detail.html'
    #queryset = Modelo.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Modelo, id=id_)


class ModeloUpdateView(UpdateView):
    template_name = 'modelo/modelo_create.html'
    form_class = ModeloForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Modelo, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class ModeloDeleteView(DeleteView):
    template_name = 'modelo/modelo_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Modelo, id=id_)

    def get_success_url(self):
        return reverse('modelo:modelo_list')
