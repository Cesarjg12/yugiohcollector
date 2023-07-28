from django.urls import path
from . import views
	
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('yugioh/', views.yugioh_index, name='index'),
    path('yugioh/<int:yugioh_card_id>/', views.yugioh_detail, name='yugioh_detail'),
    path('yugioh/create/', views.YugiohCreate.as_view(), name='Yugioh_create'),
    path('yugioh/<int:pk>/update/', views.YugiohUpdate.as_view(), name='Yugioh_update'),
    path('yugioh/<int:pk>/delete/', views.YugiohDelete.as_view(), name='Yugioh_delete'),
    path('yugioh/<int:yugioh_card_id>/assoc_deck/<int:deck_id>/', views.assoc_deck, name='assoc_deck'),
    path('yugioh/<int:yugioh_card_id>/unassoc_deck/<int:deck_id>/', views.unassoc_deck, name='unassoc_deck'),
    path('deck/', views.DeckList.as_view(), name='deck_index'),
    path('deck/<int:pk>/', views.DeckDetail.as_view(), name='deck_detail'),
    path('deck/create/', views.DeckCreate.as_view(), name='deck_create'),
    path('deck/<int:pk>/update/', views.DeckUpdate.as_view(), name='deck_update'),
    path('deck/<int:pk>/delete/', views.DeckDelete.as_view(), name='deck_delete'),
]