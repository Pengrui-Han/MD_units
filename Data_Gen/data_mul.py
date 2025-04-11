import random
import json

def generate_multiplication_division_dataset(num_multiplication=200, num_division=200):
    dataset = []
    
    # Generate multiplication problems
    for _ in range(num_multiplication):
        # Generate numbers (smaller range for multiplication to keep results manageable)
        a = random.randint(2, 30)
        b = random.randint(2, 30)
        correct_answer = a * b
        
        # Generate incorrect answer
        error_type = random.random()
        if error_type < 0.3:  # Small error
            incorrect_answer = correct_answer + random.choice([-10, -5, -2, -1, 1, 2, 5, 10])
        elif error_type < 0.5:  # Digit swap
            correct_str = str(correct_answer)
            if len(correct_str) >= 2:
                i, j = random.sample(range(len(correct_str)), 2)
                incorrect_str = list(correct_str)
                incorrect_str[i], incorrect_str[j] = incorrect_str[j], incorrect_str[i]
                incorrect_answer = int(''.join(incorrect_str))
            else:
                incorrect_answer = correct_answer + random.randint(1, 5)  # Fallback
        elif error_type < 0.7:  # Common multiplication error: adding instead
            incorrect_answer = a + b
        else:  # Random error
            incorrect_answer = correct_answer + random.randint(1, 20) * random.choice([-1, 1])
        
        # Ensure incorrect answer is different and positive
        if incorrect_answer == correct_answer or incorrect_answer <= 0:
            incorrect_answer = correct_answer + random.randint(1, 10)
        
        dataset.append({
            "type": "multiplication",
            "problem": f"{a} × {b}",
            "correct_equation": f"{a} × {b} = {correct_answer}",
            "incorrect_equation": f"{a} × {b} = {incorrect_answer}",
            "a": a,
            "b": b,
            "correct_answer": correct_answer,
            "incorrect_answer": incorrect_answer
        })
    
    # Generate division problems
    for _ in range(num_division):
        # For division, create b first, then a = b * quotient to ensure clean division
        b = random.randint(2, 20)
        quotient = random.randint(2, 20)
        a = b * quotient  # This ensures a is divisible by b
        
        correct_answer = quotient  # a ÷ b = quotient
        
        # Generate incorrect answer
        error_type = random.random()
        if error_type < 0.3:  # Small error
            incorrect_answer = correct_answer + random.choice([-3, -2, -1, 1, 2, 3])
        elif error_type < 0.5:  # Digit swap (if applicable)
            correct_str = str(correct_answer)
            if len(correct_str) >= 2:
                i, j = random.sample(range(len(correct_str)), 2)
                incorrect_str = list(correct_str)
                incorrect_str[i], incorrect_str[j] = incorrect_str[j], incorrect_str[i]
                incorrect_answer = int(''.join(incorrect_str))
            else:
                incorrect_answer = correct_answer + random.randint(1, 3)  # Fallback
        elif error_type < 0.7:  # Inversion error: b ÷ a instead of a ÷ b
            # Avoid division by zero or very small numbers
            if a == 0:
                incorrect_answer = correct_answer + random.randint(1, 3)
            else:
                try:
                    incorrect_answer = round(b / a, 1)
                    # If this gives the same answer or is very close, use a different error
                    if abs(incorrect_answer - correct_answer) < 0.5:
                        incorrect_answer = correct_answer + random.randint(1, 5)
                except:
                    incorrect_answer = correct_answer + random.randint(1, 5)
        else:  # Random error
            incorrect_answer = correct_answer + random.randint(1, 5) * random.choice([-1, 1])
        
        # Ensure incorrect answer is different and positive
        if incorrect_answer == correct_answer or incorrect_answer <= 0:
            incorrect_answer = correct_answer + random.randint(1, 5)
        
        # Round to integer if the incorrect answer is close enough
        if isinstance(incorrect_answer, float) and abs(incorrect_answer - round(incorrect_answer)) < 0.01:
            incorrect_answer = round(incorrect_answer)
        
        dataset.append({
            "type": "division",
            "problem": f"{a} ÷ {b}",
            "correct_equation": f"{a} ÷ {b} = {correct_answer}",
            "incorrect_equation": f"{a} ÷ {b} = {incorrect_answer}",
            "a": a,
            "b": b,
            "correct_answer": correct_answer,
            "incorrect_answer": incorrect_answer
        })
    
    return dataset

# Generate the dataset
arithmetic_dataset = generate_multiplication_division_dataset()

# Save to JSON file
with open('multiplication_division_dataset.json', 'w') as f:
    json.dump(arithmetic_dataset, f, indent=2)

print(f"Generated {len(arithmetic_dataset)} multiplication and division problems")