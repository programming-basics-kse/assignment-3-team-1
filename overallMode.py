from nonSpecific import *

class getOverallMode:

    def __init__(self, dictionary, header, otherRows, countries):
        self.dictionary = dictionary
        self.header = header
        self.otherRows = otherRows
        self.countries = countries

    def getOverall(self):
        outputData = []

        yearIdx = self.header.index('Year')
        teamIdx = self.header.index('Team')
        medalIdx = self.header.index('Medal')
        country_codeIdx = self.header.index('NOC')

        for row in self.otherRows:
            currMedal = row[medalIdx]
            currCountry = row[country_codeIdx]
            currTeam = row[teamIdx]
            currYear = row[yearIdx]
            if currMedal == DEFAULT_NULL:
                continue

            if currTeam in self.countries:
                key = currYear
                if currTeam not in self.dictionary:
                    self.dictionary[currTeam] = {}
                    self.dictionary[currTeam][key] = 1
                else:
                    if key not in self.dictionary[currTeam]:
                        self.dictionary[currTeam][key] = 1
                    else:
                        self.dictionary[currTeam][key] += 1

            elif currCountry in self.countries:
                key = currYear
                if currCountry not in self.dictionary:
                    self.dictionary[currCountry] = {}
                    self.dictionary[currCountry][key] = 1
                else:
                    if key not in self.dictionary[currCountry]:
                        self.dictionary[currCountry][key] = 1
                    else:
                        self.dictionary[currCountry][key] += 1

        return outputData