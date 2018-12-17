#!/usr/bin/python
''' simple.py '''
from module_root import fun_root
from module.module_sub import fun_sub

print 'Hello, I will call module_root'
fun_root()

print 'I will call module_sub'
fun_sub()

print "I will try to call module_sub_not_imported"
print "Note that we haven't imported it from module.module_sub"
try:
  fun_sub_2()
except Exception as e:
  print "As you can see it failed to run. Exception message was: " + str(e)
