from django.shortcuts import render

# Create your views here.

def calculator(request):
    number1 = request.POST['number1']
    char = request.POST['char']
    number2 = request.POST['number2']
    res = 0
    if char == '+':
        res = int(number1) + int(number2)
    elif char == '-':
        res = int(number1) - int(number2)
    return render(request, 'math_modul/calculator.html', context={'res':res})