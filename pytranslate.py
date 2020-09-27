#Importing the library package
import goslate

#Taking input from user
text = input("Enter the text:\t")

#Calling the goslate function
gs = goslate.Goslate()

#Translating the text to our preferred language
trans = gs.translate(text,'en')

#Displaying the output
print(trans)