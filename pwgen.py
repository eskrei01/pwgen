import random, string

#This function generates the password
def pwgen(length):
    keyval = 2
    for q in range(quantity): #Generates password from user choices
        result_str = ''.join(random.choice(chars) for i in range(length))
        ini_dict = {keyval:result_str}
        print("Your random password is:", result_str)
        keyval = keyval + 1
    rev_dict = {}
    for key, value in ini_dict.items(): 
        rev_dict.setdefault(value, set()).add(key) 

    result = [key for key, values in rev_dict.items() 
                                  if len(values) > 1]
    print("duplicate values", str(result)) 

#Ask user for input
quantity=int(input("How many passwords do you want? : "))
length=int(input("How many characters do you want? (15+): "))
complexity=int(input((("Choose which complexity you want: \n" 
    "1: Letters, Punctuation and Digits \n" 
    "2: Letters and Punctuation \n" 
    "3: Punctuation and Digits \n" 
    "4: Letters and Digits \n" 
    "5: Punctuation \n" 
    "6: Letters \n" 
    "7: Digits \n" 
    ": "))))

if length >= 15: #Demands password of at least 15 characters
    if complexity == 1:
        chars = string.ascii_letters + string.punctuation + string.digits
        pwgen(length)
            
    elif complexity == 2:   
        chars = string.ascii_letters + string.punctuation
        pwgen(length)

    elif complexity == 3:
        chars = string.punctuation + string.digits
        pwgen(length)

    elif complexity == 4:
        chars = string.ascii_letters + string.digits
        pwgen(length)

    elif complexity == 5:
        chars = string.punctuation
        pwgen(length)

    elif complexity == 6:
        chars = string.ascii_letters
        pwgen(length)

    elif complexity == 7:
        chars = string.digits
        pwgen(length)

    input("Press enter to exit: ")

elif length >= 15:
    