#!/bin/python3
import pygal

barchart = pygal.Bar()
barchart.title = 'Favourite Pets & Animals'
barchart.add('Dog' , 6)
barchart.add('Cat' , 4)
barchart.add('Hompter' , 3)
barchart.add('Fich' , 2)
barchart.add('snek' , 1)
barchart.render()

file = open('pets.txt' , 'r')

for line in file.read().splitlines():
    label, value = line.split(' ')
    print(label, value)

file.close()
