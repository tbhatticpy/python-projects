#A project about concatenation of strings
#Consists of a paragraph with blanks to be filled by the user
#three methods of string concatenation
#string1 = "concatenation"
#method 1:
#print("Using this string for " + string1)
#method 2:
#print("Using this string for {}".format(string1))
#method 3: f string
#print(f"Using this string for {string1}")

#we will use f string method
#project starts here

adj = input("Adjective: ")
verb1 = input("Verb 1: ")
verb2 = input("Verb 2: ")
famous_person = input("Famous Person: ")

madlibs = f"Computer programming is really {adj}! It makes me so excited because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlibs)