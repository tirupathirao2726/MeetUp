from django.urls import path
from MeetUp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('active/<str:topic>/<str:current>/',views.active_users_on_topic,name='active_users')
]