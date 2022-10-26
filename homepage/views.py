from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.
def ind(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        confirm_password = request.POST.get('re_pass')
        myuser=User.objects.create_user(name, email, password)
        myuser.save()
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        name1 = request.POST.get('your_name')
        passw1 = request.POST.get('your_pass')
        u1 = auth.authenticate(username=name1, password=passw1)
        if u1 is not None:
            # A backend authenticated the credentials
            auth.login(request, u1)
            return redirect("/")
        else:
            # No backend authenticated the credentials
            return render(request, 'index.html')
    return render(request, 'index.html')

