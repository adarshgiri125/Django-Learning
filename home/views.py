from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    # return HttpResponse("<h1> hello world </h1>")
    people = [
        {'name' :'adarsh', 'age' : 21},
        {'name' : 'ad', 'age' : 22},
        {'name' : 'gagg', 'age' : 12},
        {'name' : 'eduue', 'age' : 66},
    ], 

    for people in people:
        print(people)

    return render(request, 'index.html', context={'people': people})

def hurraa(request):
    return HttpResponse("<h2> hey i am learning django </h2 >")
    
