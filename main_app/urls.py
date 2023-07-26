from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('yugioh/', views.yugioh_index, name='index'),
    path('yugioh/<int:yugioh_card_id>/', views.yugioh_detail, name='detail'),
]