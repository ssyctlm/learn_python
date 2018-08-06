from sys import argv
script, aaa, bbb = argv

z1 = open(aaa)

z2 = open(bbb,'w')

z2.write(z1.read())

print "finished"

z1.close
z2.close
print "files are closed"