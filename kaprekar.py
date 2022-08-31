number = input('Enter a 4-digit number consisting of at least two different digits: ')     
while True:  
    if not number.isdigit() or len(number) != 4:    
        print('Only 4 positive numbers are allowed')
        number = input('Enter a 4-digit number consisting of at least two different digits: ') 
        continue    
    else:
        for i in range(len(number)):
            if number.count(number[i]) > 2:
                print('Sorry, the four-digit number must contain no more than two equal digits.')  
                number = input('Enter a 4-digit number consisting of at least two different digits: ')
                continue
        break
print('\n',number)
while True:    
    numberA = ''.join(sorted(number, reverse=True)) 
    numberB = numberA[::-1]
    numberC = int(numberA)-int(numberB)
    print(f'{numberA} - {numberB} = {numberC}')    
    if numberC != 6174: number = str(numberC)
    else: break
