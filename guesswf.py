import math as mt
import random as rd
import csv
import sys

rd.seed(1)

def RN(m1,m2,m3):
  t=m1*w1+m2*w2+m3*w3+b
  return sigmoide(t)

def sigmoide(t):
  return 1/(1+mt.exp(-t))

# the two parameters of the dataset are temp and hum now
with open('datas.csv') as file:
  reader = csv.reader(file)

  count = 0
  dataset = []

  for row in reader:
    dataset.append(row)    
    count += 1

# print(dataset)
dataset = [[int(float(j)) for j in i] for i in dataset]
# print(dataset)

def sigmoide_p(t):
  return sigmoide(t)*(1-sigmoide(t))

def train():
  w1=rd.random()
  w2=rd.random()
  w3=rd.random()
  b=rd.random()

  iterazioni = 10000
  learning_rate = 0.1

  for i in range(iterazioni):

    ri = rd.randint(0,len(dataset)-1)
    point = dataset[ri]

    z = point[0] * w1 + point[1] * w2 + point[2] * w3 + b
    pred = sigmoide(z)

    target = point[3]

    cost = (pred - target)**2

    dcost_dpred = 2 * (pred - target)
    dpred_dz = sigmoide_p(z)

    dz_dw1 = point[0]
    dz_dw2 = point[1]
    dz_dw3 = point[2]
    dz_db = 1

    dcost_dz = dcost_dpred * dpred_dz

    dcost_dw1 = dcost_dz * dz_dw1
    dcost_dw2 = dcost_dz * dz_dw2
    dcost_dw3 = dcost_dz * dz_dw3
    dcost_db = dcost_dz * dz_db

    w1 = w1 - learning_rate * dcost_dw1
    w2 = w2 - learning_rate * dcost_dw2
    w3 = w3 - learning_rate * dcost_dw3
    b = b - learning_rate * dcost_db

  return w1, w2, w3, b

w1, w2, w3, b = train()

# input values from user
try:
  t, h, w = map(float,input('Enter your input: (temp, hum, wind) ').split())
except ValueError:
  print('Not a number')
  sys.exit(1)

# call the function
previsione=RN(t, h, w)

# print the result
print(previsione)