import os
import requests
from dotenv import load_dotenv
from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

# Initialize Flask and SocketIO
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables")

def chat_with_groq(prompt):
    """Simple, direct implementation of chat functionality"""
    # Basic input validation
    if not isinstance(prompt, str) or not prompt.strip():
        return "Please provide a valid question."

    try:
        # API request configuration
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        data = {
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "system", "content": "You are a helpful healthcare assistant."},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.5,
            "max_tokens": 200
        }

        # Make request
        response = requests.post(url, headers=headers, json=data, timeout=30)
        
        # Handle non-200 status
        if response.status_code != 200:
            return f"Error: API returned status {response.status_code}"

        # Parse response directly
        try:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        except (KeyError, IndexError):
            return "Error: Invalid response format"
        except Exception as e:
            return f"Error parsing response: {str(e)}"

    except requests.Timeout:
        return "Error: Request timed out"
    except requests.RequestException as e:
        return f"Error making request: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    socketio.emit('bot_response', {
        'response': "Hello! I'm your HealthSync Assistant. How can I help you today?"
    })

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('user_message')
def handle_message(data):
    """Simple message handler"""
    try:
        # Get message from data
        message = data.get('message', '').strip()
        if not message:
            socketio.emit('bot_response', {'response': "Please send a message."})
            return

        # Get response from chat function
        response = chat_with_groq(message)
        
        # Send response back to client
        socketio.emit('bot_response', {'response': response})

    except Exception as e:
        print(f"Error in handle_message: {e}")
        socketio.emit('bot_response', {
            'response': "Sorry, something went wrong. Please try again."
        })

if __name__ == '__main__':
    print("Starting server...")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
