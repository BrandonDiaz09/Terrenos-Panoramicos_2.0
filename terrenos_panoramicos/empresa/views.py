from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#Form
from empresa.forms import OfreceForm

#Models
from ventas.models import Inmueble


# Create your views here.
def home(request):
    return render(request, 'ventas/home.html')

def conocenos(request):
    return render(request, 'empresa/conocenos.html')


@login_required
def ofrecer_predio(request):
    if request.method == 'POST':
        form = OfreceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('update_profile')
    else:
        form=OfreceForm()

    return render(
        request=request,
        template_name = 'empresa/ofrece.html',
        context = {
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )