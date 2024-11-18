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
    nameIdx = header.index('Name')
    teamIdx = header.index('Team')
    medalIdx = header.index('Medal')
    sportIdx = header.index('Sport')

    for el in otherRows:
        currMedal = el[medalIdx]
        if currMedal == DEFAULT_NULL:
            continue
        currTeam = el[teamIdx]
        currSport = el[sportIdx]
        currName = el[nameIdx]
        currYear = el[yearIdx]

        if countryName in currTeam and currYear == year:
            outputData.append(f"{currName} {currSport} {currMedal}")

        if currTeam not in dictionary:
            dictionary[countryName] = {}
            dictionary[countryName][BRONZE_MEDAL_NAME] = 0
            dictionary[countryName][GOLD_MEDAL_NAME] = 0
            dictionary[countryName][SILVER_MEDAL_NAME] = 0
            dictionary[countryName][currMedal] = 1
        else:
            if currMedal not in dictionary[countryName]:
                dictionary[countryName][currMedal] = 0
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
            if currMedal not in dictionary[currTeam]:
                dictionary[currTeam][currMedal] = 0
            else:
                dictionary[currTeam][currMedal] += 1

    for k, v in dictionary.items():
        medals = f"{k} - {v[GOLD_MEDAL_NAME]} - {v[SILVER_MEDAL_NAME]} - {v[BRONZE_MEDAL_NAME]}"
        outputData.append(medals)

    return outputData


def start(filePath, countryName, year, outputPath, total):
    isTotalMode = total is not None

    with open(filePath) as file:
        reader = csv.reader(file, delimiter="\t", quotechar='"')
        allData = list(reader)
        header = allData[0]
        headerToString = joinBy("\t", header)
        otherRows = allData[1:]

        if isTotalMode:
            outputData = getTotal(header, otherRows, total)
        else:
            outputData = getMedals(header, otherRows, countryName, year)

    res = ""
    if not isTotalMode:
        res = headerToString + "\n"

    res += joinBy("\n", outputData[:10]) + "\n"

    if not isTotalMode:
        print(dictionary[countryName])
    else:
        res += f"Total: {len(outputData)}"

    if outputPath:
        with open(outputPath, mode="w") as outputFile:
            outputFile.write(res)
    else:
        print(res)


parser = argparse.ArgumentParser(prog='Medals')

parser.add_argument('filename')
parser.add_argument('year', nargs="?")
parser.add_argument('-medals', nargs="?")
parser.add_argument('-output', nargs="?")
parser.add_argument('-total', nargs="?")

args = parser.parse_args()

start(args.filename, args.medals, args.year, args.output, args.total)
