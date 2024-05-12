from django.shortcuts import render
import requests
import base64
from web3 import Web3
from mint import handle_transaction
import os

stable_diffusion_API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
stable_diffusion_API_TOKEN = os.getenv('stable_diffusion_API_TOKEN')
stable_diffusion_headers = {"Authorization": f"Bearer {stable_diffusion_API_TOKEN}"}


ipfs_api_url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
pinata_secret_api_key = os.getenv('pinata_secret_api_key')
pinata_api_key = os.getenv('pinata_api_key')
ipfs_headers = {'pinata_api_key': pinata_api_key, 'pinata_secret_api_key':pinata_secret_api_key}

# Create your views here.

def query(payload):
    response = requests.post(stable_diffusion_API_URL, headers=stable_diffusion_headers, json=payload)
    image_data = response.content
    return image_data

def home(request):
    image_data = None

    if request.method == 'POST':
        if 'description' in request.POST:  # Handling the first POST request for getting description
            description = request.POST.get('description')
            image_in_binary = query(description)

            # Encode the binary data as base64 string
            image_data = base64.b64encode(image_in_binary).decode('utf-8')

        elif 'image_data' in request.POST:  # Handling the second POST request for minting NFT
            image_data = request.POST.get('image_data')
            address = request.POST.get('address')
            # Decode the base64 image data
            image_in_binary = base64.b64decode(image_data)

            # Upload the image data to IPFS
            response = requests.post(ipfs_api_url, headers=ipfs_headers, files={'file': image_in_binary})
            if response.status_code == 200:
                ipfs_hash = response.json().get('IpfsHash')

                # Mint the NFT using the ipfs_hash
                checksum_from_addr = Web3.to_checksum_address(address)
                token_uri = f"https://green-magic-skunk-117.mypinata.cloud/ipfs/{ipfs_hash}"
                handle_transaction("mintNFT", [checksum_from_addr, token_uri])


    return render(request, 'home.html', {'image_data': image_data})