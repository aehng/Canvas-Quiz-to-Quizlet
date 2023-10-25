from bs4 import BeautifulSoup

def clean_text(text):
    # Remove commas and semicolons from the text
    cleaned_text = text.replace(",", "").replace(";", "")
    return cleaned_text

def convert(file_content: str) -> dict:
    '''
    Given a string-ified HTML file, use Beautiful Soup to extract questions and their respective correct answers.
    Clean and return a dict of Q&A pairs
    '''
    soup = BeautifulSoup(file_content, 'html.parser')
    questions = []
    answers = []

    # Find all input elements with type "checkbox" and the "checked" attribute
    checkbox_elements = soup.find_all('input', {'type': 'checkbox', 'checked': True})

    for checkbox in checkbox_elements:
        # Extract the associated answer text and clean it
        answer_text = clean_text(checkbox.find_next('div', class_='answer_text').get_text())
        
        # Extract the associated question text (if available) and clean it
        question = checkbox.find_previous('div', class_='question_text')
        if question:
            question_text = clean_text(question.get_text())
        else:
            question_text = None
        
        questions.append(question_text)
        answers.append(answer_text)

    # Find all input elements with type "radio" and the "checked" attribute
    radio_elements = soup.find_all('input', {'type': 'radio', 'checked': True})

    for radio in radio_elements:
        # Extract the associated answer text and clean it
        answer_text = clean_text(radio.find_next('div', class_='answer_text').get_text())
        
        # Extract the associated question text (if available) and clean it
        question = radio.find_previous('div', class_='question_text')
        if question:
            question_text = clean_text(question.get_text())
        else:
            question_text = None
        
        questions.append(question_text)
        answers.append(answer_text)
    
    # Find question and answer pairs in the new form
    matching_answer_elements = soup.find_all('select')

    for element in matching_answer_elements:
        # Extract the associated answer text and clean it
        answer_text = clean_text(element.find_next('option').get_text())
        
        # Extract the associated question text (if available) and clean it
        question = element.find_previous('div', class_='answer_match_left')
        if question:
            question_text = clean_text(question.get_text())
        else:
            question_text = None
        questions.append(question_text)
        answers.append(answer_text)

    # Create a dictionary of Q&A pairs
    pairs = {}

    for question, answer in zip(questions, answers):
        if question is not None:
            if question in pairs:
                pairs[question] += f" & {answer}"
            else:
                pairs[question] = answer

    return pairs

def write_pairs(pairs: dict, location: str):
    '''Writes question-and-answer pairs to a text file in the Quizlet tab-separated format'''
    with open(location, 'w', encoding="utf8") as f:
        for key in pairs.keys():
            f.write(f"{key},{pairs[key]};")

def main():
    '''Program driver for user input and instructions'''
    in_location = input("Please enter the address and/or name of your input HTML file.\n" + "WSL ~ Example - /mnt/c/Users/elijk/OneDrive - USU/Saving-Storage/Random/canvas-to-quizlet/Jazz/Quiz1.html \n" + "NOT WSL ~ Example - C:\\Users\\elijk\\OneDrive - USU\\Saving-Storage\\Random\\canvas-to-quizlet\\Jazz\\Quiz1.html \n")

    out_location = input("Please enter the address and/or name of your output txt file.\n" + "WSL ~ Example - /mnt/c/Users/elijk/OneDrive - USU/Saving-Storage/Random/canvas-to-quizlet/Jazz/Quiz1_Quizlet.txt \n" + "NOT WSL ~ Example - C:\\Users\\elijk\\OneDrive - USU\\Saving-Storage\\Random\\canvas-to-quizlet\\Jazz\\Quiz1_Quizlet.txt \n")

    with open(in_location, "r", encoding="utf8") as file:
        file_content = file.read()

    pairs = convert(file_content)
    write_pairs(pairs, out_location)

    print(f'Flashcards written to {out_location}. To import into Quizlet:')
    print('1. Create a new set')
    print('2. Click "+ Import from Word, Excel, Google Docs, etc."')
    print('3. Paste the entirety of the text file into the box and hit "Import".')
    print('Happy studying!')

if __name__ == "__main__":
    main()
