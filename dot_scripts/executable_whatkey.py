#! /usr/bin/python3

#DOC#@CLI@$in_progress$ "detect most probable scale"

import operator

gammes = {"C" : ["C","D","E","F","G","A","B"], "G" : ["G", "A", "B", "C", "D", "E", "F#"], "D" : ["D", "E", "F#", "G", "A", "B", "C#"], "A" : ["A", "B", "C#", "D", "E", "F#", "G#"], "E" : ["E", "F#", "G#", "A", "B", "C#", "D#"], "B" : ["B", "C#", "D#", "E", "F#", "G#", "A#"], "F#" : ["F#", "G#", "A#", "B", "C#", "D#", "E#"], "Db" : ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"], "Ab" : ["Ab", "Bb", "C", "Db", "Eb", "F", "G"], "Eb" : ["Eb", "F", "G", "Ab", "Bb", "C", "D"], "Bb" : ["Bb", "C", "D", "Eb", "F", "G", "A"], "F" : ["F", "G", "A", "Bb", "C", "D", "E"]}

cor = [["Cb", "B"], ["C#", "Db"], ["D#", "Eb"], ["E#", "F"], ["Fb", "E"], ["F#", "Gb"], ["G#", "Ab"], ["A#", "Bb"], ["B#", "C"], ["A"],["D"], ["G"]]

notes = [a[0].upper() + a[1:] for a in input("enter notes\n").split(" ")]

full = []
for i in cor:
    for j in notes:
        if j in i:
            if i not in full:
                full.append(i)
number = len(full)

scores = {k:0 for k in gammes.keys()}
for n in scores.keys():
    for l in full:
        for i in l:
            if i in gammes[n]:
                scores[n] += 1

results = {k:round(100*v/7,1) for k,v in scores.items()}
sorted_results = dict(sorted(results.items(), key=operator.itemgetter(1),reverse=True))

for i in sorted_results.keys():
    if len(gammes[i])==7:
        print("{:^5}{:<6}{:<3}{:<3}{:<3}{:<3}{:<3}{:<3}{:<3}".format(i,str(sorted_results[i]),gammes[i][0],gammes[i][1],gammes[i][2],gammes[i][3],gammes[i][4],gammes[i][5],gammes[i][6]))
    else:
        print("{:^5}{:<6}{:<30}".format(i,str(sorted_results[i])," ".join(gammes[i])))
