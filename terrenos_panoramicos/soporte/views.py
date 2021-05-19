from django.http import response
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#Models
from .models import Pregunta_frecuente, Reporte

#Forms
from .forms import FaqForm, ReporteForm

def soporte_FAQ(request):
    faqs = Pregunta_frecuente.objects.all()
    return render(request=request, 
                template_name='soporte/faqs/faqs.html',
                context={'faqs': faqs,})

@login_required
def createFAQ(request):
    form = FaqForm()
    
    if request.method == 'POST':
        #print('Printing POST', request.POST)
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faqs')
    return render(
        request=request,
        template_name='soporte/faqs/faqs_form.html',
        context={
            'form':form,
            #'user':request.user,
            #'reuniones': Servicio_Reunion.objects.all()
        }
    ) 

@login_required
def updateFAQ(request, pk):
    faq = Pregunta_frecuente.objects.get(pk=pk)
    form = FaqForm(instance=faq)

    if request.method == 'POST':
        form = FaqForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            return redirect('faqs')
    return render(
        request=request,
        template_name='soporte/faqs/faqs_form.html',
        context={
            'form':form,
            #'user':request.user,
            #'reuniones': Servicio_Reunion.objects.all()
        }
    )

@login_required
def deleteFAQ(request, pk):
    faq = Pregunta_frecuente.objects.get(pk=pk)
    if request.method == 'POST':
        faq.delete()
        return redirect('faqs')
    return render(request=request, 
                template_name='soporte/faqs/faqs_delete.html',
                context={'faq': faq})

@login_required
def soporte_reporte(request):
    reportes_true = Reporte.objects.filter(atendido=True)
    reportes_false = Reporte.objects.filter(atendido=False)
    form = ReporteForm()
    if request.method == 'POST':
        form = ReporteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reporte')

    return render(request=request, 
                template_name='soporte/reporte/reporte.html',
                context={'form':form,
                        'user':request.user,
                        'reportes_atendidos': reportes_true, 
                        'reportes_no_atendidos': reportes_false,}) 

@login_required
def updateReporte(request, pk):
    reporte = Reporte.objects.get(pk=pk)
    form = ReporteForm(instance=reporte)

    if request.method == 'POST':
        form = ReporteForm(request.POST, instance=reporte)
        if form.is_valid():
            form.save()
            return redirect('reporte')
    return render(
        request=request,
        template_name='soporte/reporte/reporte_update.html',
        context={
            'form':form,
            #'user':request.user,
            #'reuniones': Servicio_Reunion.objects.all()
        }
    )

@login_required
def updateReporte_atendido(request, pk):
    reporte = Reporte.objects.get(pk=pk)

    if request.method == 'POST':
        if reporte.atendido:
            reporte.update(atendido=False)
            url = reverse('reporte',)
            return redirect(url)
        else:
            reporte.update(atendido = True)
            return redirect('reporte')
    return render(
        request=request,
        template_name='soporte/reporte/reporte_atender.html',
        context={
            'reporte': reporte
        }
    )