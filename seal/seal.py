# -*- coding: utf-8 -*-
# Nimi: Zhaoyang Chen
# Opiskelijanumero: 875497
# ​‌​​​​​‌‌‌​‌​​​ A class to describe a seal object
# ​‌​​​​​‌‌‌​‌​​​ Implement the missing functions here below

class Seal:

    def __init__(self, name: str):
        # raise NotImplementedError("You have not implemented the constructor.")
        self.name = name
        self.energy = 3
        self.friends = []
        self.location = "water"

    def eat(self):
        self.location = "water"
        self.energy = 5
        string = self.name + " ate a fish!"
        return string

    def climb_on_rock(self):
        self.location = "rock"
        string = self.name + ": Such a nice rock! :3"
        return string

    def do_banana_pose(self):
        if self.location == "water":
            return self.name + " is not on a rock."
        elif self.location == "rock" and self.energy > 1:
            self.energy -= 1
            return self.name + ": -__;3"
        elif self.location == "rock" and self.energy == 1:
            return self.name + ": I won't. ___:3"

    def add_friend(self, x):
        if x not in self.friends:  # to avoid adding the same friends over and over again
            self.friends.append(x)
            x.friends.append(self)

    def tell_friends(self):
        if len(self.friends) == 0:
            return ""
        else:
            string = ""
            string += self.friends[0].name
            if len(self.friends) > 1:
                for index in range(len(self.friends)):
                    if index == 0:
                        continue
                    else:
                        string += ", " + self.friends[index].name
            return string

    def request_banana_pose(self):
        if len(self.friends) == 0:
            return []
        else:
            response = []
            for friend in self.friends:
                response.append(friend.do_banana_pose())
            return response

    def __repr__(self):
        # ​‌​​​​​‌‌‌​‌​​​ Returns the representation of the object as a string:
        # ​‌​​​​​‌‌‌​‌​​​ the name of the seal and the unique identifier of this particular
        # ​‌​​​​​‌‌‌​‌​​​ Seal object. Reference for id():
        # ​‌​​​​​‌‌‌​‌​​​ https://docs.python.org/3/library/functions.html#id

        # ​‌​​​​​‌‌‌​‌​​​ You don't need to modify this method. It is used implicitly in the
        # ​‌​​​​​‌‌‌​‌​​​ unit tests to identify Seal objects that have been created in the
        # ​‌​​​​​‌‌‌​‌​​​ case some unit test does not pass.
        return "<Seal {}, id {}>".format(self.name, id(self))


if __name__ == "__main__":
    pass
    # ​‌​​​​​‌‌‌​‌​​​ You can experiment with the Seal class here
