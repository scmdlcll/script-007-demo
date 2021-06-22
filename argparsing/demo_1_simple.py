import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--opt', help='This will be option')  # named argument
parser.add_argument('myparam', help='This will be parameter')  # positional argument
parser.add_argument('-b', '--bool', action='store_true', help='This will be flag')  # flag
parser.add_argument('-c', '--choice', choices=['1', '2', '3'], help='This will be choice')  # choice
parser.add_argument('-n', '--name', dest='myvar', help='Another variable name')
parser.add_argument('-r', '--required', help='Required parameter', required=True)
parser.add_argument('-d', '--default', help='Use default value', default='my value')

params = parser.parse_args()
print(str(params))
