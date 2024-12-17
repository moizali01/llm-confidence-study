import json
import csv

def convert_json_to_csv(input_file, output_file):
    # Read JSON data
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    # Open CSV file for writing
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Write header
        writer.writerow(['generated', 'log_probs', 'linear_probs', 'correct_answer'])
        
        # Process each entry
        for entry in data:
            # Find the correct_answer key (it will be in format correct_answer_i)
            correct_answer_key = next(key for key in entry.keys() if key.startswith('correct_answer_'))
            correct_answer = entry[correct_answer_key]
            
            # Get the token data (first token since there's only one per entry)
            token_data = entry['tokens'][0]
            
            # Write the row
            writer.writerow([
                token_data['generated_token'],
                token_data['log_probability'],
                token_data['linear_probability'],
                correct_answer
            ])

# Usage
input_file = 'gpt_logprob_Science_position.json'
output_file = 'gpt_logprob_Science_position.csv'

try:
    convert_json_to_csv(input_file, output_file)
    print(f"Successfully converted {input_file} to {output_file}")
except Exception as e:
    print(f"An error occurred: {str(e)}")
