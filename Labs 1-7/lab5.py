#Python RegEx
#ex1- build in package called re
import re

#ex2-using regular expressions
#Check if the string starts with "The" and ends with "Spain":
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")
#YES! We have a match!


#ex3-Metacharacters
#[]	A set of characters
#Find all lower case characters alphabetically between "a" and "m":
import re

txt = "The rain in Spain"

x = re.findall("[a-m]", txt)
print(x) #['h', 'e', 'a', 'i', 'i', 'a', 'i']

#\	Signals a special sequence (can also be used to escape special characters)
#Find all digit characters:
import re

txt = "That will be 59 dollars"


x = re.findall("\d", txt)
print(x) #['5', '9']

#.	Any character (except newline character)
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
import re

txt = "hello planet"

x = re.findall("he..o", txt)
print(x)#['hello']

#^	Starts with
#Check if the string starts with 'hello':
import re

txt = "hello planet"

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
#Yes, the string starts with 'hello'

#$	Ends with
#Check if the string ends with 'planet':
import re

txt = "hello planet"

x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")
#Yes, the string ends with 'planet'

#*	Zero or more occurrences
#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
import re

txt = "hello planet"

x = re.findall("he.*o", txt)

print(x) #['hello']

#+	One or more occurrences
#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
import re

txt = "hello planet"

x = re.findall("he.+o", txt)

print(x) #['hello']

#?	Zero or one occurrences
#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"
import re

txt = "hello planet"

x = re.findall("he.?o", txt)

print(x) #[]

#{}	Exactly the specified number of occurrences
#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
import re

txt = "hello planet"

x = re.findall("he.{2}o", txt)

print(x) #['hello']

#|	Either or
#Check if the string contains either "falls" or "stays":
import re

txt = "The rain in Spain falls mainly in the plain!"

x = re.findall("falls|stays", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#['falls'] Yes, there is at least one match!

#()	Capture and group

#Special Sequences
#\A	Returns a match if the specified characters are at the beginning of the string
import re

txt = "The rain in Spain"

#Check if the string starts with "The":

x = re.findall("\AThe", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")
#['The'] Yes, there is a match!

#\b	Returns a match where the specified characters are at the beginning or at the end of a word
#(the "r" in the beginning is making sure that the string is being treated as a "raw string")
import re

txt = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#[] No match

import re

txt = "The rain in Spain"

#Check if "ain" is present at the end of a WORD:

x = re.findall(r"ain\b", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#['ain', 'ain'] Yes, there is at least one match!

#\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
#(the "r" in the beginning is making sure that the string is being treated as a "raw string")
import re

txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the beginning of a word:

x = re.findall(r"\Bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#['ain', 'ain'] Yes, there is at least one match!

import re

txt = "The rain in Spain"

#Check if "ain" is present, but NOT at the end of a word:

x = re.findall(r"ain\B", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#[] No match

#\d	Returns a match where the string contains digits (numbers from 0-9)
import re

txt = "The rain in Spain"

#Check if the string contains any digits (numbers from 0-9):

x = re.findall("\d", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#[] No match

#\D	Returns a match where the string DOES NOT contain digits
import re

txt = "The rain in Spain"

#Return a match at every no-digit character:

x = re.findall("\D", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  #['T', 'h', 'e', ' ', 'r', 'a', 'i', 'n', ' ', 'i', 'n', ' ', 'S', 'p', 'a', 'i', 'n'] 
  # Yes, there is at least one match!

#\s	Returns a match where the string contains a white space character
import re

txt = "The rain in Spain"

#Return a match at every white-space character:

x = re.findall("\s", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#[' ', ' ', ' '] Yes, there is at least one match!

#\S	Returns a match where the string DOES NOT contain a white space character
import re

txt = "The rain in Spain"

#Return a match at every NON white-space character:

x = re.findall("\S", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n']
#Yes, there is at least one match!

#\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
import re

txt = "The rain in Spain"

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.findall("\w", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#['T', 'h', 'e', 'r', 'a', 'i', 'n', 'i', 'n', 'S', 'p', 'a', 'i', 'n']
#Yes, there is at least one match!

#\W	Returns a match where the string DOES NOT contain any word characters
import re

txt = "The rain in Spain"

#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):

x = re.findall("\W", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#[' ', ' ', ' ']
#Yes, there is at least one match!

#\Z	Returns a match if the specified characters are at the end of the string
import re

txt = "The rain in Spain"

#Check if the string ends with "Spain":

x = re.findall("Spain\Z", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")
#['Spain']
#Yes, there is a match!

#Sets
#[arn]	Returns a match where one of the specified characters (a, r, or n) is present
import re

txt = "The rain in Spain"

#Check if the string has any a, r, or n characters:

x = re.findall("[arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#['r', 'a', 'n', 'n', 'a', 'n']
#Yes, there is at least one match!

#[a-n]
import re

txt = "The rain in Spain"

#Check if the string has any characters between a and n:

x = re.findall("[a-n]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#['h', 'e', 'a', 'i', 'n', 'i', 'n', 'a', 'i', 'n']
#Yes, there is at least one match!

#[^arn]
import re

txt = "The rain in Spain"

#Check if the string has other characters than a, r, or n:

x = re.findall("[^arn]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#['T', 'h', 'e', ' ', 'i', ' ', 'i', ' ', 'S', 'p', 'i']
#Yes, there is at least one match!

#[0123]
import re

txt = "The rain in Spain"

#Check if the string has any 0, 1, 2, or 3 digits:

x = re.findall("[0123]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  #[]
#No match

#[0-9]
import re

txt = "8 times before 11:45 AM"

#Check if the string has any digits:

x = re.findall("[0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
   #['8', '1', '1', '4', '5']
#Yes, there is at least one match!

#[0-5][0-9]
import re

txt = "8 times before 11:45 AM"

#Check if the string has any two-digit numbers, from 00 to 59:

x = re.findall("[0-5][0-9]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#['11', '45']
#Yes, there is at least one match!

#[a-zA-Z]
import re

txt = "8 times before 11:45 AM"

#Check if the string has any characters from a to z lower case, and A to Z upper case:

x = re.findall("[a-zA-Z]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#['t', 'i', 'm', 'e', 's', 'b', 'e', 'f', 'o', 'r', 'e', 'A', 'M']
#Yes, there is at least one match!

#[+]
import re

txt = "8 times before 11:45 AM"

#Check if the string has any + characters:

x = re.findall("[+]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
#[]
#No match

#The findall() Function
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x) #['ai', 'ai']

#Return an empty list if no match was found
import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x) #[] No match

#The search() Function
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())
#The first white-space character is located in position: 3

#Make a search that returns no match:
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x) #None

#The split() Function
import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x) #['The', 'rain', 'in', 'Spain']

#maxsplit parameter:
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x) #['The', 'rain in Spain']

#The sub() Function
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x) #The9rain9in9Spain

#count parameter:
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x) #The9rain9in Spain

#Match Object
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

#Print the position (start- and end-position) of the first match occurrence.
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span()) #(12, 17)

#Print the string passed into the function:
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string) #The rain in Spain

#Print the part of the string where there was a match.
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group()) #Spain




