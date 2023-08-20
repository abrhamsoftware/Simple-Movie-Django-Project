from django.http import HttpResponse

from django.shortcuts import render

def movies(request):
    data={
        'movies':[
                  
                  {
                    'id': 5,
                    'title' : 'Jaws',
                    'year':1669, 
                  },
                  {
                    'id': 6,
                    'title' : 'Hell',
                    'year':1829,
                  },
                  {
                    'id': 7,
                    'title' : 'There',
                    'year':1921,
                  }  
                    
        ]
        }
    return render(request,'movies/movies.html',data)


def home(request):
    return HttpResponse("Home Page")


def about(request):
    return HttpResponse("About Us")