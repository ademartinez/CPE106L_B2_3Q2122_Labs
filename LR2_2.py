"""
CPE106L_B1_3Q2122 Problem 2
Filename: LR2_2.py
Program Description: Prints the contents of a specific line from a text file.
"""

def main():
    fileName = input("Enter fileName: ")
    f = open(fileName, 'r')
    textLines = []

    while True:
        for line in f:
            textLines.append(line.strip())
        print("The amount of lines in the file is: " + str(len(textLines)))
        number = int(input("Please type the line number: "))
        if number == 0: 
            quit()
        if number <= len(textLines):
            print(textLines[number - 1])
        else:
            print("There is no such line number in the file")
main()