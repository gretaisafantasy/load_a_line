"""
Program: lines.py
Author: Greta Tanudjaja
Date: 6/25/2020

This program allows the user to load a file and, repeatedly, display
a line of their choice.

Input: The file name as a string and the line number that the user
would like to see as an int number.
Output:  The total number of lines in the file and a line of text
based on the supplied input.
"""

def main():
    """The main function for this script."""

    # Assign return to the function
    lineList = fileList()

    # Display the total number of lines in the file
    lineCount = print(len(lineList))
    
    # Infinite loop until the user terminates the program
    while True:

        # Prompt user for the line number that they would like to see
        lineNumber = int(input("Enter the line number that you would like "
                               "to see: "))

        # Ensure that the line number is not greater than the number of lines in
        # the file. If not, print an error and continue to ask for another number
        while lineNumber > len(lineList):
            print("Error: The line number that you would like to see is "
                  "greater than the number of lines in the file. Please enter "
                  "another number.")
            lineNumber = int(input("Enter the line number that you would like "
                                   "to see: "))

        # Ensure that the line number is not 0. If yes, exit the program
        if lineNumber == 0:
            break

        # If the line number is non-zero, display the appropriate line of text
        elif lineNumber <= len(lineList):
            print(lineList[lineNumber - 1])

    # Script will pause until the user presses the enter or return key
    input("Please press enter or return to quit the program.")

def fileList():
    """Returns the file contents into a list."""
    
    # Prompt user to input the file name
    fileName = input("Enter the file name: ")

    # Open and read text from the file name
    f = open(fileName, 'r')

    # Read the file contents into a list
    lineList = list(f)

    # Strip \n at the end of each line
    lineList = [line.strip('\n') for line in open(fileName)]

    # Return the list
    return lineList

# The entry point for program execution
if __name__ == "__main__":
     main()
    


    
    
