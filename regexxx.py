import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1 2,3 4,5,6 7 8,90
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
urls = ''' https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov     '''
sentence = 'Start a sentence and then bring it to an end'
# x= '1 2,3 4,5,6 7 8,90,'
# pattern = re.compile(r'[\d\s,]+[\d]')
# matches = pattern.finditer(x)
# for match in matches:
#     print (match)


#
# for match in matches:
#     print (match)                     --->    <re.Match object; span=(1, 4), match='abc'>

# pattern = re.compile(r'\.')
# matches = pattern.finditer(text_to_search)  --> '.' is a special character in regex if you search like that you got all the elements
#                                                 so,you have to search with '\.'
#
# for match in matches:
#     print (match)

# if you have to search for 'coreyms.com',then you have to go for 'coreyms\.com'

# we are looking for  above phone numbers like 321-555-4321
# ('.') it represents any character excepts new line
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print (match)

# checking phone numbers in data.txt
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# with open('data.txt','r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#     for match in matches:
#         print (match)

# we are looking for  above phone numbers like 321-555-4321
# without . character
# pattern = re.compile(r'\d\d\d[-.*]\d\d\d[-.*]\d\d\d\d')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print (match)

# we are looking for  above phone numbers 800-555-1234,900-555-1234
# without . character
# pattern = re.compile(r'[89]00-\d\d\d-\d\d\d\d')
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print (match)

#patterns =re.compile(r'[1-5]')  --> give the character that has range between 1 to 5
# r'[a-zA-Z]' --> gives the characters between a to z and A to Z

# we are looking for cat,mat,pat not bat
# r'[^b]at'

#r'Mr\.'   --> Mr.
#r'Mr\.?'  --> Mr. and Mr (not containing'.')
#r'Mr/.?\s'  --> containing space after the previous command
#r'Mr\.?\s[A-Z]\w*' ---> containing a 1 word character or more  after'Mr. S'
#r'(Mr|Ms|Mrs)'   ---> return Mr or Ms or Mrs

#r'[a-zA-Z]+@[a-z]+\.com'       --->            CoreyMSchafer@gmail.com
#r'[a-zA-Z]+\.[a-z]+@[a-z]+\.edu'               corey.schafer@university.edu

#r'[a-zA-Z0-9.-]+[a-z]+@[a-z-]+\.(edu|com|net)' --->'CoreyMSchafer@gmail.com','corey.schafer@university.edu','corey-321-schafer@my-work.net'

# pattern  = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print (match)         --> o/p is url

# for match in matches:
#     print(match.group(0))     --> o/p is all the urls

# for match in matches:
#     print (match.group(1))
# o/p is
# www.
# None
# None
# www.

# for match in matches:
#     print (match.group(2))
# o/p is
# google
# coreyms
# youtube
# nasa

# for match in matches:
#     print (match.group(3))
# o/p is
# .com
# .com
# .com
# .gov

# we are looking for urls
# o/p is urls
# pattern  = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
# subbed_urls = pattern.sub(r'\2\3',urls)
# print (subbed_urls)
#o/p is
# google.com
# coreyms.com
# youtube.com
# nasa.gov

# pattern = re.compile(r'[a-zA-Z0-9.-]+[a-z]+@[a-z-]+\.[a-z]+')
# matches = pattern.findall(text_to_search) ----> findall returns match string
#
# for match in matches:
#     print (match)

# o/p is    CoreyMSchafer@gmail.com,corey.schafer@university.edu,corey-321-schafer@my-work.net

# pattern = re.compile(r'[a-zA-Z0-9.-]+[a-z]+@[a-z-]+\.(com|edu|net)')
# matches = pattern.findall(text_to_search)  --> if group is there,then it works with groups
#
# for match in matches:
#     print (match)
#o/p is
# com
# edu
# net

# pattern = re.compile('Start')
# matches = pattern.match(sentence)     ---> it matches only at the start of the string
# print (matches)                       ---> o/p:   <re.Match object; span=(0, 5), match='Start'>

# pattern = re.compile('sentence')
# matches = pattern.match(sentence)
# print (matches)                           ---> o/p:None

# pattern = re.compile('sentence')
# matches = pattern.search(sentence)     ---> <re.Match object; span=(8, 16), match='sentence'>
# print (matches)

#flags used to provide  more searching fuctionality
# pattern = re.compile('start',re.IGNORECASE)
# matches = pattern.search(sentence)            ----> <re.Match object; span=(0, 5), match='Start'>
# print (matches)
