#!/usr/bin/python
''' simple.py '''
import module_root
import module.module_sub

print 'Hello, I will call module_root'
module_root.fun_root()

print 'I will call fun_sub'
module.module_sub.fun_sub()

print "I will call fun_sub_2"
module.module_sub.fun_sub_2()
