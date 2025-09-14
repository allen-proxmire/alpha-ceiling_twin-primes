# twin_gap_checker_v2.py
import math
from typing import Generator

def segmented_sieve(start: int, end: int, segment_size: int = 100_000) -> Generator[int, None, None]:
    """
    Generate primes in [start, end] (inclusive) using a segmented sieve.
    Memory usage ~ O(sqrt(end) + segment_size).
    """
    if end < 2:
        return
    if start < 2:
        start = 2

    limit = int(math.isqrt(end)) + 1
    sieve = bytearray(limit + 1)  # 0 = prime candidate, 1 = composite
    small_primes = []
    for i in range(2, limit + 1):
        if sieve[i] == 0:
            small_primes.append(i)
            ii = i * i
            if ii <= limit:
                sieve[ii : limit + 1 : i] = b'\x01' * (((limit - ii) // i) + 1)

    for low in range(start, end + 1, segment_size):
        high = min(low + segment_size - 1, end)
        seg_size = high - low + 1
        segment = bytearray(seg_size)

        for p in small_primes:
            start_index = (low + p - 1) // p * p
            if start_index < p * p:
                start_index = p * p
            for multiple in range(start_index, high + 1, p):
                segment[multiple - low] = 1

        for i in range(seg_size):
            if segment[i] == 0:
                yield low + i

def find_twin_gaps(start: int = 1, end: int = 100_000, segment_size: int = 100_000):
    """
    Finds twin primes (p, p+2) and prints gaps between consecutive twin-firsts
    that are bigger than the previous twin-first prime.
    """
    prime_gen = segmented_sieve(start, end, segment_size)
    last_prime = None
    last_twin_first = None
    found_any = False

    for p in prime_gen:
        if last_prime is not None and (p - last_prime) == 2:
            twin_first = last_prime
            if last_twin_first is not None:
                gap = twin_first - last_twin_first
                if gap > last_twin_first:
                    print(
                        f"Gap {gap} between twins starting at {last_twin_first} and {twin_first} "
                        f"exceeds previous twin first {last_twin_first}"
                    )
                    found_any = True
            last_twin_first = twin_first
        last_prime = p

    if not found_any:
        print(f"No twin-prime gap exceeded the previous twin's first prime in [{start}, {end}].")

if __name__ == "__main__":
    # Adjustable range and segment size
    START = 7
    END = 5_000_000_000
    SEGMENT_SIZE = 100_000_000

    find_twin_gaps(START, END, SEGMENT_SIZE)
