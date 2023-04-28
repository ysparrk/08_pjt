from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),  # 전체 영화 목록 페이지 조회
    path('<int:movie_pk>/', views.detail, name='detail'), # 단일 영화 상세 페이지 조회
    path('recommended/', views.recommended, name='recommended'), # 추천 영화 페이지 조회
    path('recommended/<int:genre_pk>/', views.genre_recommended, name='genre_recommended'), # 단일 장르 추천 영화
]
