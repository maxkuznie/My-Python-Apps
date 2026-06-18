#!/bin/python3
import pygal

piechart = pygal.Pie()
piechart.title = 'Favourite Pets & Animals'
piechart.add('Dog' , 6)
piechart.add('Cat' , 4)
piechart.add('Hompter' , 3)
piechart.add('Fich' , 2)
piechart.add('snek' , 1)
piechart.render()

file = open('pets.txt' , 'r')

for line in file.read().splitlines():
    label, value = line.split(' ')
    print(label, value)

file.close()
