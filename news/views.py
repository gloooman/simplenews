from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView
from news.form import CommentForm, NewsForm

from news.models import News


class NewsList(ListView):
    queryset = News.objects.filter(status='APR')
    template_name = 'home.html'


class NewsDetail(FormView, DetailView):
    model = News
    template_name = 'news_detail.html'
    pk_url_kwarg = 'id'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(NewsDetail, self).get_context_data(**kwargs)
        try:
            context['comments'] = self.get_object().comment_set.all()
        except:
            pass
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print('form is valid')
            comment = form.save(commit=False)
            print(self.get_object())
            comment.news = self.get_object()
            comment.save()
            return redirect(comment.news)
        return redirect(self.get_object())


class NewsCreate(CreateView):
    form_class = NewsForm
    template_name = 'news_create.html'

    def post(self, request, *args, **kwargs):
        form = NewsForm(request.POST)
        if form.is_valid():
            new_news = form.save(commit=False)
            new_news.author = request.user
            if not new_news.author.premoderation:
                new_news.status = "APR"
            new_news.save()
            return redirect(new_news)
        return render(request, self.template_name)


# class CommentCreate(CreateView):
#     form_class = NewsForm
#     template_name = 'news_create.html'
#
#     def post(self, request, *args, **kwargs):
#         pass
