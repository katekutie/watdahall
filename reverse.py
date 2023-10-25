from django.urls import reverse
from django.shortcuts import redirect

def my_view(request):
    # Redirect to the dashboard
    return redirect(reverse('dashboard'))
