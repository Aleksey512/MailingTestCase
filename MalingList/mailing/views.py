from django.shortcuts import render

def home(request):
    context = {"context" : "Hello dear friend"}
    return render(request, "home.html", context=context)
