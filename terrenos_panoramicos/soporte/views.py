from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#Models
from .models import Pregunta_frecuente

#Forms
from .forms import FaqForm

def soporte_FAQ(request):
    faqs = Pregunta_frecuente.objects.all()
    return render(request=request, 
                template_name='soporte/faqs.html',
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
        template_name='soporte/faqs_form.html',
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
        template_name='soporte/faqs_form.html',
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
                template_name='soporte/faqs_delete.html',
                context={'faq': faq})