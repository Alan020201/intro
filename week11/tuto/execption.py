4CS001 - Introductory Programming And Problem Solving
Autumn 2022
Stream
Classwork
People
Classwork for 4CS001 - Introductory Programming And Problem Solving Autumn 2022
All topics
Coding Challenges
Lecture
Tutorial
Workshop
Extra Resource
Weekly Assignment
Coding Challenges
Coding Challenges
Assignment
Coding Challenge 3
Due Feb 6, 11:59 PM
Completed Assignment
Coding Challenge 2
3
3 comments
Due Jan 16, 11:59 PM
Completed Assignment
Coding Challenge 1
Due Dec 21, 2022, 11:59 PM
Lecture
Lecture
Material
Week 11 (Python)
Posted Jan 27
Material
Week 10(Python)
Posted Jan 19
Material
Week 9 (Python)
Posted Jan 13
Material
Week 7 (Python)
Edited Jan 1
Material
Week 6 (Python)
Posted Dec 22, 2022
Material
week 5 (Java)
Edited Dec 18, 2022
Material
week 4 (Java)
Edited Dec 13, 2022
Material
Week 3 (Java)
Posted Dec 2, 2022
Material
Week 2 (Java)
Posted Nov 26, 2022
Material
Week 1 (Java)
Posted Nov 17, 2022
Tutorial
Tutorial
Material
Week 11 (Python)
Edited Jan 30

Exception Handling.pptx
PowerPoint

File_Handling.pptx
PowerPoint

File_Handling_Solutions.txt
Text

data.csv
Comma Separated Values

Exception_Handling_Solutions.txt
Text
Material
Week 10 Tutorial
Posted Jan 20
Material
Week 9 Tutorial
Edited Jan 16
Material
Week 7 (python)
Edited Jan 1
Material
Week 6 (Python)
Posted Dec 23, 2022
Material
Week 5 (Java)
Edited Dec 16, 2022
Material
Week 4 (Java)
Edited Dec 14, 2022
Material
Week 3 (Java)
Posted Dec 4, 2022
Material
Week 1 (Java)
Edited Dec 2, 2022
Material
Week 2 (Java)
Edited Dec 2, 2022
Workshop
Workshop
Material
Week 11 Workshop
Posted Jan 29
Material
Workshop 9 (Python)
Posted Jan 15
Material
Week 7 (Python)
Edited Jan 2
Material
Week 6 (Python)
Posted Dec 25, 2022
Material
Week 5 (Java)
1
1 comment
Posted Dec 18, 2022
Material
Week 4 (Java)
Edited Dec 13, 2022
Material
Week 3 (Java)
Posted Dec 4, 2022
Material
Week 2 (Java)
3
3 comments
Edited Dec 4, 2022
Material
Week 1 (Java)
2
2 comments
Edited Dec 4, 2022
Extra Resource
Extra Resource
Material
Revision Slides
Posted Jan 25
Material
Additional Questions For Week 7
Posted Jan 2
Material
Python 3.11.1 Documentation From python.org
Posted Jan 1
Material
Drake Equation Sample Resource
Posted Dec 23, 2022
Material
More Java Practice Questions
Edited Dec 4, 2022
Material
Java Documentation From Oracle
Edited Dec 4, 2022
Material
Reeborg's World
Posted Dec 4, 2022
Weekly Assignment
Weekly Assignment
Assignment
Workshop Submission Week 11
Due Feb 4
Completed Assignment
Workshop Submission Week 9
Due Jan 21, 11:59 PM
Completed Assignment
Workshop Submission (Week 6 and Week 7)
1
1 comment
Due Jan 11, 11:59 PM
Completed Assignment
Workshop Submission Week 5
Due Dec 25, 2022, 11:59 PM
Completed Assignment
Workshop Submission Week 4
1
1 comment
Due Dec 18, 2022, 11:59 PM
Completed Assignment
Workshop Submission Week 3
Due Dec 12, 2022, 11:59 PM
Completed Assignment
Workshop Submission (Week 1 and Week 2)
12
12 comments
Due Dec 5, 2022, 11:59 PM
Exception Handling

# Exercise - 1 Solution

def factorial():
    try:
        num = int(input("Enter a number: "))
        result = 1
        for i in range(1,num+1):
            result = result*i
        return result
    except ValueError:
        print("Invalid input. Please enter a valid number")
        
result = factorial()

# Exercise - 2 Solution

def sort_words_in_file(file_name):
    try:
        with open(file_name, 'r') as f:
            words = f.readlines()
            words.sort()
    except IOError:
        print("Error reading the file.")
        return
    try:
        with open("sorted_"+file_name, 'w') as f:
            for word in words:
                f.write(word)
    except IOError:
        print("Error creating the new file.")

file_name = input("Enter the file name: ")
sort_words_in_file(file_name)

Exception_Handling_Solutions.txt
Displaying Exception_Handling_Solutions.txt.