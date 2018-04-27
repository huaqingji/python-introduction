## 3. Read the File Into a String ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
first_five = names_list[:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')

nested_list = []
for name in names_list:
    comma_list = name.split(',')
    nested_list.append(comma_list)

print(nested_list)

## 6. Convert Numerical Values ##

numerical_list = []
for element in nested_list:
    numerical_list.append(
        [element[0],float(element[1])])
print(numerical_list[:5])
                           

## 7. Filter the List ##

thousand_or_greater = []
for element in numerical_list:
    if element[1] >= 1000:
        thousand_or_greater.append(element[0])
print(thousand_or_greater[:10])