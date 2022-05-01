# import requests

# response = requests.get("http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)

# print(iss_position)
        
def points(games):
    count = 0
    for i in games:
        new = i.split(":")
        if new[0] > new[1]:
            count += 3
        elif new[0] == new[1]:
            count += 1
    return count

print(points(["1:3", "2:2", "1:4"]))