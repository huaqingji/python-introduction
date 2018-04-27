## 2. Parsing the File ##

weather_data = []
f = open('la_weather.csv', 'r')
data = f.read()
rows = data.split('\n')
for row in rows:
    weather_data.append(row.split(','))

## 3. Getting a Single Column From the Data ##

weather = []
for element in weather_data:
    weather.append(element[1])

## 4. Counting the Items in a List ##

count = 0
for element in weather:
    count += 1

## 5. Removing the Header ##

new_weather = weather[1:]

## 6. The In Statement ##

animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]
cat_found = 'cat' in animals
space_monster_found = 'space_monster' in animals

## 7. Weather Types ##

weather_types = ["Rain", "Sunny", "Fog", "Fog-Rain", "Thunderstorm", "Type of Weather"]
weather_type_found = []
for type in weather_types:
        weather_type_found.append(type in new_weather)