from django.urls import path
from .views import HomePageView, AddNewView, MyNewsView, AllNewsView, NewDetailView, NewUpdateView, NewDeleteView, SearchView, CategoryPageView

app_name = "home"
urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('add-new/', AddNewView.as_view(), name='add_new'),
    path('detail-new/<uuid:uuid>/', NewDetailView.as_view(), name='new_detail'),
    path('new-update/<uuid:uuid>/', NewUpdateView.as_view(), name='new_update'),
    path('new-delete/<uuid:uuid>/', NewDeleteView.as_view(), name='new_delete'),
    path('my-news/', MyNewsView.as_view(), name='my_news'),
    path('all-news/', AllNewsView.as_view(), name='all_news'),
    path('search/', SearchView.as_view(), name='search'),
    path('category/<uuid:uuid>/', CategoryPageView.as_view(), name='category'),
]