def sub(num1, num2):
	return int(num1)-int(num2)

def add(num3, num4):
	return int(num3)+int(num4)

def multiply(num5, num6):
	return int(num5)*int(num6)

def divide(num7, num8):
	return int(num7)/int(num8)

# Adding Strings vs Adding Ints
# When adding two strings together, they don't combine into a different number, they are only put next to eachother.
# For example, if I were to add str(num7)+str(num8), and num7 == "4" then num8 == "6", instead of getting 10, you'd
# get 46. However, with an integer, it add the numbers and you'd get 10. So make sure when doing this you make the numbers integers
# before the get added together.