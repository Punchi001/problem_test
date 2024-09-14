def solution(N):
    # Convert the number to a binary list, removing the '0b' prefix
    bina = list(bin(N)[2:])
    gap = 0
    max_gap = 0
    sequence = 0
    
    for bit in bina:
        if bit == '1':
            # If we find a '1', we check the current gap and reset
            max_gap = max(max_gap, gap)
            gap = 0  # Reset the gap counter
        elif bit == '0':
            # If it's a '0', we are in the middle of a gap
            gap += 1
    
    return f'gap: {max_gap}, sequence: {sequence}'

# Example usage
result = solution(20)
print(result)