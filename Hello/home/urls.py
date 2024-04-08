from django.contrib import admin
from django.urls import path,include
from home import views
urlpatterns = [
    path("index", views.index, name='index'),
    path("customers", views.customers, name='customers'),
    path("orders", views.orders, name='orders'),
    path("analytics", views.analytics, name='analytics'),
    path("messages", views.messages, name='messages'),
    path("products", views.products, name='products'),
    path("reports", views.reports, name='reports'),
    path("settings", views.settings, name='settings'),
    path("addproduct", views.addproduct, name='addproduct'),
    path("", views.login, name='login'),
    path('<str:room>/',views.room,name='room'),
    path('checkview',views.checkview,name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    
]

