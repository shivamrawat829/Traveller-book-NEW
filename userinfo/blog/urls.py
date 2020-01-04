"""blog URL Configuration
"""
from django.urls import path
from blog import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('contact/',views.contact_us, name='contact'),
    path('about/', views.about_us, name='about'),
    path('<int:pk>-<slug:slug>', views.post_list, name='post_list'),
    path('create/', views.create_post, name ='post_create'),
    path('update/<int:pk>', views.update_post, name='update_post'),
    path('delete/<int:pk>', views.delete_post, name='delete_post'),
    # path('register/', views.register, name='register'),
    # path("login", views.login_request, name="login"),
    # path("logout", views.logout_request, name="logout"),


]