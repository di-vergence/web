import csv

c = csv.writer(open("MYFISTCSV.csv","wb"))

c.writerow(["Name", "Adress", "Telephone", "Fax", "E-mail", "Others"])