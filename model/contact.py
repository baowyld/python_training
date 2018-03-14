from sys import maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None,
                 homephone=None, mobilephone=None, workphone=None, secondaryphone=None,
                 id=None, all_phones_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize