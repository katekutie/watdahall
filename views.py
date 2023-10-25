from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.utils import timezone  # Import timezone
from django.http import JsonResponse
from .models import UserProfile  # Import your UserProfile model

# Create your views here.
@login_required

def home(request):
    return HttpResponse("Welcome to BudgetPro!")

def home(request):
    return render(request, "BudgetPro/Log-in.html")

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if User.objects.filter(username=username):
            messages.error(request, "Username already exists, please try another.")
            return redirect('home')
        
        if User.objects.filter(email=email):
            messages.error(request, "Email already registered!")
            return redirect('home')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        myuser = User.objects.create_user(username, email, password1)
        messages.success(request, "Your account has been successfully registered.")
        
        return redirect('login')

    return render(request, "BudgetPro/Register.html")

def login(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return render(request, "BudgetPro/user-profile.html", {'username': username})
            
        else:
            messages.error(request, "Incorrect or unknown user!!!")
    
    return render(request, "BudgetPro/Log-in.html")

def userprofile(request):
    # Update the last login date for the user
    request.user.last_login = timezone.now()
    request.user.save()

    # Render the user-profile.html template with the updated last login date
    return render(request, "BudgetPro/user-profile.html", {'username': request.user.username})

def dashboard(request):
    if request.method == 'POST':
        if 'deposit-amount' in request.POST:
            amount = float(request.POST.get('deposit-amount'))
            note = request.POST.get('deposit-note')

            # Assuming you have a UserProfile associated with the user
            user_profile = UserProfile.objects.get(user=request.user)

            # Update the balance
            user_profile.balance += amount
            user_profile.save()

            response_data = {'message': 'Deposit successful'}
            return JsonResponse(response_data)

        elif 'credit-amount' in request.POST:
            credit_amount = float(request.POST.get('credit-amount'))

            # Assuming you have a UserProfile associated with the user
            user_profile = UserProfile.objects.get(user=request.user)

            # Update the balance
            user_profile.balance += credit_amount
            user_profile.save()

            response_data = {'message': 'Credit added successfully'}
            return JsonResponse(response_data)

        elif 'savings-amount' in request.POST:
            savings_amount = float(request.POST.get('savings-amount'))

            # Assuming you have a UserProfile associated with the user
            user_profile = UserProfile.objects.get(user=request.user)

            # Add savings to the balance
            user_profile.balance += savings_amount  # Update the balance with savings
            user_profile.save()  # Save the updated balance

            response_data = {'message': 'Savings added successfully'}
            return JsonResponse(response_data)

    return render(request, "BudgetPro/Dashboard.html", {'username': request.user.username})



def tips(request):
    return render(request, "BudgetPro/Tips.html", {'username': request.user.username})

def landingpage(request):
    return render(request, "BudgetPro/LandingPage.html", {'username': request.user.username})