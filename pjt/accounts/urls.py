from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'), # 회원 생성 페이지 조회 & 단일 회원 데이터 생성 (회원가입)
    path('login/', views.login, name='login'), # 로그인 페이지 조회 & 세션 데이터 생성 및 저장 (로그인)
    path('logout/', views.logout, name='logout'), # 세션 데이터 삭제 (로그아웃)
    path('profile/<username>/', views.profile, name='profile'), # 사용자 상세 조회 페이지 (프로필 조회)
    path('<int:user_pk>/follow/', views.follow, name='follow'), # 사용자 팔로우 기능
]
