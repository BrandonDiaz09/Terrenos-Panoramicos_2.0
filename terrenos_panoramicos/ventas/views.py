from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from django.http import JsonResponse

from django.db.models import Q

# Models
from ventas.models import Inmueble


# class InmuebleView(LoginRequiredMixin, ListView):
#     """Return published inmuebles."""

#     template_name = 'ventas/catalogo.html'
#     model = Inmueble
#     queryset = Inmueble.objects.filter(status__exact='Oferta')
#     ordering = ('-created',)
#     paginate_by = 4
#     context_object_name = 'inmuebles'

@login_required
def catalogo_view(request):
    #Inmuebles con una superfice menor a 250m
    inmuebles_todos = Inmueble.objects.filter(status__exact='Oferta').all()
    #Inmuebles con una superfice menor a 250m
    inmuebles_sup_menos250 = Inmueble.objects.filter(Q(status__exact='Oferta'), Q(surface__lt = 250))
    #Inmuebles con una frente mayor a 10m
    inmuebles_front_mas10 = Inmueble.objects.filter(Q(status__exact='Oferta'), Q(front__gt = 250))
    #Inmueble con un fondo mayor a 16m
    inmuebles_bot_mas15 = Inmueble.objects.filter(Q(status__exact='Oferta'), Q(bottom__gt = 250))
    #Inmueble con un precio menor a 20 mil persos por metro cuandrado
    inmuebles_precio_menos20k = Inmueble.objects.filter(Q(status__exact='Oferta'), Q(price__lt = 20000))
    #Inmueble con una precio total menor a un millón de pesos
    inmuebles_Totprecio_menos1m = Inmueble.objects.filter(Q(status__exact='Oferta'), Q(totalprice__lt = 100000))
    #Inmueble con con regimen proiedad privada
    inmuebles_rp_privada = Inmueble.objects.filter(Q(status__exact='Oferta'), Q(regimen_propiedad__exact = 'Privada'))
    #inmueble con regimen proviedad ejidL
    inmuebles_rp_ejidal = Inmueble.objects.filter(Q(status__exact='Oferta'), Q(regimen_propiedad__exact = 'Ejidal'))
    #Inmueble con regimen propiedad comunal
    inmuebles_rp_comunal = Inmueble.objects.filter(Q(status__exact='Oferta'), Q(regimen_propiedad__exact = 'Comunal'))
    #Inmuebles con uso de suelo residencial
    inmuebles_us_residencial = Inmueble.objects.filter(Q(status__exact='Oferta'), Q(uso_suelo__exact = 'Residencial'))
    #Inmuebles con uso de suelo actividades productivas
    inmuebles_us_ap = Inmueble.objects.filter(Q(status__exact='Oferta'), Q(uso_suelo__exact = 'Residencial'))
    #Inmuebles con uso de suelo residencial
    inmuebles_us_residencial = Inmueble.objects.filter(Q(status__exact='Oferta'), Q(uso_suelo__exact = 'Actividades Productivas'))
    #Inmuebles con uso de suelo Equipamiento
    inmuebles_us_equipamiento = Inmueble.objects.filter(Q(status__exact='Oferta'), Q(uso_suelo__exact = 'Equipamiento'))
    #Inmuebles con uso de suelo Infraestructura
    inmuebles_us_infraestructura = Inmueble.objects.filter(Q(status__exact='Oferta'), Q(uso_suelo__exact = 'Infraestructura'))
    #Inmuebles con uso de suelo Area Verde
    inmuebles_us_averde = Inmueble.objects.filter(Q(status__exact='Oferta'), Q(uso_suelo__exact = 'Area Verde'))
    
    querset = request.GET.get("buscar")
    if querset:
        inmuebles = Inmueble.objects.filter(
            Q(status__exact='Oferta'),
            Q(description__icontains=querset) | 
            Q(surface__icontains=querset) | 
            Q(front__icontains=querset) | 
            Q(bottom__icontains=querset) | 
            Q(price__icontains=querset) | 
            Q(totalprice__icontains=querset)
        ).distinct() 

    return render(request, 'ventas/catalogo.html', {inmuebles_todos:'inmuebles_todos',
                                                    inmuebles_sup_menos250:'inmuebles_sup_menos250',
                                                    inmuebles_front_mas10:'inmuebles_front_mas10',
                                                    inmuebles_bot_mas15:'inmuebles_bot_mas15',
                                                    inmuebles_precio_menos20k:'inmuebles_precio_menos20k',
                                                    inmuebles_Totprecio_menos1m:'inmuebles_Totprecio_menos1m',
                                                    inmuebles_rp_privada:'inmuebles_rp_privada',
                                                    inmuebles_rp_ejidal:'inmuebles_rp_ejidal',
                                                    inmuebles_rp_comunal:'inmuebles_rp_comunal',
                                                    inmuebles_us_residencial:'inmuebles_us_residencial',
                                                    inmuebles_us_ap:'inmuebles_us_ap',
                                                    inmuebles_us_residencial:'inmuebles_us_residencial',
                                                    inmuebles_us_equipamiento:'inmuebles_us_equipamiento',
                                                    inmuebles_us_infraestructura:'inmuebles_us_infraestructura',
                                                    inmuebles_us_averde:'inmuebles_us_averde',
                                                    })

def me_interesa(request):
    user=request.user
    if request.method == 'POST':
        inmueble_id = request.POST['inmueble_id']
        inmueble_obj= Inmueble.objects.get(id=inmueble_id)
        if user in inmueble_obj.interesados.all():
            inmueble_obj.interesados.remove(user)
        else:
            inmueble_obj.interesados.add(user)
        data = {
            'interesados' : inmueble_obj.interesados.all().count()
        }
        return JsonResponse(data,safe=False)
    return redirect('catalogo')