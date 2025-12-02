'''
Randomly picking a line from a text file, think about scalability
Point: 1. Strong Randomness, 2. Scalability 3. Memory Efficiency

Reservoir Sampling:
Use when you need to randomly pick a line from the data stream
1. Initialize a variable chosen_line and set it to None
2. Iterate the lines of the file. For each line, generate a ran num 'r' between 0 and i
3. If r is 0, set chosen_line to the current line
4. After iteration, the chosen_line will contain a random line from the file
'''

import random

def random_line_from_file(file_path):
  chosen_line = None
  with open(file_path, 'r') as file:
    for i, line in enumerate(file):
      if random.randint(0, i) == 0:
        chosen_line = line.strip()
  return chosen_line