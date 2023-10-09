# my_list = ["Povilas", 36, 33.5, ]
# print(type(my_list [0]))
# print(type(my_list [1]))
# print(type(my_list [2]))


# my_list = [1.452, 2.524, 3.652]
# for number in my_list:
#   print(round(number, 2))

# student_list = ["Povilas", "Andrius", "Jonas", "Tomas"]
# sorted_list = sorted(student_list)
# print(sorted_list)

# my_list = input("enter your number: ")
# float_my_list = float(my_list)
# round_list = round(float_my_list)
# print(round_list)

# print(my_list.isdecimal())




# ls(get_users_ids("uid12345"), ["12345"])
# test.assert_equals(get_users_ids("   uidabc  "), ["abc"])
# test.assert_equals(get_users_ids("#uidswagger"), ["swagger"])
# test.assert_equals(get_users_ids("uidone, uidtwo"), ["one", "two"])
# test.assert_equals(get_users_ids("uidCAPSLOCK"), ["capslock"])

# my_string = " uidone, uidtwo"
# prefix = "uid"

# delete_uid = my_string.index(prefix) + len(prefix)
# my_string = my_string[delete_uid:]
# print(my_string)

# name = input("enter your name")
# age = input("enter your age")

# born_year = 2023 - int(age)
# print(born_year)
# print(name[::-1])
# print(name[::2])


# 5 prat

number = input("Enter the number with minimum 3 digits after point: ")
no_check_dot = number.replace(".","").isnumeric()
no_check_comma = number.replace(",","").isnumeric()
if no_check_dot and len(number)>=5:    
    number = round(float(number), 1)   
    print(f"Rounden number value: {number}")
elif no_check_comma and len(number)>=5:   
    number = number.replace(",",".")    
    number = round(float(number),1)    
    print(f"Rounden number value: {number}")
else:   
    print(f"You have failed enter the number")




