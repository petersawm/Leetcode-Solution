# When process with small files
import re

def show_tail(file_path, count):
  try:
    with open(file_path, 'r', encoding='utf-8') as file:
      content = file.read() # Read the whole file
    
    words = re.findall(r'\b\w+\b', content) # Get all the words 
    
    return words[-count:] # Return the last 'count' words
  
  except FileNotFoundError:
    print(f"Error: file '{file_path}' not found!")
    return []
  except Exception as e:
    print(f"An error occurred: {e}")
    return []

if __name__ == "__main__":
  file_path = "example.txt"
  count = 5
  result = show_tail(file_path, count)
  print(f"Last {count} words: {result}")