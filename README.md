# DFA Email Pattern Visualizer

This project implements a Deterministic Finite Automaton (DFA) designed to accept a specific language $L$ defined by custom email formatting rules. The tool visualizes the state diagram and verifies input strings based on an abstraction layer.

## Formal Definition

The DFA $M$ accepts the language $L(M) = L$, where:

$$L = \{ w \in \Sigma^* : \text{name@string1.string2} \}$$

### Constraints
The components of the email are defined as follows:

1.  **$\Sigma$ (Alphabet):** Any typable character.
2.  **name:**
    * $name \in \text{NAME}^*$ where $\text{NAME} = \{ a-z, A-Z, 0-9, \_ \}$
    * **Rule 1:** Must start with a letter.
    * **Rule 2:** Must contain at least **1 digit**.
3.  **string1:**
    * $string1 \in \text{STRING1}^*$ where $\text{STRING1} = \{ a-z, 0-9 \}$
    * **Rule:** Must contain **exactly 2 digits**.
4.  **string2:**
    * Must be strictly one of the following: `“eu”` or `“pl”`.

## Abstraction Logic

Since defining transitions for every ASCII character is inefficient, the Python script translates raw input into abstract symbols before processing:

* **Letters (a-z, A-Z)** $\rightarrow$ `L`
* **Digits (0-9)** $\rightarrow$ `D`
* **Underscore (_)** $\rightarrow$ `_`
* **@** $\rightarrow$ `@`
* **Dot (.)** $\rightarrow$ `.`

*(Note: To strictly validate "eu" or "pl", the DFA logic assumes the abstract input sequence matches the length and structure of these domains).*

## Requirements

* Python 3.x
* Graphviz (System Binary installed and added to PATH)
* Libraries: `automata-lib`, `visual-automata`

## Usage

1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
2.  Run the visualizer:
    ```bash
    python dfaVisualizer.py
    ```
3.  Enter the DFA components (States, Alphabet, Transitions) via the command line interface to model the rules described above.