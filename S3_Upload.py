import boto3
i = 0
car = ['audi','acura','bmw','bugatti','cadillac','dodge','ferrari','ford','gmc','honda','hyundai','infiniti','jeep','kia','lexus','lincoln','mazda','mercedes','mitsubishi','nissan','pontiac','porsche','ram','subaru','tesla','toyota','volkswagen']

def upload():
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('de-car-times')
    s3.Object('de-car-times', f"0:60-times/{''.join(car[i])}.csv").put(Body=open(f"/Users/kordellewalker/Documents/GitHub/DEProjects/Webscrape-DWH/Resultss/{''.join(car[i])}.csv", 'rb'))

# Uploads all "car.csv" files
while i < 26:
    i += 1
    upload()

#Uploads only "Master_table.csv" file
s3 = boto3.resource('s3')
bucket = s3.Bucket('de-car-times')
s3.Object('de-car-times', "master_table.csv").put(Body=open(f"/Users/kordellewalker/Documents/GitHub/DEProjects/Webscrape-DWH/Resultss/master_table.csv", 'rb'))