list=[1,2,3,4,5]
search_element=int(input("Enter a number to search:"))
if search_element in list:
    print(f"{search_element} exists in the list.")
else:
    print(f"{search_element} does not exit in the list.")