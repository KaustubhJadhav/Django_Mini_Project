from django.shortcuts import render
import pandas as pd
from .models import *
from .utils import *

# Create your views here.
def index(request):
    IMDB.objects.all().delete()
    top_5_revenue = fetch_and_analyze_data_by_revenue()
    top_5_rating = fetch_and_analyze_data_by_rating()
    context = {
        'top_5_revenue': top_5_revenue,
        'top_5_rating': top_5_rating
    }
    return render(request,'index.html', context)

