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

def gross(keyword, df):
    gross = 0
    for i in df.index:
        if any(keyword in g for g in df['genresList'][i]):
            gross += (df['domestic_gross'][i])
    return(gross)

def count(keyword, df):
    count = 0
    for i in df.index:
        if any(keyword in g for g in df['genresList'][i]):
            count += 1
    return(count)

def meanGross(keyword, df):
    genreGross = gross(keyword, df)
    genreCount = count(keyword, df)
    mean = genreGross/genreCount
    return mean

def budget(keyword, df):
    budget = 0
    for i in df.index:
        if any(keyword in g for g in df['genresList'][i]):
            budget += (df['production_budget'][i])
    return(budget)

def meanBudget(keyword, df):
    genreBudget = budget(keyword, df)
    genreCount = count(keyword, df)
    mean = genreBudget/genreCount
    return mean

def returnRate(keyword):
    gross = meanGross(keyword)
    budget = meanBudget(keyword)
    increase = gross - budget
    returnRate = (increase/budget) * 100
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







