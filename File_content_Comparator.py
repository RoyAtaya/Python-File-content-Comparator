#test_file = open("test2.txt","w+") # create file with w+ and open a file
#                                   # use ab+ to read and append to file
#                                   # use wb to write to the file
#                                   # use r+ to read adn write to the file
#
# print(test_file.mode) #tells you what mode the file is in,
# print(test_file.name)
#
# test_file.write("This is from pycharm. Hello world, I am now using the mode r+\n") #write to a file.
#
# print(test_file.read())
#
# test_file.close() #close a file


with open("test.txt") as x:
    d = x.read()
    f = " ".join(d).split()
# print(len(f))
# for i, value in enumerate(f):
#      print(i+1, value)
x.close()
with open("test2.txt") as z:
    e = z.read()
    s = " ".join(e).split()
z.close()


if len(s) == len(f):
    print("Lengths are the same")
    length = len(f)
else:
    print("Lengths are not the same")
    if len(s) > len(f):
        length = len(s)
    elif len(s) < len(f):
        length = len(f)

for i in range(length):
    if s[i] != f[i]:
        print("Mismatch found at index for list: ", i)
        print("element for position i list s: ", s[i])
        print("element for position i list f: ", f[i])
    elif i == length-1:
        print("No mismatches found")




# print("\n\n")
# m = "123"
# print("m = ", m)
# print(type(m))
# s = " ".join(m)
# print("s = ", s)
# print(type(s))
# ss = s.split()
# print("ss = ",ss)
# print(type(ss))
# print(len(ss))
# for i, value in enumerate(ss):
#     print(i, value)