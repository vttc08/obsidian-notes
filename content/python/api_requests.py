import requests

# Define variables
video_id = ""
start_time = ""
end_time = "" 
category = "" # sponsor, selfpromo
user_id = "N5BrKnIpxltUjsBfcOXoqeCrP3sUXNuapCZf"

# Prepare the data for the request
data = {"userID": user_id, "videoID": video_id, "segments": [{"segment": [start_time,end_time],"category": category}]}

# Send the request
response = requests.post(f"https://api.sponsor.ajay.app/api/skipSegments/?videoID={video_id}", json=data) # (api url, json data)

# Check the response

print(response.status_code, response.text) # a good request should be 200