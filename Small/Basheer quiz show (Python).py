print("Welcome to my quiz show!")
print("There will be many questions in this show if you answer anyone of them with the wrong answer you will lose the game.")
import time
time.sleep(3)
print("Please press (enter) to continue.")
input()
correct = "Amazing, your answer is correct."
false = ":( , sorry you just lost."
print("Please type the answer number")
print("First question:")
print("What year was the very first model of the iPhone released?")
print("1. 2002")
print("2. 2003")
print("3. 2006")
print("4. 2007")
a = input("Answer: ")
if a == "1" :
    import os
    os.system('color 4')
    print(false)
    import time
    time.sleep(1)
    exit()
elif a == "2" :
    import os
    os.system('color 4')
    print(false)
    import time
    time.sleep(3)
    exit()
elif a == "3" :
    import os
    os.system('color 4')
    print(false)
    import time
    time.sleep(3)
    exit()
elif a == "4" :
    import os
    os.system('color 2')
    print(correct)
    import time
    time.sleep(3)
    import os
    os.system('color 7')
else:
    print("Error")
    import time
    time.sleep(3)
    exit()

    
print("Second question:")
print("Which country produces the most coffee in the world? ")
print("1. Syria")
print("2. Brazil")
print("3. China")
print("4. India")
b = input("Answer: ")
if b == "1" :
    import os
    os.system('color 4')
    print(false)
    import time
    time.sleep(3)
    exit()
elif b == "2" :
    import os
    os.system('color 2')
    print(correct)
    import time
    time.sleep(1)
    import os
    os.system('color 7')
elif b == "3" :
    import os
    os.system('color 4')
    print(false)
    import time
    time.sleep(3)
    exit()
elif b == "4" :
    import os
    os.system('color 4')
    print(false)
    import time
    time.sleep(3)
    exit()
else:
    print("Error")
    import time
    time.sleep(3)
    exit()

    
print("Third question:")
print("What was Superman’s birth name?")
print("1. Kal-El")
print("2. Sendo")
print("3. Raw-ren")
print("4. Jack")
c = input("Answer: ")
if c == "1" :
    import os
    os.system('color 2')
    print(correct)
    import time
    time.sleep(1)
    import os
    os.system('color 7')
elif c == "2" :
    import os
    os.system('color 4')
    print(false)
    import time
    time.sleep(3)
    exit()
elif c == "3" :
    import os
    os.system('color 4')
    print(false)
    import time
    time.sleep(3)
    exit()
elif c == "4" :
    import os
    os.system('color 4')
    print(false)
    import time
    time.sleep(3)
    exit()
else:
    print("Error")
    import time
    time.sleep(3)
    exit()

print("Third question:")
print("Which cartoon character lives in a pineapple under the sea?")
print("1. Gumball")
print("2. Spongebob Squarepants")
print("3. Tom (from Tom and Jerry)")
print("4. Tweety")
d = input("Answer: ")

if d == "1" :
    import os
    os.system('color 4')
    print(false)
    import time
    time.sleep(3)
    exit()
elif d == "2" :
    import os
    os.system('color 2')
    print(correct)
    import time
    time.sleep(1)
    import os
    os.system('color 7')
elif d == "3" :
    import os
    os.system('color 4')
    print(false)
    import time
    time.sleep(3)
    exit()
elif d == "4" :
    import os
    os.system('color 4')
    print(false)
    import time
    time.sleep(3)
    exit()
else:
    print("Error")
    import time
    time.sleep(3)
    exit()

print("GG, You just answerd all the questions correcttly")
print("Bye..")
import time
time.sleep(5)


