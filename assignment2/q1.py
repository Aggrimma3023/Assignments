print("Enter a string.")
str_=input()
#part(a)
print("The length of the entered string is",len(str_))
#part(b)
rev_=str_[::-1]
print("The string in reverse order is", rev_)
#part(c)
newstr_=str_[10:]
print("The new string you have created is ",newstr_)
#part(d)
beginstr_=str_[:10]
endstr_="object oriented"
print("Your required string is",beginstr_+endstr_)
#part(e)
index=str_.find("a")
print("Index of a in the string is ", index)
#part(f)
nospace_=str_.replace(" ","")
print(nospace_)
