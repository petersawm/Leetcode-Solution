import os 
import re

def replace_email(file_path, replacement="[REDACTED]"):
  # Open and read the file
  with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
  
  # Use regex to find all email addresses and replace them
  email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._]+\.[a-zA-Z]{2,}'
  updated_content = re.sub(email_pattern, replacement, content)
  
  # Write the updated content back to the file
  with open(file_path, 'w', encoding='utf-8') as file:
    file.write(updated_content)

def process_directory(directory_path, replacement="[REDACTED]"):
  # Iterate over all files in the directory
  for root, _, files in os.walk(directory_path):
    for file_name in files:
      if file_name.endswith('.html'): # Only process HTML files
        file_path = os.path.join(root, file_name)
        print(f"Processing file: {file_path}")
        replace_email(file_path, replacement)

if __name__ == "__main__":
  directory_path = "./html_files"
  replacement_text = "[REDACTED]"
  process_directory(directory_path, replacement_text)
   