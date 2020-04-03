text = input("Input something: ")

# strip removes white spaces from beginning and end of text, returns a new string
print(text.strip())
# len gives the length of the string (includes whitespaces if not removed)
print(len(text))
# lower puts text in lower case
print(text.lower())
# upper puts text in upper case
print(text.upper())
# split splits the text into a list at the delimiter in quotes
print(text.split(', '))
# slice operator cuts out a portion of the string
# start:end:interval
# empty first number starts at beginning, empty second number ends at end
print(text[::2])
print(text[1:4:1])
# You can use slice to insert into an array
fruits = ['apples', 'pears', 'strawberries']
fruits[1:1] = 'beets'
print(fruits)