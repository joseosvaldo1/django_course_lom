from django.urls import path
from recipes.views import home, about, contact


# dominio/recipes/sobre
urlpatterns = [
    path('', home),             # Home
    path('about/', about),      # About (sobre)      /about
    path('contact/', contact),  # Contact (contato)  /contact         
]