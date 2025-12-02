import sys

def find_duplicate_words(files):
  set = [] # use to store the words in each file
  
  for file_path in files:
    try:
      with open(file_path, 'r') as file:
        text = file.read().lower()  # Read the file and convert to lowercase
        words = set(text.split()) # Split the text into words and put in set
        set.append(words)
    except FileNotFoundError:
      print(f"Error: File '{file_path}' not found!")
      sys.exit(1)
  
  # Fint the duplicate words across the files
  duplicates = set.intersection(*set)
  return duplicates

def main():
  # at least 2 files are needed to compare
  if len(sys.argv) < 3:
    print(f"Usage: python Find Duplicate Words in Files.py <file1> <file2> ...")
    sys.exit(1)
  
  # Get the file path from the command line arguments
  files = sys.argv[1:]
  duplicates = find_duplicate_words(files)
  print("Duplicate words across the files:")
  for word in sorted(duplicates):
    print(word)

if __name__ == "__main__":
  main()
  