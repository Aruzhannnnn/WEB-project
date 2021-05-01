from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from back.views import *
from back.views.views import comment_list, comment_detail
from back.views.views_cbv import UserListAPIView, UserDetailAPIView, CommentAPIView

urlpatterns = [

    path('login/', obtain_jwt_token),
    path('tours/', TourListAPIView.as_view()),
    path('tours/<int:pk>/',  TourDetailAPIView.as_view()),
    path('about/',  AboutListAPIView.as_view()),
    path('about/<int:pk>/', AboutDetailAPIView.as_view()),
    path('comments/', comment_list),
    path('comments/<int:comment_id>/', comment_detail),
    path('users/', UserListAPIView.as_view(), name='userList'),
    path('users/<int:pk>', UserDetailAPIView.as_view(), name='userDetail'),
    path('comment/', CommentAPIView.as_view()),
    path('comment/<int:pk>/', CommentAPIView.as_view())]
