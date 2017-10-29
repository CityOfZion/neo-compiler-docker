import sys
from boa.compiler import Compiler

path = '/compile/src/' + sys.argv[1]
Compiler.load_and_save(path)