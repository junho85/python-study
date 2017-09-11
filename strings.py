print("hello"*5)

greet = 'Hello Bob'
print(greet.upper())

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

text = "X-DSPAM-Confidence:    0.8475";
print(float(text[text.find(":")+1:].strip()))
print(float(text.split(":")[1]))