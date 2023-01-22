import argparse
import time
import sys

sys.path.append('./src')
import openai_api
import input
import output


class ListenLinda:
    def __init__(self, mic=False, stdin=True, speak=True, stdout=True):
        self.mic = mic
        self.stdin = stdin
        self.speak = speak
        self.stdout = stdout

        # Ensure the proper flags are set
        if self.stdin and self.mic:
            print("Only one (self.stdin or self.mic) must be True")
            exit(1)
        if not self.stdin and not self.mic:
            print("Either self.mic or self.stdin must be True")
            exit(1)

        self.api = openai_api.LindaOpenAI()
        self.input = input.LindaInput(mic=self.mic, stdin=self.stdin)
        self.output = output.LindaOutput(speak=self.speak, stdout=self.stdout)
        

    def _match_phrases(self, test_input: str, expected_output: list()) -> list:
        print(f'test_input: {test_input}')
        print(f'expected_output: {expected_output}')
        matches = [phrase for phrase in expected_output if phrase.lower() in test_input.lower()]
        print(f'matches: {matches}')
        return matches

    def _exit_if_asked(self, input_string) -> None:
        # Exit program on keyword
        exit_keywords = ['exit the linda program', 'exit the program', 'exit program']
        matches = self._match_phrases(input_string, exit_keywords)
        if matches:
            self.output.speak(f"Okay, I will {matches[0]}")
            exit(1)
    

    def _keyword_trigger(self, input_string) -> bool:
        # Trigger Command on keyword
        trigger_keywords = ['linda', 'listen linda', 'morning linda', 'okday linda', 'christine', 'ai overlord']
        return self._match_phrases(input_string, trigger_keywords)
        

    def run(self) -> None:
        while(True):
            # Gather Input
            input_string = ""
            if self.stdin:
                input_string = self.input.get_string_from_stdin()
            elif self.mic:
                input_string = self.input.get_string_from_mic()

            # Exit application if asked via input_string
            self._exit_if_asked(input_string)

            # Query OpenAI
            output_string = ""
            if self.stdin:
                output_string = self.api.ask_openai(input_string)
            elif self.mic:
                trigger = self._keyword_trigger(input_string)
                if trigger:
                    # Chop off key word before submitting to OpenAI
                    input_string = input_string.split(trigger[0])[-1]
                    # Provide the input_string to open_ai to gather a response as a string and return it
                    output_string = self.api.ask_openai(input_string)

            # Output openai response
            if self.stdout:
                self.output.stdout(output_string)
            if self.speak:
                self.output.speak(output_string)                                 

            # Sleep before starting new loop
            time.sleep(0.1)


if __name__ == '__main__':
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser()

    # Add the 'stdin' and 'speak' arguments to the parser
    parser.add_argument("--stdin",  action="store_true", help="Accept input from stdin")
    parser.add_argument("--mic",    action="store_true", help="Accept input from speaking")
    parser.add_argument("--stdout", action="store_true", help="Send output to stdout")
    parser.add_argument("--speak",  action="store_true", help="Send output to your speakers as the voice of Linda")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Check if either 'stdin' or 'mic' was specified, but not both
    if args.stdin and args.mic:
        print("You cannot specify both the 'stdin' and 'mic' arguments")
        parser.print_help()
        exit(1)
    elif not args.stdin and not args.mic:
        print("You must specify either the 'stdin' or 'mic' arguments")
        parser.print_help()
        exit(1)

    # Check if either 'stdout' or 'speak' was specified, but not both
    if not args.stdout and not args.speak:
        print("You must specify either the 'stdout' or 'speak' arguments")
        parser.print_help()
        exit(1)

    linda = ListenLinda(
        mic=args.mic if args.mic else False, 
        stdin=args.stdin if args.stdin else False, 
        speak=args.speak if args.speak else False, 
        stdout=args.stdout if args.stdout else False
    )
    linda.run()
