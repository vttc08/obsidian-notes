Basic setup for debugging Flask app in VSCode
```json
{
  "name": "Python Debugger: Flask",
  "type": "debugpy",
  "request": "launch",
  "module": "flask",
  "env": {
    "FLASK_APP": "$APP$.py",
    "FLASK_DEBUG": "1"
  },
  "args": ["run", "--no-debugger"],
  "jinja": true,
  "justMyCode": true,
  "configurations": [
    {
      "name": "Python Debugger: Flask",
      "type": "debugpy",
      "request": "launch",
      "module": "flask",
      "env": { "FLASK_APP": "server.py", "FLASK_DEBUG": "1" },
      "args": ["run", "--no-debugger", "--port=$PORT$"],
      "jinja": true,
      "autoStartBrowser": false
    }
  ]
}
```
This configuration is default provided by Microsoft, enables debugging and hot reloading.
- change `$APP$` to the python file name
- change `$PORT$` to the port of the Flaks server