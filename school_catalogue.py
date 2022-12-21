"""
Name: Joe Fraser
Date: 12/5/22
Description: School Catalogue
"""

class School:
    # Constructor
    def __init__(self, name, level, numberOfStudents):
        self.name = name
        self.level = level
        self.numberOfStudents = numberOfStudents

    # Getters
    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_numberOfStudents(self):
        return self.numberOfStudents

    # Setters
    def set_numberOfStudents(self, numberOfStudents):
        self.numberOfStudents = numberOfStudents

    # String represent
    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.numberOfStudents} students"


class PrimarySchool(School):
    def __init__(self, name, numberOfStudents, pickupPolicy):
        super().__init__(name, 'primary', numberOfStudents)
        self.pickupPolicy = pickupPolicy

    # Getters
    def get_pickupPolicy(self):
        return self.pickupPolicy

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + "The pickup policy is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)

class HighSchool(School):
    def __init__(self, name, numberOfStudents, sportsTeams):
        super().__init__(name, 'high', numberOfStudents)
        self.sportsTeams = sportsTeams

    # Getters
    def get_sportsTeams(self):
        return self.get_sportsTeams

    def __repr__(self):
        parentRepr = super().__repr__()
        return parentRepr + "List of sports teams {sportsTeams}".format(sportsTeams = self.sportsTeams)
    

class MiddleSchool:
    pass





def main():
    school1 = School('Lincoln High', 'high', 400)
   
    print("Get methods")
    print(school1.get_name())
    print(school1.get_level())
    print(school1.get_numberOfStudents())

    school1.set_numberOfStudents(789)
    print(school1.get_numberOfStudents())

    schoolPrimary = PrimarySchool('Patrick Henry', 154, 'Curb')
    print("Get methods")
    print(schoolPrimary.get_name())
    print(schoolPrimary.get_level())
    print(schoolPrimary.get_numberOfStudents())

    schoolPrimary.set_numberOfStudents(875)
    print(schoolPrimary.get_numberOfStudents())
    print(schoolPrimary.get_pickupPolicy())
    print(schoolPrimary)

    team_list = ['Falcons', 'Phoenix', 'Badgers', 'Ottors']
    schoolHigh = HighSchool("Orge", 513, team_list)
    print()
    print(schoolHigh)



if __name__ == "__main__":
    main()