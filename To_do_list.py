to_do_list = []

to_do_list.append("Buy groceries")
to_do_list.append("Do laundry")
to_do_list.append("Clean the house")


print("To-do list:")
for item in to_do_list:
    print(item)


to_do_list.remove("Do laundry")

print("To-do list:")
for item in to_do_list:
    print(item)
