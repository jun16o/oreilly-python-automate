#! python3

import openpyxl, pprint
print('ワークブックを開いています...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
county_data = {}

#TODO: county_dataに郡の人口と地域数を格納する
print('行を読み込んでいます...')
for row in range(2, sheet.max_row + 1):
    # スプレッドシートの1行に、ひとつの人口調査標準地域のデータがある
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

#TODO: 新しいテキストファイルを開き、county_dataの内容を書き込む