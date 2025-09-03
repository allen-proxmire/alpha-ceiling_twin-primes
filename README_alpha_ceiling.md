# The Alpha Ceiling and Twin Prime Distribution

**Author:** Allen Proxmire  
**Date:** 02 September 2025  

## Overview
This project presents a short research note introducing the **Alpha Ceiling**: a geometric property of consecutive primes based on "prime triangles."  

### Key Ideas
- **Prime Triangle:** Right triangle formed from a consecutive prime pair \((p_n, p_{n+1})\).  
- **Alpha Angle (α):** Defined as \(\alpha = \arctan(p_n / p_{n+1})\).  
- **Twin Prime Ceiling:** For any twin prime pair \((p_n, p_n+2)\), all consecutive primes between it and the next twin have strictly smaller α values. Thus, **twin primes set local α-ceilings.**

### Main Result
- **Lemma:** If \((p_n, p_n+2)\) is a twin prime and \((p_k, p_k+g_k)\) is any later consecutive prime pair, then  
  \[
  \alpha_k > \alpha_n \;\;\Rightarrow\;\; p_k > \tfrac{p_n g_k}{2}.
  \]  
- **Remark:** By Bertrand–Chebyshev’s theorem, there is always a prime before this threshold, so primes always have the *opportunity* not to break the ceiling.  
- **Computations:** Verified up to large bounds, showing no ceiling violations. Twin primes are the only α-record breakers in all checked ranges.  

### Conjecture
The **Twin Prime α-Ceiling Conjecture** states that twin primes always set unbroken α-ceilings until the next twin prime appears.  

---

## Repository Contents
- 📄 **Alpha Ceiling Twin Prime_NOTE.pdf** — Main paper.  
- 📜 **README_alpha ceiling.md** — Project summary.  
- (Optional: add computational scripts, data, plots if you want to include them later.)

---

## Citation
If you use this work, please cite:


[![DOI](https://zenodo.org/badge/1050031809.svg)](https://doi.org/10.5281/zenodo.17049966)


---

## License
This work is released under the **MIT License** (or whichever license you prefer).
