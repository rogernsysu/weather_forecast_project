from django.shortcuts import render
from django.http import JsonResponse
from bs4 import BeautifulSoup
import requests
from .models import Restaurant

# List of sample cities
sample_cities = ['Taipei', 'New York', 'London', 'Paris']

def restaurant_list(request):
    return render(request, 'food/restaurant_list.html', {'cities': sample_cities})

def get_restaurants(request):
    city = request.GET.get('city', '')

    # Define a dictionary to hold the scraped restaurant data
    scraped_restaurants = []

    # Perform web scraping to fetch restaurant data for the selected city
    if city == 'Taipei':  # Replace with your own logic to handle different cities
        url = 'https://tw.hotels.com/go/taiwan/best-taipei-local-food'  # Replace with the actual URL
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Implement scraping logic here to extract restaurant information
            # For example:ß
            restaurant_elements = soup.find_all('div', class_='restaurant')
            for element in restaurant_elements:
                name = element.find('h2').text
                type = element.find('p', class_='type').text
                scraped_restaurants.append({'name': name, 'type': type})
        else:
            return JsonResponse({'error': 'Failed to fetch restaurant data'})

    return JsonResponse(scraped_restaurants, safe=False)

