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