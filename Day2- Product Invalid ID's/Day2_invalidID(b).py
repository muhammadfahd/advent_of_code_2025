def solve_part2_IDs(file_content):
    # Clean the input just like before
    data = file_content.strip().replace('\n', '') # Fixed typo '/n' to '\n'

    total_sum = 0
    ranges = data.split(',')
    
    for r in ranges:
        parts = r.split('-')
        start = int(parts[0])
        end = int(parts[1])

        for num in range(start, end + 1):
            s_num = str(num)
            length = len(s_num)
            
            # Optimization: Single digit numbers (length 1) cannot repeat
            if length < 2:
                continue

            found_pattern = False

            # --- NEW LOGIC FOR PART 2 ---
            # We check pattern lengths from 1 up to half the string's length. Example: For "121212" (Len 6), we check pat_len 1, 2, 3.
            for pat_len in range(1, (length // 2) + 1):
                
                # 1. The total length must be divisible by the pattern length
                # You can't fit a length-2 pattern into a length-9 string evenly.
                if length % pat_len == 0:
                    
                    # 2. Extract the candidate pattern
                    pattern = s_num[:pat_len]
                    
                    # 3. Calculate how many times it must repeat
                    multiplier = length // pat_len
                    
                    # 4. Rebuild the string and check if it matches
                    # Example: "12" * 3 -> "121212"
                    if pattern * multiplier == s_num:
                        found_pattern = True
                        break # Found a match! Stop checking this number.
            
            if found_pattern:
                total_sum += num
                
    return total_sum

# --- RUNNER ---
with open('input(b).txt', 'r') as f:
    content = f.read()
    print("Sum is ", solve_part2_IDs(content))