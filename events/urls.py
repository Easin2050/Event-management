from django.urls import path
from events.views import home_page,event_page,create_event,show_dashboard,base
urlpatterns = [
  path('home-page/',home_page,name="home-page"),
  path('event-page/',event_page,name="event-page"),
  path('create-event/',create_event,name="create-event"),
  path('show-dashboard/',show_dashboard,name="show-dashboard"),
  path('base/',base,name="base"),
]
