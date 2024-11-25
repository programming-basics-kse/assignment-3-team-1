from nonSpecific import *

class getTotalMode:

    def __init__(self, dictionary, header, otherRows, year):
        self.dictionary = dictionary
        self.header = header
        self.otherRows = otherRows
        self.year = year


    def getTotal(self):
        outputData = []
        yearIdx = self.header.index('Year')
        teamIdx = self.header.index('Team')
        medalIdx = self.header.index('Medal')

        for el in self.otherRows:
            currMedal = el[medalIdx]
            if currMedal == DEFAULT_NULL:
                continue
            currTeam = el[teamIdx]
            currYear = el[yearIdx]
            if currYear != self.year:
                continue

            if currTeam not in self.dictionary:
                self.dictionary[currTeam] = {}
                self.dictionary[currTeam][BRONZE_MEDAL_NAME] = 0
                self.dictionary[currTeam][GOLD_MEDAL_NAME] = 0
                self.dictionary[currTeam][SILVER_MEDAL_NAME] = 0
                self.dictionary[currTeam][currMedal] = 1
            else:
                self.dictionary[currTeam][currMedal] += 1

        for k, v in self.dictionary.items():
            medals = f"{k} - {v[GOLD_MEDAL_NAME]} - {v[SILVER_MEDAL_NAME]} - {v[BRONZE_MEDAL_NAME]}"
            outputData.append(medals)

        return outputData