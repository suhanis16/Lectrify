import spacy  

nlp = spacy.load("en_core_web_sm")

# Input text
input_text = "Mahatma Gandhi also known as Father of the nation played a very important role in the freedom of India. He started various movements against the Britishers like Non-Cooperation Movement, Civil Disobedience Movement, Swaraj, and Quit-India movement and Salt Satyagrah."

# Process input text
doc = nlp(input_text)

# Define question templates
question_templates = [
    "Can you tell me more about {}?",
    "What impact did {} have on people?",
    "How did {} contribute to the freedom of India?",
]

# Identify named entities
named_entities = [entity.text for entity in doc.ents]

# Generate follow-up questions
questions = []
for template in question_templates:
    for entity in named_entities:
        question = template.format(entity)
        questions.append(question)

# Print generated questions
for question in questions:
    print(question)
