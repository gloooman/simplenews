from django.urls import path
from news.views import NewsList, NewsDetail, NewsCreate


urlpatterns = [
    path('', NewsList.as_view(), name='home'),
    path('news/<int:id>/', NewsDetail.as_view(), name='news_detail'),
    path('news/create/', NewsCreate.as_view(), name='news_create'),
    # path('comment/create/', CommentCreate.as_view(), name='comment_create'),
]
