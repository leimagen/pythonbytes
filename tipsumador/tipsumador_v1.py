print("\n")
print("\n")
print("-")
print("-=")
print("-=-")
print "    ----  Hello and welcome to \"Tip Sumador v.1.0\""
print("-==")
print("-=")
print("-")
print("\n")
print("\n")

print "Please fill in the amount of each day tip earnings:"

day1 = float(raw_input("Monday: "))
day2 = float(raw_input("Tuesday: "))
day3 = float(raw_input("Wednesday: "))
day4 = float(raw_input("Thursday: "))
day5 = float(raw_input("Friday: "))

def week_earnings(mon,tue,wed,thu,fri):
	final_earnings = float(mon + tue + wed + thu + fri)
	print("\n")
	print("\n")
	print "*** Congratulations! Your week earnings were $%s! ***" % final_earnings
	
week_earnings(day1,day2,day3,day4,day5)