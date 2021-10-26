from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import(
   CreateView, DetailView, ListView, UpdateView, DeleteView
)

from .forms import MaterialForm
from .models import Material


class MaterialCreateView(CreateView):
    template_name = 'material/material_create.html'
    form_class = MaterialForm
    queryset = Material.objects.all() # <blog>/<modelname>_list.html
    #success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class MaterialListView(ListView):
    template_name = 'material/material_list.html'
    queryset = Material.objects.all() # <blog>/<modelname>_list.html


class MaterialDetailView(DetailView):
    template_name = 'material/material_detail.html'
    #queryset = Material.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Material, id=id_)


class MaterialUpdateView(UpdateView):
    template_name = 'material/material_create.html'
    form_class = MaterialForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Material, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class MaterialDeleteView(DeleteView):
    template_name = 'material/material_delete.html'
    
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Material, id=id_)

    def get_success_url(self):
        return reverse('material:material_list')
