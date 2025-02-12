from django.shortcuts import render

def index(request):

    context = {
        'title': 'Home Page',
        'content': 'This is the home page content'
    }

    return render(
        request, 
        'home/index.html', 
        context    
    )
