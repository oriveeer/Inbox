# -*- coding: utf-8 -*-

#文字列の分割

test_str = 'python-izm'

print test_str.split('-')

#文字列の行揃え

test_str = '1234'

print test_str.rjust(10, '0')
print test_str.rjust(10, '!')

#文字列の検索

test_str = 'python-izm'

print 'z' in test_str
print 's' in test_str
