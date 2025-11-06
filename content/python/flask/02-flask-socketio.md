Flask Basics

## Install
```bash
pip install flask_socketio
```

**Note:** For optimal performance, it's recommended to also install `eventlet` or `gevent` for asynchronous I/O.

```bash
# Choose one of the following:
pip install eventlet
# OR
pip install gevent
```
### Basic Flask-SocketIO App (`app.py`)

Here's a minimal example of a Flask-SocketIO application:

```python
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(data):
    print(f'received message: {data}')
    # Emit the message back to all connected clients
    emit('message', {'message': data}, broadcast=True)

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('message', {'message': 'Welcome! You are connected.'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    # Use eventlet or gevent for production deployment
    # socketio.run(app, host='0.0.0.0', port=5000, debug=True, use_reloader=True)
    socketio.run(app, debug=True)
```

### 4. Client-Side (`templates/index.html` and `static/script.js`)

**`templates/index.html`:**

```html
<!DOCTYPE html>
<html>
<head>
    <title>Flask-SocketIO Chat</title>
</head>
<body>
    <h1>Flask-SocketIO Demo</h1>
    <div id="messages"></div>
    <input type="text" id="message_input" placeholder="Type a message...">
    <button onclick="sendMessage()">Send</button>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    <script src="{{ url_for('static', filename='script.js') }}"></script>
</body>
</html>
```

**`static/script.js`:**

```javascript
const socket = io.connect(window.location.origin);

socket.on('connect', () => {
    console.log('Connected to server!');
});

socket.on('message', (data) => {
    const messagesDiv = document.getElementById('messages');
    const newMessage = document.createElement('p');
    newMessage.textContent = data.message;
    messagesDiv.appendChild(newMessage);
});

socket.on('disconnect', () => {
    console.log('Disconnected from server.');
});

function sendMessage() {
    const messageInput = document.getElementById('message_input');
    const message = messageInput.value;
    if (message.trim() !== '') {
        socket.emit('message', message); // Send message to server
        messageInput.value = ''; // Clear input
    }
}
```