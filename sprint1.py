import gedcom_parser
import datetime

# UserStory1 Dates before current date
# Dates (birth, marriage, divorce, death) should not be after the current date
# Author: Gireesh Singh Thakurathi

file_path = 'InputFiles/Project01.ged'
def UserStory1():
    individualFailed_list = []
    familyFailed_list = []
    peopleList, famList = gedcom_parser.parse(file_path)
    curr_datetime = datetime.datetime.today()
    today = datetime.date(curr_datetime.year, curr_datetime.month, curr_datetime.day)

    for person in peopleList:
        if person.birthday == 'NA' and person.birthday > today:
            individualFailed_list.append(person)
        elif person.death != 'NA' and person.death > today:
            individualFailed_list.append(person)

    for fam in famList:
        if fam.married != 'NA' and fam.married > today:
            familyFailed_list.append(fam)
        elif fam.divorced != 'NA' and fam.divorced > today:
            familyFailed_list.append(fam)

    return individualFailed_list, familyFailed_list

# UserStory2 Birth before marriage
# Birth should occur before marriage of an individual
# Author: Gireesh Singh Thakurathi
def UserStory2():
    individualFailed_list = []
    peopleList, famList = gedcom_parser.parse(file_path)

    for fam in famList:
        if fam.husbandId != 'NA':
            husb = gedcom_parser.getPerson(fam.husbandId, peopleList)
            if fam.married != 'NA' and husb.birthday > fam.married:
                husb.marriage = fam.married
                individualFailed_list.append(husb)
        if fam.wifeId != 'NA':
            wife = gedcom_parser.getPerson(fam.wifeId, peopleList)
            if fam.married != 'NA' and wife.birthday > fam.married:
                wife.marriage = fam.married
                individualFailed_list.append(wife)
    return individualFailed_list

# UserStory3 Birth before death
# Birth should occur before death of an individual
# Author: Ishan Sahu
def UserStory3():
    individualFailed_list = []
    peopleList, famList = gedcom_parser.parse(file_path)
    curr_datetime = datetime.datetime.today()
    today = datetime.date(curr_datetime.year, curr_datetime.month, curr_datetime.day)
    for person in peopleList:
        if person.alive and not person.death:
            individualFailed_list.append(person)
        elif not person.alive and person.death == "NA":
            individualFailed_list.append(person)
        elif not person.alive and person.death > today:
            individualFailed_list.append(person)
        elif not person.alive and person.birthday > person.death:
            individualFailed_list.append(person)
        elif not person.birthday:
            individualFailed_list.append(person)
    return individualFailed_list

# UserStory4 Marriage before divorce
# Marriage should occur before divorce of spouses, and divorce can only occur after marriage
# Author: Ishan Sahu
def UserStory4():
    individualFailed_list = []
    peopleList, famList = gedcom_parser.parse(file_path)
    for fam in famList:
        if fam.husbandId != 'NA' and fam.married != 'NA' and fam.divorced != 'NA' and fam.divorced < fam.married:
                individualFailed_list.append(fam)
    return individualFailed_list
