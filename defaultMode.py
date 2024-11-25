from nonSpecific import *
class defaultMode:

    def __init__(self, header, otherRows, countryName, year, dictionary):
        self.header = header
        self.otherRows = otherRows
        self.countryName = countryName
        self.year = year
        self.dictionary = dictionary

    def getMedals(self):
        outputData = []

        yearIdx = self.header.index('Year')
        teamIdx = self.header.index('Team')
        sportIdx = self.header.index('Sport')
        nameIdx = self.header.index('Name')
        medalIdx = self.header.index('Medal')
        country_codeIdx = self.header.index('NOC')

        for el in self.otherRows:
            currMedal = el[medalIdx]
            if currMedal == DEFAULT_NULL:
                continue
            currTeam = el[teamIdx]
            currYear = el[yearIdx]
            currSport = el[sportIdx]
            currName = el[nameIdx]
            curr_country_code = el[country_codeIdx]

            if (self.countryName in currTeam or self.countryName in curr_country_code) and currYear == self.year:
                outputData.append(f"{currName} {currSport} {currMedal}")

                if self.countryName not in self.dictionary:
                    self.dictionary[self.countryName] = {}
                    self.dictionary[self.countryName][BRONZE_MEDAL_NAME] = 0
                    self.dictionary[self.countryName][GOLD_MEDAL_NAME] = 0
                    self.dictionary[self.countryName][SILVER_MEDAL_NAME] = 0
                    self.dictionary[self.countryName][currMedal] = 1
                else:
                    self.dictionary[self.countryName][currMedal] += 1

        return outputData
