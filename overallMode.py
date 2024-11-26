from nonSpecific import *

class getOverallMode:

    def __init__(self, dictionary, header, otherRows, countries):
        self.dictionary = dictionary
        self.header = header
        self.otherRows = otherRows
        self.countries = countries
        self.result = ''

    def getOverall(self):

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

            if currTeam in self.countries or currCountry in self.countries:
                key = currYear
                countryKey = currTeam if currTeam in self.countries else currCountry

                if countryKey not in self.dictionary:
                    self.dictionary[countryKey] = {}
                    self.dictionary[countryKey][key] = 1
                else:
                    if key not in self.dictionary[countryKey]:
                        self.dictionary[countryKey][key] = 1
                    else:
                        self.dictionary[countryKey][key] += 1