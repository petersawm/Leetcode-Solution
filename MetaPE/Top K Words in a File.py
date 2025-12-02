import sys
from collections import Counter
# Time: O(N+VlogK), Space: (N+V+K)

def top_k_words(file_path, k):
  try:
    with open(file_path, 'r') as file:
      text = file.read().lower()  # Read the file and convert to lowercase
      words = text.split() # Split the text into words
      count = Counter(words) # Count the frequency of each word
      top_k = count.top_k(k) # Get the top k words
      return top_k
  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found!")
    sys.exit(1)

def main():
  # ignore the words like "a", "the", "in"...,
  # so we can focus on the more important words
  if len(sys.argv) != 3:
    print("Usage: python Top K Words in a File.py <file_path> <k>")
    sys.exit(1)
    
  file_path = sys.argv[1]
  k = int(sys.argv[2])
  top_k = top_k_words(file_path, k)
  print(f"Top {k} words:")
  for word, count in top_k:
    print(f"{word}: {count}")

if __name__ == "__main__":
  main()