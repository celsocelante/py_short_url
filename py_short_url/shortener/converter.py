# Dictionary of Base62 (position is the key and chars, the value)
base = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
base_value = len(base)

# Function that converts any string (supposed to be a base62 number) to a correspondent decimal number
def toDecimal(string):
    sum = 0
    position = 0
    # Generate a downto for to calculate correspodent decimal value to a string
    for exp in range(len(string),-1,-1)[1:]:
        sum = sum + pow(base_value,exp)*base.index(string[position])
        position = position + 1

    return sum

# Function that converts any integer number to a correspondent string (a base62 number)
def toString(number):
    final_list = []

    remainder = number % base_value
    number = number / base_value
    final_list.append(base[remainder])

    # Uses 'serie of divisions' method to convert any number to a base62 string
    while (number > base_value):
        remainder = number % base_value
        number = number / base_value
        final_list.append(base[remainder])

    final_list.append(base[number])
    final_list.reverse()

    # Converts a list to a string
    final_string = ''.join(final_list)

    # Fix the 0 in the left of some strings
    if(final_string[0] == '0' and final_string[1] != '0'):
        final_string = final_string[1:]

    return final_string
