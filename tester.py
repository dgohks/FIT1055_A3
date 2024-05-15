# Import for image metadata extraction
from PIL import Image
from PIL.ExifTags import TAGS

# Import for blockchain and steganography
import subprocess
from stegano import lsb

# Open the image file
try:
    img_filename = str(input('Enter the image filename: '))
    secret = lsb.reveal(img_filename)
except:
    raise Exception ('The image is not validated! Highly likely the image is tampered|deepfaked.')

# Extract the hidden hmac_hashed from the image
print(f'Hidden hash: {secret}')
secret = secret.split(' ')
hmac_hashed = secret[0].strip()
exif_hashed = secret[1].strip()

# Connect to Sepolia ethereum testnet blockchain
# Call for the Javascript to connect to API
command = f'node retrieve.js {hmac_hashed}'
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)

# Read the output from the API
output, error = process.communicate()

# Decode the output from the API
output = output.decode('utf-8').strip()
# debug output
print(f'tester output: {output}')
print(f'exif_hashed: {exif_hashed}')

# Compare the output from the blockchain with the original exif_hashed
if output == exif_hashed and output != 0:
    print('The image is validated')
else:
    print('The image is not validated! Highly likely the image is tampered|deepfaked.')