import os

# print (os.getcwd())
# os.chdir('/Users/headshot/PycharmProjects/untitled10')
# print (os.listdir())
# os.mkdir('monty')
# os.rmdir('monty')
# os.rename('monty','mayank')
# os.rmdir('mayank')
# print (os.walk('/Users/headshot/PycharmProjects/untitled10'))
# for path,dir,file in os.walk(os.getcwd()):
#     if 'oss.py' in file:
#         print (path)
# print (os.path.join('/Users/headshot/PycharmProjects/untitled10','oss.py'))
# print (os.path.basename('/Users/headshot/PycharmProjects/untitled10/oss.py'))
# print (os.path.splitext('/Users/headshot/PycharmProjects/untitled10/oss.py'))
# print (os.path.isfile('/Users/headshot/PycharmProjects/untitled10/oss'/Users/headshot/PycharmProjects/untitled10'.py'))
# print (os.path.exists('/Users/headshot/PycharmProjects/untitled10/oss.py'))

for path,dir,file in os.walk('/Users/headshot/PycharmProjects'):
    if 'oss.py' in file:
        print (path)

        print (os.path.join(path,'oss.py'))