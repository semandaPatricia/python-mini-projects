#string concatenation
# for example fill in the blank "i love to -------"

#few ways to do this
#print("i love to " + hobby)
#print( "i love to {}" .format(hobby))
#print (f" i love to {hobby}")


hob= input("hobby: ")
country =input("country: ")

madlib= f"my favorate thing to do on weekends is to {hob} and during the summer we visit a country called {country}"
print(madlib)