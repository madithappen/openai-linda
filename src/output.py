# Import the pyttsx3 library
import pyttsx3


class LindaOutput:
    """
    The LindaOutput Class
    
    Current outputs:
    - speak
    - stdout

    """

    def __init__(self, speak=True, stdout=True):

        """Initialize the base class."""
        if speak:
            # Initialize the text-to-speech engine
            self.engine = pyttsx3.init()

            # Get the available voices
            self.voices = self.engine.getProperty('voices')

            # Set the voice to "Linda"
            self.engine.setProperty('voice', self.voices[1].id)
            self.engine.setProperty('rate', 160)


        if stdout:
            pass


    # This function speaks the given string using the text-to-speech engine.
    # If the string contains the substring "Traceback (most recent call last)", it will not be spoken.
    def speak(self, string: str) -> None:
        """
        Linda's voice providing the answer to life's problems.
        
        Args:
            string (str): The string to be spoken by Linda.
        """

        # Speak the string using the text-to-speech engine
        if "Traceback (most recent call last)" not in string:
            self.engine.say(string)
            self.engine.runAndWait()


    # This function prints the given string to the standard output.
    def stdout(self, string: str) -> None:
        """
        Print the given string to the standard output.
        
        Args:
            string (str): The string to be printed.
        """
        print(string)
        print("")


# If this script is run directly, call the 'speak()' and 'stdout()' functions and pass them the string "Hello, world! How are you doing today?".
if __name__== '__main__':
    import argparse
    
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser()

    # Add the 'stdin' and 'speak' arguments to the parser
    parser.add_argument("--stdout",  action="store_true",   help="Give output in the form of standard out")
    parser.add_argument("--speak",    action="store_true",   help="Give output in the form of voice")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Instantiate LindaOutput class
    out = LindaOutput()

    # Check if the 'stdin' or 'speak' arguments were provided
    if args.stdout:
        out.stdout("Hello, world! How are you doing today?")

    if args.speak:
        # Accept input by speaking
        out.speak("Hello, world! How are you doing today?")
    
    if not args.stdout and not args.speak:
        # No input method was specified, so raise an error
        print("You must specify either 'stdout', 'speak', or both. Exiting script")
        parser.print_help()
        exit(1)