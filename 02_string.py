# Python Strings
# String is a sequence of characters

a = 'this is a single quote string'
b = "this is a double quote string"
c = '''
This is a multi-line string
'''

d = "I can't stop laughing"

e = 'I hate "Air Quotes"!!'

print(a)
print(b)
print(c)

#Replicating strings
print("-" * 10)
#formatting strings

#Modulo operator %

print('%d %s cost $%.2f' % (6, "bananas", 5.4689))

#string.format method
print('{0} {1} cost ${}'.format(3, "apples", 3.42))

print('{quantity} {item} cost ${price}'.format(quantity=7, item="oranges", price=12.45))

#f-string
quantity = 24
item = "jackfruit"
price = 5.67
print(f'{quantity} {item} cost ${price}')

print("-" * 50)

#concatenation & conversion
print(str(quantity) + ' ' + item + ' cost $' + str(price)) #any variable that is not a string must be converted to string by casting with str

#autoconcatenation
print('These' 'Words' 'Are' 'Auto' 'Concatenated')

#print length of string
print(len(a)) #length of string also includes spaces

#removing white spaces
d = '  this is a string with white spaces  '

d1 = d.strip() #removes white spaces from both ends
print(f'[{d1}]')

d2 = d.lstrip() #removes white spaces from left end
print(f'"[{d2}]"')

d3 = d.rstrip() #removes white spaces from right end
print(f'[{d3}]')

#partition 
print("-" * 50)

#accessing (indexing) strings

letters = 'abcdefghijklmnopqrstuvwxyz'

print(letters[3]) #indexing starts from 0
print(letters[-1]) #negative indexing starts from -1
print(letters[3:6]) #slicing from 3 to 6
print(letters[:6]) #slicing from start
print(letters[3:]) #slicing till end
print(letters[3:6:2]) #slicing with step
print(letters[::-1]) #reverse string prints whole string of characters in reverse order

print("-" * 50)

#finding substrings
print(letters.find('lmn')) #returns the index of the first occurence of the substring

music = 'Peter, Paul, and Mary'

print(music.find("Mary")) #returns the index of the first occurence of the substring
print(music.rfind("Mary")) 

print("-" * 50)

#replacing strings

name = "My name is Anglebert Humperdinck"
new_name = name.replace('Anglebert', 'Arnold')
print(new_name)

print("-" * 50) 

#splitting string
vowels = 'a e i o u'
split_vowels = vowels.split('') #splits the string into a list of substrings based on the delimiter ' '

print(split_vowels)

nums = '1,2,3,4,5,6,7,8,9'
split_nums = nums.split(',') #splits the string into a list of substrings based on the delimiter ','
print(split_nums)

#join strings
joined_nums = ':'.join(split_nums) #joins the substrings in the list with the delimiter ':'
print(joined_nums)

print("-" * 50)

# cases
v = "UPPER lower"

print(v.upper())
print(v.lower())
print(v.swapcase())
print(v.title())
print(v.capitalize())






