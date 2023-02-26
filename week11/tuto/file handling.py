#Exercise-1 Solution

file_name = input("Enter the file name: ")
word_to_search = input("Enter the word to search for: ")

try:
    with open(file_name, 'r') as f:
        text = f.read()
        word_count = text.count(word_to_search)
        print("The word '{}' appears {} times in the file.".format(word_to_search, word_count))
except:
    print("Error reading the file.")


#Case Study-1 Solution

import csv

def average_salary(file_name):
    total_salary = 0
    count = 0
    try:
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            next(reader) # skipping the header row
            for row in reader:
                total_salary += float(row[2])
                count += 1
            return total_salary / count
    except:
        print("Error reading the file.")

file_name = "employees.csv"
print("Average salary:", average_salary(file_name))
