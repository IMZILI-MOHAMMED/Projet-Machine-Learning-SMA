from django.urls import path, include
from .views import morocco,countries_list,home,get_info_by_country,trendingNews
urlpatterns = [
    path('all', home),
    path('morocco/', morocco),
    path('news/', trendingNews),
    path('countries/', countries_list),
    path('countries/<country>', get_info_by_country),
]