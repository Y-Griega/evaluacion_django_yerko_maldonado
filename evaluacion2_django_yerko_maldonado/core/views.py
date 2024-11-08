from django.shortcuts import render

def buttons(request):
    return render(request, 'core/buttons.html')

def login(request):
    return render(request, 'core/login.html')

def register(request):
    return render(request, 'core/register.html')

def index(request):
    return render(request, 'core/index.html')

def forms(request):
    return render(request, 'core/forms.html')

def alert(request):
    return render(request, 'core/alert.html')

def card(request):
    return render(request, 'core/card.html')

def typography(request):
    return render(request, 'core/typography.html')

def icontabler(request):
    return render(request, 'core/icontabler.html')

def samplepage(request):
    return render(request, 'core/samplepage.html')



