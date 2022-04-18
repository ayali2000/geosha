from multiprocessing import context
from django.shortcuts import render
from . forms import *
from django.contrib import messages

def sign_up(request):
    frm = SignUpForm()
    if request.method == "POST":
        frm = SignUpForm(request.POST)
        if frm.is_valid():
            frm.save()
            messages.success(request,("User created successfully"))
        else:
            messages.success(request,("""
            Couldint create account. It's either your username 
            is already taken or your passwords didn't match.
            Note: Password should contain letters,symbols and digits
                  Password can't be similar to username
            """
            ))
            frm = SignUpForm() 

    context ={"frm":frm}           

    return render(request,'users/signup.html',context)
