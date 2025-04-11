import random
import json

def generate_word_problems(num_problems=400):
    # Dictionary for number to word conversion
    num_to_word = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty",
        21: "twenty-one", 22: "twenty-two", 23: "twenty-three", 24: "twenty-four", 25: "twenty-five",
        26: "twenty-six", 27: "twenty-seven", 28: "twenty-eight", 29: "twenty-nine", 30: "thirty",
        31: "thirty-one", 32: "thirty-two", 33: "thirty-three", 34: "thirty-four", 35: "thirty-five",
        36: "thirty-six", 37: "thirty-seven", 38: "thirty-eight", 39: "thirty-nine", 40: "forty",
        41: "forty-one", 42: "forty-two", 43: "forty-three", 44: "forty-four", 45: "forty-five",
        46: "forty-six", 47: "forty-seven", 48: "forty-eight", 49: "forty-nine", 50: "fifty"
    }
    
    # Function to convert number to word
    def number_to_words(num):
        if num in num_to_word:
            return num_to_word[num]
        return str(num)  # Fallback if number is outside our dictionary
    
    # Define possible scenarios, objects, and characters
    characters = ["Alex", "Emma", "Noah", "Olivia", "Liam", "Sophia", "Jackson", "Ava", 
                 "Lucas", "Isabella", "Mason", "Mia", "Ethan", "Charlotte", "Logan",
                 "Amelia", "Aiden", "Harper", "James", "Evelyn", "Lily", "Benjamin",
                 "Michael", "Sofia", "Jacob", "Abigail", "Daniel", "Emily", "Henry",
                 "Ella", "Matthew", "Madison", "Samuel", "Scarlett", "David", "Victoria"]
    
    objects = [
        {"name": "apple", "plural": "apples", "context": "fruit"},
        {"name": "orange", "plural": "oranges", "context": "fruit"},
        {"name": "book", "plural": "books", "context": "school"},
        {"name": "pencil", "plural": "pencils", "context": "school"},
        {"name": "cookie", "plural": "cookies", "context": "food"},
        {"name": "sticker", "plural": "stickers", "context": "collection"},
        {"name": "marble", "plural": "marbles", "context": "game"},
        {"name": "toy car", "plural": "toy cars", "context": "toy"},
        {"name": "doll", "plural": "dolls", "context": "toy"},
        {"name": "stamp", "plural": "stamps", "context": "collection"},
        {"name": "coin", "plural": "coins", "context": "money"},
        {"name": "flower", "plural": "flowers", "context": "garden"},
        {"name": "balloon", "plural": "balloons", "context": "party"},
        {"name": "chocolate", "plural": "chocolates", "context": "food"},
        {"name": "card", "plural": "cards", "context": "game"},
    ]
    
    # Templates for addition problems
    addition_templates = [
        "{char1} has {num1} {obj_plural}. {char2} has {num2} {obj_plural}. How many {obj_plural} do they have together?",
        "{char1} found {num1} {obj_plural}. Then {char1} found {num2} more {obj_plural}. How many {obj_plural} did {char1} find in total?",
        "There are {num1} {obj_plural} in the basket. {char1} puts {num2} more {obj_plural} in the basket. How many {obj_plural} are in the basket now?",
        "{char1} baked {num1} {obj_plural}. {char2} baked {num2} {obj_plural}. How many {obj_plural} did they bake altogether?",
        "{char1} collected {num1} {obj_plural} on Monday and {num2} {obj_plural} on Tuesday. How many {obj_plural} did {char1} collect in these two days?",
    ]
    
    # Templates for subtraction problems
    subtraction_templates = [
        "{char1} had {num_total} {obj_plural}. {char1} gave {num2} {obj_plural} to {char2}. How many {obj_plural} does {char1} have left?",
        "There were {num_total} {obj_plural} on the table. {char1} took {num2} {obj_plural}. How many {obj_plural} remain on the table?",
        "{char1} had {num_total} {obj_plural}. After giving some to {char2}, {char1} had {num1} {obj_plural} left. How many {obj_plural} did {char1} give to {char2}?",
        "{char1} had some {obj_plural}. After {char1} got {num2} more {obj_plural}, {char1} had {num_total} {obj_plural}. How many {obj_plural} did {char1} have at first?",
        "{char1} had {num_total} {obj_plural}. {num2} of them were eaten. How many {obj_plural} does {char1} have now?",
    ]
    
    dataset = []
    
    for i in range(num_problems):
        # Randomly decide if this will be addition or subtraction
        problem_type = random.choice(["addition", "subtraction"])
        
        # Pick random characters and object
        char1 = random.choice(characters)
        char2 = random.choice([c for c in characters if c != char1])
        obj = random.choice(objects)
        obj_plural = obj["plural"]
        
        if problem_type == "addition":
            # Generate two random numbers for addition
            num1 = random.randint(2, 20)
            num2 = random.randint(2, 20)
            correct_answer = num1 + num2
            
            # Convert numbers to words
            num1_word = number_to_words(num1)
            num2_word = number_to_words(num2)
            correct_answer_word = number_to_words(correct_answer)
            
            # Generate a plausible incorrect answer
            error_type = random.random()
            if error_type < 0.4:  # Small error
                incorrect_answer = correct_answer + random.choice([-2, -1, 1, 2])
            elif error_type < 0.7:  # Moderate error
                incorrect_answer = correct_answer + random.choice([-5, -4, -3, 3, 4, 5])
            else:  # Large error or operation error (using subtraction)
                incorrect_answer = random.choice([num1 - num2, num2 - num1, correct_answer + 10])
                # Ensure positive answer
                if incorrect_answer <= 0:
                    incorrect_answer = correct_answer + random.randint(3, 7)
            
            # Convert incorrect answer to words
            incorrect_answer_word = number_to_words(incorrect_answer)
            
            # Select a template and format it
            template = random.choice(addition_templates)
            problem = template.format(
                char1=char1, char2=char2, 
                num1=num1_word, num2=num2_word, 
                obj_plural=obj_plural
            )
            
            # Create the answer statements
            correct_statement = f"They have {correct_answer_word} {obj_plural} in total."
            incorrect_statement = f"They have {incorrect_answer_word} {obj_plural} in total."
            
        else:  # subtraction
            # For subtraction, we need to ensure num_total > num2 to avoid negative answers
            num2 = random.randint(2, 15)
            num1 = random.randint(2, 15)  # This will be the result for some templates
            num_total = num1 + num2
            
            correct_answer = num1  # This will be the answer for most templates
            
            # Convert numbers to words
            num1_word = number_to_words(num1)
            num2_word = number_to_words(num2)
            num_total_word = number_to_words(num_total)
            
            # Generate a plausible incorrect answer
            error_type = random.random()
            if error_type < 0.3:  # Small error
                incorrect_answer = correct_answer + random.choice([-2, -1, 1, 2])
            elif error_type < 0.5:  # Using addition instead
                incorrect_answer = num_total + num2
            elif error_type < 0.7:  # Subtracting in wrong order
                incorrect_answer = num2 - num1 if num2 > num1 else num1 - num2
            else:  # Other error
                incorrect_answer = correct_answer + random.choice([-5, -3, 3, 5])
            
            # Ensure positive answer
            if incorrect_answer <= 0:
                incorrect_answer = correct_answer + random.randint(1, 5)
            
            # Convert correct and incorrect answers to words
            correct_answer_word = number_to_words(correct_answer)
            incorrect_answer_word = number_to_words(incorrect_answer)
            
            # Select a template and format it
            template = random.choice(subtraction_templates)
            problem = template.format(
                char1=char1, char2=char2, 
                num1=num1_word, num2=num2_word, 
                num_total=num_total_word,
                obj_plural=obj_plural
            )
            
            # Create the answer statements
            if "How many remain" in problem or "have left" in problem:
                correct_statement = f"There are {correct_answer_word} {obj_plural} left."
                incorrect_statement = f"There are {incorrect_answer_word} {obj_plural} left."
            elif "did" in problem and "give" in problem:
                correct_statement = f"{char1} gave {correct_answer_word} {obj_plural} to {char2}."
                incorrect_statement = f"{char1} gave {incorrect_answer_word} {obj_plural} to {char2}."
            elif "have at first" in problem:
                correct_statement = f"{char1} had {correct_answer_word} {obj_plural} at first."
                incorrect_statement = f"{char1} had {incorrect_answer_word} {obj_plural} at first."
            else:
                correct_statement = f"{char1} has {correct_answer_word} {obj_plural} now."
                incorrect_statement = f"{char1} has {incorrect_answer_word} {obj_plural} now."
        
        # Add to dataset
        problem_data = {
            "type": problem_type,
            "problem": problem,
            "correct_statement": correct_statement,
            "incorrect_statement": incorrect_statement
        }
        
        if problem_type == "addition":
            problem_data.update({
                "num1": num1,
                "num2": num2,
                "correct_answer": correct_answer,
                "incorrect_answer": incorrect_answer
            })
        else:  # subtraction
            problem_data.update({
                "num_total": num_total,
                "num2": num2,
                "correct_answer": correct_answer,
                "incorrect_answer": incorrect_answer
            })
        
        dataset.append(problem_data)
    
    return dataset

# Generate the dataset
word_problems = generate_word_problems(400)  # Generate 50 word problems

# Save to JSON file
with open('word_problems_dataset.json', 'w') as f:
    json.dump(word_problems, f, indent=2)

print(f"Generated {len(word_problems)} word problems")

# No external libraries needed