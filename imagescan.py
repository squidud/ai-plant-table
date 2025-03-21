import requests
import json
import os
from pprint import pprint
from dotenv import load_dotenv
from google import genai
from logger import log_action

IMAGE_PATH = "static/image.jpg"

def scanny():
  load_dotenv()

  API_KEY = os.getenv("API-KEY")	# Your API_KEY here
  PROJECT = "all"; # try specific floras: "weurope", "canada"…
  api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"

  image_path_1 = IMAGE_PATH
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
  log_action(common_name+" detected succesfully. Sending to gemini...")


  #google gemini response bullshit
  gem_prompt = "For a plant " + common_name +", please tell me the ideal moisture level as measured by a capacitive soil moisture sensor as well as the ideal number of hours per day to have it's grow light on. Respond only in the format of 'moisturevalue_percent()hours'. These should not be ranges, but a single int values with no other characters. For example, a correctly-formatted response would be: 70()12"

  client = genai.Client(api_key=os.getenv('GEMINI-API-KEY'))
  response = client.models.generate_content(
      model="gemini-2.0-flash", contents=gem_prompt
  )
  print("Gemini response {ideal_moisture_as_percent, hours_of_light/day}: " + response.text)
  log_action("Gemini response: " + response.text)

  #writes information to json file
  newjsondata = {
      "commonname": common_name,
      "sunlight": int(response.text.split("()")[1]),
      "moisture": int(response.text.split("()")[0])
  }

  filename = "static/data.json"

  with open(filename, 'w') as file:
      json.dump(newjsondata, file, indent=4)

  print(f"Data written to {filename}")

  #returns plant name for gui business
  return common_name



