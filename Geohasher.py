import hashlib
from datetime import date

today = date.today()

userDegLat = input("Your current degrees latitude? (Number before decimal point): ")
userDegLong = input("Your current degrees longitude? (Number before decimal point): ")
dow = input("Today's Dow opening price: ")

geoString = str(today) + "-" + dow # create the string "yyyy-mm-dd-dowopening"
hashResult = hashlib.md5(geoString.encode())
geoHash = hashResult.hexdigest()
print("\nGeohash: " + geoHash)

# create a fractional hex value from each half of the string
firstHalf = geoHash[0:16]
secondHalf = geoHash[16:32]

# convert both hex values to decimal
latTail = 0;
longTail = 0;
for x in range(0, 16):
    latTail += int(firstHalf[x], 16) * 16 ** -(x + 1)
    longTail += int(secondHalf[x], 16) * 16 ** -(x + 1)

print(str(latTail) + " " + str(longTail))

latitude = str(userDegLat) + str(round(latTail, 6))[1:8]
longitude = str(userDegLong) + str(round(longTail, 6))[1:8]

print("\nLatitide: " + latitude)
print("Longitude: " + longitude)
print("Coordinates: " + latitude + ", " + longitude)
input("\nPress enter to close")
