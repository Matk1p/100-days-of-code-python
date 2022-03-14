from cmath import pi
import random
import myModule

# to understand the use of the random library provided by python
# understanding how to import and make the python files more modular for inter files use

random_integer = random.randint(2, 10) # places a random integer from 2 - 10
print(random_integer)
print(myModule.pi) # this is how to call a variable that exist in a separate python file

random_float = random.random() 

#Since random.random() doesn't take in any arguments, we cannot pass in the range as per random.randint()
# to overcome this, we can just * by the number we need the limit to be

random_float_with_limit = random.random() * 5 # say the limit is 5, not it can go beyond 1 and within 5
print(random_float_with_limit)