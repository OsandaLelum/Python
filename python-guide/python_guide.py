# -*- coding: utf-8 -*-
"""python-guide.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qOPeYBx7HtDQe1vdL9Blu3LIG74YWI7Y

**The Zen of Python**

The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren’t special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you’re Dutch.
Now is better than never.
Although never is oen better than right now.
If the implementation is hard to explain, it’s a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea – let’s do more of those! *italicized text*

The Zen of Python is basically a list of Python Aphorishm’s written down in a poetic manner, to best showcase the good programming practices in Python.
The Zen of Python is a collection of guiding principles and aphorisms that capture the philosophy and design principles of the Python programming language. It was written by Tim Peters and is accessible by importing the "this" module in Python. The Zen of Python serves as a set of guidelines to encourage clean, readable, and Pythonic code. Here's an explanation of each line:

1. **Beautiful is better than ugly.**
   This line encourages writing code that is aesthetically pleasing and readable, as opposed to code that is messy or convoluted.

2. **Explicit is better than implicit.**
   It promotes being clear and explicit in your code rather than relying on hidden or implicit behavior.

3. **Simple is better than complex.**
   It suggests that simplicity in code is preferable to overly complicated solutions.

4. **Complex is better than complicated.**
   While simplicity is favored, if a problem requires complexity to solve, it's better to have a straightforward complex solution rather than an unnecessarily convoluted one.

5. **Flat is better than nested.**
   Code with fewer levels of indentation and nesting is considered more readable and maintainable.

6. **Sparse is better than dense.**
   It encourages using whitespace and newlines to make code more visually spacious and easier to comprehend.

7. **Readability counts.**
   The readability of code is crucial, as code is read more often than it is written.

8. **Special cases aren't special enough to break the rules. Although practicality beats purity.**
   While adhering to Pythonic principles is essential, it is acceptable to deviate if it leads to more practical and understandable solutions.

9. **Errors should never pass silently. Unless explicitly silenced.**
   Errors and exceptions should be made visible and handled properly rather than being ignored and causing hidden issues.

10. **In the face of ambiguity, refuse the temptation to guess.**
    When there are multiple possible interpretations, it's better to be explicit and avoid guessing.

11. **There should be one-- and preferably only one --obvious way to do it.**
    This reflects Python's principle of having one clear and idiomatic way to accomplish a particular task.

12. **Although that way may not be obvious at first unless you’re Dutch.**
    A light-hearted nod to Guido van Rossum, Python's creator, who is Dutch and might have a slightly different perspective on what is considered obvious.

13. **Now is better than never. Although never is often better than right now.**
    While timely development is important, it's better to wait and plan properly than rush into something hastily.

14. **If the implementation is hard to explain, it’s a bad idea. If the implementation is easy to explain, it may be a good idea.**
    Code should be straightforward and easy to understand by both the developer who wrote it and others who may need to read or maintain it.

15. **Namespaces are one honking great idea – let’s do more of those!**
    This line emphasizes the usefulness of namespaces to organize and avoid naming conflicts in code. It encourages using them effectively.

**Python is a high-level, interpreted, and dynamically-typed programming language known for its simplicity, readability, and versatility. It was created by Guido van Rossum and was first released in 1991. Python's design philosophy emphasizes code readability and a clean syntax, which allows programmers to express their ideas in fewer lines of code compared to other programming languages.**


**High-Level Programming Languag**e: Python is a high-level language, which means it provides abstractions that make it easier for developers to write code without worrying about low-level details. This allows programmers to focus more on the logic of their programs rather than managing memory or hardware-specific operations.

**Inbuilt Data Structures**: Python comes with a rich set of built-in data structures such as lists, tuples, dictionaries, sets, etc., which make it convenient to handle various types of data and manipulate them efficiently.

**Dynamic Binding **: Python is dynamically typed, which means the data types of variables are determined at runtime. This flexibility allows you to reassign variables to different data types during the execution of the program.

**Interpreted Language**: Python is an interpreted language, which means that the code is executed line by line by the Python interpreter. This allows for quick development and easy debugging since you can see the output of each line as you run the program.

**Object-Oriented Programming**: Python supports object-oriented programming (OOP) principles, allowing developers to structure their code into classes and objects, which promotes code reusability, encapsulation, and modularity.

**Easy to Write and Understand Syntax**: Python's syntax is designed to be simple and readable, using a clean and consistent indentation-based block structure. This readability makes it easy for beginners to learn and for experienced developers to maintain and collaborate on projects.

**Extensive Applicability and Library Support**: Python boasts a vast standard library that provides a wide range of functionalities for various tasks, from web development and data analysis to machine learning and scientific computing. Additionally, there is a rich ecosystem of third-party libraries and frameworks, such as NumPy, pandas, Django, Flask, TensorFlow, and PyTorch, which make Python extremely versatile and suitable for a wide array of applications.

Arithmetic operators are used to perform various mathematical operations on numeric values. Here are the main arithmetic operators in Python:

Addition (+): Used to add two or more numbers or concatenate strings.

Subtraction (-): Used to subtract the right operand from the left operand.

Multiplication (*): Used to multiply two numbers or repeat a string.

Division (/): Used to divide the left operand by the right operand. The result is always a float.

Floor Division (//): Used to divide the left operand by the right operand and truncate the result to an integer (rounded towards negative infinity).

Modulus (%): Used to find the remainder of the division of the left operand by the right operand.

Exponentiation ():** Used to raise the left operand to the power of the right operand.
"""

# Addition
result_add = 5 + 3
print(result_add)  # Output: 8

# Subtraction
result_sub = 10 - 4
print(result_sub)  # Output: 6

# Multiplication
result_mul = 3 * 5
print(result_mul)  # Output: 15

# Division
result_div = 15 / 4
print(result_div)  # Output: 3.75

# Floor Division
result_floor_div = 15 // 4
print(result_floor_div)  # Output: 3

# Modulus
result_mod = 15 % 4
print(result_mod)  # Output: 3

# Exponentiation
result_exp = 2 ** 3
print(result_exp)  # Output: 8



