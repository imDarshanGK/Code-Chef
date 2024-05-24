# Code Chef
Code Chef

Arrays in Python are commonly referred to as lists.

Arrays are used to store multiple values in a single variable, instead of declaring separate variables for each value.

In Python, a list is denoted by square brackets []

* It can hold elements of different data types, such as numbers, strings, or even other lists.
* Lists are mutable, which means you can modify them by adding, removing, or changing elements.
  
Consider the list 'fruits' and 'numbers' below

    fruits = ["apple", "banana", "orange", "grape"]

    numbers = [20, 10, 0, -5]
# Task

Write a program which does the following

* Create an Array of the first 5 positive integers - name it 'integers'
* Once the array is define - output "Done" to the console.
# While Loop
Loops can execute a block of code as long as a specified condition is reached.
They are handy because they save time, reduce errors, and they make code more readable.
The while loop loops through a block of code as long as a specified condition is true:

    while (condition):
        // code to be executed
Example

    counter = 0
    while counter < 5:
        print("The counter is:", counter)
        counter += 1
In the example above, the 'while' loop is executed as long as the condition 'counter < 5' is true.
The initial value of 'counter' is 0.

The code block inside the loop prints the value of 'counter' and increments it by 1 with the statement 'counter += 1'.
The loop will continue executing until 'counter' becomes equal to or greater than 5.

# Task
Write a program which does the following

 * Declare a variable a and initialise it to 0
 * Use the syntax above to create a loop, output the following to the console
      * Print a in separate lines as long as it is less than 7.
      * Increment a by 1 in each iteration.
        
solution:

        0
        1
        2
        3
        4
        5
        6
# Continue Statement
Recall that 'break' exit the loop entirely when its condition was met - ignoring all subsequent iterations.
The 'continue' statement skips one iteration (in the loop), if a specified condition occurs, and continues with the next iteration in the loop.

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for number in numbers:
        if number % 2 == 0:
            continue
        print(number)
In this example, the 'for' loop iterates over each number in the 'numbers' list.
Inside the loop, there is an 'if' statement that checks if the current number is even (divisible by 2).
If the condition is true, the 'continue' statement is executed, and the remaining code block for that iteration is skipped.

As a result, when an even number is encountered, the 'continue' statement is triggered, and the program jumps back to the beginning of the loop for the next iteration, without executing the 'print' statement.

Therefore, only the odd numbers in the list will be printed.

# Task
Write a program that does the following
* Declare a variable n and set it to a user defined input
* Output to the console a series of numbers from 1 to 10 with the following condition
  * Skips the number inserted by the user.

solution:

        1
        2
        3
        4
        6
        7
        8
        9
        10
# Data Types
Lets look at some common data types found in programming problems for beginners

 * Integers
    * Integers are whole numbers that can be negative, zero or positive. Examples - 15, 0, -5
 * Float
    * A float will have a decimal place. Examples - 4.5, -2.778
    * Note that 4.0, -2.0 are also floats
 * Strings
    * Strings are a group of characters. Examples - abcde, CodeChef, START69
    * Note that strings can also contain numerical characters. Examples a1b2c3d4, 532
 * Arrays / Lists
    * Arrays or lists are used to store multiple variables or input types. Examples of arrays
      * Array containing 6 integers - [1 , 5, 7, 10, 15, 2]
      * Array containing 4 strings - ["abcd", "d", "ccc", "c123"]
      * Array containing a combination of string and integers - ["abcd", 4, "ccc", 25]
    * Note that the strings in the array were denoted as "abcd" - we will come to this at a later stage
      
solution:

        -5
        4.0
        1234abc
        [1, 'ab', 3, 'name']
# What are test cases        
In the previous problem - we wrote the program to accept 5 inputs on 5 separate lines.

* What will we do if we expect 100 inputs or test cases?
* What about 100,000 inputs or test cases?
# Task
Lets solve a simple problem.
Write a program in the IDE which does the following
* Accepts the count of test cases - t - as an integer input given in the 1st line. This is followed by t lines - Each line contains an integer N
* For each test cases, prints out the integer N to console on a separate line (our Input mirror problem)
  
# Test cases with multiple lines of input
In the previous problem, we had t test cases and each test case had 1 line of input.

