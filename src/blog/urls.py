from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView


app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
    path('create/', ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
]
