## 1. Overview ##

f = open('movie_metadata.csv', 'r')
data = f.read()
rows = data.split('\n')
movie_data = []
for row in rows:
    movie_data.append(row.split(','))
print(movie_data[:5])



## 3. Writing Our Own Functions ##

def first_elts(input_lst):
    output_lst = []
    for item in input_lst:
        output_lst.append(item[0])
    return output_lst

movie_names = first_elts(movie_data)
print(movie_names[:5])

## 4. Functions with Multiple Return Paths ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input):
    if input[6] == 'USA':
        return True
    else:
        return False
    
wonder_woman_usa = is_usa(wonder_woman)
        


    
 

## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def index_equals_str(lst, index, string):
    if lst[index] == string:
        return True
    else:
        return False
    
wonder_woman_in_color = index_equals_str(lst = wonder_woman, string = 'Color', index = 2)
print(wonder_woman_in_color)

## 6. Optional Arguments ##

def feature_counter(input_lst, input_str, index, header_row = False):
    if header_row == True:
        input_lst = input_lst[1:]
    count = 0
    for item in input_lst:
        if item[index] == input_str:
            count += 1
    return count

num_of_us_movies = feature_counter(movie_data,'USA', 6, True)

## 7. Calling a Function inside another Function ##

def feature_counter(input_lst, input_str, index, header_row = False):
    if header_row == True:
        input_lst = input_lst[1:]
    count = 0
    for item in input_lst:
        if item[index] == input_str:
            count += 1
    return count

def summary_statistics(input_lst):
    
    num_japan_films = feature_counter(input_lst, 'Japan', 6, header_row = True)
    num_color_films = feature_counter(input_lst, 'Color', 2, header_row = True)
    num_films_in_english = feature_counter(input_lst, 'English', 5, header_row = True)
    
    output_dict = {}
    output_dict['japan_films'] = num_japan_films
    output_dict['color_films'] = num_color_films
    output_dict['films_in_english'] = num_films_in_english
    
    return output_dict

summary = summary_statistics(movie_data)