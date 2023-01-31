import re

number = int(input())

pattern = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"

for num in range(number):
    barcode = input()
    matches = re.findall(pattern, barcode)

    if matches:
        current_barcode = "".join(matches)
        product_group = ""

        for element in current_barcode:
            if element.isdigit():
                product_group += element

        if product_group:
            print(f"Product group: {product_group}")
        else:
            print("Product group: 00")

    else:
        print("Invalid barcode")

# second_solution

# import re
#
# number = int(input())
#
# for num in range(number):
#     barcode = input()
#     pattern = r"@#+([A-Z][A-Za-z\d]{4,}[A-Z])@#+"
#     matches = re.finditer(pattern, barcode)
#
#     match_found = False
#
#     for match in matches:
#         barcode_group = ""
#         match_found = True
#
#         for el in match.group(1):
#             if el.isdigit():
#                 barcode_group += el
#
#         if barcode_group == "":
#             barcode_group = "00"
#
#         print(f"Product group: {barcode_group}")
#
#     if not match_found:
#         print("Invalid barcode")
