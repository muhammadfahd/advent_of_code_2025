
def in_correctIDs(file_content):
    
    data=file_content.strip().replace('/n','')

    total_sum=0
    # split into range
    ranges=data.split(',')
    
    for i in ranges:
        parts= i.split('-')
        starts=int(parts[0])
        end=int(parts[1])

        '''
        iterating through range and 
        converting each number into string and 
        find total length 
    '''
        for num in range(starts, end+1):
            string_num=str(num)
            length=len(string_num)

            if length%2!=0:
                continue

            # checking for repated sequecne
            # as invalid id could not odd lengyth so they are even
            mid=length//2
            first_half=string_num[:mid]
            second_half=string_num[mid:]

            if first_half==second_half:
                total_sum+=num
    
    return total_sum            


with open('input(a).txt','r')as f :
    content=f.read()

    print("Sum is ",in_correctIDs(content))