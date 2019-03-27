
name = 'allen'
print('%s' % (name))

filename = "%s.pub" %name

# Create a file object:
# in "write" mode
FILE = open(filename, "w")

e = 99
phi_n = 1000

public_key = str(e, phi_n)
public_key = str(public_key)
# Write all the lines at once:
FILE.writelines(public_key)

# Close
FILE.close()

'''
f = open(FILE, 'r')
print(f.read())
f.close()
'''