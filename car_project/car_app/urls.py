from django.urls import path
from car_app import views as v
urlpatterns = [
    path("",v.index , name='home'),
    path("login/page/",v.login),
    path("register",v.register),
    path('users/', v.user_list, name='user-list'),
    path('users/<int:pk>/', v.user_detail, name='user-detail'),
    path('login/', v.login_view, name='login_view'),


    path('create_car/', v.create_car, name='create_car'),
    path('edit_car/<int:car_id>', v.edit_car, name='create_car'),
    path('book_car/<int:car_id>/<int:user_id>/', v.book_car, name='book_car'),
    path('view_bookings/', v.view_bookings, name='view_bookings'),


    path('cars/', v.car_list, name='car-list'),
    path('cars/<int:pk>/', v.car_detail, name='car-detail'),
    path('bookings/', v.booking_list, name='booking-list'),
    path('bookings/<int:pk>/', v.booking_detail, name='booking-detail'),

]