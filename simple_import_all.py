#!/usr/bin/python
''' simple.py '''
from module_root import *
from module.module_sub import *

print 'Hello, I will call module_root'
fun_root()

print 'I will call fun_sub'
fun_sub()

print "I will call fun_sub_2"
fun_sub_2()
