print("Please enter a string")
str=input()
#splitting the sentence into words
lis=str.split(" ")
print(lis)
if (" ") in str:
     #storing unique words in a set
     words=set(lis)
     #printing the count of each unique word
     print("Count of each word:")
     for word in words:
          print(word, "occurs", lis.count(word),"times")
else:
     alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
     for letter in alpha:
          if str.count(letter)>0:
               print(letter, "occurs", str.count(letter), "times")
