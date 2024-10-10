#!/usr/bin/python3

def canUnlockAll(boxes):
    unlocked = set()  
    unlocked.add(0)   
    keys = [0]      

    while keys:
        current_box = keys.pop() 
        for key in boxes[current_box]:
            if key not in unlocked:  
                unlocked.add(key)    
                keys.append(key)     

    return len(unlocked) == len(boxes)
