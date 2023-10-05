import os
import subprocess
import webbrowser

# Path to the "Content" folder
content_folder = r"C:\Users\bheagney\Documents\VotingLines2"

# 1. Open a specific .exe file within the "Content" folder
exe_path = os.path.join(content_folder, "HTML5LaunchHelper.exe")
subprocess.Popen([exe_path])

# 2. Open a specific URL in a web browser
url = "http://localhost:8000/index.html"
webbrowser.open(url)