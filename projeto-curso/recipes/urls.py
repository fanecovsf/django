from django.urls import path
from recipes.views import *

urlpatterns = [
    path('', home),
    path('sobre/', about),
    path('contato/', contact),
]