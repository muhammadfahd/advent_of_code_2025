# def fresh_count_part2(content):
#     # Split ranges from the rest (we don't need the bottom half anymore)
#     parts = content.strip().split('\n\n')
#     ranges_raw = parts[0].strip().split('\n')
    
#     parsed_ranges = []
#     for line in ranges_raw:
#         start, end = line.split('-')
#         parsed_ranges.append((int(start), int(end)))

#     # Set to store unique numbers that will automatically ignores duplicates!
#     unique_fresh_ids = set()

#     for start, end in parsed_ranges:
#         # Loop through every number in this specific range
#         # Remember: range() in Python excludes the last number, so we use end + 1
#         for num in range(start, end + 1):
#             unique_fresh_ids.add(num)
            
#     # The length of the set is the count of unique fresh IDs
#     return len(unique_fresh_ids)

# # --- Runner ---
# with open('input(b).txt', 'r') as file:
#     f_content = file.read()
#     total = fresh_count_part2(f_content)
#     print("Total Fresh IDs:", total)





def solve_large_ranges(content):
    parts = content.strip().split('\n\n')
    ranges_raw = parts[0].strip().split('\n')
    
    # 1. Parse and Sort
    # Sorting is crucial for the merge logic to work!
    parsed_ranges = []
    for line in ranges_raw:
        if not line: continue
        start, end = line.split('-')
        parsed_ranges.append((int(start), int(end)))
    
    # Sort by the start number
    parsed_ranges.sort(key=lambda x: x[0])
    
    # 2. Merge Intervals
    merged_ranges = []
    
    for current_start, current_end in parsed_ranges:
        if not merged_ranges:
            merged_ranges.append((current_start, current_end))
        else:
            # Get the last range we added
            last_start, last_end = merged_ranges[-1]
            
            # Check for overlap If the current start is inside the last range (or touches it)
            if current_start <= last_end: 
                # Merge them: The new end is the max of both ends
                new_end = max(last_end, current_end)
                # Update the last range in the list
                merged_ranges[-1] = (last_start, new_end)
            else:
                # No overlap, add as a new range
                merged_ranges.append((current_start, current_end))
                
    # 3. Calculate Total
    total_count = 0
    for start, end in merged_ranges:
        # Math: The number of items is (End - Start) + 1
        total_count += (end - start + 1)
        
    return total_count

# --- RUNNER ---
# Copy the huge block of numbers you pasted into 'input_part2.txt'
# or paste it into a string variable.
with open('input(b).txt', 'r') as file:
    f_content = file.read()
    total = solve_large_ranges(f_content)
    print(f"Total Fresh IDs: {total}")