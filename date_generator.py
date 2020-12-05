y = 0
m = 0
d = 0

year = 1900
month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

yearArry = [''] * 201


for i in range(200):

    yearArry.insert(i,str (year))
    year += 1

i = 0

while(i < 200):

    print(str(yearArry[y]) + str(month[m]) + str(day[d])) 

    if (d == 29):
        d += 1
        print(str(yearArry[y]) + str(month[m]) + str(day[d])) 
        d = 0
        if (m == 11):
            m = -1
            y += 1
            i += 1
        m += 1
        if (i != 200):
            print(str(yearArry[y]) + str(month[m]) + str(day[d])) 

    d += 1
