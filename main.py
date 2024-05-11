# Import for image metadata extraction
from PIL import Image
from PIL.ExifTags import TAGS

# Hashing metadata
import hashlib
import json

# Import for blockchain and steganography
import subprocess
from stegano import lsb
import hmac

# Open the image file
img_filename = str(input("Enter the image filename with extension: "))
img = Image.open(img_filename)

# Extract the EXIF (metadata) from the image
exif_data = img._getexif()

# Transform the EXIF data into a dictionary
keys_wanted = {'ExifOffset', 'ExifImageWidth', 'ExifImageHeight'}
exif = {TAGS[key]: exif_data[key] for key in exif_data.keys() if TAGS[key] in keys_wanted}

# # debug print the exif data
# print(f'exif data{exif_data}')
# print(f'exif{exif}')

# Convert EXIF data to JSON
exif_json = json.dumps(exif)
# #debug print the JSON data
# print(f'exif json{exif_json}')

# Hash the JSON data string
exif_hashed = hashlib.sha256(exif_json.encode()).hexdigest()
#debug print the hashed data
print(f'exif hashed {exif_hashed}')

# Hash the hashed exif with HMAC
key = 'secret'
hmac_hashed = hmac.new(key.encode(), exif_hashed.encode(), hashlib.sha256).hexdigest()
#debug print the hashed data
print(f'hmac hashed {hmac_hashed}')

# Connect to Sepolia ethereum testnet blockchain
# Call for the Javascript to connect to API
command = f'node call.js {hmac_hashed} {exif_hashed}'
process = subprocess.Popen(command, shell=True)
process.communicate()

# Hide the hmac_hashed in the image
secret = lsb.hide(img_filename, f'{hmac_hashed} {exif_hashed}')

# Save the image with the hidden hmac_hashed
secret.save('validatedImage.png')