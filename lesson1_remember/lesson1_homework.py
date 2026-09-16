# 1.
def clean_name(name):
    return name.strip().title()

print(clean_name(" anna smith   "))
print(clean_name(" DAVID COHEN"))

# 2.
def normalize_email(email):
    return email.strip().lower()

print(normalize_email("Anna.Smith@Example.COM"))

# 3.
def is_python_file(filename):
    return filename.lower().endswith(".py")

print(is_python_file("lesson.py"))
print(is_python_file("HOMEWORK.PY"))
print(is_python_file("notes.txt"))

# 4.
def fix_message(text):
    return text.replace("bad", "good")
message = "bad weather, bad mood"
result = fix_message(message)
print(result)

# 5.
def count_letter(text, letter):
    return text.count(letter)

print(count_letter("Mississippi", "i"))

# 6.


def create_login(first_name, last_name):
    first_name = first_name.strip().lower()
    last_name = last_name.strip().lower()

    res = first_name + "." + last_name
    return res


print(create_login("  Anna ", " SMITH  "))







