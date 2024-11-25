from nonSpecific import *

class interactiveMode:

    def __init__(self, header, otherRows, dictionary):
        self.header = header
        self.otherRows = otherRows
        self.dictionary = dictionary

    def startInteractiveMode(self):
        while True:
            try:
                countryName = input("Enter a country name or country code: ")
                if countryName == "q":
                    break

                yearIdx = self.header.index('Year')
                teamIdx = self.header.index('Team')
                medalIdx = self.header.index('Medal')
                countryCodeIdx = self.header.index('NOC')

                for el in self.otherRows:
                    currMedal = el[medalIdx]
                    if currMedal == DEFAULT_NULL:
                        continue
                    currTeam = el[teamIdx]
                    currYear = el[yearIdx]
                    currCountryCode = el[countryCodeIdx]

                    if currCountryCode not in countryName and currTeam not in countryName:
                        continue

                    if countryName not in self.dictionary:
                        self.dictionary[countryName] = {}
                        self.dictionary[countryName]["events"] = {currYear}
                        self.dictionary[countryName]["year"] = int(currYear)

                        self.dictionary[countryName][currYear] = 1

                        self.dictionary[countryName][BRONZE_MEDAL_NAME] = 0
                        self.dictionary[countryName][GOLD_MEDAL_NAME] = 0
                        self.dictionary[countryName][SILVER_MEDAL_NAME] = 0
                        self.dictionary[countryName][currMedal] = 1
                    else:
                        if currYear not in self.dictionary[countryName]:
                            self.dictionary[countryName][currYear] = 1
                        else:
                            self.dictionary[countryName][currYear] += 1

                        self.dictionary[countryName]["events"].add(currYear)
                        self.dictionary[countryName]["year"] = min(int(currYear), self.dictionary[countryName]["year"])
                        self.dictionary[countryName][currMedal] += 1

                country = self.dictionary[countryName]
                allEventsCountry = len(country["events"])
                avgNumOfMedals = f"Avg: {round(country[GOLD_MEDAL_NAME] / allEventsCountry)} Gold {round(country[SILVER_MEDAL_NAME] / allEventsCountry)} Silver {round(country[BRONZE_MEDAL_NAME] / allEventsCountry)} Bronze"
                mostNumOfMedals = findMinOrMax("max", countryName)
                leastNumOfMedals = findMinOrMax("min", countryName)

                print(avgNumOfMedals)
                print(f"Most num of medals {mostNumOfMedals[1]} in {mostNumOfMedals[0]}")
                print(f"Least num of medals {leastNumOfMedals[1]} in {leastNumOfMedals[0]}")
            except:
                print("Country not exist")
                continue