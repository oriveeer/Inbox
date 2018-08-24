import ui

num = 0

def plus(sender):
	global num
	label = sender.superview['label1']
	num = num + 1
	label.text = str(num)

v = ui.load_view()
v.present('sheet')

def clear(sender):
	global num
	label = sender.superview['label1']
	num = 0
	label.text = str(num)

v = ui.load_view()
v.present('sheet')
