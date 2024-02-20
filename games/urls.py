from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page, name='home'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('shop/', shop_page, name='shop'),
    path('detail/<int:game_id>/', detail_page, name='detail'),
    path('contact/', contact_page, name='contact'),
    path('check_username/', check_username, name='check_username'),
    path('logout/', user_logout, name='logout'),
    path('game_reviews/<int:game_id>/', game_reviews, name='game_reviews'),
    path('download_count/', download_count, name='downloaded'),
    path('profile/', profile_page, name='profile'),
]
