from atexit import register
from django.urls import path
from .import views
from .views import HotelListView,BookingList,BookingView,HotelDetailView,HotelList

app_name='projects'

urlpatterns=[
    path('',views.home, name='home'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('scenaries',views.scenaries,name='scenaries'),
    path('booking',views.booking,name='booking'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('hotel_list/',HotelList.as_view(),name='HotelList'),
    path('booking_list/',BookingList.as_view,name='BookingList'),
    path('book',BookingView.as_view,name='BookingView'),
    path('hotel/<category>',HotelDetailView.as_view,name='HotelDetailView'),
   # path('project/<str:pk>',views.project,name="project"),
]