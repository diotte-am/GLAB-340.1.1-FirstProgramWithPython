[![Per Scholas](per_scholas_logo.png)](https://www.perscholas.org) 

# First Program With Python

Introduction
hello.py is a simple program that asks the user for their name and age, and then greets them. When the user runs this program, it will prompt them to enter their name and age. After they enter this information, the program will greet them by name and tell them their age.

Lab Overview
This is the first lab for Python. In this lab, learners will write their first program. By the end of this lab, learners will be able to print messages including inputs from user using Python.


### hello.py

```
name = input("What's your name? ")
age = input("How old are you? ")

print("Hello, " + name + "!")
print("You are " + age + " years old.")
```

### hello.py (breakdown)

This program consists of three parts:

***User input:*** The program prompts the user to enter their name and age using the input() function. The input() function takes a string argument (in this case, the prompt), displays it on the screen, and waits for the user to enter a value. Whatever the user enters is returned as a string and stored in the variables name and age.

***Variable assignment:*** The program assigns the values entered by the user to two variables, name and age. Variables are used to store data that can be used later in the program. In Python, you don't need to specify the data type of a variable - Python will automatically assign the correct type based on the value you assign to it.

***Output generation:*** The program uses the print() function to generate output. The print() function takes one or more arguments and prints them to the screen. In this case, the program generates two output messages, one that greets the user by name, and another that tells the user their age.

Overall, this program is a very simple example of how Python can be used to take user input and generate output. With these basic concepts, you can begin to build more complex programs that perform more advanced tasks.

### Running the code

We can run this code with installed python version. Fire up your terminal (mac) or cmd/powershell(windows) to run the following commands:

*Check the version of the python first to make sure it has been installed*

```
python --version
```

*Run the script hello.py*

```
python hello.py
```

***Walkthrough***

![](https://github.com/ps-manish/GLAB-340.1.1-FirstProgramWithPython/blob/main/FirstProgramWithPython.gif)
