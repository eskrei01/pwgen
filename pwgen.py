import random
import string

#This function generates the password
def pwgen(length):
    result_str = ''.join(random.choice(chars) for i in range(length))
    print("Your random password is:", result_str)

#Ask user for input
quantity=int(input("How many passwords do you want? : "))
length=int(input("How many characters do you want? (15+): "))
complexity=int(input("Choose which complexity you want: \n1: Letters, Punctuation and Digits \n2: Letters and Punctuation \n3: Punctuation and Digits \n4: Letters and Digits \n5: Punctuation \n6: Letters \n7: Digits \n: "))

if length >= 15: #Demands password of at least 15 characters
    for i in range(quantity): #Generates password from user choices
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
            
else:
    print("You must create a password with at least 15 characters")
    input("Press enter to exit: ")
