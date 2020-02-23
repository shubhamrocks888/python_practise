
# f = open('test.txt','r') --> for opening a file AND also assign operation to it ..btw default is r
# f.name --> give the name of file
# f.mode --> give the mode of file  forex: it return r for the given f
# f.close() --> its a good practise to always close the file
# with open('test.txt','r') as f --> a context manager used to open a file and close it automatically when code block execution gets over
# f.read() ---> a whole file data is printed out
# f.readlines() --> a list of lines is printed
# f.readline() -->  only first line is printed(when you are calling again this funcion ,a next line is printed)
# for line in f.readlines():
#  print(line,end='')   --> print line by line
# f_contents = f.read(100)
    # print(f_contents,end='')      --> print 100 characters from line(when you are calling again this funcion ,a next 100 characters is printed)
# size_to_read = 100
#     f_contents = f.read(size_to_read)
#
#     while len(f_contents)>0:          --> print 100 characters each time
#         print(f_contents,end='')
#         f_contents = f.read(size_to_read)
# f.tell()  -->tell at what position we are currently in
#size_to_read = 10
    # f_contents = f.read(size_to_read)
    # print (f.tell())  -->  return 10
# f.seek(<position of pointer>) --> set the pointer to the desired position
# with open('test2.txt','w') as f:
#     f.write('Test')           --> create a file test2 if it is not created and it overwrite with the Test
# with open('test2.txt','w') as f:
#     f.write('Test')
#     f.seek(2)                 -->return "TeReady"
#     f.write('Ready')
# with open('test.txt','r') as rf:
#     with open('test_copy.txt','w') as wf:
#         for line in rf:                   -->  copy one file data into another file
#             wf.write(line)


