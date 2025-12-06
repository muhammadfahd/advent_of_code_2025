def fresh_count(content):
    data = content.strip().split('\n\n')

    # Ranges string block
    ranges_raw = data[0].strip().split('\n')
    # IDs string block
    IDs = data[1].strip().split('\n')

    # FIX 1: Rename variable from 'range' to 'parsed_ranges' to avoid conflict
    parsed_ranges = []
    
    for i in ranges_raw:
        start, end = i.split('-')
        # FIX 2: Use double parentheses to append a Tuple
        parsed_ranges.append((int(start), int(end)))

    count = 0
    for i in IDs:
        current = int(i)
        is_fresh = False

        # FIX 3: Iterate over 'parsed_ranges' (the tuples), NOT 'ranges_raw' (the strings)
        for start, end in parsed_ranges:
            if start <= current <= end:
                is_fresh = True
                break
        
        if is_fresh:
            count += 1
            
    return count 

# --- Runner ---
with open('input(a).txt', 'r') as file:
    f_content = file.read()
    total = fresh_count(f_content)
    print("Total result is ", total)