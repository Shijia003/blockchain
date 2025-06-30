import requests
import json

PINATA_BASE_URL = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
PINATA_GATEWAY = "https://gateway.pinata.cloud/ipfs/"
PINATA_API_KEY = "643065627ab15d753e71"
PINATA_SECRET_API_KEY = "01714bb5dacce226d92ab7d60eb474dc535b4a9210d1e6d8808f116da847de01"

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	headers = {
		"Content-Type": "application/json",
		"pinata_api_key": PINATA_API_KEY,
		"pinata_secret_api_key": PINATA_SECRET_API_KEY,
  }

  response = requests.post(PINATA_BASE_URL, data=json.dumps({"pinataContent": data}), headers=headers)

  if response.status_code != 200:
      raise Exception(f"Failed to pin JSON to IPFS: {response.text}")

  cid = response.json()["IpfsHash"]

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	

	assert isinstance(data,dict), f"get_from_ipfs should return a dict"
	return data
