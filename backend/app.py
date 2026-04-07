from flask import Flask

# create Flask app FIRST
app = Flask(__name__)

# route
@app.route("/")
def home():
    return "ATS SaaS Backend Running 🚀"

# run app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
