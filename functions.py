import locale
def int_to_dollar(x):
    return locale.currency(x, grouping=True)
    
def dollar_to_int(dollar):
    #x = dollar.replace('$', "").replace(',', "")
    return float(dollar.replace('$', "").replace(',', ""))

def add_columns(x, y):
    if (x > 0) & (y > 0):
        return x + y
    else:
        return 0
    
# Genre Functions

def gross(keyword, dfName):
    gross = 0
    for i in dfName.index:
        if any(keyword in g for g in dfName['genresList'][i]):
            gross += (dfName['domestic_gross'][i])
    return(gross)

def count(keyword, dfName):
    count = 0
    for i in dfName.index:
        if any(keyword in g for g in dfName['genresList'][i]):
            count += 1
    return(count)

def meanGross(keyword, dfName):
    genreGross = gross(keyword, dfName)
    genreCount = count(keyword, dfName)
    mean = genreGross/genreCount
    return mean

def budget(keyword, dfName):
    budget = 0
    for i in dfName.index:
        if any(keyword in g for g in dfName['genresList'][i]):
            budget += (dfName['production_budget'][i])
    return(budget)

def meanBudget(keyword, dfName):
    genreBudget = budget(keyword, dfName)
    genreCount = count(keyword, dfName)
    mean = genreBudget/genreCount
    return mean

def meanReturnRate(keyword, dfName):
    gross = meanGross(keyword, dfName)
    budget = meanBudget(keyword, dfName)
    returnRate = (gross/budget) * 100
    return returnRate

# Column Functions

def splitNewCol(dfName, columnName):
    newColumn = []
    for val in dfName[columnName]:
        newColumn.append(val.split(","))
    return(newColumn)

def countNewCol(dfName, columnName):
    newCount = []
    for val in dfName[columnName]:
        newCount.append(len(val))
    return(newCount)

def removeFirstLastChar(dfName, columnName, char1, char2):
    newCol = []
    for val in dfName[columnName]:
        newCol.append(val.replace(char1, '').replace(char2, ''))
    return(newCol)







