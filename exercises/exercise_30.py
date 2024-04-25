roman_numerals = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

numeral_input = input()

numeral_sum = 0

for i in range(len(numeral_input)):
    if i < len(numeral_input) - 1:
        
        if roman_numerals[numeral_input[i]] < roman_numerals[numeral_input[i + 1]]:
            numeral_sum -= roman_numerals[numeral_input[i]]
            
        else:
            numeral_sum += roman_numerals[numeral_input[i]]
            
    else:
        numeral_sum += roman_numerals[numeral_input[i]]

print(numeral_sum)