from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as palm

app = Flask(__name__)
CORS(app)

import json

# Configure the generative AI with your API key
palm.configure(api_key='AIzaSyA-uP7sDjeao6hta53e6U7wECV1dy_iEO8')

def extract_and_parse_json(input_string):
    # Find the first '[' character
    start_index = input_string.find('[')
    
    # Find the last ']' character
    end_index = input_string.rfind(']')
    
    # Check if '[' and ']' were found
    if start_index != -1 and end_index != -1:
        # Extract the substring between '[' and ']'
        json_string = input_string[start_index:end_index+1]
        print("####################START######################")
        print(json_string)
        print("####################END######################")
        # Parse the extracted JSON string into a list
        parsed_json = json.loads(json_string)
        return parsed_json
    
    # Return None if '[' and ']' were not found or if there was an error
    return ""

@app.route('/generate_quiz', methods=['POST'])
def generate_quiz():
    # Get the data from the request
    data = request.get_json()

    # Extract quiz_topic and no_of_questions from the JSON data
    quiz_topic = data.get('quiz_topic')
    no_of_questions = data.get('no_of_questions')
    try:
        # quiz_topic = request.form.get('quiz_topic')
        # no_of_questions = int(request.form.get('no_of_questions'))
        # print("Generated Question Hitted")
        # print(quiz_topic)
        # print(no_of_questions)

        # # Generate the prompt based on user input
        prompt = f"""Generate Quiz for {quiz_topic} in following JSON json_format . And Generate {no_of_questions} question in JSON list. Format is given below
        json_format :```{{
        "quizQuestion": <quiz Question>,
        "option_1": <Option 1>,
        "option_2": <Option 2>,
        "option_3": <Option 3>,
        "option_4": <Option 4>,
        "correctAns": <Correct Option Number in integer format>,
        "quizTopic": <user provided quiz_topic>
        }}```

        Don't include any other string in response only give me JSON data. Make sure you follow standard convention to generate JSON response.Ensure String key and value is there in double quotes.
        """ 

        # Create a new conversation
        response = palm.chat(messages=prompt)

        # Extract the last response from the model
        generated_quiz = response.last
    
        # print(generated_quiz)

        extracted_json = extract_and_parse_json(generated_quiz)
        return extracted_json
        
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
