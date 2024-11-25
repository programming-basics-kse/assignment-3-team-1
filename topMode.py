from nonSpecific import *


class getTopMode:
    def __init__(self, header, otherRows, top, dictionary):
        self.header = header
        self.otherRows = otherRows
        self.top = top
        self.dictionary = dictionary

    def getTop(self):
        outputData = []

        is_filter_by_gender = 'F' in self.top or 'M' in self.top
        is_filer_by_age = False

        for i in range(1, 5):
            if str(i) in self.top:
                is_filer_by_age = True
                break

        genderIdx = self.header.index('Sex')
        nameIdx = self.header.index('Name')
        ageIdx = self.header.index('Age')
        medalIdx = self.header.index('Medal')

        max_medals = 0
        max_medals_leader = ""

        for el in self.otherRows:
            currMedal = el[medalIdx]
            if currMedal == DEFAULT_NULL:
                continue
            currGender = el[genderIdx]
            currAge = el[ageIdx]
            currName = el[nameIdx]
            if currAge == DEFAULT_NULL:
                continue
            ageCategory = getAgeCategory(int(currAge))

            if is_filter_by_gender and currGender not in self.top:
                continue

            if is_filer_by_age and ageCategory not in self.top:
                continue

            if currName not in self.dictionary:
                self.dictionary[currName] = 1
            else:
                self.dictionary[currName] += 1
                num_of_medals = self.dictionary[currName]

                if num_of_medals > max_medals:
                    max_medals = num_of_medals
                    max_medals_leader = el

        leader_name = max_medals_leader[nameIdx]
        leader_age = max_medals_leader[ageIdx]

        outputData.append(f"Leader is {leader_name} who is {leader_age} y.o. with {max_medals} medals")

        return outputData
