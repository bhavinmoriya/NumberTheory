def collatz_sequence(n):
    """Generate the Collatz sequence for a given number n."""
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

# Example usage
number = int(input("Enter a positive integer: "))
sequence = collatz_sequence(number)
print(f"Collatz sequence for {number}: {sequence}")
print(f"Maximal height for {number}: {max(sequence)}")
