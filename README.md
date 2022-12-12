# openai-linda
Listen Linda is a Python3 program for interacting with OpenAI. It accepts input via microphone or stdin and outputs responses via text-to-speech or stdout.

## Requirements
- Python3
- pip3
- A valid API key for OpenAI

## Installation
Clone this repository to your local machine using `git clone https://github.com/madithappen/listen-linda.git`

Navigate to the cloned repository using `cd listen-linda`
Install the required Python packages using `pip3 install -r requirements.txt`

Create a `.env` file in the project root and add the following line: `OPENAI_SECRET_KEY=<your-openai-secret-key>`

## Usage
To start the program, use the following command:

```python
python3 main.py [--stdin] [--mic] [--stdout] [--speak]
```

## Arguments
- `stdin`: Accept input from stdin
- `mic`: Accept input from microphone
- `stdout`: Send output to stdout
- `speak`: Send output to text-to-speech


## Examples
To accept input from stdin and send output to stdout, use the following command:

```python
python3 main.py --stdin --stdout
```


To accept input from the microphone and send output to text-to-speech, use the following command:

```python
python3 main.py --mic --speak
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.