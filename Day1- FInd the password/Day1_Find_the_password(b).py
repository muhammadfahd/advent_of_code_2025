
def safe_dial_rotation(rotations):
    # initializing 
    current_pos=50
    no_of_zeors=0

    for i in rotations: 
        i=i.strip()
        direction=i[0]   # for chracter like left or right
        steps=int(i[1:]) # for distance like how many time move


        # count full circle - every 100 gurantee 0 
        no_of_zeors+=steps//100
        reminder =steps%100
        if direction=='R':
            if current_pos + reminder >=100:
                no_of_zeors+=1
            current_pos = (current_pos + reminder) % 100    
        
        elif direction=='L':
            if current_pos != 0 and (current_pos - reminder <= 0 ):
                no_of_zeors+=1
            current_pos=(current_pos-reminder)%100

    return no_of_zeors
             

with open('input(b).txt', 'r') as f:
    file_lines = f.readlines()
    real_result = safe_dial_rotation(file_lines)
    print(f"Puzzle Answer: {real_result}")