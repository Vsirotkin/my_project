from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .forms import ArticleModelForm
from .models import Article


# Create your views here.
class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    success_url = '/'


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'


    def get_object(self, queryset=None):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=id_)


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()
    success_url = reverse_lazy('articles:article_list')

    def get_object(self, queryset=None):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=id_)


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('articles:article_list')

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=id_)