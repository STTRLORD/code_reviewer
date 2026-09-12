# Code Reviewer

[![Live Demo](https://code-reviewer-zsw8.onrender.com)](https://code-reviewer-zsw8.onrender.com)

An AI-powered code analysis tool that provides comprehensive code reviews, explanations, and optimization suggestions. Paste your code and get instant feedback on logic, complexity, potential issues, and improvement suggestions.

## ✨ Features

- 🔍 **Smart Code Analysis**: Automatically detects programming languages and analyzes code structure
- 📝 **Clear Explanations**: Breaks down complex code into easy-to-understand descriptions
- ⏱️ **Complexity Analysis**: Provides Big-O time and space complexity analysis
- ⚠️ **Issue Detection**: Identifies potential bugs, errors, and problems in code
- 💡 **Improvement Suggestions**: Offers recommendations for code quality, performance, and readability
- 🚀 **Code Optimization**: Generates optimized versions of your code
- 🌐 **Modern Web Interface**: User-friendly Streamlit UI with dark theme and responsive design
- ⚡ **Fast AI Processing**: Powered by Groq's high-performance AI inference
- 🎨 **Beautiful UI**: Clean, modern interface with skeleton loading states and smooth animations

## 🛠️ Tech Stack

- **Streamlit**: Modern web interface framework for building interactive Python applications
- **LangChain**: Powerful AI/LLM framework for prompt engineering and structured output
- **Groq**: Ultra-fast AI model inference with low latency
- **Pydantic**: Data validation and structured output parsing
- **Python 3.8+**: Core programming language

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Groq API key (free sign-up required)

### Step 1: Clone the repository
```bash
git clone https://github.com/STTRLORD/code_reviewer.git
cd code_reviewer
```

### Step 2: Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set up environment variables
Create a `.env` file in the project root with your Groq API key:
```bash
GROQ_API_KEY=your_api_key_here
```

You can get a free API key from [Groq Console](https://console.groq.com/)

## 💻 Usage

### Web Interface (Recommended)

Start the Streamlit application:
```bash
streamlit run ui.py
```

The application will open in your browser at `http://localhost:8501`

**How to use:**
1. Paste your code into the text area
2. Click "Review code" button
3. View the comprehensive analysis including:
   - Detected programming language
   - Time and space complexity
   - Code explanation
   - Identified issues
   - Improvement suggestions
   - Optimized code version

### Command Line Interface

For terminal-based code analysis:
```bash
python app.py
```

Follow the prompts to paste your code and receive the analysis directly in your terminal.

## 📁 Project Structure

```
code_reviewer/
├── app.py              # Command-line interface implementation
├── ui.py               # Streamlit web interface with modern UI
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not tracked in git)
├── .gitignore         # Git ignore rules
└── README.md          # Project documentation
```

### Key Components

- **ui.py**: Main Streamlit application with custom CSS, dark theme, and responsive design
- **app.py**: Alternative CLI version for terminal-based code analysis
- **requirements.txt**: All necessary Python packages for the project

## 🔑 API Key Setup

This application uses Groq's high-performance AI models for code analysis. You'll need a free API key:

### Getting Your Groq API Key

1. Visit [Groq Console](https://console.groq.com/)
2. Sign up for a free account (no credit card required)
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key and add it to your `.env` file:

```bash
GROQ_API_KEY=gsk_your_actual_api_key_here
```

**Note:** Never commit your `.env` file to version control. It's already included in `.gitignore`.

## 📊 Example Output

When you analyze code, the tool provides comprehensive feedback:

### Sample Analysis
**Input Code:**
```python
def find_max(arr):
    max_val = arr[0]
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val
```

**Output:**
- **Language**: Python
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)
- **Explanation**: Iterates through array to find maximum value
- **Issues**: None detected
- **Improvements**: Consider using built-in `max()` function for better performance
- **Optimized Code**: `return max(arr) if arr else None`

### What You Get
- **Language Detection**: Identifies the programming language used
- **Code Explanation**: Simple, clear description of functionality
- **Time Complexity**: Big-O notation for algorithmic efficiency
- **Space Complexity**: Memory usage analysis
- **Issues**: List of bugs, potential problems, or anti-patterns
- **Improvements**: Suggestions for better code quality and performance
- **Optimized Code**: Improved version of your code with best practices

## 🌐 Deployment

### Deploy to Render (Recommended)

The live demo is deployed on Render. To deploy your own instance:

1. Fork this repository
2. Create a new account on [Render](https://render.com/)
3. Connect your GitHub repository
4. Add your `GROQ_API_KEY` as an environment variable in Render settings
5. Deploy as a Web Service with the following build command:
   ```bash
   pip install -r requirements.txt
   ```
6. Start command:
   ```bash
   streamlit run ui.py --server.port=$PORT --server.address=0.0.0.0
   ```

### Other Platforms

The app can be deployed to any platform that supports Python:
- **Streamlit Cloud**: Direct deployment from GitHub
- **Heroku**: With proper buildpacks
- **Railway**: Simple container-based deployment
- **AWS/Azure/GCP**: Using container services

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Improvement
- Support for more programming languages
- Additional AI models integration
- Enhanced code visualization
- Batch code analysis
- Code comparison features
- Export analysis results (PDF, JSON, etc.)

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **[Streamlit](https://streamlit.io/)** - Modern web framework for data apps
- **[LangChain](https://langchain.com/)** - Powerful framework for AI applications
- **[Groq](https://groq.com/)** - Ultra-fast AI inference platform
- **[Pydantic](https://pydantic-docs.helpmanual.io/)** - Data validation using Python type annotations

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the documentation

## 🌟 Star History

If you find this project helpful, please consider giving it a star on GitHub!

---

**Built with ❤️ using modern AI technologies**
