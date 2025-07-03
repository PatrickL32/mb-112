from django.urls import path
from posts import views


urlpatterns =[
    path("",views.PostListView.as_view(),name="list"),
    path("<init:pk>/" ,views.PostDetailView.as_view(),name="detail"),
]