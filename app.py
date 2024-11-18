import argparse
import csv

dictionary = {}

DEFAULT_NULL = 'NA'
GOLD_MEDAL_NAME = 'Gold'
BRONZE_MEDAL_NAME = 'Bronze'
SILVER_MEDAL_NAME = 'Silver'


def joinBy(separator, arr):
    return separator.join(str(x) for x in arr)

def getMedals(header, otherRows, countryName, year):
    outputData = []

    yearIdx = header.index('Year')
    teamIdx = header.index('Team')
    sportIdx = header.index('Sport')
    nameIdx = header.index('Name')
    medalIdx = header.index('Medal')
    country_codeIdx = header.index('NOC')

    for el in otherRows:
        currMedal = el[medalIdx]
        if currMedal == DEFAULT_NULL:
            continue
        currTeam = el[teamIdx]
        currYear = el[yearIdx]
        currSport = el[sportIdx]
        currName = el[nameIdx]
        curr_country_code = el[country_codeIdx]

        if (countryName in currTeam or countryName in curr_country_code) and currYear == year:
            outputData.append(f"{currName} {currSport} {currMedal}")

            if countryName not in dictionary:
                dictionary[countryName] = {}
                dictionary[countryName][BRONZE_MEDAL_NAME] = 0
                dictionary[countryName][GOLD_MEDAL_NAME] = 0
                dictionary[countryName][SILVER_MEDAL_NAME] = 0
                dictionary[countryName][currMedal] = 1
            else:
                dictionary[countryName][currMedal] += 1

    return outputData

def getOverall(header, otherRows, countries, year):
    outputData = []

    yearIdx = header.index('Year')
    teamIdx = header.index('Team')
    medalIdx = header.index('Medal')

    for row in otherRows:
        currMedal = row[medalIdx]
        if currMedal == DEFAULT_NULL:
            continue

        currTeam = row[teamIdx]
        currYear = row[yearIdx]


        if currTeam in countries:
            key = currYear
            if currTeam not in dictionary:
                dictionary[currTeam] = {}
                dictionary[currTeam][key] = 1
            else:
                if key not in dictionary[currTeam]:
                    dictionary[currTeam][key] = 1
                    continue
                dictionary[currTeam][key] += 1

    return outputData

def getTotal(header, otherRows, year):
    outputData = []

    yearIdx = header.index('Year')
    teamIdx = header.index('Team')
    medalIdx = header.index('Medal')

    for el in otherRows:
        currMedal = el[medalIdx]
        if currMedal == DEFAULT_NULL:
            continue
        currTeam = el[teamIdx]
        currYear = el[yearIdx]
        if currYear != year:
            continue

        if currTeam not in dictionary:
            dictionary[currTeam] = {}
            dictionary[currTeam][BRONZE_MEDAL_NAME] = 0
            dictionary[currTeam][GOLD_MEDAL_NAME] = 0
            dictionary[currTeam][SILVER_MEDAL_NAME] = 0
            dictionary[currTeam][currMedal] = 1
        else:
            dictionary[currTeam][currMedal] += 1

    for k,v in dictionary.items():
        medals = f"{k} - {v[GOLD_MEDAL_NAME]} - {v[SILVER_MEDAL_NAME]} - {v[BRONZE_MEDAL_NAME]}"
        outputData.append(medals)

    return outputData

def start(filePath, countryName, year, outputPath, totalByYear, overallByCountries):
    mode = ""

    if totalByYear is not None:
        mode = "total"
    elif overallByCountries is not None:
        mode = "overall"
    else:
        mode = "medals"

    with open(filePath) as file:
        reader = csv.reader(file, delimiter='\t', quotechar='"')
        allData = list(reader)
        header = allData[0]
        otherRows = allData[1:]

        if mode == "total":
            outputData = getTotal(header,otherRows,totalByYear)
        elif mode == "medals":
            outputData = getMedals(header, otherRows, countryName, year)
        else:
            outputData = getOverall(header, otherRows, overallByCountries, year)

    result = ""
    if mode == "medals":
        result += joinBy("\n", outputData[:10]) + "\n"
        result += f"Gold - {dictionary[countryName][GOLD_MEDAL_NAME]} Silver - {dictionary[countryName][SILVER_MEDAL_NAME]} Bronze - {dictionary[countryName][BRONZE_MEDAL_NAME]} \n"
    elif mode == "overall":
        for country in overallByCountries:
            max_v = -float('inf')
            max_k = ""
            for k,v in dictionary[country].items():
                if v > max_v:
                    max_k = k
                    max_v = v
            result += country + " " + max_k + " " + str(max_v) + "\n"
    else:
        result += joinBy("\n", outputData) + "\n"
        result += f"Total: {len(outputData)}"

    if outputPath:
        with open(outputPath, mode="w") as outputFile:
            outputFile.write(result)
    else:
        print(result)


parser = argparse.ArgumentParser(prog='Medals')

parser.add_argument('filename')
parser.add_argument('year', nargs="?")
parser.add_argument('-medals', nargs="?")
parser.add_argument('-output', nargs="?")
parser.add_argument('-total', nargs="?")
parser.add_argument('-overall', nargs="+")

args = parser.parse_args()

start(args.filename, args.medals, args.year, args.output, args.total, args.overall)