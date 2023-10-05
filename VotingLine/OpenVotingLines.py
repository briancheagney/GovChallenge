import os
import subprocess

# Get the current directory
current_directory = os.path.dirname(__file__)

# Path to the "Content" folder
content_folder_path = os.path.join(current_directory, 'Content')

# Path to the specific .exe file inside the "Content" folder
exe_file_path = os.path.join(content_folder_path, 'HTML5LaunchHelper.exe')

# Path to the HTML file you want to open (in the same folder as the script)
html_file_path = os.path.join(current_directory, 'index.html')

try:
    # Open the specific .exe file
    subprocess.Popen([exe_file_path])

    # Open the HTML file using the default web browser
    os.system(f'start {html_file_path}')

except Exception as e:
    print(f"An error occurred: {e}")