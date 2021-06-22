import os

os.chdir(path) - установить текущий каталог
os.getcwd() - получить текущий каталог

>>> os.getcwd()
'C:\\Work\\TC\\Trainings\\My\\python\\script-007\\demo\\argparsing'

>>> os.path.dirname('c:\\1\\2\\3.txt')
'c:\\1\\2'

>>> os.path.join(os.getcwd(), 'data')
'C:\\Work\\TC\\Trainings\\My\\python\\script-007\\demo\\argparsing\\data'

>>> os.path.join(os.getcwd(), 'data', 'testfiles')
'C:\\Work\\TC\\Trainings\\My\\python\\script-007\\demo\\argparsing\\data\\testfiles'

>>> os.path.exists('c:\\1')
False
>>> os.path.exists('c:\\')
True

os.path.isfile(path)
os.path.getsize(path)

os.listdir(path='.')

os.remove(path)
os.rmdir(path)
os.removedirs(name)

os.makedirs(name, mode=0o777, exist_ok=False)
os.mkdir(path, mode=0o777, *, dir_fd=None)

