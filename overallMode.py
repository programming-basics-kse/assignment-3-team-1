from nonSpecific import *

class getOverallMode:

    def __init__(self, dictionary, header, otherRows, countries):
        self.dictionary = dictionary
        self.header = header
        self.otherRows = otherRows
        self.countries = countries
        self.result = ''

    def getOverall(self):
        outputData = []

        yearIdx = self.header.index('Year')
        teamIdx = self.header.index('Team')
        medalIdx = self.header.index('Medal')
        country_codeIdx = self.header.index('NOC')

        for row in self.otherRows:
            currMedal = row[medalIdx]
            currCountry = row[country_codeIdx]
            keyCountry = row[teamIdx]
            currYear = row[yearIdx]
            if currMedal == DEFAULT_NULL:
                continue

            if keyCountry in self.countries or currCountry in self.countries:
                keyYear = currYear
                keyCountry = currCountry if currCountry in self.countries else keyCountry

                if keyCountry not in self.dictionary:
                    self.dictionary[keyCountry] = {}
                    self.dictionary[keyCountry][keyYear] = 1
                else:
                    if keyYear not in self.dictionary[keyCountry]:
                        self.dictionary[keyCountry][keyYear] = 1
                    else:
                        self.dictionary[keyCountry][keyYear] += 1

        for country in self.countries:
            maxMedals = -float('inf')
            year = ""
            try:
                for years, medals in self.dictionary[country].items():
                    if medals > maxMedals:
                        year = years
                        maxMedals = medals
                self.result += country + " " + year + " " + str(maxMedals) + "\n"
            except KeyError:
                self.result += country + " no medals" + "\n"
        return self.result