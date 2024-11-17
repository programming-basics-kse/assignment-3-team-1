import argparse
import csv

dictionary = {}

DEFAULT_NULL = 'NA'


def joinBy(separator, arr):
    return separator.join(str(x) for x in arr)


def start(filePath, countryName, year, outputPath):
    outputData = []

    with open(filePath) as file:
        reader = csv.reader(file)
        allData = list(reader)
        header = allData[0]
        headerToString = joinBy(",", header)
        otherRows = allData[1:]

        yearIdx = header.index('Year')
        teamIdx = header.index('Team')
        medalIdx = header.index('Medal')

        for el in otherRows:
            currMedal = el[medalIdx]
            if currMedal == DEFAULT_NULL:
                continue
            currTeam = el[teamIdx]
            currYear = el[yearIdx]

            dataToAppend = el

            if countryName in currTeam and currYear == year:
                outputData.append(joinBy(",", el))

            if currYear in dictionary:
                if currTeam in dictionary[currYear]:
                    dictionary[currYear][currTeam].append(dataToAppend)
                    continue

                dictionary[currYear][currTeam] = [dataToAppend]
            else:
                dictionary[currYear] = {}
                dictionary[currYear][currTeam] = [dataToAppend]

    res = headerToString + "\n"
    res += joinBy("\n", outputData[:10])
    res += f"Total: {len(outputData)}"

    if outputPath:
        with open(outputPath, mode="w") as outputFile:
            outputFile.write(res)
    else:
        print(res)


parser = argparse.ArgumentParser(prog='Medals')

parser.add_argument('filename')
parser.add_argument('year')
parser.add_argument('-medals', nargs="?")
parser.add_argument('-output', nargs="?")

args = parser.parse_args()

start(args.filename, args.medals, args.year, args.output)
