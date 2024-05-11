# FIT1055_A3
Monash FIT1055 A3 - Prototyping Blockchain and Hidden Watermarking

- Steps to run the code:
1. Run main.py - enter the image name
2. Edit the imageValidated.png file to test the hidden watermarking
3. Run tester.py to test the integrity of the hidden watermark and blockchain record.

- Requirements:
A .env file with the following variables:
```
ETHEREUM_NETWORK = "sepolia"
INFURA_API_KEY = "YOUR_INFURA_API_KEY"
SIGNER_PRIVATE_KEY = "YOUR_WALLET_PRIVATE_KEY"
DEMO_CONTRACT = "YOUR_CONTRACT_ADDRESS"
```