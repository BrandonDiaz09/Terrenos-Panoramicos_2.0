from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

# Forms
#from ventas.forms import 

# Models
from ventas.models import Inmueble


class InmuebleView(LoginRequiredMixin, ListView):
    """Return published inmuebles."""

    template_name = 'ventas/catalogo.html'
    #model = Inmueble
    queryset = Inmueble.objects.filter(status__exact='OF')
    #ordering = ('-created',)
    paginate_by = 4
    context_object_name = 'inmuebles'

# @login_required
# def catalogo_view(request):
#     return render(request, 'ventas/catalogo.html')