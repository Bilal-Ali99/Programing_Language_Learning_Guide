
# Programming Language Learning Guide


A comprehensive GenAI-powered application that provides personalized learning roadmaps, daily schedules, and timelines for learning any programming language using LangChain and Google's Gemini AI.
## 🌟 Features

🗺️ Comprehensive Roadmap: Detailed learning path from basics to advanced concepts

📅 Daily Schedule: Structured daily learning plan based on your time commitment

⏱️ Timeline Estimation: Realistic timeline for achieving different proficiency levels

🎯 20+ Languages: Support for popular programming languages

🔄 Real-time Updates: Dynamic content updates when switching languages

🎨 User-friendly Interface: Clean and intuitive Streamlit interface

📱 Cross-compatible: Works with older and newer Streamlit versions
## 🚀 Supported Programming Languages

* Python, JavaScript, Java, C++, C#

* Go, Rust, TypeScript, Swift, Kotlin

* PHP, Ruby, Dart, HTML/CSS

* R, MATLAB, Scala, SQL

* C, Assembly, Bash/Shell

* Haskell, Perl, Lua
## 📋 Prerequisites

* Python 3.8 or higher
* Google Gemini API key (free from Google AI Studio)
* Internet connection for API calls
## ⚙️ Installation

1. Clone the Repository
#### bash

git clone <repository-url>

cd programming-learning-guide


2. Create Virtual Environment (Recommended)
#### bash

python -m venv .venv

### On Windows
.venv\Scripts\activate

### On macOS/Linux
source .venv/bin/activate

3. Install Dependencies

#### bash

pip install -r requirements.txt

4. Set Up Environment Variables
#### bash

### Copy the example file
cp .env.example .env

### Edit .env file and add your Gemini API key
GEMINI_API_KEY=your_actual_api_key_here

5. Get Your Gemini API Key

* Visit Google AI Studio
* Sign in with your Google account
* Create a new API key
* Copy the key and paste it in your .env file
## 🎮 Usage

### Running the Application
#### bash
streamlit run main.py

### Using the Application

1. Access the app: Open your browser and go to http://localhost:8501
2. Select language: Choose a programming language from the sidebar dropdown
3. Set preferences: 
* Choose your experience level (Complete Beginner, Some Programming Background, Experienced in Other Languages)
* Set your daily time commitment (0.5 to 8 hours)

4. Generate plan: Click "Generate Learning Plan" button
5. View results: Use the dropdown to switch between:

* 🗺️ Learning Roadmap
* 📅 Daily Schedule
* ⏱️ Timeline

### Dynamic Language Switching

* Change the language in the sidebar to automatically generate a new plan
* Results are cached for better performance
* Switch between different sections using the dropdown menu



## 📁 Project Structure


programming-learning-guide


├── main.py                 # Main Streamlit application

├── sequential_chain.py     # LangChain chains implementation

├── requirements.txt        # Python dependencies

├── .env.example           # Environment variables template

├── .env                   # Your environment variables (create this)

├── README.md             # Project documentation

└── .venv/                # Virtual environment (optional)


## 🔧 Technical Architecture


Core Components
1. Main Application (main.py)

* Streamlit UI: Clean, responsive interface with sidebar navigation
* Session State Management: Caches results and manages user interactions
* LLM Initialization: Configured and cached Gemini AI model
* Error Handling: Comprehensive error handling and user feedback

2. Sequential Chain System (sequential_chain.py)

* Chain 1 - Roadmap Generator: Creates comprehensive learning roadmaps
* Chain 2 - Schedule Creator: Develops daily learning schedules
* Chain 3 - Timeline Estimator: Provides realistic time estimates
* Custom Sequential Execution: Chains execute in sequence with data flow

How It Works

    User Input →   Roadmap Chain → Schedule Chain → Timeline Chain → Display Results

        ↓              ↓              ↓              ↓              ↓
    Language      Comprehensive   Daily Learning  Time Estimates  Organized

    Experience → Learning Path → Schedule Plan → & Milestones → Display Time Avail.
## 🎛️ Configuration Options


### Experience Levels

* Complete Beginner: No prior programming experience
* Some Programming Background: Basic understanding of programming concepts
* Experienced in Other Languages: Familiar with programming but new to the selected language

### Time Commitment

