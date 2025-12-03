
def safe_dial_rotation(rotations):
    # initializing 
    current_pos=50
    no_of_zeors=0

    for i in rotations: 
        i=i.strip()
        direction=i[0]   # for chracter like left or right
        steps=int(i[1:]) # for distance like how many time move

        if direction=='R':
            current_pos=(current_pos+steps)%100    # as % will allows to wrap around 99
        elif direction=='L':
            current_pos=(current_pos-steps)%100

        if current_pos==0:
            no_of_zeors+=1

    return no_of_zeors
             

with open('input(a).txt', 'r') as f:
    file_lines = f.readlines()
    real_result = safe_dial_rotation(file_lines)
    print(f"Puzzle Answer: {real_result}")