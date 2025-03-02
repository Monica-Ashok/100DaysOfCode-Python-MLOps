# Day 13: Beginner - Debugging in Python  

## Topics Covered  

### 1. Identifying and Fixing Errors  
- Debugged small code snippets to identify syntax, logical, and runtime errors.  
- Used `print()` statements to trace the flow of execution and verify expected outputs.  

### 2. Understanding Function Logic  
- Reviewed function return values to ensure correct results.  
- Fixed incorrect conditions in functions to produce accurate outputs.  

### 3. Conditional Statements & Edge Cases  
- Handled edge cases in conditionals (`if`, `elif`, `else`) to prevent unexpected behavior.  
- Ensured logical correctness in number evaluation and leap year calculation.  

### 4. Loop Debugging  
- Checked the behavior of loops in `FizzBuzz` to confirm expected output sequences.  
- Verified loop termination conditions to avoid infinite loops.  

---

## Debugged Code Snippets  

### 1. **Odd or Even Checker**  

#### **Issue:**  
- The function correctly determined odd/even numbers, but needed verification.  

#### **Fixes Applied:**  
- Ensured correct modulus calculation to check divisibility by `2`.  
- Verified outputs with test cases for both even and odd numbers.  

---

### 2. **Leap Year Checker**  

#### **Issue:**  
- The function followed the leap year rules but required debugging for correct cases.  
- Edge cases like `2025` (non-leap year) needed validation.  

#### **Fixes Applied:**  
- Checked for correct ordering of leap year conditions (`divisible by 4`, `not divisible by 100`, or `divisible by 400`).  
- Verified with various test cases, including leap and non-leap years.  

---

### 3. **FizzBuzz Debugging**  

#### **Issue:**  
- The loop needed validation for `Fizz`, `Buzz`, and `FizzBuzz` cases.  
- Checked if `number % 3 == 0 and number % 5 == 0` was evaluated first.  

#### **Fixes Applied:**  
- Ensured `FizzBuzz` condition was checked before individual `Fizz` and `Buzz` cases.  
- Verified correct output sequence for numbers from `1` to `20`.  

---

## Key Learnings  

1. **Debugging Techniques**  
   - Used `print()` for step-by-step verification of function outputs.  
   - Identified where logic was failing by isolating conditions.  

2. **Logical Flow and Edge Cases**  
   - Tested boundary values like leap years (`2025`, `2024`, `2000`).  
   - Ensured loop conditions properly executed for `FizzBuzz`.  

3. **Refactoring & Code Readability**  
   - Maintained clear condition checks for better readability.  
   - Ensured correct indentation and structure to prevent syntax errors.  

---

## Next Steps  

- Use Python’s built-in `debugger` (`pdb`) for more complex debugging.  
- Explore logging instead of `print()` for scalable debugging.  
- Apply debugging techniques to larger projects like the **Number Guessing Game**.  
