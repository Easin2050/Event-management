from django.urls import path
from events.views import home_page,event_page,dashboard,base,create_event,create_participant,create_category,search,update_event,delete_event
urlpatterns = [
  path('home-page/',home_page,name="home-page"),
  path('event-page/<int:id>/',event_page,name="event-page"),
  path('create-event/',create_event,name="create-event"),
  path('create-participant/',create_participant,name="create-participant"),
  path('create-category/',create_category,name="create-category"),
  path('dashboard/',dashboard,name="dashboard"),
  path('search/',search,name="search"),
  path('base/',base,name="base"),
  path('update/<int:id>/',update_event,name="update"),
  path('delete/<int:id>/',delete_event,name="delete"),
]
