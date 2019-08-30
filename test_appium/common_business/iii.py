


s = "PYTHON"

s1 = "{0:30}".format(s)



s2 = "{0:>30}".format(s)


s3 = "{0:*^30}".format(s)


s4 = "{0:-^30}".format(s)


s5 = "{0:3}".format(s)


print("宽度")

l1 = "{0:-^20,}".format(1234567890)

l2 = "{0:-^20}".format(1234567890)
l3 = "{0:-^20,}".format(12345.67890)
print(s1,'\n',s2,'\n',s3,'\n',s4,'\n',s5)
print(l1,'\n',l2,'\n',l3)



f = "{0:.2f}".format(12345.67890)
