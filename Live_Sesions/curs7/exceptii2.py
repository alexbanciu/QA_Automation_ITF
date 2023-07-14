import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip()) # The default behavior of the strip() method is to remove the whitespace from the beginning and at the end of the string
    print(i)
    print(s)
except IOError as err:
    print("I/O error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise # The raise statement allows the programmer to force a specified exception to occur
          # simple raise - don’t intend to handle the exception

# To learn more, visit: https://docs.python.org/3.3/tutorial/errors.html


# f = open('myfile.txt')
# s = f.readline()
# # i = int(s.strip()) # The default behavior of the strip() method is to remove the whitespace from the beginning and at the end of the string
# # print(i)
# print(s)