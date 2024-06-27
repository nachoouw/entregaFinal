from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomLoginForm,CustomUserCreationForm
from .models import PlanEntreno
from .forms import PlanEntrenoForm
from django.views import View
from django.contrib import messages 

# Las que tenÃ­amos
def index(request):
    return render(request, 'app/index.html')

def carrito2(request):
    return render(request, 'app/carrito2.html')

def Entrenamientos(request):
    return render(request, 'app/Entrenamientos.html')

def GenerarReceta(request):
    return render(request, 'app/GenerarReceta.html')

def nutricion(request):
    return render(request, 'app/nutricion.html')

def habla_nosotro(request):
    return render(request, 'app/habla_nosotro.html')

# Nuevas vistas para PlanEntreno
def plan_entreno_create(request):
    if request.method == 'POST':
        form = PlanEntrenoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/plan_entreno/create/')  # Ajusta esto a tu vista de lista
    else:
        form = PlanEntrenoForm()
    return render(request, 'app/PlanEntreno.html', {'form': form})

class PlanEntrenoListView(View):
    template_name = 'app/plan_entreno_list.html'  # Nombre del template donde se listará
    
    def get(self, request):
        planes_entrenamiento = PlanEntreno.objects.all()
        return render(request, self.template_name, {'planes_entrenamiento': planes_entrenamiento})

def plan_entreno_edit(request, pk):
    plan_entreno = get_object_or_404(PlanEntreno, pk=pk)

    if request.method == 'POST':
        form = PlanEntrenoForm(request.POST, instance=plan_entreno)
        if form.is_valid():
            form.save()
            return redirect('plan_entreno_list')  # Redirigir a la lista de planes de entrenamiento después de editar
    else:
        form = PlanEntrenoForm(instance=plan_entreno)

    return render(request, 'app/PlanEntreno.html', {'form': form})


class PlanEntrenoDeleteView(View):
    template_name = 'app/plan_entreno_confirm_delete.html'  # Nombre del template para confirmar eliminación
    
    def get(self, request, pk):
        plan_entreno = get_object_or_404(PlanEntreno, pk=pk)
        return render(request, self.template_name, {'plan_entreno': plan_entreno})
    
    def post(self, request, pk):
        plan_entreno = get_object_or_404(PlanEntreno, pk=pk)
        plan_entreno.delete()
        return redirect('plan_entreno_list')


def custom_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['username'] = username
                return redirect('dashboard')  # Redirigir a la página principal después de iniciar sesión
            else:
                messages.error(request, 'Credenciales inválidas. Por favor, intenta de nuevo.')
    else:
        form = CustomLoginForm()

    return render(request, 'app/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Puedes personalizar la redirección después del registro aquí
            return redirect('login')  # Redirigir a la página de inicio de sesión después del registro exitoso
    else:
        form = CustomUserCreationForm()

    return render(request, 'app/register.html', {'form': form})

def LogoutView(request):
    logout(request)
    return redirect('dashboard')
