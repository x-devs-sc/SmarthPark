from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.LoginPage, name='login'),
    path('index/', views.IndexPage, name='index'),
    path('index/cadastro/', views.CadastroPage, name='cadastro'),
    path('logout/', views.LogoutPage, name='logout'),

]
