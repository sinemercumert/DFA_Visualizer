from automata.fa.dfa import DFA
from visual_automata.fa.dfa import VisualDFA
import os

def get_user_input_as_set(prompt_text):
    user_input = input(prompt_text)
    return set(item.strip() for item in user_input.split(','))

def classify_character(char):
    if char.isalnum():
        if char.isdigit():
            return 'D'
        else:
            return 'L'
    elif char == '@':
        return '@'
    elif char == '.':
        return '.'
    elif char == '_':
        return '_'
    else:
        return 'UNKNOWN'

def translate_word_to_abstract(word):
    translated = ""
    for char in word:
        translated += classify_character(char)
    return translated

print("--- DFA Definition Screen ---")

states = get_user_input_as_set("Enter states (Q) (e.g., q0, q1): ")
input_symbols = get_user_input_as_set("Enter input alphabet (e.g., L,D,_,@,.): ")
initial_state = input("Enter initial state (q0): ").strip()
final_states = get_user_input_as_set("Enter final states (F): ")

print("\n----- Define Transition Functions (Delta) -----")
transitions = {}

for state in states:
    transitions[state] = {}
    for symbol in input_symbols:
        target = input(f"For state '{state}' and input '{symbol}', enter target state: ").strip()
        transitions[state][symbol] = target

try:
    logic_dfa = DFA(
        states=states,
        input_symbols=input_symbols,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
    )

    visual_dfa = VisualDFA(
        states=states,
        input_symbols=input_symbols,
        transitions=transitions,
        initial_state=initial_state,
        final_states=final_states
    )

    if visual_dfa:
        print("\nDFA created successfully.")
        visual_dfa.show_diagram(view=True) 

        while True:
            raw_word = input("\nEnter word to check (type 'exit' to quit): ")
            if raw_word.lower() == 'exit':
                break
            
            abstract_word = translate_word_to_abstract(raw_word)
            print(f"DEBUG: Translated '{raw_word}' to abstract format -> '{abstract_word}'")

            try:
                if logic_dfa.accepts_input(abstract_word):
                    print(f"RESULT: '{raw_word}' is ACCEPTED.")
                else:
                    print(f"RESULT: '{raw_word}' is REJECTED.")
            except Exception as e:
                print(f"REJECTED (Invalid Input for Logic): {e}")

except Exception as e:
    print(f"An error occurred: {e}") 