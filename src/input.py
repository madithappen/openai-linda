# Import the SpeechRecognition library and alias it as 'sr'
import speech_recognition as sr
import re

class LindaInput:
    """
    The LindaInput Class
    
    Current inputs:
    - mic
    - stdin

    """

    def __init__(self, mic=True, stdin=False):

        """Initialize the base class."""
        if mic:
            # Create a Recognizer object
            self.r = sr.Recognizer()

            # Set the pause threshold to 1.0 seconds
            self.r.pause_threshold = 0.5

        if stdin:
            pass

    def _strip_special_chars(self, string: str) -> str:
        """
        Remove special characters from the given string.
        
        Args:
            string (str): The string to be stripped of special characters.
        
        Returns:
            str: The string with the special characters removed.
        """
        # Use a regular expression to remove special characters
        return re.sub(r"[^A-Za-z0-9 ]+", "", string)


    def get_string_from_mic(self) -> str:
        """
        Listen to the microphone, transcribe the recorded audio using the Google Speech Recognition API, and return the transcribed text as a string.
        If there is an error during transcription, return an empty string.
        """
        # Listen to the microphone and store the recorded audio in a variable
        with sr.Microphone() as source:
            print("Speak now:")
            audio = self.r.listen(source)

        try:
            # Use the Google Speech Recognition API to transcribe the recorded audio
            text = self.r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Could not understand audio")
            return ""
        except sr.RequestError as e:
            print(f"Error making request: {e}")
            return ""


    def get_string_from_stdin(self) -> str:
        """
        Listen to the microphone, transcribe the recorded audio using the Google Speech Recognition API, and return the transcribed text as a string.
        If there is an error during transcription, return an empty string.
        """
        # Prompt the user for input
        value = input("Enter Input: ")
        value = self._strip_special_chars(value)

        # Return value
        return value


# If this script is run directly, call the 'get_string_from_mic()' function and print the result.
if __name__== '__main__':
    import argparse
    
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser()

    # Add the 'stdin' and 'speak' arguments to the parser
    parser.add_argument("--stdin",  action="store_true",   help="Accept input from stdin")
    parser.add_argument("--mic",    action="store_true",   help="Accept input by speaking")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Initialize Input Class
    ins = LindaInput()

    # Check if the 'stdin' or 'speak' arguments were provided
    if args.stdin:
        # Accept input from stdin
        value = ins.get_string_from_stdin()
    elif args.mic:
        # Accept input by speaking
        value = ins.get_string_from_mic()
    else:
        # No input method was specified, so raise an error
        print("You must specify either the 'stdin' or 'mic' argument. Exiting script")
        parser.print_help()
        exit(1)

    print(value)
