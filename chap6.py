# Enter your answrs for chapter 6 here
# Name: Tharathorn (Joy) Rimchala


# Ex. 6.6
def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

def print_test_word(word):
	if len(word) < 1:
		print "input is empty."
	else:
		print "first(" + word + ") = " + first(word)
		print "middle(" + word + ") = " + middle(word)
		print "last(" + word + ") = " + last(word)	

def is_palindrome(word):
	if (len(word) > 1):
		if (first(word) == last(word)):
			is_palindrome(middle(word))
			return True
		else:
			return False
	else:
		return False

def palindrome_check(word):
	boo = is_palindrome(word)
	if (boo == True):
		print word + " is a palindrome."
	else:
		print word + " is NOT a palindrome."
### Exercise 6.8.1
# ======================
print "Running Ex 6.8.1"
word1 = "a"
print_test_word(word1)

word2 = "ab"
print_test_word(word2)

word0 = ""
print_test_word(word0)

### Exercise 6.8.2
# ======================
print "Running Ex 6.8.2"
w1 = "a"
palindrome_check(w1)
w2 = "aa"
palindrome_check(w2)
w3 = "ab"
palindrome_check(w3)
w4 = "abcdcba"
palindrome_check(w4)
w5 = ""
palindrome_check(w5)

# Ex 6.8
def gcd(a,b):
	if (a < b):
		at = b
		b = a
		a = at

	if (b == 0): 
		return a
	else:
		r = a%b
		if (r == 0):
			return b
		else:
			gcd(b,r)

print str(gcd(25,50))