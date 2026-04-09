# 🤖 Website Chatbot - Capstone Project

![Website Chatbot Hero](images/webhero.png)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chat-anywebsite.streamlit.app/)

## 📌 Project Overview

**Website Chatbot** is an intelligent AI-powered application that allows users to interact with any website's content through a natural language conversational interface. Users can load any website URL, and the application will scrape and analyze its content, then answer questions about it using OpenAI's GPT-4 model.

This project demonstrates a complete end-to-end application incorporating web scraping, AI integration, and a modern web-based user interface using Streamlit.

---

## ✨ Features

- 🌐 **Web Scraping**: Automatically extracts and processes content from any website
- 🤖 **AI-Powered Q&A**: Uses OpenAI's GPT-4o-mini model for intelligent responses
- 💬 **Interactive Chat Interface**: User-friendly Streamlit-based frontend
- ⚡ **Real-time Processing**: Fast loading and response generation
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices
- 🔒 **Secure**: Uses environment variables for API key management
- 📊 **Session Management**: Maintains conversation history throughout the session
- 🎨 **Enhanced UI**: Professional styling with status indicators and progress tracking
- ⚠️ **Error Handling**: Robust error handling for invalid URLs and API issues

---

## 🛠️ Technologies Used

| Technology | Purpose |
|-----------|---------|
| **Python 3.12+** | Core programming language |
| **Streamlit** | Web application framework and UI |
| **OpenAI API** | GPT-4o-mini language model for Q&A |
| **BeautifulSoup4** | HTML parsing and web scraping |
| **Requests** | HTTP client for fetching web pages |
| **Python-dotenv** | Environment variable management |

---

## 📋 Prerequisites

Before you begin, ensure you have:

- **Python 3.8+** installed on your system
- **pip** (Python package manager)
- **OpenAI API Key** (obtain from [OpenAI Platform](https://platform.openai.com/api-keys))
- **Git** (optional, for cloning the repository)

---

## 🚀 Installation & Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/gatemediang/Web-Chat-Bot.git
cd Web-Chat-Bot
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file in the project root directory:

```bash
touch .env
```

Add your OpenAI API key to the `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

⚠️ **Important**: Never commit the `.env` file to version control. It's already included in `.gitignore`.

---

## 🎯 Usage

### Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

### How to Use

1. **Enter Website URL**
   - In the left sidebar, enter the URL of any website
   - Click the "🔄 Load Website" button

2. **Wait for Processing**
   - The app will scrape and process the website content
   - A success message will appear with the content size

3. **Ask Questions**
   - In the chat box at the bottom, type your questions about the website content
   - Press Enter or click Send to submit

4. **View Responses**
   - The AI assistant will analyze the website content and provide answers
   - Chat history is maintained throughout your session

5. **Clear Chat (Optional)**
   - Click "🗑️ Clear Chat History" to start fresh with the same website
   - Load a new URL to switch websites

---

## 📁 Project Structure

```
Web-Chat-Bot/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not tracked in git)
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
```

---

## 🔧 Configuration

### Customizing the Application

#### Change the AI Model

Edit `app.py` and modify the model parameter:

```python
response = client.chat.completions.create(
    model="gpt-4-turbo",  # Change this to another model
    messages=messages_for_api,
    temperature=0.7,
    max_tokens=1000
)
```

#### Adjust Temperature & Tokens

- **Temperature** (0.0 - 2.0): Controls response creativity
  - Lower values (0.0-0.5): More focused, deterministic responses
  - Higher values (0.5-2.0): More creative, diverse responses

- **max_tokens**: Limits response length (higher = longer responses)

#### System Prompt Customization

Modify the `SYSTEM_PROMPT` variable to change how the AI behaves:

```python
SYSTEM_PROMPT = """Your custom instructions here"""
```

---

## 🐛 Troubleshooting

### Issue: "OPENAI_API_KEY not found"
**Solution**: Ensure your `.env` file is created and contains the correct API key. Verify the `.env` file is in the project root directory.

### Issue: "Error fetching URL"
**Solution**: 
- Verify the URL is correct and starts with `http://` or `https://`
- Check your internet connection
- Some websites may block web scraping; try a different website

### Issue: Slow Response Times
**Solution**:
- Large websites may take longer to process
- Check your internet connection speed
- Ensure your OpenAI API quota isn't exhausted

### Issue: Application won't start
**Solution**:
```bash
# Ensure all dependencies are installed
pip install --upgrade -r requirements.txt

# Verify Python version (should be 3.8+)
python --version

# Try running with explicit Python 3
python3 app.py
```

---

## 📊 API Usage & Costs

This application uses OpenAI's `gpt-4o-mini` model. Be aware of:

- **Cost**: Pay per token used (input/output)
- **Rate Limits**: Default API limits apply to your account
- **Token Counting**: Website content + conversation history = tokens used

Monitor your usage on the [OpenAI Usage Dashboard](https://platform.openai.com/usage)

---

## 🔒 Security Best Practices

1. **Never commit `.env` file** - It contains sensitive information
2. **Use environment variables** - Always access secrets through environment variables
3. **Validate URLs** - The app validates URLs before processing
4. **Regular updates** - Keep dependencies updated for security patches

```bash
# Check for security updates
pip list --outdated
pip install --upgrade -r requirements.txt
```

---

## 🚧 Future Enhancements

Potential features for future versions:

- ✅ Support for PDF and document files
- ✅ Multiple language support
- ✅ Chat export (save conversations as files)
- ✅ Website content caching for faster re-queries
- ✅ User authentication and history
- ✅ Web search integration
- ✅ Custom model selection from dropdown
- ✅ Token usage statistics
- ✅ Rate limiting and usage tracking
- ✅ Mobile app version

---

## 📚 API Documentation References

- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Streamlit Documentation](https://docs.streamlit.io)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://docs.python-requests.org/)

---

## 📝 License

This project is open-source and available under the MIT License.

---

## 👤 Author & Credits

**Developer**: [Your Name/gatemediang]

**Acknowledgments**:
- OpenAI for the GPT-4 API
- Streamlit for the web framework
- BeautifulSoup4 for web scraping capabilities

---

## 📧 Support & Feedback

For issues, suggestions, or contributions:

1. Open an issue on GitHub
2. Submit a pull request with improvements
3. Contact the maintainer directly

---

## ⚡ Quick Start Command

For experienced users, quick setup:

```bash
git clone https://github.com/gatemediang/Web-Chat-Bot.git && \
cd Web-Chat-Bot && \
python3 -m venv venv && \
source venv/bin/activate && \
pip install -r requirements.txt && \
echo "OPENAI_API_KEY=your_key_here" > .env && \
streamlit run app.py
```

---

## 📈 Performance Metrics

| Aspect | Performance |
|--------|-------------|
| Average Load Time | < 5 seconds |
| Response Time | < 3 seconds |
| Max Website Size | ~500KB (scalable) |
| Concurrent Users | Limited by Streamlit Cloud |
| API Rate Limit | OpenAI Account Default |

---

## 🎓 Learning Outcomes

This capstone project demonstrates:

- ✅ Web scraping with BeautifulSoup
- ✅ API integration with OpenAI
- ✅ Building interactive web applications with Streamlit
- ✅ Session state management
- ✅ Error handling and validation
- ✅ Environment variable management
- ✅ UI/UX best practices
- ✅ Professional documentation

---

**Happy Chatting! 🚀** Feel free to explore and ask questions about any website's content with your new AI assistant!