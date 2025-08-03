
# Watson AI Assistant for Audio Signal Processing

A console-based AI assistant powered by IBM Watson that specializes in audio signal processing queries and general technical questions.

## Features

- Interactive console interface
- Real-time streaming responses from IBM Watson
- Specialized in audio signal processing topics
- Secure API key management through environment variables
- Error handling and robust connection management

## Prerequisites

- Python 3.12 or higher
- IBM Watson API key
- Internet connection

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/watson-ai-assistant.git
   cd watson-ai-assistant
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Copy `.env.example` to `.env`
   - Add your IBM Watson API key to the `.env` file:
     ```
     IBM_API_KEY=your_actual_api_key_here
     ```

## Usage

Run the assistant:
```bash
python app.py
```

- Type your questions about audio signal processing or any other topic
- Type 'quit', 'exit', or 'q' to end the session
- The assistant provides streaming responses in real-time

## Example Questions

- "What is an operational amplifier?"
- "Explain frequency response in audio systems"
- "How does digital signal processing work?"
- "What are the differences between analog and digital filters?"

## Project Structure

```
watson-ai-assistant/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variables template
├── .gitignore         # Git ignore rules
├── README.md          # Project documentation
└── pyproject.toml     # Python project configuration
```

## Configuration

The application uses the following environment variables:

- `IBM_API_KEY`: Your IBM Watson API key (required)

## Dependencies

- `requests>=2.32.4` - HTTP library for API calls
- `python-dotenv>=1.1.1` - Environment variable management

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

## Deployment on Replit

This project is optimized for Replit deployment:

1. Import this repository to Replit
2. Add your `IBM_API_KEY` to Replit Secrets
3. Click the Run button to start the console application

The application will run in the Replit console and is ready for interactive use.
