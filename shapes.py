#!/usr/bin/env python3
# Drawing shapes

def draw_circle(t, x, y, r):
    ''' draws a circle from point x,y with radius r using turtle t'''
    t.pu()
    t.goto(x,y)
    t.pd()
    t.circle(r)

