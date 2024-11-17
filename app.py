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

def start(filePath, countryName, year, outputPath, totalByYear):
    outputData = []
    isTotalMode = totalByYear is not None

    with open(filePath) as file:
        reader = csv.reader(file, delimiter='\t', quotechar='"')
        allData = list(reader)
        header = allData[0]
        headerToString = joinBy("\t", header)
        otherRows = allData[1:]

        if isTotalMode:
            outputData = getTotal(header,otherRows,totalByYear)
        else:
            outputData = getMedals(header, otherRows, countryName, year)

    result = ""
    if not isTotalMode:
        result += joinBy("\n", outputData[:10]) + "\n"
        result += f"Gold - {dictionary[countryName][GOLD_MEDAL_NAME]} Silver - {dictionary[countryName][SILVER_MEDAL_NAME]} Bronze - {dictionary[countryName][BRONZE_MEDAL_NAME]} \n"
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

args = parser.parse_args()

start(args.filename, args.medals, args.year, args.output, args.total)
