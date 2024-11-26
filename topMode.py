from nonSpecific import *

class getTopMode:
    def __init__(self, header, otherRows, top, dictionary):
        self.header = header
        self.otherRows = otherRows
        self.top = top
        self.dictionary = dictionary
        self.genderAndAgeDictionary = {}

    def getTop(self):
        outputData = []

        for element in self.top:
            if not element.isnumeric():
                self.genderAndAgeDictionary[element] = []
            else:
                for key in self.genderAndAgeDictionary:
                    self.genderAndAgeDictionary[key].append(element)

        genderIdx = self.header.index('Sex')
        nameIdx = self.header.index('Name')
        ageIdx = self.header.index('Age')
        medalIdx = self.header.index('Medal')

        for key in self.genderAndAgeDictionary:
            for element in self.genderAndAgeDictionary[key]:
                compareMedalsDictionary = {}
                max_medals = 0
                max_medals_leader = ""

                for el in self.otherRows:
                    currMedal = el[medalIdx]
                    currGender = el[genderIdx]
                    currAge = el[ageIdx]
                    currName = el[nameIdx]

                    if currAge == DEFAULT_NULL:
                        continue
                    ageCategory = getAgeCategory(int(currAge))
                    if currMedal == DEFAULT_NULL or currGender != key or ageCategory != element:
                        continue

                    if currName not in compareMedalsDictionary:
                        compareMedalsDictionary[currName] = 1
                    else:
                        compareMedalsDictionary[currName] += 1

                for name in compareMedalsDictionary:
                    if compareMedalsDictionary[name] > max_medals:
                        max_medals = compareMedalsDictionary[name]
                        max_medals_leader = name

                if max_medals_leader not in self.dictionary:
                    self.dictionary[max_medals_leader] = [max_medals]
                else:
                    self.dictionary[max_medals_leader].append(max_medals)

        for name in self.dictionary:
            for medal in self.dictionary[name]:
                outputData.append(f"Leader is {name} with {medal} medals")

        return outputData