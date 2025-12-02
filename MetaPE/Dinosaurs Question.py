import csv
import math

'''
dinosaurs question:

You will be supplied with two data files in CSV format. The first file contains
statistics about various dinosaurs. The second file contains additional data.

Given the following formula:
speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)

Write a program to read in the data files from disk, it must then print the names
of only the bipedal dinosaurs from fastest to slowest. Do not print any other information.

$ cat dataset1.csv
NAME,LEG_LENGTH,DIET
Hadrosaurus,1.2,herbivore

Struthiomimus,0.92,omnivore
Velociraptor,1.0,carnivore
Triceratops,0.87,herbivore
Euoplocephalus,1.6,herbivore
Stegosaurus,1.40,herbivore
Tyrannosaurus Rex,2.5,carnivore

$ cat dataset2.csv
NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.87,quadrupedal
Stegosaurus,1.90,quadrupedal
Tyrannosaurus Rex,5.76,bipedal
Hadrosaurus,1.4,bipedal
Deinonychus,1.21,bipedal
Struthiomimus,1.34,bipedal
Velociraptor,2.72,bipedal
'''

def read_csv(file_path):
  data = {}
  with open(file_path, 'r') as file:
    reader = csv.DictReader(file) # Read the CSV file as a dictionary
    for row in reader:
      data[row['NAME']] = row
  return data

def calculate_speed(leg_length, stride_length):
  g = 9.8
  return ((stride_length / leg_length) - 1) * math.sqrt(leg_length * g)

def main():
  # read the CSV file
  dataset1 = read_csv('dataset1.csv')
  dataset2 = read_csv('dataset2.csv')
  
  # merge the datasets and calculate the speed
  speeds = [] # store the speed of bipedal dinosaurs (name, speed)
  for name, data2 in dataset2.items(): # data2 is the value of the key(name)
    if data2['STANCE'] == 'bipedal' and name in dataset1:
      leg_length = float(dataset1[name]['LEG_LENGTH'])
      stride_length = float(data2['STRIDE_LENGTH'])
      speed = calculate_speed(leg_length, stride_length)
      speeds.append((name, speed))
  
  # sort the speeds in desc order
  speeds.sort(key=lambda x: x[1], reverse=True)
  
  # print the result
  for name, _ in speeds:
    print(name)

if __name__ == "__main__":
  main()