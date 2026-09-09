# Code Reviewer

An AI-powered code analysis tool that provides comprehensive code reviews, explanations, and optimization suggestions.

## Features

- 🔍 **Code Analysis**: Automatically detects programming languages and analyzes code structure
- 📝 **Simple Explanations**: Breaks down complex code into easy-to-understand descriptions
- ⏱️ **Complexity Analysis**: Provides Big-O time and space complexity analysis
- ⚠️ **Issue Detection**: Identifies potential bugs, errors, and problems in code
- 💡 **Improvement Suggestions**: Offers recommendations for code quality, performance, and readability
- 🚀 **Code Optimization**: Generates optimized versions of your code
- 🌐 **Web Interface**: User-friendly Streamlit UI for easy code analysis

## Tech Stack

- **Streamlit**: Web interface framework
- **LangChain**: AI/LLM framework for prompt engineering
- **Groq**: High-performance AI model inference
- **Pydantic**: Data validation and structured output

## Installation

1. Clone the repository:
```bash
git clone https://github.com/STTRLORD/code_reviewer.git
cd code_reviewer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

## Usage

### Web Interface (Recommended)

Run the Streamlit UI:
```bash
streamlit run ui.py
```

The application will open in your browser at `http://localhost:8501`

### Command Line Interface

Run the command-line version:
```bash
python app.py
```

Then paste your code when prompted.

## Project Structure

```
code_reviewer/
├── app.py              # Command-line interface
├── ui.py               # Streamlit web interface
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not tracked)
├── .gitignore         # Git ignore rules
└── README.md          # Project documentation
```

## API Key Setup

To use this application, you need a Groq API key:

1. Sign up at [Groq Console](https://console.groq.com/)
2. Create an API key
3. Add it to your `.env` file:
```
GROQ_API_KEY=gsk_your_api_key_here
```

## Example Output

The analyzer provides:
- **Language Detection**: Identifies the programming language used
- **Code Explanation**: Simple, clear description of functionality
- **Time Complexity**: Big-O notation for algorithmic efficiency
- **Space Complexity**: Memory usage analysis
- **Issues**: List of bugs or potential problems
- **Improvements**: Suggestions for better code quality
- **Optimized Code**: Improved version of your code

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [LangChain](https://langchain.com/)
- AI inference by [Groq](https://groq.com/)
