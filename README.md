# Canvas-to-Quizlet

Converts an HTML file of a completed Canvas quiz to a Quizlet flashcard set. 

This project was made because I didn't want to spend 8 minutes typing my jazz quiz into quizlet so instead I spent 2 hours writing code to do it for me

## Usage
You should begin with a completed Canvas quiz:

Hit Ctrl-S to save the html file of the quiz. Run the script, `beautiful-soup.py`, and when prompted paste the location of the quiz .html file into the Python console. Then paste the location of the desired output .txt file -- if none exists, one will be created. 

Copy the entirety of the .txt file and import into Quizlet by creating a new set and selecting "+ Import" pasting, and changing to "Comma" and "Semicolon".

## Notes
* Will only use your answer for the quiz, EVEN IF IT IS INCORRECT
* Questions containing an image or table will be removed since Quizlet does not allow them to be imported

Original idea and base model taken from https://github.com/nhend/canvas-to-quizlet (Basically nothing is even close to the same)
