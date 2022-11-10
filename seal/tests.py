# -*- coding: utf-8 -*-
# Nimi: Zhaoyang Chen
# Opiskelijanumero: 875497
#​‌​​​​​‌‌‌​‌​​​ Seal: unit tests for student
#​‌​​​​​‌‌‌​‌​​​ Instruction: run this as a Python unit test in Eclipse PyDev.


import unittest
from seal import Seal

class Test(unittest.TestCase):

    def test_01_constructor(self):
        """The constructor should initialise the correct values."""

        s = Seal("Aristoteles")
        self.assertEqual(s.name, "Aristoteles")
        self.assertEqual(s.energy, 3)
        self.assertEqual(s.friends, [])
        self.assertEqual(s.location, "water")

    def test_02_eat(self):
        """eat() should work correctly."""

        s = Seal("Alina")
        self.assertEqual(s.eat(), "Alina ate a fish!")
        self.assertEqual(s.energy, 5,
            "Seal's energy should be 5 after eating a fish.")
        self.assertEqual(s.location, "water",
            "Seal's location should be water after eating a fish.")

    def test_03_climb_on_rock(self):
        """climb_on_rock() should work correctly."""

        s = Seal("Walter")
        self.assertEqual(s.climb_on_rock(), "Walter: Such a nice rock! :3")
        self.assertEqual(s.location, "rock")

    def test_04_do_banana_pose(self):
        """The do_banana_pose() method should have three cases."""

        s = Seal("Ella")
        self.assertEqual(s.do_banana_pose(), "Ella is not on a rock.")
        s.climb_on_rock()
        self.assertEqual(s.do_banana_pose(), "Ella: -__;3")
        self.assertEqual(s.do_banana_pose(), "Ella: -__;3")
        self.assertEqual(s.do_banana_pose(), "Ella: I won't. ___:3")

    def test_05_add_friend(self):
        """add_friend() should work correctly."""

        s1 = Seal("Aristoteles")
        s2 = Seal("Alina")
        s3 = Seal("Walter")

        s1.add_friend(s2)
        self.assertEqual(s1.friends, [s2],
            ("After adding seal {0} to friends of seal {1}, {1}'s friend list "
            "should have {0} once.").format(s2.name, s1.name))

        self.assertEqual(s2.friends, [s1],
            ("After adding seal {0} to friends of seal {1}, also {0}'s friend list "
            "should have {1} once.").format(s2.name, s1.name))

        self.assertEqual(s3.friends, [],
            "If seals A and B become friends, it should not affect seal C's "
            "list of friends.")

    def test_06_tell_friends(self):
        """tell_friends() should work correctly."""
        s1 = Seal("Aristoteles")
        s2 = Seal("Alina")
        s3 = Seal("Walter")

        s1.add_friend(s2)
        self.assertEqual(s1.tell_friends(), s2.name,
            ("After {0} and {1} have become friends, {0}'s tell_friends() "
            "should return '{1}'.").format(s1.name, s2.name))

        s2.add_friend(s3)
        s3.add_friend(s1)

        list1 = s2.name + ", " + s3.name
        list2 = s1.name + ", " + s3.name
        list3 = s2.name + ", " + s1.name
        explanation = (
            ("When {0} and {1} are already friends, then {1} and {2} "
            "become friends, and finally {2} and {0}, then the friend "
            "descriptions should be:\n"
            "{0}: {3}\n"
            "{1}: {4}\n"
            "{2}: {5}").format(s1.name, s2.name, s3.name, list1, list2, list3)
            )

        self.assertEqual(s1.tell_friends(), list1, explanation)
        self.assertEqual(s2.tell_friends(), list2, explanation)
        self.assertEqual(s3.tell_friends(), list3, explanation)

    def test_07_request_banana_pose(self):
        """The result of requesting a banana pose should depend on friends."""
        s1 = Seal("Aristoteles")
        s2 = Seal("Alina")
        s3 = Seal("Walter")
        s4 = Seal("Ella")

        s2.add_friend(s1)
        s1.add_friend(s3)
        s3.add_friend(s4)

        friend_situation = "- {}: {}\n- {}: {}\n- {}: {}\n- {}: {}\n".format(
            s1.name, s1.tell_friends(),
            s2.name, s2.tell_friends(),
            s3.name, s3.tell_friends(),
            s4.name, s4.tell_friends())

        s2.climb_on_rock()
        s3.climb_on_rock()
        self.assertListEqual(s1.request_banana_pose(),
            [s2.name + ": -__;3", s3.name + ": -__;3"],
            ("\nWhen the friend situation is:\n" + friend_situation +
            "and {0} requests a banana pose,\n"
            "and {1} and {2} are on the rock,\n"
            "both {1} and {2} should do the banana pose, but not {3}.")
            .format(s1.name, s2.name, s3.name, s4.name)
            )



if __name__ == "__main__":
    #​‌​​​​​‌‌‌​‌​​​import sys;sys.argv = ['', 'Test.test_default_sequence']
    unittest.main()

