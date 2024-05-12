# MINT Gen AI NFT

MINT Gen AI NFT is a Django web application that allows users to generate and mint NFTs using AI-generated images. Users can provide a description, which is used to generate an AI-generated image. They can then mint an NFT using the generated image by uploading it to IPFS and executing a transaction on the blockchain.

## Features

- Generate AI-generated images based on user-provided descriptions.
- Upload generated images to IPFS for decentralized storage.
- Mint NFTs using the uploaded images by executing transactions on the blockchain.
- View the status of NFT minting process.
- Responsive design for both desktop and mobile devices.

## Installation

1. Clone the repository:

```
git clone https://github.com/your_username/mint-gen-ai-nft.git
```

2. Navigate to the project directory:

```
cd GenAI_NFT_Minting
```

3. Install dependencies:
```
pip install -r requirements.txt
```
4. Run migrations:
```
python manage.py migrate
```

5. Start the development server:
```
python manage.py runserver
```

6. Access the application in your web browser at `http://localhost:8000`.

## Usage

1. Open the application in your web browser.
2. Enter a description in the provided input field.
3. Click the "Submit" button to generate an AI-generated image based on the description.
4. Review the generated image.
5. If satisfied, enter an Ethereum wallet address in the "Address to Mint NFT On" input field.
6. Click the "Mint NFT" button to upload the image to IPFS and mint the NFT.
7. Once the NFT is successfully minted, you will see a confirmation message.

## Technologies Used

- Solidity: Smart Contracts
- IPFS (InterPlanetary File System)
- Web3 (Ethereum blockchain interaction)
- Python (Django)
- JavaScript (AJAX)
- HTML/CSS

## Smart Contract

The NFT smart contract used in this project has been deployed on the [Ethereum](https://sepolia.etherscan.io/address/0x18c005e964227f873a03ef89f14a7b5678dce697) blockchain. You can find the source code for the smart contract in the [`contracts`](contracts/) directory of this repository.


## Contributors

- [Sitanshu Kushwaha](https://github.com/Sitanshuk)
- [Yash Amin]()

## License

This project is in the public domain. You are free to use, modify, and distribute it without any restrictions.


