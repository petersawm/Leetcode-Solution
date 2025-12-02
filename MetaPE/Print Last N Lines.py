# Print the last N lines of a file
# Use when the file is small

def print_last_n_lines(file_path, n):
  try:
    with open(file_path, 'r') as file:
      lines = file.readlines()
      last_n_lines = lines[-n:]
      
      for line in last_n_lines:
        print(line, end="")
  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found!")
  except Exception as e:
    print(f"An error occurred: {e}")  

if __name__ == "__main__":
  file_path = "example.txt"
  n = 5
  print_last_n_lines(file_path, n)
  
# Use whent the file is large: Deque
from collections import deque

def print_last_n_lines_2(file_path, n):
  try:
    with open(file_path, 'r') as file:
      last_n_lines = deque(file, maxlen=n)
      
      for linec in last_n_lines:
        print(line, end="")
  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found!")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  file_path = "example.txt"
  n = 5
  print_last_n_lines_2(file_path, n)

# When when the file is super large: seek from the end of the file
# 逆向读取文件（按字节读取）
def print_last_n_lines_3(file_path, n):
  try:
    with open(file_path, 'rb') as file:
      file.seek(0, 2) # Move to the end of the file
      buffer = bytearray()
      lines = []
      
      while len(lines) <= n:
        file.seek(-1024, 1) # each time read 1024 bytes forwords
        buffer = file.read(1024) + buffer
        lines = buffer.splitlines()
        
      for line in lines[-n:]:
        print(line.decode('utf-8'))
  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found!")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  file_path = "example.txt"
  n = 5
  print_last_n_lines_3(file_path, n)