from django.urls import path
from events.views import home_page
urlpatterns = [
  path('home-page/',home_page,name="home-page")
]
