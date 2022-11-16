#!/usr/bin/env python3

wordbank= ["identification", "spaces"]

tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

wordbank.append(4)
print(wordbank)

pick= int(input("Choose a number between 0 and 20.\n"))
pick= int(pick)

student_name= tlgstudents[pick]

print(f"{student_name} always uses {wordbank[-1]} {wordbank[1]} to indent.")
