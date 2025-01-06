from django.shortcuts import render

def groceries(request):
    return render(request,'gro.html')
