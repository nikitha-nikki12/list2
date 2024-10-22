Write a program to create a list and display it. 
Input format:
Input consist of n+1 integers
First integer corresponds to the size of the list
Next n inputs corresponds to the elements in the list 
Output format: 
Output is an integer list
Sample Input
4 
1
2
3
4
Output
[1, 2, 3, 4]
# Function to create and display a list
def create_and_display_list():
    # Read the size of the list
    n = int(input("Enter the size of the list: "))
    
    # Initialize an empty list
    my_list = []
    
    # Read n elements and append them to the list
    for _ in range(n):
        element = int(input("Enter an element: "))
        my_list.append(element)
    
    # Display the list
    print(my_list)

# Call the function
create_and_display_list()


2)Write a program to create a list and display it. 
Input format:
Input consist of n+1 integers
First integer corresponds to the size of the list
Next n inputs corresponds to the elements in the list 
Output format: 
Output is an integer list
Sample Input
4 
1
2
3
4
Output
1 2 3 4
# Function to create and display a list
def create_and_display_list():
    # Read the size of the list
    n = int(input())
    
    # Initialize an empty list
    my_list = []
    
    # Read n elements and append them to the list
    for _ in range(n):
        element = int(input())
        my_list.append(element)
    
    # Display the list elements separated by spaces
    print(" ".join(map(str, my_list)))

# Call the function
create_and_display_list()

3)Write a Python Program to find the largest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
6
# Function to find the largest number in a list
def find_largest_number():
    # Read the size of the list
    n = int(input())
    
    # Initialize an empty list
    my_list = []
    
    # Read n elements and append them to the list
    for _ in range(n):
        element = int(input())
        my_list.append(element)
    
    # Find the largest element
    largest_number = max(my_list)
    
    # Display the largest number
    print(largest_number)

# Call the function
find_largest_number()

4)Write a Python Program to put the even and odd elements in a list into two different lists.
Input format:
Input consists of one integer and one list.
First input consists of the size of the list.
Second input consists of the elements based on the size.
Output format:
Output consists of two lists.
First list consists of all the even numbers in the list.
Second list consists of all the odd numbers in the list.
Sample Input:
5
1
2
3
6
5
Sample Output:
The even list [2, 6]
The odd list [1, 3, 5]
# Function to separate even and odd numbers into two lists
def separate_even_odd():
    # Read the size of the list
    n = int(input())
    
    # Initialize an empty list to store the elements
    my_list = []
    
    # Read n elements and append them to the list
    for _ in range(n):
        element = int(input())
        my_list.append(element)
    
    # Initialize lists for even and odd numbers
    even_list = []
    odd_list = []
    
    # Separate the elements into even and odd lists
    for num in my_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    
    # Display the results
    print("The even list", even_list)
    print("The odd list", odd_list)

# Call the function
separate_even_odd()

5)Write a program to find the sum of the elements in the array. 
Input Format: 
Input consists of n+1 integers where n corresponds to the number of elements in the array.
The first integer corresponds to n and the next n integers correspond to the elements in the array.
Assume that the maximum number of elements in the array is 20. 
Output Format: 
Output consists of a double value which corresponds to the mean of the array.
Refer sample input and output for formatting specifications.
Sample Input: 
5
2
4
1
3
1
Sample Output:
11
# Function to calculate the sum of elements in an array
def sum_of_elements():
    # Read the size of the array
    n = int(input())
    
    # Initialize a variable to store the sum
    total_sum = 0
    
    # Read n elements and calculate the sum
    for _ in range(n):
        element = int(input())
        total_sum += element
    
    # Output the sum
    print(total_sum)

# Call the function
sum_of_elements()

6)Write a Python Program to find the smallest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
1
  # Function to find the smallest number in a list
def find_smallest_number():
    # Read the size of the list
    n = int(input())
    
    # Initialize an empty list
    my_list = []
    
    # Read n elements and append them to the list
    for _ in range(n):
        element = int(input())
        my_list.append(element)
    
    # Find the smallest element
    smallest_number = min(my_list)
    
    # Display the smallest number
    print(smallest_number)

# Call the function
find_smallest_number()

7)Write a Program to find the search element in the given list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the elements of list in single line separated by space.
Third input consists of the element which we need to search
Sample Input 1:
5
1 2 3 6 5
3
Sample Output 1:
3 is present in the given list
Sample Input 2:
5
1 2 3 6 5
4
Sample Output 2:
# Function to search for an element in a list
def search_in_list():
    # Read the size of the list
    n = int(input())
    
    # Read the elements of the list as a single line of space-separated integers
    elements = list(map(int, input().split()))
    
    # Read the element to search for
    search_element = int(input())
    
    # Check if the search element is in the list
    if search_element in elements:
        print(f"{search_element} is present in the given list")
    else:
        print(f"{search_element} is not present in the given list")

# Call the function
search_in_list()

4 is not present in the given list
8)Write a program to count the number of times the given value is repeated.
Input Format:
First line of input consists of our list elements.
Second line of input consists of value to count.
Output Format:
Print thr number of times the given value is repeated in the list.
Sample Input:
10 20 10 40 10
10
Sample Output:
3
  # Function to count occurrences of a value in a list
def count_occurrences():
    # Read the list elements from the first line
    elements = list(map(int, input().split()))
    
    # Read the value to count from the second line
    value_to_count = int(input())
    
    # Count the occurrences of the value in the list
    count = elements.count(value_to_count)
    
    # Print the result
    print(count)

# Call the function
count_occurrences()

9)Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10 
10)Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 
# Function to print the list in reverse order
def print_reverse():
    # Read the list elements from the input
    elements = input().split()
    
    # Print the elements in reverse order
    print(" ".join(elements[::-1]))

# Call the function
print_reverse()
