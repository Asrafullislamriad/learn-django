 
from django.urls import   path
from .views import TodoGetCreate,TodoSerilizer
urlpatterns = [
   path("",TodoGetCreate.as_view()), 
   path("<int:pk>",TodoGetCreate.as_view()),
]
