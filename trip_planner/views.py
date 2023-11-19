from django.shortcuts import render
from .models import Flight
import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup

def scrape_flight_prices(origin, destination, departure_date):
    try:
        # Construct the URL for flight search
        url = f'https://example.com/flights?origin={origin}&destination={destination}&date={departure_date}'

        # Send an HTTP request to the website
        response = requests.get(url)

        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find the flight price element
            price_element = soup.find('span', class_='flight-price')

            if price_element:
                # Extract the flight price
                price = price_element.text.strip()
                return price
            else:
                return 'Price not found'
        else:
            return 'Request failed'
    except Exception as e:
        return str(e)

def flight_list(request):
    flights = Flight.objects.all()

    # Define a dictionary to store flight prices
    flight_prices = {}

    for flight in flights:
        origin = flight.origin
        destination = flight.destination
        departure_date = flight.departure_date

        # Use the scrape_flight_prices function to get flight prices
        flight_prices[flight.id] = scrape_flight_prices(origin, destination, departure_date)

    return render(request, 'trip_planner/flight_list.html', {'flights': flights, 'flight_prices': flight_prices})

def search_flights(request):
    if request.method == 'GET':
        origin = request.GET.get('origin', '')
        destination = request.GET.get('destination', '')
        departure_date = request.GET.get('departure_date', '')

        # Use the scrape_flight_prices function to get flight prices
        price = scrape_flight_prices(origin, destination, departure_date)

        return JsonResponse({'price': price})



