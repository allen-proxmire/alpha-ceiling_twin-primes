import math
import sympy

# Define the new start and end points for the search
START = 2_000_000_000
LIMIT = 5_000_000_000

def main():
    # Initialize prev_prime to the last prime before the START of our range
    # This is crucial for the logic to work correctly from the beginning.
    prev_prime = sympy.prevprime(START)
    
    twin_alpha = None
    twin_prime = None
    last_twin = None

    # Generator for primes within the specified range
    prime_gen = sympy.primerange(START, LIMIT + 1)

    print(f"Starting search for primes between {START:,} and {LIMIT:,}...")
    print(f"Initial previous prime set to: {prev_prime:,}")

    # Store the previous prime to detect twin primes
    for prime in prime_gen:
        # Check if previous prime and current prime form a twin
        if prime - prev_prime == 2:
            # Compute alpha for this twin
            twin_alpha = math.atan(prev_prime / prime)
            twin_prime = prev_prime
            # Store index to start checking after this twin
            last_twin = (prev_prime, prime)
        elif twin_alpha is not None:
            # Check consecutive primes for alpha exceeding previous twin
            alpha = math.atan(prev_prime / prime)
            if alpha > twin_alpha:
                print(f"Counterexample found after twin {last_twin}:")
                print(f"Consecutive primes ({prev_prime}, {prime}) with alpha {alpha:.10f} > twin alpha {twin_alpha:.10f}")
                # You can stop here if you only want the first counterexample
                return
        prev_prime = prime

    print(f"No counterexamples found between {START:,} and {LIMIT:,}")

if __name__ == "__main__":
    main()