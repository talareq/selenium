from model.user import User
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 1
f = "data/user.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_string_letters(prefix, maxlen):
     symbols_letters = string.ascii_letters + " "*5
     return prefix + "".join([random.choice(symbols_letters) for i in range(random.randrange(maxlen))])

def random_string_digits(prefix, maxlen):
    symbols_digits = string.digits + " "*5
    return prefix + "".join([random.choice(symbols_digits) for i in range(random.randrange(maxlen))])




testdata = [User(firstname="", lastname="", postcode="", city="", email="", phone="", password="",)] + [
    User(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
         postcode="32-600", city=random_string_letters("city", 10),
         email=random_string_letters("email", 1) + "@" +random_string_letters( "", 3)+ ".com", password=random_string_letters("", 7),)
    for i in range(1)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

