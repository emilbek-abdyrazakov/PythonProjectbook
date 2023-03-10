rivers = {
    'naryn': 'kyrgyzstan',
    'lena': 'russia',
    'amazon': 'brasil',
    'missouri': 'usa'
    }
for river in rivers.keys():
    print(river.title())
    print("...")
for river in rivers.values():
    print(river.title())
    print("...")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
if country == 'usa':
    print(f"The {river.title()} runs through {country.upper()}")

