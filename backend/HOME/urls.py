from django.urls import path
from . import views

urlpatterns = [
   path('search/username/',views.SearchView.as_view(),name='username_search'),
]
