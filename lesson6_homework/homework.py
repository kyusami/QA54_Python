#1

# def get_product(products, index):
#     try:
#         return products[index]
#     except IndexError:
#         return "Product index is out of range"
#
#
# product_list = ["coffee", "tea", "milk"]
#
# print(get_product(product_list, 0))
# print(get_product(product_list, 7))

#2

# def get_settings_value(settings, key):
#     try:
#         return settings[key]
#     except KeyError:
#         return "Setting was not found"
#
#
# settings_data = {
#     "language": "English",
#     "theme": "dark"
# }
#
# print(get_settings_value(settings_data, "theme"))
# print(get_settings_value(settings_data, "font"))

#3

# def calculate_total_price(price, quantity):
#     try:
#         price = float(price)
#         quantity = float(quantity)
#         result = price * quantity
#         return result
#     except ValueError:
#         return "Value must be a number"
#     except TypeError:
#         return "Invalid data type"
#
# print(calculate_total_price("12.5", "4"))
# print(calculate_total_price("coffe", "4"))
# print(calculate_total_price(None, "4"))

#4
# def read_temperature():
#     try:
#         float(input("Enter temperature: "))
#         print("Temperature was entered successfully")
#     except ValueError:
#         print("Invalid temperature")
#     finally:
#         print("Program finished")
#
# read_temperature()

#5
def validate_discount(discount):
    if discount < 0:
        raise ValueError("Discount cannot be negative")

    if discount > 100:
        raise ValueError("Discount cannot be greater than 100")

    return discount

print(validate_discount(20))