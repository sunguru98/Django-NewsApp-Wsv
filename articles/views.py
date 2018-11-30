from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Article
# Create your views here.


class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"
    context_object_name = "article"

    
class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = "article_update.html"
    success_url = reverse_lazy("articles_app:article_list")


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("articles_app:article_list")


class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_create.html"
    fields = ("title", "body")
    success_url = reverse_lazy("articles_app:article_list")

    def form_valid(self, form):
        print(self.request.user)
        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form)