* Range: 0.5 to 8 hours per day
* Recommendation: 1-2 hours for beginners, 2-4 hours for intensive learning
* Flexibility: Adjustable based on personal schedule

### Language Selection

* 20+ Languages: Comprehensive coverage of popular programming languages
* Dynamic Switching: Real-time plan generation when switching languages
* Specialized Content: Language-specific roadmaps and best practices
## 🛠️ API Configuration


### Gemini AI Setup

    python

#### The application uses Google's Gemini AI through LangChain

    llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.7,
    google_api_key=os.getenv("GEMINI_API_KEY")
    )


### API Best Practices

* Rate Limiting: Built-in handling for API rate limits
* Error Recovery: Graceful error handling for API failures
* Cost Optimization: Efficient prompt design to minimize API calls
* Caching: Results cached in session state to avoid duplicate calls
## 🔍 Troubleshooting


### Common Issues and Solutions
1. API Key Error
Error: Failed to initialize the AI model
#### Solution:

* Check if your .env file exists and contains the API key
* Verify the API key is correct and active
* Ensure no extra spaces or quotes around the API key

2. Import/Module Errors
#### Error: No module named 'langchain'
#### Solution:
    bash
    pip install -r requirements.txt
    # or individually:
    pip install streamlit langchain langchain-google-genai

3. Streamlit Version Compatibility
#### Error: module 'streamlit' has no attribute 'tabs'
#### Solution: The app now uses selectbox instead of tabs for better compatibility. Update Streamlit if needed:

    bashpip install --upgrade streamlit>=1.15.0


4. Port Already in Use
#### Error: Port 8501 is already in use
#### Solution:
    bash
    streamlit run main.py --server.port 8502


5. Environment Variables Not Loading
#### Solution:

* Ensure .env file is in the root directory
* Check file permissions
* Verify the python-dotenv package is installed



## 🚀 Advanced Usage


### Custom Chain Execution
    python
    from sequential_chain import create_custom_roadmap

### Create custom learning plan
    result = create_custom_roadmap(
        llm=your_llm,
        language="Python",
        experience_level="Complete Beginner",
        daily_hours=2.0
    )
### Extending the Application
#### Adding New Languages
    python
    # In main.py, add to the languages list
    languages = [
        "Python", "JavaScript", "Java", 
        "YourNewLanguage"  # Add here
    ]
### Customizing Prompts
#### Edit the prompt templates in   sequential_chain.py:
    python
    roadmap_template = """
    Your custom prompt template here...
    {language}, {experience_level}
    """
## 📊 Performance Optimization



### Caching Strategy

* LLM Initialization: Cached using @st.cache_resource
* Session State: Results cached to avoid regeneration
* Input Validation: Early validation to prevent unnecessary API calls

### Memory Management

* Efficient session state usage
* Cleanup of unused variables
* Optimized prompt lengths
## 🤝 Contributing


### Development Setup

* Fork the repository
* Create a feature branch: git checkout -b feature-name
* Make your changes
* Test thoroughly
* Submit a pull request

### Code Style

* Follow PEP 8 for Python code
* Use meaningful variable names
* Add docstrings for functions
* Include error handling

### Testing
    bash
    # Test the application
    streamlit run main.py

    # Test with different languages and settings
    # Verify error handling
    # Check API integration
## 📝 Version History


### v1.2.0 (Current)

✅ Fixed SequentialChain compatibility issues

✅ Improved error handling and user feedback

✅ Added cross-version Streamlit compatibility

✅ Enhanced session state management

✅ Better API error recovery


### v1.1.0

✅ Added 20+ programming languages

✅ Implemented dynamic language switching

✅ Added user preference settings

### v1.0.0

✅ Initial release with core functionality

✅ Basic roadmap, schedule, and timeline generation
## 🆘 Support


### Getting Help

* Documentation: Check this README first
* Issues: Create an issue in the repository
* API Documentation: Google AI Studio Docs
* LangChain Docs: LangChain Documentation

### Contact
#### For questions or support:

* Create an issue in the repository
* Check existing issues for solutions
* Refer to the troubleshooting section
## 🎯 Quick Start


    bash
    # Clone and setup
    git clone <repo-url> && cd programming-learning-guide
    pip install -r requirements.txt
    cp .env.example .env
    # Add your API key to .env
    streamlit run main.py


Happy Learning! 🚀
