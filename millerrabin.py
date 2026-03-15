import streamlit as st
import matplotlib.pyplot as plt
import random

st.set_page_config(page_title="Miller-Rabin primality test", layout="wide")

def is_prime(n, k=5):
    """Miller-Rabin primality test."""
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0:
            return n == p
    s, d = 0, n - 1
    while d % 2 == 0:
        s, d = s + 1, d // 2
    for _ in range(k):
        a = random.randint(2, n - 1)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for __ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def miller_rabin_visualization(n, a):
    """
    Visualizes the behavior of the Miller-Rabin loop for a given number n and base a.
    Returns the sequence of x values and whether the 'else' block was executed.
    """
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    x = pow(a, d, n)
    states = [x]
    if x == 1 or x == n - 1:
        return states, False
    for _ in range(s - 1):
        x = pow(x, 2, n)
        states.append(x)
        if x == n - 1:
            return states, False
    return states, True

def visualize_states(states, else_executed, n):
    """Plots the evolution of x during the Miller-Rabin test."""
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(states, marker='o', linestyle='-', color='blue', label="x values")
    ax.axhline(n - 1, color='red', linestyle='--', label="n-1")
    ax.axhline(1, color='green', linestyle='--', label="1")
    ax.set_title(f"Evolution of x in Miller-Rabin Test for n={n}")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("x (mod n)")
    ax.legend()
    ax.grid(alpha=0.4)
    if else_executed:
        ax.text(len(states) - 1, states[-1], "Else Executed!", color="red", fontsize=12)
    return fig

# Streamlit UI
st.title("Miller-Rabin Primality Test Visualization")
st.write("This app visualizes the Miller-Rabin test for a given number `n` and base `a`.")

n = st.number_input("Enter a number (n) to test:", min_value=2, value=91)
a = st.number_input("Enter a base (a) for the test:", min_value=2, value=2)

if st.button("Run Miller-Rabin Test"):
    if n < 2:
        st.error("n must be ≥ 2.")
    else:
        states, else_executed = miller_rabin_visualization(n, a)
        fig = visualize_states(states, else_executed, n)
        st.pyplot(fig)
        if else_executed:
            st.warning(f"Base {a}: n = {n} is **composite** (Miller-Rabin test failed).")
        else:
            st.success(f"Base {a}: n = {n} is **probably prime** (Miller-Rabin test passed).")
