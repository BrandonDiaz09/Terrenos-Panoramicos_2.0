from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView


#Models
from django.contrib.auth.models import User
from ventas.models import Inmueble

#Forms
from users.forms import ProfileForm, SignupForm


# Create your views here.

class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'

    # def get_context_data(self, **kwargs):
    #     """Add user's favorites to context."""
    #     context = super().get_context_data(**kwargs)
    #     user = self.get_object()
    #     context['posts'] = Post.objects.filter(user=user).order_by('-created')
    #     return context

def login_view(request):

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username,password=password)
        if user:
            login(request, user)
            return redirect('catalogo')
        else:
            return render(request, 'users/login.html', {'error' : 'Usuario o contraseña invalidos'})
    return render(request, 'users/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
    )


@login_required
def logout_view(request):

    logout(request)
    return redirect('login')

@login_required
def update_profile(request):

    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.curp = data['curp']
            profile.phone_number = data['phone_number']
            profile.ine = data['ine']
            profile.picture = data['picture']
            profile.save()

            url = reverse('detail', kwargs={'username': request.user.username})
            return redirect(url)

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'form':form,
            'profile': profile,
            'user':request.user,
        }
    )
   