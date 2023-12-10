import csv
path = "..\\riot_api\\data.csv"
champion = {}
with open(path) as csvfile:
    data = csv.reader(csvfile, quoting=csv.QUOTE_NONE, delimiter=',')
    for row in data:
        team1 = row[:5]
        team2 = row[5:10]
        win = row[10]
        if win == '0':
            print("team 0 won")
            for char in team1:
                if(char in champion):
                    champion[char] += 1
                else:
                    champion[char] = 1
        else:
            print("team 1 won")
            for char in team2:
                if(char in champion):
                    champion[char] += 1
                else:
                    champion[char] = 1
print(champion)
        #rowlist = row[0].split(',')
        


    #    for a in line:
    #        b = (a.split(','))
    #        for champion in b:
    #            print(champion)


    