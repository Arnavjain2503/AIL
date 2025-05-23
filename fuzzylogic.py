# -*- coding: utf-8 -*-
"""FuzzyLogic.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zZA65irQ1Gm2h-fm8unWp1DB40vy9Z1w
"""

import numpy as np

# Function to ask user for fuzzy set values for all sets
def get_fuzzy_sets_input():
    n = int(input("Enter the number of elements in the fuzzy sets: "))
    sets = []
    for i in range(3):
        print(f"Enter membership values for Fuzzy Set {i+1}:")
        elements = []
        for j in range(n):
            value = float(input(f"Enter membership value for element {j+1} (between 0 and 1): "))
            elements.append(value)
        sets.append(np.array(elements))
    return sets

# Function to compute complement of a fuzzy set
def complement(fuzzy_set):
    return 1 - fuzzy_set

# Function to compute union of two fuzzy sets
def union(fuzzy_set1, fuzzy_set2):
    return np.maximum(fuzzy_set1, fuzzy_set2)

# Function to compute intersection of two fuzzy sets
def intersection(fuzzy_set1, fuzzy_set2):
    return np.minimum(fuzzy_set1, fuzzy_set2)

def main_program_12():
    print("Program 12: Fuzzy Set Operations - Union, Intersection and Complement with 3 fuzzy sets")

    fuzzy_sets = get_fuzzy_sets_input()

    fuzzy_set1, fuzzy_set2, fuzzy_set3 = fuzzy_sets

    print("Fuzzy Set 1:", fuzzy_set1)
    print("Fuzzy Set 2:", fuzzy_set2)
    print("Fuzzy Set 3:", fuzzy_set3)

    # Union of all three sets
    union_result = union(union(fuzzy_set1, fuzzy_set2), fuzzy_set3)
    print("Union of all three sets:", union_result)

    # Intersection of all three sets
    intersection_result = intersection(intersection(fuzzy_set1, fuzzy_set2), fuzzy_set3)
    print("Intersection of all three sets:", intersection_result)

    # Complement of all three sets
    complement_result1 = complement(fuzzy_set1)
    complement_result2 = complement(fuzzy_set2)
    complement_result3 = complement(fuzzy_set3)

    print("Complement of Fuzzy Set 1:", complement_result1)
    print("Complement of Fuzzy Set 2:", complement_result2)
    print("Complement of Fuzzy Set 3:", complement_result3)

if __name__ == "__main__":
    main_program_12()

import numpy as np

# Function to ask user for fuzzy set values for both sets
def get_fuzzy_sets_input():
    n = int(input("Enter the number of elements in the fuzzy sets: "))
    sets = []
    for i in range(2):
        print(f"Enter membership values for Fuzzy Set {i+1}:")
        elements = []
        for j in range(n):
            while True:
                value = float(input(f"Enter membership value for element {j+1} (between 0 and 1): "))
                if 0 <= value <= 1:
                    elements.append(value)
                    break
                else:
                    print("Invalid input! Please enter a value between 0 and 1.")
        sets.append(np.array(elements))
    return sets

# Function to compute complement of a fuzzy set
def complement(fuzzy_set):
    return 1 - fuzzy_set

# Function to compute union of two fuzzy sets
def union(fuzzy_set1, fuzzy_set2):
    return np.maximum(fuzzy_set1, fuzzy_set2)

# Function to compute intersection of two fuzzy sets
def intersection(fuzzy_set1, fuzzy_set2):
    return np.minimum(fuzzy_set1, fuzzy_set2)

