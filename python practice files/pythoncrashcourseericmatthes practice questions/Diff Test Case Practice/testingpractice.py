

# def city_country(city, country):
#     return(f'{city.lower().title()}, {country.lower().title()}')



def city_country(city, country, population=''):
    if population != '':
        return(f'{city.lower().title()}, {country.lower().title()} - {str(population)}')
    else:
        return(f'{city.lower().title()}, {country.lower().title()}')



if __name__ == '__main__':
    print(city_country('athens','gReece',5000))

