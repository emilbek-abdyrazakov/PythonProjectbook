def city(country, capital):
    country_capital = f"{country} , {capital}"
    return country_capital.title()
places = city('kyrgyzstan' , 'bishkek')
print (places)