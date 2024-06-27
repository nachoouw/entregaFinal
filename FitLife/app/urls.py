
from django.urls import path
from .views import index, carrito2, Entrenamientos, GenerarReceta, habla_nosotro, nutricion
from . import views
from .views import PlanEntrenoListView, plan_entreno_edit , PlanEntrenoDeleteView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name="index"),
    path('carrito/', carrito2, name="carrito2"),
    path('entrenamiento/', Entrenamientos , name="Entrenamiento"),
    path('GenerarReceta/', GenerarReceta, name="GenerarReceta"),
    path('nutricion/', nutricion , name="nutricion"),
    path('hablanosotros/', habla_nosotro, name="hablanosotros"),
    path('plan_entreno/create/', views.plan_entreno_create, name='plan_entreno_create'),
    path('planes_entrenamiento/', PlanEntrenoListView.as_view(), name='plan_entreno_list'),
    path('plan_entreno/<int:pk>/edit/', plan_entreno_edit, name='plan_entreno_edit'),
    path('plan_entreno/<int:pk>/delete/', PlanEntrenoDeleteView.as_view(), name='plan_entreno_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]

