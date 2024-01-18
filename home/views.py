from django.shortcuts import render

def account(request):
    return render(request, 'account.html')

def cart(request):
    return render(request, 'cart.html')

def contact(request):
    return render(request, 'contact.html')

def create_account(request):
    return render(request, 'create-account.html')

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def product(request):
    return render(request, 'product.html')

def shop(request):
    return render(request, 'shop.html')
