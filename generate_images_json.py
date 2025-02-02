import os
import json

# Directory containing images
image_directory = "assets/images/mysweetgirl"

# Allowed image formats
allowed_extensions = {".png", ".jpg", ".jpeg", ".webp"}

# Get a list of all image files in the directory with allowed extensions
image_files = [f for f in os.listdir(image_directory) if os.path.splitext(f)[1].lower() in allowed_extensions]

# Path to save the JSON file
json_path = os.path.join(image_directory, "images.json")

# Save the file list as JSON
with open(json_path, "w") as json_file:
    json.dump(image_files, json_file, indent=4)

print(f"Generated {json_path} with {len(image_files)} images.")
