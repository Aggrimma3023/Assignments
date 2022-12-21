a=56
b=10
#a&b
andopt=a&b
print("a&b gives value",str(andopt))
#a|b
oropt=a|b
print("a|b gives value",str(oropt))
#a^b
xoropt=a^b
print("a^b gives value", str(xoropt))
#left shift
lefta_= a<<2
leftb_= b<<2
print("left shift of a by 2 bits",str(lefta_), "left shift of b by 2 bits",str(leftb_))
#right shift
righta_= a>>2
rightb_= b>>4
print("right shift of a by 2 bits",str(righta_), "right shift of a by 4 bits", str(rightb_))