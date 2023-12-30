from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import News, Category
from .forms import AddNewsForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from hitcount.views import HitCountDetailView
# Create your views here.


class HomePageView(HitCountDetailView):
    count_hit = True
    def get(self, request):
        news = News.objects.filter(is_active=True).order_by('-create_at')[:10]
        context = {
            'news' : news
        }
        return render(request, 'home.html', context)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['hit_count'] = self.get_hit_count()
    #     return context




class AddNewView(LoginRequiredMixin, CreateView):
    model = News
    form_class = AddNewsForm
    template_name = "add_new.html"
    success_url = reverse_lazy("home:home_page")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form )


class MyNewsView(LoginRequiredMixin, ListView, HitCountDetailView):
    template_name = 'my_news.html'
    model = News
    count_hit = True
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['my_news'] = News.objects.filter(user=self.request.user).order_by('-create_at')
        return context


class AllNewsView(LoginRequiredMixin, HitCountDetailView):
    count_hit = True
    def get(self, request):
        if self.request.user.is_superuser:
            all_news = News.objects.filter(user=self.request.user).order_by('-create_at')
            context ={
                'all_news' : all_news
            }
        return render(request, 'all_news.html', context)
    

class NewDetailView(HitCountDetailView, DetailView):
    count_hit = True
    def get(self, request, uuid):
        news = News.objects.filter(is_active=True, uuid=uuid)
        category = News.objects.filter(is_active=True, category=news[0].category).order_by('-create_at')[:3]
        for i in category:
            if i.uuid==news[0].uuid:
                category = News.objects.filter(is_active=True, category=news[0].category).order_by('-create_at')[:4]
                break
        context = {
            'new_detail' : news,
            'recomendation' : category,
        }
        return render(request, 'new_detail_page.html', context)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hit_count'] = self.get_hit_count()
        return context


class NewUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, HitCountDetailView):
    model = News
    template_name = "new_update.html"
    form_class = AddNewsForm
    count_hit = True
    
    def get_object(self, queryset=None):
        return News.objects.get(uuid=self.kwargs['uuid'])
    
    def get_success_url(self) -> str:
        uuid = self.kwargs['uuid']
        return reverse("home:new_detail", kwargs={'uuid':uuid})
    
    def test_func(self) -> bool | None:
        obj = self.get_object()
        return obj.user == self.request.user or self.request.user.is_superuser


class NewDeleteView(LoginRequiredMixin, UserPassesTestMixin, HitCountDetailView):
    count_hit = True
    template_name = 'new_delete.html'

    def get(self, request, uuid):
        new_delete = News.objects.filter(uuid=uuid)
        return render(request, self.template_name, {'new_delete':new_delete})

    def post(self, request, uuid):
        object = get_object_or_404(News, uuid=uuid)
        object.is_active = False
        object.save()
        return redirect('home:home_page')

    def test_func(self) -> bool | None:
        obj = get_object_or_404(News, uuid=self.kwargs['uuid'])
        return obj.user == self.request.user or self.request.user.is_superuser


class SearchView(ListView):
    template_name = 'search.html'
    model = News

    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get("search")
        object_list = News.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query) | Q(body__icontains=query)
        )
        return object_list

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get("search")
        return context
    

class CategoryPageView(HitCountDetailView):
    count_hit = True
    def get(self, request, uuid):
        category = Category.objects.get(uuid=uuid)
        news_category = category.news_category.all().order_by('-create_at')
        context = {
            'news' : news_category
        }
        return render(request, 'home.html', context)







