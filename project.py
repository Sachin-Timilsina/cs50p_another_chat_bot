import sys
import random
from keyword_list import KeywordList, ResponseList

def main():
    print("> Hello, I am Eliza. I'll be your therapist today.")
    previous_input = None
    count = 0
    while True:
        # If forcefully quit
        try:
            user_input = input("* ").strip().lower()
        except KeyboardInterrupt:
            print()
            sys.exit("> See you later")
        # If same input twice 
        if previous_input == user_input:
            count += 1
        if count > 1:    
            print("> Do you really expect a different answer if you keep repeating yourself?")
            count = 0
            continue
        # If quit
        if user_input in ['exit', 'quit']:
            print("> See you later")
            break
        output_txt = get_response(user_input)
        print(f"> {output_txt}")
        # Set Previous Input
        previous_input = user_input


def get_response(user_input) -> str: 
    split_input = user_input.split(" ")
    if 'hello' in split_input:
        return 'Formalities aside. Talk more about yourself!'

    extracted_keywords = extract_keywords(user_input)
    return generate_response(extracted_keywords, user_input)

def extract_keywords(user_input: str):
    # All list combined
    all_keywords = KeywordList.personal_pronouns_list +\
        KeywordList.emotions_list + KeywordList.relationship_list +\
        KeywordList.well_being_list + KeywordList.negation_list +\
        KeywordList.time_keyword_list + KeywordList.common_verb_list
    all_keywords.append('am')

    # Tokanize or Split the words
    user_input = user_input.split(' ')
    extracted_keywords = []
    # Check if the sentence contains the words in keyword_list and append
    for word in user_input:
        if word in all_keywords:
            extracted_keywords.append(word)
    return extracted_keywords

def generate_response(keywords: list, user_input: str): 
    response_list = []
    
    if user_input == 'i love you' or user_input == 'love you':
        return "I am flattered!"

    # Combined response
    all_responses = {}
    all_responses.update(ResponseList.emotion_based_response)
    all_responses.update(ResponseList.negation_responses)
    all_responses.update(ResponseList.relationship_responses)
    all_responses.update(ResponseList.well_being_responses)
    all_responses.update(ResponseList.time_keyword_responses)
    all_responses.update(ResponseList.verb_responses)

    # Provide the correct response for different keywords
    for keyword in keywords:
        if keyword in all_responses:
            #Randomly select response if keyword matches
            response_list.append(random.choice(all_responses[keyword]))

    # Reflective response
    if 'am' in keywords:
        response_list.append('Why do you think you are?')
    
    # Check if it contains pronouns
    for word in keywords:
        if 'am' in keywords:
            break
        if word in KeywordList.personal_pronouns_list:
            # Switch pronoun
            pronouns_switched = switch_pronouns(user_input)
            response_list.append(f'Elaborate on why {pronouns_switched}?')
            break
    
    if response_list == []:
        return 'Tell me more about that.'
    else:
        response = ' '.join(response_list)
        return response

# Function to switch pronouns
def switch_pronouns(user_input: str) -> str: 
    words = user_input.split(' ')
    match_words = []
    for word in words:
        if word in KeywordList.personal_pronouns_map:
            match_words.append(KeywordList.personal_pronouns_map[word])
        else:
            match_words.append(word)
    joined_mapped_words = " ".join(match_words)
    return joined_mapped_words

if __name__ == "__main__":
    main()
