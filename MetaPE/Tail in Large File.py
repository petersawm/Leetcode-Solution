# When deal with large file
import re
from collections import deque

def show_tail_large_file(file_path, count):
  try:
    with open(file_path, count):
      # use deque to keep the last count words
      tail_words = deque(maxlen=count)
      
      # read the file line by line
      for line in file:
        words = re.findall(r'\b\w+\b', line)
        tail_words.extend(words)
    
    return list(tail_words)
  
  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found!")
    return []
  except Exception as e:
    print(f"An error occurred: {e}")
    return []

if __name__ == "__main__":
  file_path = "largeFile.txt"
  count = 5
  result = show_tail_large_file(file_path, count)
  print(f"Last {count} words: {result}")