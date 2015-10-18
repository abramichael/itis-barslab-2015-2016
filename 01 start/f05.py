def print_dictionary(**kwargs):
	for k,v in kwargs.iteritems():
		print "[%s]:<%s>" % (k, v)
		
print_dictionary(name="Victor", age="18", f=abs, pr=True)