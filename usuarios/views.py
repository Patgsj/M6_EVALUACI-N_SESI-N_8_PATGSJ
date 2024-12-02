from django.shortcuts import render, redirect
from .forms import BookForm, RegistroUsuarioForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import BookForm

def home(request):
    return redirect('inputbook')

def input_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Libro agregado exitosamente!')
            return redirect('success')
    else:
        form = BookForm()
    return render(request, 'usuarios/inputbook.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            messages.success(request, '¡Registro exitoso!')
            login(request, user)
            return redirect('inputbook')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/register.html', {'form': form})

def success(request):
    return render(request, 'usuarios/success.html')  # Renderiza la plantilla success.html
