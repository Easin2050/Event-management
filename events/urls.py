from django.urls import path
from events.views import home_page,event_page
urlpatterns = [
  path('home-page/',home_page,name="home-page"),
  path('event_page/',event_page,name="event-page")
]
