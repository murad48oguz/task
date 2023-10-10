
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('login', views.loginPage, name="loginPage"),
   path('logout/', views.user_logout, name='user_logout'),
   path('userPage', views.userPage, name="userPage"),
   path('upload', views.upload, name="upload"),
   path('userFiles',views.user_files,name="userFiles"),
   # path('userDetail',views.user_detail,name="userDetail"),
   path('share/<int:file_id>/', views.share_file, name='share_file'),
]

