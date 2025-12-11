def solve_batteries_part2(file_content):
    banks = file_content.strip().split('\n')
    total_joltage = 0
    
    # We now need exactly 12 digits
    REQUIRED_DIGITS = 12
    
    for bank in banks:
        bank = bank.strip()
        if not bank: continue # Skip empty lines
        
        # We will build the final 12-digit number as a string e.g. "98765..."
        current_joltage_str = ""
        
        #  so we don't go backwards
        current_search_start_index = 0
        
        for i in range(REQUIRED_DIGITS):
            
            # How many digits do we still need to find AFTER this current one?  If i=0 (1st digit), we need 11 more. If i=11 (last digit), we need 0 more.
            digits_needed_after = (REQUIRED_DIGITS - 1) - i
            
            # We must stop searching early enough to leave 'digits_needed_after' characters Example: If bank length is 15, and we need 11 more digits, 

            search_end_limit = len(bank) - digits_needed_after
            
            # Slice the "Window" where it is safe to pick a number We look from our current spot up to the limit
            search_window = bank[current_search_start_index : search_end_limit]
            
            # --- GREEDY STEP --- Find the biggest digit in this safe window
            best_digit = max(search_window)
            
            # Add it to our result
            current_joltage_str += best_digit
            
            # --- MOVE FORWARD ---
            # We found the digit! Now we must advance our search start index  to be *after* the digit we just picked.
            
            relative_index = search_window.index(best_digit)
            
            # Update the main index for the next loop
            current_search_start_index += relative_index + 1
            
        # Convert the final "987..." string to an integer and add to total
        total_joltage += int(current_joltage_str)

    return total_joltage


# --- RUNNER ---
with open('input(b).txt', 'r') as file:
    file_content = file.read()
    print("Total sum is : ", solve_batteries_part2(file_content))