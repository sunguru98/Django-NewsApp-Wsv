from django.urls import path
from . import views

app_name = "articles_app"

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="article_list"),
    path("<int:pk>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("delete/<int:pk>/", views.ArticleDeleteView.as_view(), name="article_delete"),
    path("edit/<int:pk>/", views.ArticleUpdateView.as_view(), name="article_edit"),
    path("new/", views.ArticleCreateView.as_view(), name="article_create")
]