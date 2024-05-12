
# Generative AI Q&A ChatBot

Generative AI Q&A is a simple application built with Python's Tkinter library and utilizes OpenAI's GPT-3 model via the Eden AI API to generate questions and evaluate user answers.

## Features

- **Question Generation**: Automatically generates basic questions related to selected topics.
- **Answer Evaluation**: Allows users to submit answers and provides feedback on correctness.
- **Topic Selection**: Provides a dropdown menu to choose from different topics such as Geography, Health, and Sports.
- **User Interface**: Simple and intuitive GUI for easy interaction.

## How to Use

1. **Topic Selection**: Choose a topic from the dropdown menu.
2. **Generated Question**: Once a topic is selected, a question related to that topic will be automatically generated.
3. **Answer Submission**: Enter your answer in the provided field and click the "Submit" button.
4. **Feedback**: Receive immediate feedback on whether your answer is correct or not.

## Requirements

- Python 3.x
- Tkinter library
- Requests library
- Eden AI API key

## Installation

1. Clone this repository:
   ```bash
   git clone [https://github.com/your_username/generative-ai-qa.git](https://github.com/Parimal07/Basic-QnA-ChatBot-using-text-davinci-002-LLM-Model.git)
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Obtain an API key from [Eden AI](https://www.edenai.co) and replace `YOUR_API_KEY` in the code with your actual API key.

## Usage

Run the application by executing the following command:
```bash
python main.py
```

## Acknowledgements

- OpenAI for providing the GPT-3 model.
- Eden AI for providing access to the GPT-3 model via their API.
