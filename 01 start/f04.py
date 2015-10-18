def print_date(year=1970, month=1, day=1):
	#print "The date is " + month + "/" + day + "/" + year + "!"
	print "The date is %s/%s/%s" % (month, day, year)
	
print_date(1990, 7, 2)
print_date()
print_date(1980)

print_date(month=5)
print_date(year=1800, day=5)

print_date(1900, day=20)



