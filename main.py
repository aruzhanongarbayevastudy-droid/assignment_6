# 1. Declare 2 numbers and calculate their sum
a = 10
b = 5
print(a + b)

# 2. Declare a string and reverse it
text = "hello"
print(text[::-1])

# 3. Declare a string and calculate its length
text = "Aru"
print(len(text))

# 4. Declare 2 strings and concatenate them
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)

# 5. Declare a character and check if it is a vowel
char = "a"
print(char.lower() in "aeiou")

# 6. Declare a string and swap the first and last characters
text = "hello"
result = text[-1] + text[1:-1] + text[0]
print(result)

# 7. Declare a string and convert it to uppercase
text = "hello world"
print(text.upper())

# 8. Declare the length and width of a rectangle and calculate its area
length = 10
width = 5
print(length * width)

# 9. Declare a number and check if it is even
number = 8
print(number % 2 == 0)

# 10. Declare a string and extract the first three characters
text = "Python"
print(text[:3])

# 11. Declare name and age and use string interpolation
name = "Aruzhan"
age = 27
message = f"My name is {name} and I am {age} years old."
print(message)

# 12. Declare a string and extract characters from index 2 to 5 (inclusive)
text = "Programming"
print(text[2:6])

# 13. Declare a number as a string and convert it to an integer
number = "123"
print(int(number))

# 14. Declare a string and repeat it 3 times
text = "Hi"
print(text * 3)

# 15. Declare 2 numbers and calculate the quotient and remainder
a = 17
b = 5
print("Quotient:", a // b)
print("Remainder:", a % b)

# 16. Declare 2 numbers and calculate the result of float division
a = 7
b = 2
print(a / b)

# 17. Declare a string and count the occurrences of a character
text = "banana"
print(text.count("a"))

# 18. Declare a string with double quotes inside using escape sequences
text = "She said, \"Hello!\""
print(text)

# 19. Declare and print a multi-line string
text = "Hello\nMy name is Aruzhan\nI learn Python"
print(text)

# 20. Declare base and exponent and calculate the power
base = 2
exponent = 3
print(base ** exponent)

# 21. Declare a palindrome string and check it without using loops
text = "racecar"
print(text == text[::-1])

# 22. Declare 2 strings and check if they are anagrams (ignoring case)
str1 = "listen"
str2 = "silent"
print(sorted(str1.lower()) == sorted(str2.lower()))