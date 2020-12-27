"""
@author: leonardomunoz
version 12.27.20
"""

import numpy as np

def menu():
    menu_selection = input("Welcome! Which operation would you like to perfom?\n1.) Addition\n2.) Subtraction\n")
    if int(menu_selection) == 1:
        rows = input("Rows: ")
        cols = input("Columns: ")
        addition(int(rows), int(cols))
    elif int(menu_selection) == 2:
        rows = input("Rows: ")
        cols = input("Columns: ")
        subtraction(int(rows), int(cols))
        

def matrix_builder(rows,cols):
    matrix = np.zeros((rows, cols), dtype=int)
    for i in range(len(matrix)):
        for k in range(len(matrix[i])):
            argu = input()
            try:
                matrix[i][k] = argu
            except ValueError:
                pass
    print(matrix)
    return matrix

def addition(rows, cols):
    print("Input the values for the 1st matrix from left to right and top to bottom one argument at a time.")
    matrix1 = matrix_builder(rows, cols)
    print("Input the values for the 2nd matrix from left to right and top to bottom one argument at a time.")
    matrix2 = matrix_builder(rows, cols)
    result = np.zeros((rows, cols), dtype=int)
    
    for i in range(len(result)):
        for k in range(len(result[i])):
            result[i][k] = matrix1[i][k] + matrix2[i][k]
    print(result)
    return


def subtraction(rows, cols):
    return
if __name__=="__main__":
    menu()