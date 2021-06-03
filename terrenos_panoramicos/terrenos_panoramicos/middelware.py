from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import logout
from django.shortcuts import render


class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous:
            if request.path in [reverse('solicitud_reunion'),reverse('ofrece')]:
                if request.user.is_superuser:
                    return self.get_response(request)
                
                if request.user.profile:
                    profile = request.user.profile
                    if not profile.picture or not profile.born or not profile.phone_number or not profile.curp or not profile.ine:
                        return redirect('update_profile')
        response = self.get_response(request)
        return response
