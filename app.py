import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    secret = os.getenv("MY_SECRET")

    if secret:
        return f"""
        <h1>✅ Secret Successfully Loaded!</h1>
        <h3>Secret Value:</h3>
        <pre>{secret}</pre>
        """
    else:
        return """
        <h1>❌ Secret Not Found</h1>
        <p>MY_SECRET environment variable is missing.</p>
        """

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
