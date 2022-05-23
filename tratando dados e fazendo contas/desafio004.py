quote = input('Digite algo:')

print('O tipo primitivo é ',type(quote))
print('É alfanúmerico?',quote.isalnum())
print('É decimal?',quote.isdecimal())
print('É númerico?',quote.isnumeric())
print(quote.islower())
print(quote.isupper())