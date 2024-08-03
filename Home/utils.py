import pandas as pd
from .models import IMDB

def fetch_and_save_data():
    url = 'https://raw.githubusercontent.com/LearnDataSci/articles/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv'
    df = pd.read_csv(url)
    
    movies = []
    for _, row in df.iterrows():
        movies.append(IMDB(
            rank=row['Rank'],
            title=row['Title'],
            genre=row['Genre'],
            description=row['Description'],
            director=row['Director'],
            actors=row['Actors'],
            year=row['Year'],
            runtime=row['Runtime (Minutes)'],
            rating=row['Rating'],
            votes=row['Votes'],
            revenue=row['Revenue (Millions)'] if not pd.isna(row['Revenue (Millions)']) else None,
            metascore=row['Metascore'] if not pd.isna(row['Metascore']) else None
        ))
    
    IMDB.objects.bulk_create(movies)

def fetch_and_analyze_data_by_rating():
    fetch_and_save_data()
    top_5_rated = IMDB.objects.all().order_by('-rating')[:5]
    return top_5_rated

def fetch_and_analyze_data_by_revenue():
    fetch_and_save_data()
    
    top_5_revenue = IMDB.objects.all().order_by('-revenue')[:5]
    return top_5_revenue
