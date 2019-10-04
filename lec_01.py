import openpyxl, pprint

print('Opening workbook...')

wb          = openpyxl.load_workbook("censuspopdata.xlsx")
sheet       = wb['Population by Census Tract']
countryData = {}

print("Reading rows...")

for row in range(2, sheet.max_row + 1):
    state   = sheet['B'+str(row)].value
    country = sheet['C'+str(row)].value
    pop     = sheet['D'+str(row)].value

    #state 해당하는 key 생성
    countryData.setdefault(state,{})
    #[state][country] key 생성
    countryData[state].setdefault(country, {'tracts':0, 'pop':0})

    countryData[state][country]['tracts'] += 1
    countryData[state][country]['pop']    += int(pop)

    #print(state,country,pop,countryData[state][country]['tracts'], countryData[state][country]['pop'])

    #if row == 10 :
    #    break

print("Writing results...")
resultFile = open("census2010.py","w")
resultFile.write('allData = ' + pprint.pformat(countryData))
resultFile.close()
print("Done.")

import census2010, os

