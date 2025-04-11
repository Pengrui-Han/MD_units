import random
import json

def generate_arithmetic_dataset(num_addition=25, num_subtraction=25):
    dataset = []
    
    # Generate addition problems
    for _ in range(num_addition):
        # Generate 2-digit or 3-digit numbers
        a = random.randint(10, 999)
        b = random.randint(10, 999)
        correct_answer = a + b
        
        # Generate incorrect answer
        error_type = random.random()
        if error_type < 0.3:  # Small error
            incorrect_answer = correct_answer + random.choice([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        elif error_type < 0.5:  # Digit swap
            correct_str = str(correct_answer)
            if len(correct_str) >= 2:
                i, j = random.sample(range(len(correct_str)), 2)
                incorrect_str = list(correct_str)
                incorrect_str[i], incorrect_str[j] = incorrect_str[j], incorrect_str[i]
                incorrect_answer = int(''.join(incorrect_str))
            else:
                incorrect_answer = correct_answer + random.randint(1, 10)  # Fallback
        elif error_type < 0.7:  # Operation error
            incorrect_answer = a - b  # Use subtraction instead of addition
        else:  # Random error
            incorrect_answer = correct_answer + random.randint(11, 50) * random.choice([-1, 1])
        
        # Ensure incorrect answer is different and positive
        if incorrect_answer == correct_answer or incorrect_answer < 0:
            incorrect_answer = correct_answer + random.randint(1, 20)
        
        dataset.append({
            "type": "addition",
            "problem": f"{a} + {b}",
            "correct_equation": f"{a} + {b} = {correct_answer}",
            "incorrect_equation": f"{a} + {b} = {incorrect_answer}",
            "a": a,
            "b": b,
            "correct_answer": correct_answer,
            "incorrect_answer": incorrect_answer
        })
    
    # Generate subtraction problems
    for _ in range(num_subtraction):
        # Ensure a > b to keep answers positive
        a = random.randint(50, 999)
        b = random.randint(10, a-1)
        correct_answer = a - b
        
        # Generate incorrect answer with similar strategy
        error_type = random.random()
        if error_type < 0.3:  # Small error
            incorrect_answer = correct_answer + random.choice([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        elif error_type < 0.5:  # Digit swap
            correct_str = str(correct_answer)
            if len(correct_str) >= 2:
                i, j = random.sample(range(len(correct_str)), 2)
                incorrect_str = list(correct_str)
                incorrect_str[i], incorrect_str[j] = incorrect_str[j], incorrect_str[i]
                incorrect_answer = int(''.join(incorrect_str))
            else:
                incorrect_answer = correct_answer + random.randint(1, 10)  # Fallback
        elif error_type < 0.7:  # Operation error
            incorrect_answer = a + b  # Use addition instead of subtraction
        else:  # Random error
            incorrect_answer = correct_answer + random.randint(11, 50) * random.choice([-1, 1])
        
        # Ensure incorrect answer is different and positive
        if incorrect_answer == correct_answer or incorrect_answer < 0:
            incorrect_answer = correct_answer + random.randint(1, 20)
        
        dataset.append({
            "type": "subtraction",
            "problem": f"{a} - {b}",
            "correct_equation": f"{a} - {b} = {correct_answer}",
            "incorrect_equation": f"{a} - {b} = {incorrect_answer}",
            "a": a, 
            "b": b,
            "correct_answer": correct_answer,
            "incorrect_answer": incorrect_answer
        })
    
    return dataset

# Generate the dataset
arithmetic_dataset = generate_arithmetic_dataset()

# Save to JSON file
with open('arithmetic_dataset_test.json', 'w') as f:
    json.dump(arithmetic_dataset, f, indent=2)

print(f"Generated {len(arithmetic_dataset)} arithmetic problems")