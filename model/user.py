from sys import maxsize


class User:

    def __init__(self, firstname=None, lastname=None, postcode=None, city=None, email=None, phone=None, password=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.postcode = postcode
        self.city = city
        self.email = email
        self.phone = phone
        self.password=password

        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id== other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize