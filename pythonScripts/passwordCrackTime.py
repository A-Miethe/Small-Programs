def crackPw(charcount, length, cracks_per_sec):
    return charcount**length//(cracks_per_sec*60*60*24*365)

print('Calculates the amount of time it takes for a password with fixed length and known chars to get cracked, in years.\n')

charcount = int(input('Enter charcount (e.g. 0-9,a-z,A-Z,#=%&!?_ is 70):\n'))
length = int(input('Enter length of password (amount of characters):\n'))
cracks_per_sec = int (int(input('Amount of passwords that can get cracked in one second (in billions):\n')) * 1E9)
years = crackPw(charcount, length, cracks_per_sec)

print(f'\nTime it takes in years for a {length} char long password with {charcount} possible characters:')
print('approx. ' + str(years) + ' years\n')
print(f'Amount of digits of the number: 10^{len(str(years))}' )
print('Biggest known number (that has a name) is: 1 Centillion = 10^600 (in Long Scale (european notation))')
