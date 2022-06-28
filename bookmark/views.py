from django.shortcuts import render

from django.views.generic.list import ListView

from .models import Bookmark2

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView


class BookmarkCreateView(CreateView):
    model = Bookmark2
    fields = ['site_name','url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkListView(ListView):
    model = Bookmark2
    paginate_by = 2

class BookMarkDetailView(DetailView):
    model = Bookmark2

class BookmarkUpdateView(UpdateView):
    model = Bookmark2
    fields = ['site_name','url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark2
    success_url = reverse_lazy('list')


# Create your views here.




