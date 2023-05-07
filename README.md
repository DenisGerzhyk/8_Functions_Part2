# 8_Functions_Part2


File EX 1,2,3:

1).
The popular_words function takes a string and a list of words as input, and returns a dictionary where the keys are the words in the list, and the values are the number of times each word appears in the input string. The function first converts the input string to lowercase and removes all whitespace. Then, it loops over the words in the list and uses the count method to count the number of times each word appears in the modified string. Finally, the function returns the resulting dictionary.

For example, the function call popular_words("Who are you and whats your name", ["y", "e"]) would return the dictionary {'y': 2, 'e': 2} because the letters 'y' and 'e' appear twice each in the input string.

2).
The max_min function takes a tuple of numbers as input and prints the difference between the maximum and minimum values in the tuple, rounded to two decimal places. If the input tuple is empty, the function prints 0.

For example, the function call max_min((1, 4, 6, 4, 7, 4, 2, 9, -2, 44, 2, 3)) would print the value 46.00 because the difference between the maximum value (44) and minimum value (-2) in the tuple is 46. The round function is used to round the result to two decimal places.


File FUNC3:

1).
The first function count_elements(lst, s) takes in a list lst and a string s. It creates an empty dictionary counts and loops over each element in the list lst. For each element, it adds an entry in the dictionary with the element as the key and the count of that element in the string s as the value. Finally, the function returns the dictionary counts.

For example, calling count_elements(['i', 'was'], "Hey , i was in market") would return {'i': 3, 'was': 1}.

2).
The function func(n) takes in a tuple n and returns the difference between the maximum and minimum values in the tuple rounded to 2 decimal places. The max and min functions are used to find the maximum and minimum values in the tuple, and then their difference is rounded using the round function.

For example, calling func((10.2, -2.2, 0, 1.1, 0.5)) would return 12.4.

3).
The function generate_odd_numbers(n) takes in an integer n and uses a generator to yield the cubes of odd numbers between 1 and n. It does this using a for loop that loops over the range from 1 to n, and for each odd number it yields the cube of that number using the yield keyword.

For example, calling generate_odd_numbers(5) would yield 1, 27, and 125.

4).
The function func(string) takes in a list of strings string and uses a generator to yield any string that contains the letter 'A'. It does this using a for loop that loops over each string in the list, and if the string contains the letter 'A', it yields the string using the yield keyword.

For example, calling func(["Hey Im Ann", "I look good", "Yea,i know"]) would yield "Hey Im Ann".

5).
The first function func(word) takes in a string word and uses a generator to yield each pair of adjacent characters in the string. It does this using a for loop that loops over each character in the string, and for each character it yields the pair of that character and the next character in the string using the yield keyword.

For example, calling func("allerg") would yield "al", "ll", "le", "er", and "rg".

The second function func2(word) takes in a string word and uses a generator to yield the first and last characters of the string as a pair. It does this using the yield keyword to yield the pair of the first character of the string and the last character of the string.

For example, calling func2("allerg") would yield "ag".

6).
The function func(number) takes in an integer number and uses a generator to yield the Fibonacci sequence up to number. It does this using a while loop that continues as long as the current Fibonacci number a is less than or equal to number. For each iteration, it yields the current Fibonacci number a using the yield keyword, and then updates a and b to the next two Fibonacci numbers.

For example, calling func(100) would yield 0, 1, 1, 2, 3, 5, 8, 13, 21, `34


File Практика:

1).
This program defines a function called printGroceries that takes a variable number of arguments. The function loops through the arguments and checks if each one is a string with a length of at least 2 characters. If it is, the function increments a counter and prints the counter value and the string argument.

2).
This program defines a function called personalData that takes a variable number of keyword arguments. The function loops through the keyword arguments and prints out each key-value pair in alphabetical order of the keys.

3).
This program defines a function called evaluate that takes a list of coefficients and a value for the argument x. The function uses a for loop to calculate the value of the polynomial function defined by the coefficients and the argument x. The function prints the result.

4).
This program defines a function called consonant that takes a string and a string of vowels as arguments. The function uses a lambda function and the built-in map function to map each character in the input string to either "vowel" or "consonant" depending on whether it is a vowel or not. The function returns a list of the mapped values.

5).
This program defines a function called func that takes a list of numbers and a divisor as arguments. The function uses a lambda function and the built-in `map

6).
This code defines a function positive that takes a single argument num and returns True if num is greater than or equal to 0, and False otherwise. The function main takes a list of numbers as input and returns a new list of the squares of all the non-negative numbers in the input list. This is done using the map function to apply the lambda function that calculates the square of each number, and the filter function to keep only the non-negative numbers.

7). 
This code defines two functions kratno and main1 and main2. kratno takes a single argument num and returns True if num is divisible by 3, and False otherwise. The function main1 takes a list of numbers as input and returns a new list of the cubes of all the numbers in the input list that are divisible by 3. The function main2 does the same thing as main1, but returns the original numbers instead of their cubes. This is done using the map function to apply the lambda function that calculates the cube or returns the number itself, and the filter function to keep only the numbers that are divisible by 3.

8).
This code defines a function zipper that takes two lists spis1 and spis2 as input and returns a dictionary dir that maps each element of spis1 to the corresponding element of spis2. This is done using the zip function to iterate over the two lists simultaneously and create pairs of corresponding elements, and then creating a dictionary from these pairs.

9).
This code defines a function redu that takes a single argument num and returns num if num is even, and None otherwise. The function main takes a list of numbers as input and returns the product of all the even numbers in the input list. This is done using the filter function to keep only the even numbers, and the reduce function to multiply them together. Note that the initial value of the accumulator in the reduce function is not specified, so it defaults to the first element of the filtered list.
