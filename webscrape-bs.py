from operator import ilshift
from sqlite3 import Date
from bs4 import BeautifulSoup
import requests, time, re, csv, S3_Upload
from sqlalchemy import null


def Intro():
    print(" ")
    print(">>>>>>>>>>>>> 0-60 Time import by Kordelle Walker <<<<<<<<<<<<")
    print("This Script webscrapes 0-60 times for every make and model car and")
    print("sends the output to local directory in multiple .csv format files")
    while True:
       answer = input('Do you want to create/update all csv files?: (y/n)')
       if answer.lower().startswith("y"):
          print("Creating/Updating csv files now...")
          break
       elif answer.lower().startswith("n"):
          print("Creation/Update Cancelled")
          exit()

Intro()

i = -1
#        0       1      2       3         4         5        6        7     8      9       10         11       12    13     14       15       16       17          18          19       20        21     22      23      24       25         26          
car = ['audi','acura','bmw','bugatti','cadillac','dodge','ferrari','ford','gmc','honda','hyundai','infiniti','jeep','kia','lexus','lincoln','mazda','mercedes','mitsubishi','nissan','pontiac','porsche','ram','subaru','tesla','toyota','volkswagen']
url = f"https://www.zeroto60times.com/vehicle-make/{''.join(car[i])}-0-60-mph-times/"   
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
list = doc.find_all('div',"stats__list__accordion__body__stat" )

def time_func():
       for j in list:
            jam = j.find_all('span', "stats__list__accordion__body__stat__top__right__stat-time")
            fire = j.find_all('div', "stats__list__accordion__body__stat__top__title")
            if not jam:
                continue
            mash = [jam[0].text.replace("[","")]
            separator = ", "
            hot = separator.join(mash)
            potato = [fire[0].text.strip()]
            chocolate = separator.join(potato)
            vanilla = separator.join(chocolate.split(" ", maxsplit=1))
            #cheese = [jam[1].text]
            dataset = [hot,vanilla[0:4],car[i].upper(),vanilla[6:].upper()]
            writer.writerow(dataset)

directory = f"/Users/kordellewalker/Documents/GitHub/DEProjects/Webscrape-DWH/Results_test/{''.join(car[i])}.csv"
master_directory = f"/Users/kordellewalker/Documents/GitHub/DEProjects/Webscrape-DWH/Results/master.csv"
# Overwriting initial CSV Document
print("Writing individual [model.csv] files...")
while i < 26:
    i += 1
    print(f"Writing {''.join(car[i])}.csv...",i,"/26")
    with open(f"Resultss/{''.join(car[i])}.csv", "w", newline= '') as csvfile:
        writer = csv.writer(csvfile)
        header = ['0_60_time','year','manufacturer','model']
        writer.writerow(header)
        car = ['audi','acura','bmw','bugatti','cadillac','dodge','ferrari','ford','gmc','honda','hyundai','infiniti','jeep','kia','lexus','lincoln','mazda','mercedes','mitsubishi','nissan','pontiac','porsche','ram','subaru','tesla','toyota','volkswagen']
        url = f"https://www.zeroto60times.com/vehicle-make/{''.join(car[i])}-0-60-mph-times/"
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        list = doc.find_all('div',"stats__list__accordion__body__stat" )
        time_func()
print("Individual [model.csv] files created")
time.sleep(2)

# Writining and Appending a new master file
print("Now Writing and Appending [master_table.csv] file...")
time.sleep(2)
with open("Resultss/master_table.csv", "w", newline ='') as csvfile:
    writer = csv.writer(csvfile)
    header = ['0_60_time','year','manufacturer','model']
    writer.writerow(header)

i = -1
while i < 26:
    i += 1
    print("Writing to master_table.csv...",i,"/26",f"(Appending {''.join(car[i])}.csv)")
    with open("Resultss/master_table.csv", "a", newline= '') as csvfile:
        writer = csv.writer(csvfile)
        car = ['audi','acura','bmw','bugatti','cadillac','dodge','ferrari','ford','gmc','honda','hyundai','infiniti','jeep','kia','lexus','lincoln','mazda','mercedes','mitsubishi','nissan','pontiac','porsche','ram','subaru','tesla','toyota','volkswagen']
        url = f"https://www.zeroto60times.com/vehicle-make/{''.join(car[i])}-0-60-mph-times/"
        result = requests.get(url)
        doc = BeautifulSoup(result.text, "html.parser")
        list = doc.find_all('div',"stats__list__accordion__body__stat" )
        time_func()   

print("--------Creation/Update Complete-------")

while True:
    answer = input('Do you want to update Amazon AWS S3 Bucket?: (y/n)')
    if answer.lower().startswith("y"):
        print("Uploading csv files now...")
        S3_Upload
        break
    elif answer.lower().startswith("n"):
        print("AWS S3 Update Cancelled")
        print("Goodbye")
        exit()

print("--------AWS S3 Upload Complete-------")
print("Goodbye")




