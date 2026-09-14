s = "cat"
s = s.upper()
print(s)

s1 = 'Hello'
s2 = "Hello"
s3 = """Line one
Line two"""
print(s1)
print(s2)
print(s3)

s = "Hello my group!"
print(len(s))
print(s[0])
print(s[4])
print(s[14])
print(s[-1])
s1 = "P y t h o n"

text ="automation"
print(text[2:4])

print(text[2:6])
print(text[:4])
print(text[4:])
print(text[:])
print(text[::2])
print(text[::-1])
print(text[5:100])

name = "Mariia"
last_name = "Ivanova"
age = 25
print(name+" " +last_name + " - " + str(age))
print(f"Hi my name is {name} and my last name is {last_name} and i'm {age} years old")

raw = "Automation QA"
print(raw.upper())
print(raw.lower())

print(raw.strip().upper())

cvs_line = "Login, Cart, Checkout, Mama, Papa"
parts = cvs_line.split(",")
print(parts)
print(" - ".join(parts))

msg = "Test failed: element not found"
print(msg.replace("failed", "passed"))

s = "banana"

print(s.find("na"))
print(s.index("na"))

print(s.find("xyz"))
print(s.index("xyz"))

print(s.count("na"))