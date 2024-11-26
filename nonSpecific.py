DEFAULT_NULL = 'NA'
GOLD_MEDAL_NAME = 'Gold'
BRONZE_MEDAL_NAME = 'Bronze'
SILVER_MEDAL_NAME = 'Silver'

def getAgeCategory(age):
    if 18 <= age <= 25:
        return '1'
    elif 25 < age <= 35:
        return '2'
    elif 35 < age <= 50:
        return '3'
    else:
        return '4'

def joinBy(separator, arr):
    return separator.join(str(x) for x in arr)

def findMinOrMax(type, countryName, dictionary):
    events = dictionary[countryName]["events"]
    value = 0
    key = ""

    if type == "min":
        value = float('inf')

    for k, v in dictionary[countryName].items():
        if k in events:
            if type == "max":
                if v > value:
                    key = k
                    value = v
            else:
                if v < value:
                    key = k
                    value = v

    return (key, value)