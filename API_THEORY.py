# concept- An application programming interface is a set of commands, functions, protocols, and objects that
#  programmers can use to create software or interact with an external system.

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Concept- HTTP CODES--> raise_for_status()
# 1XX: HOLD ON
# 2XX: HERE YOU GO
# 3XX: GO AWAY
# 4XX: YOU SCREWED UP
# 5XX: I SCREWED UP

for_any_error = response.raise_for_status()
print(for_any_error)

print(response)
print(response.status_code)
print(response.json())
print(response.json()["iss_position"])
print(response.json()["iss_position"]["longitude"])


