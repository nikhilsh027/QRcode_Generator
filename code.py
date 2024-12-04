import os
import pyqrcode
import re

# Link which represents the QR Code.
link = input("\nEnter your link: ")

# Sanitize the domain name to use as the file name
# Replace invalid characters with underscores
domain_name = re.sub(r'[<>:"/\\|?*]', '_', link)  # Replace invalid characters

# Generating QR Code.
url = pyqrcode.create(link)

# Create filenames for SVG and PNG
file_name_svg = f"{domain_name}.svg"
file_name_png = f"{domain_name}.png"

# Specify the desired file path (update this path to your desired directory)
save_directory = r"D:\work\QR_code_generator\QR codes"  # Use raw string to handle backslashes

# Ensure the directory exists; create it if it doesn't
if not os.path.exists(save_directory):
    os.makedirs(save_directory)
    print(f"Directory created: {save_directory}")

# Creating and saving the file as SVG with the new name.
url.svg(os.path.join(save_directory, file_name_svg), scale=10)

# Creating and saving the file as PNG with the new name.
url.png(os.path.join(save_directory, file_name_png), scale=12)

print(f"QR Code saved as {file_name_svg} and {file_name_png} in {save_directory}")
