class KeywordList():
    # List of keywords to extract
    personal_pronouns_list = [
        "i",
        "me",
        "my",
        "you",
        "your",
        "we",
        "us",
        "they",
    ]
    personal_pronouns_map = {
        "i": "you",
        "me": "you",
        "my": "your",
        "you": "I",
        "your": "my",
        "we": "you",
        "us": "you",
        "they": "them",
    }
    emotions_list = [
        "happy",
        "sad",
        "angry",
        "afraid",
        "anxious",
        "excited",
        "worried",
        "depressed",
        "love",
        "hate",
        "lonely",
    ]
    relationship_list = [
        "mother",
        "father",
        "sister",
        "brother",
        "friend",
        "husband",
        "wife",
        "partner",
    ]
    well_being_list = [
        "tired",
        "sick",
        "pain",
        "healthy",
        "stress",
        "ill",
        "weak",
        "strong",
    ]
    time_keyword_list = [
        "always",
        "never",
        "yesterday",
        "today",
        "tomorrow",
        "now",
        "soon",
        "later",
    ]
    negation_list = [
        "no",
        "not",
        "never",
        "don't",
        "can't",
        "won't",
        "isn't",
        "aren't",
    ]
    common_verb_list = [
        "want",
        "need",
        "feel",
        "think",
        "believe",
        "hope",
        "wish",
        "hate",
    ]

class ResponseList():
    # Emotion based responses
    emotion_based_response = {
        "sad": [
            "I'm really sorry to hear that you are sad. What's going on?",
            "Why are you sad nowadays?",
            "Sadness is tough. What do you think is causing it?"
        ],
        "happy": [
            "That's amazing! What's making you happy?",
            "I'm glad you're happy! Why is it?",
            "Something good happened? What's the reason?"
        ],
        "angry": [
            "Anger can be devastating! What's the reason?",
            "What's causing your anger?",
        ],
        "afraid": [
            "What are you afraid of?",
            "Begin afraid is natural. What are you afraid of?",
            "What makes you afraid?"
        ],
        "anxious": [
            "What's making you feel anxious?",
            "Anxiety can be difficult to manage. What's causing it for you?",
            "Is there a particular reason you're feeling anxious?"
        ],
        "excited": [
            "That's great! What's got you feeling excited?",
            "Tell me more about your excitement!",
            "Excitement is fun! Why are you excited"
        ],
        "worried": [
            "Why worry so much?",
            "Tell me why you are worried?",
            "If you like I can listen to your worries."
        ],
        "depressed": [
            "I'm sorry. Why are you depressed?",
            "It is a difficult situation. Do you wanna talk about it?",
            "Depression is hard. Do you want to talk about it?"
        ],
        "love": [
            "Love is a powerful emotion. Tell me more about this.",
            "Love is beautiful. What makes you love about this person?",
            "Love is blinding. What the reason for your love?"
        ],
        "hate": [
            "Hate is a strong feeling. Can you explain what's causing this?",
            "Why do you feel such hatred?",
            "What’s driving your hatred right now?"
        ],
        "lonely": [
            "Loneliness is hard. Do you feel this way often?",
            "What's causing you lonliness?",
            "Why do you think you feel lonely?"
        ]
    }
    # Relationship-based responses
    relationship_responses = {
        "mother": [
            "How do you feel about your mother?",
            "What's your relationship with her like?",
            "Is something bothering you about her?"
        ],
        "father": [
            "Tell me more about your relationship with your father.",
            "Is there something specific you'd like to discuss about him?",
            "What's your father like?"
        ],
        "sister": [
            "How's your relationship with your sister?",
            "Is there something specific you'd like to talk about?",
            "What role does your sister play in your life?"
        ],
        "brother": [
            "Tell me more about your brother.",
            "Do you get along well with him?",
            "Is there something you'd like to share about him?"
        ],
        "girlfriend": [
            "How are things going with your girlfriend?",
            "Would you like to talk more about her?",
            "What's your relationship with her like?"
        ]
    }

    # Well-being based responses
    well_being_responses = {
        "tired": [
            "You seem tired. Are you resting enough?",
            "What's been wearing you out?",
            "Why do you think you're so tired?"
        ],
        "sick": [
            "I'm sorry you're unwell. What's going on?",
            "Being sick is hard. How long has this been?",
            "Do you think you need medical help?"
        ],
        "pain": [
            "Where are you feeling pain?",
            "Can you describe the pain you're having?",
            "How long have you felt this pain?"
        ],
        "healthy": [
            "It's great you're feeling healthy!",
            "What's helping you stay healthy?",
            "How do you take care of your well-being?"
        ]
    }

    # Time-related responses
    time_keyword_responses = {
        "always": [
            "Why do you feel this always happens?",
            "What makes this a constant issue?",
            "Does this happen often?"
        ],
        "never": [
            "Why do you feel this never happens?",
            "What's stopping it from happening?",
            "Why do you think it never occurs?"
        ],
        "yesterday": [
            "What happened yesterday?",
            "Tell me more about it.",
            "Was yesterday important to you?"
        ]
    }

    # Negation-based responses
    negation_responses = {
        "no": [
            "Why did you say no?",
            "What's making you disagree?",
            "Can you explain why you said no?"
        ],
        "not": [
            "Why do you think it's not true?",
            "What's making you feel that way?",
            "Can you explain why it's not happening?"
        ]
    }

    # Common verb-based responses
    verb_responses = {
        "want": [
            "What do you want?",
            "What are you seeking?",
            "Why do you want that?"
        ],
        "need": [
            "What do you need?",
            "Why do you feel you need it?",
            "Can you explain why you need this?"
        ],
        "feel": [
            "How do you feel about this?",
            "Can you describe your feelings?",
            "Tell me more about how you're feeling."
        ]
    }

