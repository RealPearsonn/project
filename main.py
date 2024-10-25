import random

def generate_random_number(start, end):
    return random.randint(start, end)

# Example usage
if __name__ == "__main__":
    start_range = int(input("Enter the start of the range: "))
    end_range = int(input("Enter the end of the range: "))
    
    random_number = generate_random_number(start_range, end_range)
    print(f"Random number between {start_range} and {end_range}: {random_number}")
