def solve_batteries_greedy(file_content):
    banks = file_content.strip().split('\n')
    total_joltage = 0
    
    for bank in banks:
        bank = bank.strip()
        
        # --- THE GREEDY LOOP ---
        # We start asking for '9', then '8', then '7'...  range(9, -1, -1) counts: 9, 8, 7, 6, 5, 4, 3, 2, 1, 0
        found = False
        for d in range(9, -1, -1):
            target = str(d) # Convert number 9 to string "9"
            
            # 1. Find the FIRST occurrence
            # .find() returns the index of the first match, or -1 if not found
            index = bank.find(target)
            
            # 2. Validate the spot
            # index != -1 : We found the number
            # index < len(bank) - 1 : It is NOT the last digit (we need room for a second digit)
            if index != -1 and index < len(bank) - 1:
                
                # 3. Secure the "Tens" digit
                tens_digit = target
                
                # 4. Get the "Remainder" (The Tail)
                # This slice takes everything from the next index to the end
                remainder = bank[index + 1:]
                
                # 5. Greedy grab for the "Ones" digit
                # max() on a string finds the character with the highest value
                ones_digit = max(remainder)
                
                # Form the number
                joltage = int(tens_digit + ones_digit)
                total_joltage += joltage
                
                found = True
                break # STOP! We found the best possible start (e.g. 9), no need to check 8.
        
    return total_joltage










with open('input(a).txt','r') as file:
    file_content= file.read()
    print("Total sum is : ",solve_batteries_greedy(file_content))