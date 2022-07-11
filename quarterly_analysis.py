import csv

tickers = []
scores = []
industries = []
winners = []
champions = []

f = open("unique_industries.txt","r")
for x in f:
    industries.append(x.strip())
f.close()

for x in industries:
    if(x == 'Blank Check / SPAC'): path = './industry/SPAC.csv'
    elif(x == 'n/a'): path = './industry/NA.csv'
    else: path = './industry/' + x + '.csv'
    with open(path, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            tickers.append(row)
        EVEBITDA = sorted(tickers,key=lambda i: i['EV/EBITDA'])
        DE = sorted(tickers,key=lambda i: i['D/E'])
        FCFY = sorted(tickers,key=lambda i: i['FCFY'],reverse=True)
        ROICWACC = sorted(tickers,key=lambda i: i['ROIC-WACC'],reverse=True)
        PE = sorted(tickers,key=lambda i: i['P/E'])
        PB = sorted(tickers,key=lambda i: i['P/B'])
        PEG = sorted(tickers,key=lambda i: i['PEG'])
        Beta = sorted(tickers,key=lambda i: i['Beta'])
        
        for y in tickers:
            EVEBITDA_index = next((index for (index, d) in enumerate(EVEBITDA) if d["Tick"] == y['Tick']), None)
            DE_index = next((index for (index, d) in enumerate(DE) if d["Tick"] == y['Tick']), None)
            FCFY_index = next((index for (index, d) in enumerate(FCFY) if d["Tick"] == y['Tick']), None)
            ROICWACC_index = next((index for (index, d) in enumerate(ROICWACC) if d["Tick"] == y['Tick']), None)
            PE_index = next((index for (index, d) in enumerate(PE) if d["Tick"] == y['Tick']), None)
            PB_index = next((index for (index, d) in enumerate(PB) if d["Tick"] == y['Tick']), None)
            PEG_index = next((index for (index, d) in enumerate(PEG) if d["Tick"] == y['Tick']), None)
            Beta_index = next((index for (index, d) in enumerate(Beta) if d["Tick"] == y['Tick']), None)
            newscore = 999
            if(len(tickers) > 1): newscore = EVEBITDA_index/(len(tickers)-1) + DE_index/(len(tickers)-1) + FCFY_index/(len(tickers)-1) + ROICWACC_index/(len(tickers)-1) + PE_index/(len(tickers)-1) + PB_index/(len(tickers)-1) + PEG_index/(len(tickers)-1) + Beta_index/(len(tickers)-1)
            scores.append({'Tick': y['Tick'],'Score': newscore})
        
        scores = sorted(scores,key=lambda i: i['Score'])

        if(len(scores) != 0):
            temp = scores[0]
            temp2 = temp['Tick']
            winner_index = next((index for (index, d) in enumerate(tickers) if d["Tick"] == temp2), None)
            winner = tickers[winner_index]
            print(winner)
            winners.append(winner)
        tickers.clear()
        scores.clear()
    f.close()

FCFY = sorted(winners,key=lambda i: i['FCFY'],reverse=True)
ROICWACC = sorted(winners,key=lambda i: i['ROIC-WACC'],reverse=True)
PB = sorted(winners,key=lambda i: i['P/B'])
PEG = sorted(winners,key=lambda i: i['PEG'])
Beta = sorted(winners,key=lambda i: i['Beta'])

for x in winners:
    FCFY_index = next((index for (index, d) in enumerate(FCFY) if d["Tick"] == x['Tick']), None)
    ROICWACC_index = next((index for (index, d) in enumerate(ROICWACC) if d["Tick"] == x['Tick']), None)
    PB_index = next((index for (index, d) in enumerate(PB) if d["Tick"] == x['Tick']), None)
    PEG_index = next((index for (index, d) in enumerate(PEG) if d["Tick"] == x['Tick']), None)
    Beta_index = next((index for (index, d) in enumerate(Beta) if d["Tick"] == x['Tick']), None)
    newscore = 999
    if(len(winners) > 1): newscore = FCFY_index/(len(winners)-1) + ROICWACC_index/(len(winners)-1) + PB_index/(len(winners)-1) + PEG_index/(len(winners)-1) + Beta_index/(len(winners)-1)
    scores.append({'Tick': x['Tick'],'Score': newscore})

scores = sorted(scores,key=lambda i: i['Score'])

for x in range(8):
    temp = scores[x]
    temp2 = temp['Tick']
    winner_index = next((index for (index, d) in enumerate(winners) if d["Tick"] == temp2), None)
    winner = winners[winner_index]
    champions.append(winner)

f = open("champions.txt","w")
for x in champions:
    f.write(x['Tick'])
    print(x['Name'])
    f.write('\n')
f.close()