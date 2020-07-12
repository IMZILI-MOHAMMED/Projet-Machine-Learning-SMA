from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .utils import fill_country_object
# Create your views here.
from django.http import JsonResponse
# Create your views here.

def morocco(request):

    page = requests.get('https://covid.hespress.com/')
    page.encoding = "utf-8"

    # Create a BeautifulSoup object
    soup = BeautifulSoup(page.text, 'html.parser')
    rows = soup.findAll("div", {"class": "col-7 text-left"})
    table = soup.findAll('tr')
    lastUp = soup.find("span", {"class": "font-13"})
    confirmedCases = soup.find("span", {"class": "badge badge-warning pr-2 pl-2"}) 
    newDeaths = soup.find("span", {"class": "badge badge-danger pr-2 pl-2"})
    
    general = []
    states = []
   
    lastUpdate = lastUp.getText()
    nd = newDeaths.getText()
    nc = confirmedCases.getText()
      
    for row in rows:
        data = {
            'title': row.h5.getText(),
            'value': row.h4.getText()
        }
        general.append(data)

    for tab in table:
        td = tab.findAll('td')
        data = {
            'region': tab.th.a.getText(),
            'total': td[0].getText(),
            'new_cases': td[1].getText()

        }
        states.append(data)
    responseData = {
        'lastUpdate': lastUpdate,
        'ConfirmedCases': nc,
        'NewDeaths': nd,
        'general': general,
        'regions': states
        
    }

    return JsonResponse(responseData)


def countries_list(request):
    response = requests.get(
        'https://www.worldometers.info/coronavirus/')
    soup = BeautifulSoup(response.text, 'html.parser')

    countries = []

    tbody = soup.find('tbody')
    rows = tbody.findAll('tr')

    for row in rows:
        cols = row.findAll('td')
        cols = [x.text.strip() for x in cols]
        data = {
            'name': cols[1]
        }
        countries.append(data)
    responseData = {'countries': countries[7:]}
    return JsonResponse(responseData)



def home(request):
    response = requests.get(
        'https://www.worldometers.info/coronavirus/').content
    soup = BeautifulSoup(response, 'html.parser')

    confirmedCases = soup.find_all(
        'div', class_='maincounter-number')[0].text.strip(' ').strip('\n')
    deathCases = soup.find_all(
        'div', class_='maincounter-number')[1].text.strip(' ').strip('\n')
    recovered = soup.find_all(
        'div', class_='maincounter-number')[2].text.strip(' ').strip('\n')
    closedCases = soup.find_all('div', class_='number-table-main')[1].text
    lastUpdate = soup.find_all(
        'div', style='font-size:13px; color:#999; margin-top:5px; text-align:center')[0].text
    activeCases = soup.find_all(class_='number-table-main')[0].text
    activeCasesMildCondition = soup.find_all(class_='number-table')[0].text
    activeCasesSeriousCondition = soup.find_all(class_='number-table')[1].text

    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')

    countries = fill_country_object(rows)

    responseData = {'confirmedCases': confirmedCases, 'deathCases': deathCases, "recovered": recovered,
            'closedCases': closedCases, 'countries': countries, 'lastUpdate': lastUpdate, 'activeCases': activeCases,
            'activeCasesMildCondition': activeCasesMildCondition,
            'activeCasesSeriousCondition': activeCasesSeriousCondition}
    return JsonResponse(responseData)



def get_info_by_country(request, country):
    countryName = country

    response = requests.get(
        'https://www.worldometers.info/coronavirus/').content
    soup = BeautifulSoup(response, 'html.parser')
    lastUpdate = soup.find_all(
        'div', style='font-size:13px; color:#999; margin-top:5px; text-align:center')[0].text

    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')
    countries = fill_country_object(rows)
    responseData = {'infos': countries[countryName], 'lastUpdate': lastUpdate}
    return JsonResponse(responseData)
    

def trendingNews(request):
    response = requests.get(
        'https://www.challenge.ma/lessentiel/')
    soup = BeautifulSoup(response.text, 'html.parser')

    rows = soup.findAll("div", {"class": "vw-block-grid-item"})
    posts = []

    for row in rows:
        moreInfo = row.h3.find('a', href=True)
        data = {
            'title': row.h3.a.getText(),
            'body': row.p.getText(),
            'time': row.time.getText(),
            'more': moreInfo['href']
        }
        posts.append(data)
    responseData = {'news': posts}
    return JsonResponse(responseData)

