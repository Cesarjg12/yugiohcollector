from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('yugioh/', views.yugioh_index, name='index'),
    path('yugioh/<int:yugioh_card_id>/', views.yugioh_detail, name='detail'),
    path('yugioh/create/', views.YugiohCreate.as_view(), name='Yugioh_create'),
    path('yugioh/<int:pk>/update/', views.YugiohUpdate.as_view(), name='Yugioh_update'),
    path('yugioh/<int:pk>/delete/', views.YugiohDelete.as_view(), name='Yugioh_delete'),
]