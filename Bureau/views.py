from django.shortcuts import render

# Create your views here.
def bureau(request):
    return render(request, 'Bureau/templates/Bureau.html')