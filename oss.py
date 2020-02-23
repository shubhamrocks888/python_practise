# import os
# os.getcwd() --> current directory we r working  '/Users/headshot'
# os.chdir() --> change the current directory
# os.chdir('/Users/headshot/Desktop')
# os.getcwd() --> '/Users/headshot/Desktop'
# os.listdir() --> gives files and folders of current directory ['.DS_Store', 'connecting-to-atlas.ipynb', '.localized', 'my.py', 'movies_initial.csv', 'django-projects', '__pycache__', 'env', 'monty', 'test.php', 'mongodb-compass-1.18.0-darwin-x64.dmg']
# os.mkdir('mon/non') --> doesnot create folder inside folder but can create folder
# os.makedirs('mon/non) -->  can create folder inside a folder
# os.rmdir('mon/non') --> if subfolder exists delete subfolder but cannot delete parent folder,however if no subfolder exists it can delete folder
# os.removedirs('mon/non) --> delete the whole folder including subfolder
# os.rename('mon','non') --> rename the file or folder
# os.stat('<file or folder name>') -->  gives the information about file
#  os.stat('demo') --> os.stat_result(st_mode=16877, st_ino=6602757, st_dev=16777223, st_nlink=11, st_uid=501, st_gid=20, st_size=352, st_atime=1581438775, st_mtime=1580824515, st_ctime=1580824515)
# os.stat('demo').st_mtime --> 1580824515
# os.walk(<path>) --> return a generator object i.e, <generator object walk at 0x104c287c8> actually return a tuple (currentpath,directories,files) --> currentpath is a string and directories and path are list
# os.environ --> return all the environment variables
# os.environ.get(<environment variable>)
# os.environ.get('PYTHONPATH') --> '/Users/headshot/Desktop'
# os.path.join(<path >,'demo') --> create a file path for a file
# os.path.basename('/tmp/mon/test.txt')  --> return a filename      'test.txt'
# os.path.dirname('/tmp/mon/test.txt')  --> return a directory name '/tmp/mon'
# os.path.split('/tmp/mon/test.txt')  -->       ('/tmp/mon', 'test.txt')
# os.path.exists('/tmp/mon/test.txt')  --> return True or False whether path exists or not
# os.path.isdir('/tmp/mon/test.txt')   --> return true or false whether it is file or nor
# os.path.isfile('/tmp/mon/test.txt')    --> return true or false whether it is directory or nor
# os.path.splitext('wallpaper2you_464171.jpg') --> ('wallpaper2you_464171', '.jpg')