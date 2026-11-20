#!/usr/bin/env python3
"""
Simple and fast command-line calculator.
Supports basic arithmetic: addition (+), subtraction (-), multiplication (*), division (/).
"""

import sys

def calculate(a: float, op: str, b: float):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError(f"Unsupported operator: {op}")

def format_num(val: float) -> str:
    if val.is_integer():
        return str(int(val))
    return f"{round(val, 8):g}"

def main():
    if len(sys.argv) == 4:
        # CLI argument mode: python3 calculator.py 5 + 3
        try:
            a = float(sys.argv[1])
            op = sys.argv[2]
            b = float(sys.argv[3])
            res = calculate(a, op, b)
            print(format_num(res))
            return
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)

    print("Fast Simple Calculator (+, -, *, /)")
    print("Format: <number> <operator> <number> (e.g., '12 + 4' or '10 / 2')")
    print("Type 'q' or 'exit' to quit.\n")

    while True:
        try:
            raw = input("calc> ").strip()
            if not raw:
                continue
            if raw.lower() in ('q', 'exit', 'quit'):
                break

            parts = raw.split()
            if len(parts) != 3:
                print("Usage: <num1> <+|-|*|/> <num2>")
                continue

            a_str, op, b_str = parts
            a = float(a_str)
            b = float(b_str)
            result = calculate(a, op, b)
            print(f"= {format_num(result)}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

if __name__ == "__main__":
    main()
