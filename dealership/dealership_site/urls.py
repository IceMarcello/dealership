from django.contrib import admin
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, CalculatorView#, CalculationView

urlpatterns = [
    path('', PostListView.as_view(), name='dealership-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='dealership-about'),
    path('calculator/', CalculatorView.as_view(), name="dealership-calculator"),
    # path('calculation/', CalculationView.as_view(), name="dealership-calculation"),
    path('calculation/', views.calculation),
]