#1
import re

def is_positive_less_than_300(value):
    return bool(re.search(r"^([1-9]|[1-9][0-9]|[12][0-9]{2})$", value))


print(is_positive_less_than_300("1"))
print(is_positive_less_than_300("299"))
print(is_positive_less_than_300("300"))
print(is_positive_less_than_300("-5"))

#2

def is_number_from_1_to_255(value):
    return bool(re.search(r"^([1-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$", value))


print(is_number_from_1_to_255("1"))
print(is_number_from_1_to_255("255"))
print(is_number_from_1_to_255("256"))
print(is_number_from_1_to_255("025"))

#3
def is_israel_mobile(phone):
    return bool(re.search(r"^(05[0-9]|\+9725[0-9])(-?[0-9]){7}$", phone))


print(is_israel_mobile("0541234567"))
print(is_israel_mobile("054-1234567"))
print(is_israel_mobile("+97254-123-4567"))
print(is_israel_mobile("058-12-34-567"))
print(is_israel_mobile("054--12-4567"))

#4
def is_valid_time(time):
    return bool(re.search(r"^([01][0-9]|2[0-3]):[0-5][0-9]$", time))


print(is_valid_time("00:00"))
print(is_valid_time("09:30"))
print(is_valid_time("23:59"))
print(is_valid_time("24:00"))
print(is_valid_time("12:60"))
print(is_valid_time("8:30"))