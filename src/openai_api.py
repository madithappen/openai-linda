# Import the OpenAI library
import openai
import os

class LindaOpenAI:
    """
    The LindaOpenAI Class
    
    Current Function:models:
    - Completion:text-davinci-003

    """

    def __init__(self):
        self.model = "text-davinci-003"
        openai.api_key = os.getenv("OPENAI_API_KEY") or ""
        
    # This function asks a question to the OpenAI API using the given prompt and returns the answer.
    def ask_openai(self, prompt: str) -> str:
        """
        Ask a question to the OpenAI API and return the answer.
        
        Args:
            prompt (str): The question to be asked.
        
        Returns:
            str: The answer provided by the OpenAI API.
        """
        completions = openai.Completion.create(
            model=self.model,
            prompt=prompt,
            max_tokens=250,
            n=1,
            temperature=0.5,
        )
        response = completions.choices[0].text
        return response



# If this script is run directly, ask the question "Who won the world series in 1985?" to the OpenAI API and print the answer.
if __name__ == '__main__':
    import argparse
    
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser()

    # Add the 'stdin' and 'speak' arguments to the parser
    parser.add_argument("--text",  action="store",   help="Accept input from arg")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Initialize Input Class
    api = LindaOpenAI()

    # Check if the 'stdin' or 'speak' arguments were provided
    if args.text:
        query = args.text
    else:
        query = "Who won the World Series in 1985?"

    
    answer = api.ask_openai(query)
    print(answer)
