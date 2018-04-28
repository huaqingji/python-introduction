## 2. Defining the Dataset Class ##

class Dataset:
    def __init__(self):
        self.type = 'csv'
        
dataset = Dataset()
print(type(dataset))

## 3. Passing Additional Arguments to the Initializer ##

import csv

class Dataset:
    def __init__(self, data):
        self.type = "csv"
        self.data = data 

f = open('nfl.csv', 'r')
nfl_data = list(csv.reader(f))

nfl_dataset = Dataset(nfl_data)
dataset_data = nfl_dataset.data

## 4. Adding Additional Behavior ##

class Dataset:
    def __init__(self, data):
        self.data = data
        
    def print_data(self, num_rows):
        print(self.data[:num_rows])
        
nfl_dataset = Dataset(nfl_data)
nfl_dataset.print_data(5)
        

## 5. Enhancing the Initializer ##

class Dataset:
    def __init__(self, data):
        self.data = data[1:]
        self.header = data[0]

nfl_dataset = Dataset(nfl_data)
nfl_header = nfl_dataset.header

## 6. Grabbing Column Data ##

# define the class
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
        
    def column(self, label):
        col_idx = -1
        
        for idx, value in enumerate(self.header):
            if value == label:
                col_idx = idx
                
        if col_idx == -1:
            return None
        
        col_data = []
        for line in self.data:
            col_data.append(line[col_idx])
        return col_data

# use the class
nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year')
player_column = nfl_dataset.column('player')

## 7. Count Unique Method ##

# define the class
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
    # Add your count unique method here
    def count_unique(self, label):
        
        lst = self.column(label)
        return len(set(lst))
        
        
# use the class
nfl_dataset = Dataset(nfl_data)
total_years = nfl_dataset.count_unique('year')

## 8. Make Objects Human Readable ##

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    # method 1
    def __str__(self):
        return str(self.data[:10])
    
    # method 2
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
    # method 3    
    def count_unique(self, label):
        unique_results = set(self.column(label))
        count = len(unique_results)
        return count

nfl_dataset = Dataset(nfl_data)
nfl_dataset.__str__()