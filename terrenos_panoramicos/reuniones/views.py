from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, permission_required

#Models
from django.contrib.auth.models import User
from reuniones.models import Reunion, Servicio_Reunion

#Forms
from reuniones.forms import ReunionForm

from datetime import date

@login_required
@permission_required('reuniones.add_reunion',raise_exception=True)
def solicitar_reunion(request): #yyyy-MM-ddThh:mm
    hoy = date.today().strftime('%Y-%m-%dT%H:%M')
    if request.method == 'POST':
        form = ReunionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReunionForm()

    return render(
        request=request,
        template_name='reuniones/reuniones.html',
        context={
            'hoy':hoy,
            'form':form,
            'user':request.user,
            'reuniones': Servicio_Reunion.objects.all()
        }
    )
