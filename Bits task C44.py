import requests
from bs4 import BeautifulSoup


def scrape_hotels(location, max_price):
    
    url = 'https://www.shangri-la.com/en/colombo/shangrila/'
    
    
    params = {
        'location': location,
        'max_price': max_price
    }
    
    
    response = requests.get(url, params=params)
    
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    
    hotels = soup.find_all('div', class_='hotel-listing', limit=5)
    
    
    hotel_data = []
    
    
    for hotel in hotels:
        name = hotel.find('h2', class_='hotel-name').text
        price = hotel.find('span', class_='hotel-price').text
        rating = hotel.find('span', class_='hotel-rating').text
        hotel_data.append((name, price, rating))
    
    return hotel_data


def main():
    location = input('Enter the location you want to search for hotels: ')
    budget = input('Enter your budget for the hotel: ')
    
    hotels = scrape_hotels(location, budget)
    
    print(f'Hotels in {location} under {budget}:')
    for name, price, rating in hotels:
        print(f'Name: {name}, Price: {price}, Rating: {rating}')

if __name__ == '__main__':
    main()