However, each test case can have multiple lines of input as well.

# Task
Lets write a program in the IDE which performs the following
 * The 1st line of input is an integer t - the count of test cases
 * Each test case consists of 2 lines of input
     * The 1st line of input has 2 space separated integers - accept them as variables A and B
     * The 2nd line of input has 3 space separated integers - accept them as variables C, D and E
 * For each test case - output all integers on a single line
# Sample 1:

   # Input 
    3
    1 2
    3 4 5
    11 22
    33 44 55
    1 23
    456 789 101111
    
# Explanation:
    2 lines of input in test case 1:
    1 2
    3 4 5
    
    Output 1: 1 2 3 4 5

    2 lines of input in test case 2:
    11 22
    33 44 55
    
    Output 2: 11 22 33 44 55

    2 lines of input in test case 3:
    1 23
    456 789 101112

    Output 3: 1 23 456 789 101112

 # Output

    1 2 3 4 5
    11 22 33 44 55
    1 23 456 789 101112
    
# Number mirror - Negative integer    
Let us now solve some programming problems. Note that

* In the IDE - the '#' - comments will give you hints about what you need to do
* The Solution tab also has '#' - comments which give you helpful information
# Task
Write a program in the IDE which does the following

* Accepts the count of test cases - t - in the 1st line
   * The only line of each test case consists of an integer N
* You need to generate the following output - Change the sign of  N.
# String mirror - Double strings
Write a program in the IDE which does the following
* Accepts the count of test cases - t - in the 1st line
  * First line of each test case consists of a string S
* You need to perform the following operation
  * Create a variable X which contains the string S concatenated with the string S
  * Output X for each test case
# Practice problem - Tuition fees
Let's solve this practice problem.

* You will attend tuitions for X weeks, and the cost of tuition per week is Y dollars.
* You need to compute and output your total tuition fees.

# Hint
* Refer to the multiplication syntax you learnt in the previous questions
* Run your code on the sample test cases before submitting the same
# Input Format
* The first line of input will contain an integer T — the number of test cases.
* The first and only line of each test case contains two space-separated integers X and Y
# Practice problem - Fitness
Chef wants to become fit for which he decided to walk to the office and return home by walking.
* It is known that Chef's office is X km away from his home.
* If his office is open on 5 days in a week, find the number of kilometres Chef travels through office trips in a week.
# Logical operators & conditional statements
We reviewed basic conditional operators in the previous module.
In this module - we will cover logical operators in conditional statements.

. "and" and "or" statements help check multiple conditions
. Multiple "and" and "or" statements can be clubbed into a single if / else condition

# Task

You are given 3 integers N,A and B.
You need to compute and output the following for each test case

. If N is divisible by both A and B - then output 'N is divisible by A and B'
. Else if N is divisible by A and not B - then output 'N is divisible by only A'
. Else if N is divisible by B and not A - then output 'N is divisible by only B'
. Else if N is divisible by neither A nor B - then output 'N is divisible by neither A nor B'

Solve this problem in the IDE.

Sample 1:

      Input                         
      4
      10 5 2
      10 3 2
      12 3 5
      10 4 3

Output

    N is divisible by A and B
    N is divisible by only B
    N is divisible by only A
    N is divisible by neither A nor B
# Logical operators
You are given 2 integers A and B.

You need to compute and output the following for each test case.
* If A is not equal to B and A and B are both odd - then output 'A and B are different and are odd'
* Else if A is not equal to B and A and B are both even - then output 'A and B are different and are even'
* For every other value of A and B, output 'Doesn't matter'

  Sample 1:
  
      Input
        4
        -9 5
        3 3
        -10 10
        2 1
  Output

      A and B are different and are odd
      Doesn't matter
      A and B are different and are even
      Doesn't matter
# Debug this code - Advance

The code in the IDE is incorrect - debug the code to solve this problem!

Chef's current rating is X, and he wants to improve it.
It is generally recommended that a person with rating X should solve problems whose difficulty lies 
in the range [X,X+200], i.e, problems whose difficulty is at least X and at most X+200.
You find out that Chef is currently solving problems with a difficulty of Y.
Is Chef following the recommended practice or not?
