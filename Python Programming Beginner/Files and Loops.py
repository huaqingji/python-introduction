## 1. Opening Files ##

f = open('crime_rates.csv','r')

## 2. Reading In Files ##

f = open("crime_rates.csv", "r")
data = f.read()

## 3. Splitting ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[:5])

## 5. Practice - Loops ##

ten_rows = rows[0:10]
for row in rows:
    print(row)

## 6. List of Lists ##

three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []
for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)
print(final_list[0])
print(final_list[1])
print(final_list[2])

## 7. Practice - Splitting Elements in a List ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')

final_data = []
for row in rows:
    final_data.append(row.split(','))
print(final_data[:5])

## 8. Accessing Elements in a List of Lists: The Manual Way ##

cities_list = []
for element in five_elements:
    cities_list.append(element[0])

## 9. Looping Through a List of Lists ##

cities_list = []
for element in final_data:
    cities_list.append(element[0])

## 10. Challenge ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')

int_crime_rates = []
for row in rows:
    row_list = row.split(',')
    int_crime_rates.append(int(row_list[1]))
    
