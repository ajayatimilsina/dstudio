from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('portfolio/', views.portfolio_view, name='portfolio'),
    path('blog/', views.blog_view, name='blog'),
    path('contact/', views.contact_view, name='contact'),
]