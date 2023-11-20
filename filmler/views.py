
from datetime import date
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Film, Category
# filmler klasörü içindeki models dosyası içindeki Film objesini ve Category import ettik bu şekilde veritabanından bilgileri çekebiliyoruz.
# Create your views here.

# ilerleyen aşamalarda bu datalar veritabanından gelicek

data = {
    "komedi": "komedi kategorisine ait filmler",
    "aksiyon": "aksiyon kategorisine ait filmler",
    "dram": "drama film kategorisine ait filmler",
    "ask": "ask kategorisine ait filmler"
}
db = {
    "movies": [
        {
            "title" : "Komedi Filmleri",
            "description": "En İyi Komedi Film Önerileri İçin Tıklayınız..!",
            "imageUrl":"1.jpg",
            
        },
        {
            "title" : "Aksiyon Filmleri",
            "description": "En İyi Aksiyon Film Önerileri İçin Tıklayınız..!",
            "imageUrl":"2.jpg",
           
        },
        {
            "title" : "Aşk Filmleri",
            "description": "En İyi Aşk Film Önerileri İçin Tıklayınız..!",
            "imageUrl":"3.jpg",
            
        },
        {
            "title" : "Drama Filmleri",
            "description": "En İyi Drama Film Önerileri İçin Tıklayınız..!",
            "imageUrl":"drama.jpg",
            
        }  
    ],
    "categories": [
        {"id":1, "name":"Komedi Filmleri","slug":"komedi"},
        {"id":2, "name":"Aksiyon Filmleri","slug":"aksiyon"},
        {"id":3, "name":"Drama Filmleri","slug":"dram"},
        {"id":4, "name":"Aşk Filmleri","slug":"ask"},  
        ]
}

def index(request):
    filmler = Film.objects.all()
    kategoriler = Category.objects.all()

    return render(request, 'movies/index.html',{
        'categories': kategoriler,
        'movies' :  filmler
    })


def details(request, film_id):
    
    film=Film.objects.get(pk=film_id)
    
    context ={
        'film' : film
    }
    return render(request, 'movies/details.html',context)


def getMoviesByCategory(request, category_name):
    try:
        category_text = data[category_name]

        return render (request,'movies/filmler.html',{
            'category': category_name,
            'category_text': category_text
        })
    except:
        return HttpResponseNotFound("<h1>yanlış kategori secimi</h1>")


def getMoviesByCategoryId(request, category_id):
    category_list = list(data.keys())
    category_name = category_list[category_id-1]
    redirect_url = reverse('movies_by_category', args=[category_name])
    return redirect(redirect_url)
