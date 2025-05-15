dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30} #This is a dictionary with keys and values.
dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}#This is a dictionary with keys and values.
merged_dict = {**dict1, **dict2} #This will merge both dictionaries into one dictionary.
print(merged_dict) #Will print the merged dictionary.
#Output will be {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50}

