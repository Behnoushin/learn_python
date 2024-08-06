import random , string
pswwd = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(pswwd) for i in range (10))
print (password)