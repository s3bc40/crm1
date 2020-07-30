from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('user/', views.userPage, name='user-page'),

    path('account/', views.accountSettings, name='account'),

    path('products/', views.products, name='products'),
    path('customer/<int:pk>/', views.customer, name='customer'),
    
    path('create_order/<int:pk>/', views.createOrder, name='create_order'),
    path('update_order/<int:pk>/', views.updateOrder, name='update_order'),    
    path('delete_order/<int:pk>/', views.deleteOrder, name='delete_order'),

    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'), # form for submit email
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'), # message success sent email to change password
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'), # link in email to submit their password
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'), # password successfully changed
]
