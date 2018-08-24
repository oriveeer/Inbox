# -*- coding: utf-8 -*-

test_str =  """
test_1
test_2
"""
print test_str

#文字列の連結

test_str = 'python'
test_str += '345'
test_str += '678'
test_str += '9'

print test_str

#文字列へ変換

test_integer = 100

print str(test_integer) + '円'

#文字列の置換

test_str = 'python-izm'

print test_str.replace('izm', 'ism')

#

test_str = 'python-izm'

print test_str.split('-')
