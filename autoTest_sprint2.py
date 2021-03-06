import gedcom_parser
import sprint2
import unittest
import datetime

# Unit test for UserStory5
# Author: Gireesh Singh Thakurathi
class UserStory5_AutoTest(unittest.TestCase):

    def test1(self):
        individualFailed_list = sprint2.UserStory5()

        for person in individualFailed_list:
            print("UserStory5: ERROR ENCOUNTERED: " + person.id + " Name " + person.name + " Death DAY "+ str(person.death) + " should not be before Marriage Date " + str(person.marriage))

        self.assertTrue(len(individualFailed_list) == 0, "All marriages occur before deaths.")

# Unit test for UserStory6
# Author: Ishan Sahu
class UserStory6_AutoTest(unittest.TestCase):

    def test1(self):
        individualFailed_list = sprint2.UserStory6()
        for person in individualFailed_list:
            print("UserStory6: ERROR ENCOUNTERED: " + person.id + " Name " + person.name + " Divorce Day "+ str(person.divorce) + " is after death Date " + str(person.death))

        self.assertTrue(len(individualFailed_list) == 0, "All dates are correct and do not occur before MARRIAGE DATE!")



# Unit test for UserStory7
# Author: Gireesh Singh Thakurathi
class UserStory7_AutoTest(unittest.TestCase):

    def test1(self):
        deathFailed_list, peopleFailed_list = sprint2.UserStory7()
        t = datetime.datetime.today()
        today = datetime.date(t.year, t.month, t.day)

        for person in deathFailed_list:
            print("UserStory7: ERROR ENCOUNTERED: " + person.id + " Name " + person.name + " death "+ str(person.death) + " should not be greater than 150 years after birth: " + str(person.birthday))

        for person in peopleFailed_list:
            print("UserStory7: ERROR ENCOUNTERED: " + person.id + " Name " + person.name + " birth day "+ str(person.birthday) + " should be less than 150 years from today: "+ today)

        self.assertTrue(len(deathFailed_list) == 0 and len(peopleFailed_list) == 0, "All deaths occur less than 150 years after birth and current date is also less than 150 years after all birth")


if __name__ == '__main__':
    gedcom_parser.getOutput('InputFiles/Project01.ged')
    print("")
    unittest.main()