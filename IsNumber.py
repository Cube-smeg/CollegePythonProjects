str1 = "8 Hundered 12"    # decimal characters
str2 = "33.4"         # unicode digit
str3 = "½¼"        # fractional value

print("str1 :")
print("str1.isdecimal () : ", str1.isdecimal())
print("str1.isnumeric () : ", str1.isnumeric())
print("str1.isdigit () : ", str1.isdigit())

print("str2 :")
print("str2.isdecimal () : ", str2.isdecimal())
print("str2.isnumeric () : ", str2.isnumeric())
print("str2.isdigit () : ", str2.isdigit())

print("str3 :")
print("str3.isdecimal () : ", str3.isdecimal())
print("str3.isnumeric () : ", str3.isnumeric())
print("str3.isdigit () : ", str3.isdigit())