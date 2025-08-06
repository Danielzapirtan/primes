import json

def is_prime(n):
    """Check if a number is prime using trial division with optimizations."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Only check odd divisors up to sqrt(n)
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def find_nth_prime(n):
    """Find the nth prime number (1-indexed: 1st prime is 2)."""
    if n == 1:
        return 2
    
    count = 1  # We already know 2 is prime
    candidate = 3  # Start checking from 3
    
    while count < n:
        if is_prime(candidate):
            count += 1
            if count == n:
                return candidate
        candidate += 2  # Only check odd numbers after 2
    
    return candidate

def generate_milestone_primes():
    """Generate every 1000th prime from 1000th to 10000th."""
    results = {}
    
    print("Calculating milestone primes...")
    
    for n in range(1000, 101000, 1000):  # 1000, 2000, ..., 100000
        print(f"Finding the {n}th prime...")
        nth_prime = find_nth_prime(n)
        results[str(n)] = nth_prime
        print(f"The {n}th prime is: {nth_prime}")
    
    return results

def save_to_json(data, filename="milestone_primes.json"):
    """Save the results to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"\nResults saved to {filename}")

def main():
    """Main function to orchestrate the prime generation and saving."""
    milestone_primes = generate_milestone_primes()
    save_to_json(milestone_primes)
    
    # Display the results
    print("\nMilestone Primes Summary:")
    print("=" * 30)
    for n, prime in milestone_primes.items():
        print(f"{n}th prime: {prime}")

if __name__ == "__main__":
    main()
