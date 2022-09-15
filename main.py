import csv
count1=0
count=-1
flag =0
search = input("Searching for ")
f = open('result.txt', "w")
with open('books.csv', "r") as csvfile:
    table = csv.reader(csvfile, delimiter = ";")
    for row in list(table):
        count+=1
        if len(row[1])>30:
            count1+=1
        lower_case = row[3].lower()
        index = lower_case.find(search.lower())
        if index != -1 and (int(row[6][:4])==2015 or  int(row[6][:4])==2018):
            f.write(row[1] + '\n')
            flag = 1
        if 0<=count<=19:
            f.write(row[4]+'. '+row[1]+' - '+row[6][:4] + '\n')

    #f.write(row[0] + '. ' + row[1]+ '. Стоимость ' + row[7] + " рублей. \n")

    if flag == 0:
        f.write("Not find" + '\n')
        f.write(str(count)+'\n')
        f.write(str(count1)+'\n')

f.close()

