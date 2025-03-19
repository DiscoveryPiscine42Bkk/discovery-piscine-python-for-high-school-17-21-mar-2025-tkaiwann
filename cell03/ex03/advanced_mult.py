#!/usr/bin/env python3
table = 0
while table <= 10 :
    output =f"Table de {table}: "
    num = 0 
    while num <= 10 : 
        output += str(table * num) + " "
        num += 1
    print(output.strip())
    table += 1