## 2. Enumerate ##

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i, value in enumerate(ships):
    print(value)
    print(cars[i])

## 3. Adding Columns ##

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i, value in enumerate(things):
    value.append(trees[i])

## 4. List Comprehensions ##

apple_prices = [100, 101, 102, 105]
apple_prices_doubled = [2 * i for i in apple_prices]
apple_prices_lowered = [i -100 for i in apple_prices]

## 5. Counting Female Names ##

name_counts = {}
for row in legislators:
    if row[3] == 'F' and row[7] > 1940:
        name = row[1]
        if name in name_counts:
            name_counts[name] += 1
        else: 
            name_counts[name] = 1

## 7. Comparing with None ##

values = [None, 10, 20, 30, None, 50]
checks = []
for i in values:
    j = i is not None and i > 30
    checks.append(j)


## 8. Highest Female Name Count ##

max_value =None
for name in name_counts:
    count = name_counts[name]
    if max_value is None or max_value < count:
        max_value = count
        

## 9. The Items Method ##

plant_types = {"orchid": "flower", "cedar": "tree", "maple": "tree"}
for key, value in plant_types.items():
    print(key)
    print(value)

## 10. Finding the Most Common Female Names ##

top_female_names = []
for name in name_counts:
    if name_counts[name] == 2:
        top_female_names.append(name)
        

## 11. Finding the Most Common Male Names ##

# find the most common male name
top_male_names = []

male_name_counts ={}
for row in legislators:
    if row[3] == 'M' and row[7] > 1940:
        name = row[1]
        if name in male_name_counts:                 male_name_counts[name] += 1
        else:
            male_name_counts[name] = 1
            
max_value = None
for name in male_name_counts:
    count = male_name_counts[name] 
    if max_value is None or count > max_value:
        max_value = count
        
for name in male_name_counts: 
    count = male_name_counts[name]
    if count == max_value:
        top_male_names.append(name)