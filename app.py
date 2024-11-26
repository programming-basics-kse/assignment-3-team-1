import argparse
import csv
from interactiveMode import *
from medalsMode import *
from topMode import *
from totalMode import *
from overallMode import *

dictionary = {}
def start(filePath, medalArgs, outputPath, totalByYear, overallByCountries, top, interactiveM):
    result = ""

    with open(filePath) as file:
        reader = csv.reader(file, delimiter='\t', quotechar='"')
        allData = list(reader)
        header = allData[0]
        otherRows = allData[1:]

        if interactiveM:
            interactive = interactiveMode(header, otherRows, dictionary)
            interactive.startInteractiveMode()
            exit()

        elif top is not None:
            top = getTopMode(header, otherRows, top, dictionary)
            outputData = top.getTop()
            result += joinBy("\n", outputData)

        elif totalByYear is not None:
            total = getTotalMode(dictionary, header, otherRows, totalByYear)
            outputData = total.getTotal()
            result += joinBy("\n", outputData) + "\n"
            result += f"Total: {len(outputData)}"

        elif overallByCountries is not None:
            overall = getOverallMode(dictionary, header, otherRows, overallByCountries)
            result = overall.getOverall()

        else:
            countryName = medalArgs[0]
            year = medalArgs[1]
            medals = medalsMode(header, otherRows, countryName, year, dictionary)
            outputData = medals.getMedals()
            result += joinBy("\n", outputData[:10]) + "\n"
            try:
                result += f"Gold - {dictionary[countryName][GOLD_MEDAL_NAME]} Silver - {dictionary[countryName][SILVER_MEDAL_NAME]} Bronze - {dictionary[countryName][BRONZE_MEDAL_NAME]} \n"
            except KeyError:
                result += "No medals \n"

    if outputPath:
        with open(outputPath, mode="w") as outputFile:
            outputFile.write(result)
    else:
        print(result)

parser = argparse.ArgumentParser(prog='Medals')

parser.add_argument('filename')
parser.add_argument('-medals', nargs="+")
parser.add_argument('-output')
parser.add_argument('-total')
parser.add_argument('-top', nargs="+")
parser.add_argument('-overall', nargs="+")
parser.add_argument('-interactive', action="store_true")

args = parser.parse_args()

start(args.filename, args.medals, args.output, args.total, args.overall, args.top, args.interactive)
