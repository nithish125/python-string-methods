# 1.capitalize
name = "hello, and welcome to my world."
x = name.capitalize()
print ("1",x)

# 2.casefold
name = "Hello, And Welcome To My World!"
x = name.casefold()
print("2",x)

# 3.center
fruit = "banana"
x = fruit.center(20)
print("3",x)

#count
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)

#encode
txt = "Welcome to fabevy"
x = txt.encode()
print(x)

#endswith
t = "Hello, welcome to fabevy."
x = t.endswith(".")
print(x)

#expandtabs
names= "H\te\tl\tl\to"
x =  names.expandtabs(2)
print(x)

#find
text = "Hello, welcome to my world."
x = text.find("welcome")
print(x)

#format
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


#index
text = "Hello, welcome to my world."
x = text.index("welcome")
print(x)

#isalnum
text = "Company12"
x = text.isalnum()
print(x)

#isalpha
text = "CompanyX"
x = text.isalpha()
print(x)

#isascii
text = "Company123"
x = text.isascii()
print(x)

#isdecimal
text = "\u0033" #unicode for 3
x = text.isdecimal()
print(x)

#isdigit
text = "50800"
x = text.isdigit()
print(x)

#isidentifier
text = "Demo"
x = text.isidentifier()
print(x)

#islower
text = "hello world!"
x = text.islower()
print(x)

#isnumeric
txt = "5657643"
x = txt.isnumeric()
text = "5655r43"
y= text.isnumeric()
print(y)
print(x)

#isprintable
text = "Hello! Are you #1?"
x = text.isprintable()
print(x)

#isspace
text = "   "
x = text.isspace()
print(x)

#istitle
text = "Hello, And Welcome To My World!"
x = text.istitle()
print(x)

#isupper
text = "THIS IS NOW!"
x = text.isupper()
print(x)


#join
myTuple = ("John", "Peter", "Vicky")
x = "-".join(myTuple)
print(x)

#ljust
text = "banana"
x = text.ljust(20)
print(x, "is my favorite fruit.")

#lower
text = "Hello my FRIENDS"
x = text.lower()
print(x)


#lstrip
txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")

#maketrans
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))

#partition
text = "I could eat bananas all day"
x = text.partition("bananas")
print(x)


#replace
text = "I like bananas"
x = text.replace("bananas", "apples")
print(x)


#rfind
text = "Mi casa, su casa."
x = text.rfind("casa")
print(x)


#rindex
text = "Mi casa, su casa."
x = text.rindex("casa")
print(x)

#rjust
text = "banana"
x = text.rjust(20)
print(x, "is my favorite fruit.")

#rpartition
text = "I could eat bananas all day, bananas are my favorite fruit"
x = text.rpartition("bananas")
print(x)


#rsplit
text = "apple, banana, cherry"
x = text.rsplit(", ")
print(x)

#rstrip
text = "     apple     "
x = text.rstrip()
print("of all fruits", x, "is my favorite")


#split
text = "welcome to the jungle"
x = text.split()
print(x)


#splitlines
text = "Thank you for the music\nWelcome to the jungle"
x = text.splitlines()
print(x)


#startswith
text = "Hello, welcome to my world."
x = text.startswith("Hello")
print(x)

#strip
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")


#swapcase
text = "Hello My Name Is PETER"
x = text.swapcase()
print(x)

#title
text = "Welcome to my world"
x = text.title()
print(x)

#translate
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))


#upper
text = "Hello my friends"
x = text.upper()
print(x)

#zfill
text = "50"
x = text.zfill(10)
print(x)
