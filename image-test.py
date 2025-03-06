import requests
import json
import os
from pprint import pprint
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("API-KEY")	# Your API_KEY here
PROJECT = "all"; # try specific floras: "weurope", "canada"…
api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"

image_path_1 = "barrel.jpg"
image_data_1 = open(image_path_1, 'rb')

data = { 'organs': ['auto'] }

files = [
  ('images', (image_path_1, image_data_1))
]

req = requests.Request('POST', url=api_endpoint, files=files, data=data)
prepared = req.prepare()

s = requests.Session()
response = s.send(prepared)
json_result = json.loads(response.text)

likely_plant_object = json_result["results"][0] #gets first item from the 'results' list

common_names_list = likely_plant_object["species"].get("commonNames", []) #retreives list of common names from the most likely plant

common_name = common_names_list[0] #gets english common name :))

pprint("plantnet response code: " + str(response.status_code))
pprint(common_name + " detected")
pprint("sending to gemini...")


#google gemini response bullshit
gem_prompt = "For a plant " + common_name +", please tell me the ideal moisture level as measured by a capacitive soil moisture sensor as well as the ideal number of hours per day to have it's grow light on. Respond only in the format of {moisturevalue_percent, hours}. These should not be ranges, but a single int values with no other characters"

client = genai.Client(api_key=os.getenv('GEMINI-API-KEY'))
response = client.models.generate_content(
    model="gemini-2.0-flash", contents=gem_prompt
)
print("Gemini response {ideal_moisture_as_percent, hours_of_light/day}: " + response.text)