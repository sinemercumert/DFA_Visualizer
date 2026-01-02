# DFA Pattern Validator & Visualizer

This project implements a **Deterministic Finite Automaton (DFA)** capable of handling infinite alphabets (like generic text) through an **abstraction layer**. It is designed to visualize the automaton and validate user input against defined patterns, such as email formats.

## The Logic: Why Abstraction?

In a standard DFA, defining transitions for every possible ASCII character is impossible. This tool solves this by classifying raw characters into abstract symbols before processing:

### Abstraction Rules (Σ -> Abstract Alphabet)
* **Letters (a-z, A-Z)** $\rightarrow$ mapped to `L`
* **Digits (0-9)** $\rightarrow$ mapped to `D`
* **Underscore (_)** $\rightarrow$ mapped to `_`
* **At Symbol (@)** $\rightarrow$ mapped to `@`
* **Dot (.)** $\rightarrow$ mapped to `.`
* **Others** $\rightarrow$ mapped to `UNKNOWN`

## Use Case: Email Validation

This tool was specifically designed to validate emails in the format:  
`name@string1.string2`

Where:
* `name` $\in$ `{letter, digit, _}*`
* `string1` $\in$ `{letter, digit}*`
* `string2` (implicitly) $\in$ `{letter}*`

### How to Configure for Email Test
When running the script (`main.py`), use the following inputs to build the Email Validator DFA:

1.  **States (Q):** `q0, q1, q2, q3, q4`
2.  **Input Alphabet:** `L, D, _, @, .`
3.  **Initial State:** `q0`
4.  **Final States (F):** `q4`

### Transition Table (Input Guide)

| Current State | Input Symbol | Target State | Logic Explanation |
| :--- | :---: | :---: | :--- |
| **q0** (Start) | `L`, `D`, `_` | **q0** | Accepts name chars |
| **q0** | `@` | **q1** | Expects '@' to proceed |
| **q1** (After @) | `L`, `D` | **q2** | Start of domain (string1) |
| **q2** (Domain) | `L`, `D` | **q2** | Accepts domain chars |
| **q2** | `.` | **q3** | Expects '.' to proceed |
| **q3** (Extension) | `L` | **q4** | Start of extension (string2) |
| **q4** (Final) | `L` | **q4** | Accepts extension chars |

*Note: Any other transition leads to a standard "Trap/Dead" state (implicitly handled as rejection).*

## Installation & Usage

### Prerequisites
You need **Graphviz** installed on your system (not just the python library).
* **Windows:** [Download Graphviz](https://graphviz.org/download/) and add to PATH.
* **Linux:** `sudo apt install graphviz`
* **Mac:** `brew install graphviz`

### Setup
1. Clone the repository.
2. Install python dependencies:
   ```bash
   pip install -r requirements.txt