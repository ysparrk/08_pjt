from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.index, name='index'), # 전체 리뷰 목록 페이지 조회
    path('create/', views.create, name='create'), # 새로운 리뷰 생성 페이지 조회 & 단일 리뷰 데이터 저장
    path('<int:review_pk>/', views.detail, name='detail'), # 단일 리뷰 상세 페이지 조회
    path('<int:review_pk>/comments/create/', views.create_comment, name='create_comment'), # 단일 댓글 데이터 저장
    path('<int:review_pk>/like/', views.like, name='like'), # 단일 리뷰 좋아요 기능
]
