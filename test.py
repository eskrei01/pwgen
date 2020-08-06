
# Python code to demonstrate  
# finding duplicate values from a dictionary 
  
# initialising dictionary 
ini_dict = {'a':1, 'b':2, 'c':3, 'd':1} 
  
# printing initial_dictionary 
print("initial_dictionary", str(ini_dict)) 
  
# finding duplicate values 
# from dictionary 
# using a naive approach 
rev_dict = {} 
  
for key, value in ini_dict.items(): 
    rev_dict.setdefault(value, set()).add(key) 
      
result = [key for key, values in rev_dict.items() 
                              if len(values) > 1] 
  
# printing result 
print("duplicate values", str(result)) 