def main_program_2():
    print("Program: Demonstrate De Morgan’s Law (Complement of Union)")

    fuzzy_sets = get_fuzzy_sets_input()
    A, B = fuzzy_sets

    print("\nFuzzy Set A:", A)
    # Complement of A
    A_complement = complement(A)
    print("Complement of A (A'):", A_complement)

    print("\nFuzzy Set B:", B)
    # Complement of B
    B_complement = complement(B)
    print("Complement of B (B'):", B_complement)

    # Intersection of A' and B' (De Morgan's Law 2)
    A_complement_intersection_B_complement = intersection(A_complement, B_complement)
    print("\nIntersection of the complements (A' ∩ B'):", A_complement_intersection_B_complement)

    # Union of A and B
    A_union_B = union(A, B)
    print("\nUnion of A and B (A ∪ B):", A_union_B)

    # Complement of the union (De Morgan's Law 2)
    complement_A_union_B = complement(A_union_B)
    print("Complement of union (A ∪ B)':", complement_A_union_B)


    # Showing the comparison of both sides of De Morgan's Law
    print("\nDe Morgan's Law (Complement of Union):")
    print(f"Complement of Union (A ∪ B)': {complement_A_union_B}")
    print(f"Intersection of Complements (A' ∩ B'): {A_complement_intersection_B_complement}")

    # Verify De Morgan's Law (Complement of Union = Intersection of Complements)
    if np.allclose(complement_A_union_B, A_complement_intersection_B_complement):
        print("\nDe Morgan's Law (Complement of Union) holds!")
    else:
        print("\nDe Morgan's Law (Complement of Union) does not hold.")

if __name__ == "__main__":
    main_program_2()
0

import numpy as np

# Function to ask user for fuzzy set values for both sets
def get_fuzzy_sets_input():
    n = int(input("Enter the number of elements in the fuzzy sets: "))
    sets = []
    for i in range(2):
        print(f"Enter membership values for Fuzzy Set {i+1}:")
        elements = []
        for j in range(n):
            while True:
                value = float(input(f"Enter membership value for element {j+1} (between 0 and 1): "))
                if 0 <= value <= 1:
                    elements.append(value)
                    break
                else:
                    print("Invalid input! Please enter a value between 0 and 1.")
        sets.append(np.array(elements))
    return sets

# Function to compute complement of a fuzzy set
def complement(fuzzy_set):
    return 1 - fuzzy_set

# Function to compute union of two fuzzy sets
def union(fuzzy_set1, fuzzy_set2):
    return np.maximum(fuzzy_set1, fuzzy_set2)

# Function to compute intersection of two fuzzy sets
def intersection(fuzzy_set1, fuzzy_set2):
    return np.minimum(fuzzy_set1, fuzzy_set2)

def main_program():
    print("Program: Demonstrate De Morgan’s Law (Complement of Intersection)")

    fuzzy_sets = get_fuzzy_sets_input()
    A, B = fuzzy_sets

    print("\nFuzzy Set A:", A)
    # Complement of A
    A_complement = complement(A)
    print("Complement of A (A'):", A_complement)

    print("\nFuzzy Set B:", B)
    # Complement of B
    B_complement = complement(B)
    print("Complement of B (B'):", B_complement)

    # Union of the complements of A and B (De Morgan's Law 1)
    A_complement_union_B_complement = union(A_complement, B_complement)
    print("\nUnion of the complements (A' ∪ B'):", A_complement_union_B_complement)

    # Intersection of A and B
    A_intersection_B = intersection(A, B)
    print("\nIntersection of A and B (A ∩ B):", A_intersection_B)

    # Complement of the intersection (De Morgan's Law 1)
    complement_A_intersection_B = complement(A_intersection_B)
    print("Complement of intersection (A ∩ B)':", complement_A_intersection_B)

    # Showing the comparison of both sides of De Morgan's Law
    print("\nDe Morgan's Law (Complement of Intersection):")
    print(f"Complement of Intersection (A ∩ B)': {complement_A_intersection_B}")
    print(f"Union of Complements (A' ∪ B'): {A_complement_union_B_complement}")

    # Verify De Morgan's Law (Complement of Intersection = Union of Complements)
    if np.allclose(complement_A_intersection_B, A_complement_union_B_complement):
        print("\nDe Morgan's Law (Complement of Intersection) holds!")
    else:
        print("\nDe Morgan's Law (Complement of Intersection) does not hold.")

if __name__ == "__main__":
    main_program()