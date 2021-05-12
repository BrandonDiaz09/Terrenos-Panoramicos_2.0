from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from django.http import JsonResponse

# Models
from ventas.models import Inmueble


class InmuebleView(LoginRequiredMixin, ListView):
    """Return published inmuebles."""

    template_name = 'ventas/catalogo.html'
    #model = Inmueble
    queryset = Inmueble.objects.filter(status__exact='OF')
    #ordering = ('-created',)
    #paginate_by = 4
    context_object_name = 'inmuebles'

# @login_required
# def catalogo_view(request):
#     return render(request, 'ventas/catalogo.html')

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