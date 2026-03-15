# Miller-Rabin Primality Test Visualization

A **Streamlit** app to visualize the Miller-Rabin primality test, helping users understand how the test determines if a number is probably prime or composite.

---

## **Features**

- Input any integer `n` and base `a` to test for primality.
- Visualizes the evolution of `x` during the Miller-Rabin test.
- Clearly indicates whether `n` is probably prime or composite.
- Interactive and user-friendly interface.

---

## **Installation**

1. Clone this repository or download the code.
2. Install the required packages:
  ```bash
   uv add streamlit matplotlib
  ```
3. Run the app:
  ```bash
   uv run streamlit run miller_rabin_app.py
  ```

---

## **Usage**

1. Enter a number `n` (e.g., `91`).
2. Enter a base `a` (e.g., `2`).
3. Click **"Run Miller-Rabin Test"** to see the visualization and result.

---

## **Background**

The **Miller-Rabin test** is a probabilistic primality test. It decomposes `n-1` into `2^s * d` and checks if `a^d ≡ 1 (mod n)` or `a^(2^r * d) ≡ -1 (mod n)` for some `r`. If not, `n` is composite.

---

## **Example**

- For `n = 91` (composite) and `a = 2`, the test fails, and the plot shows the evolution of `x`.
- For `n = 7` (prime) and `a = 2`, the test passes.

---

## **License**

This project is open-source and available under the [MIT License](LICENSE).
