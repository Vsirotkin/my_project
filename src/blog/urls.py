from django.urls import path
from .views import *


app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list'),
]
