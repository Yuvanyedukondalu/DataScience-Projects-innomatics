from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

HOME_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>String Utility App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            margin: 0;
            padding: 20px;
            text-align: center;
        }
        h1, h2 {
            color: #4CAF50;
        }
        form {
            margin: 20px auto;
            max-width: 400px;
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        input, select, button {
            display: block;
            width: 100%;
            margin: 10px 0;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 10px 0;
        }
        a {
            color: #4CAF50;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .result {
            margin-top: 20px;
            font-size: 1.2em;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Welcome to the Creative String Utility App!</h1>
    <p>Transform your text in fun and creative ways.</p>
    <form action="/" method="post">
        <input type="text" name="name" placeholder="Enter your text here" required>
        <select name="operation">
            <option value="upper">Convert to UPPERCASE</option>
            <option value="lower">Convert to lowercase</option>
            <option value="title">Convert to Title Case</option>
            <option value="reverse">Reverse the Text</option>
            <option value="length">Get Length</option>
            <option value="palindrome">Check if Palindrome</option>
            <option value="vowel_count">Count Vowels</option>
            <option value="fun_fact">Get a Fun Fact</option>
        </select>
        <button type="submit">Transform!</button>
    </form>
    <div class="result">{{ result|safe }}</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        operation = request.form.get("operation", "")
        result = process_text(name, operation)
    return render_template_string(HOME_TEMPLATE, result=result)


def process_text(name, operation):
    if not name:
        return "<p style='color: red;'>Please enter some text!</p>"

    if operation == "upper":
        return f"<p>Your text in UPPERCASE: <strong>{name.upper()}</strong></p>"
    elif operation == "lower":
        return f"<p>Your text in lowercase: <strong>{name.lower()}</strong></p>"
    elif operation == "title":
        return f"<p>Your text in Title Case: <strong>{name.title()}</strong></p>"
    elif operation == "reverse":
        return f"<p>Reversed text: <strong>{name[::-1]}</strong></p>"
    elif operation == "length":
        return f"<p>Length of your text: <strong>{len(name)}</strong> characters</p>"
    elif operation == "palindrome":
        is_pal = name.lower() == name.lower()[::-1]
        status = "Yes, it's a palindrome!" if is_pal else "No, it's not a palindrome."
        return f"<p>Is '{name}' a palindrome? <strong>{status}</strong></p>"
    elif operation == "vowel_count":
        vowels = "aeiouAEIOU"
        count = sum(1 for char in name if char in vowels)
        return f"<p>Number of vowels in '{name}': <strong>{count}</strong></p>"
    elif operation == "fun_fact":
        facts = [
            "Did you know? The longest word in English has 189,819 letters!",
            "Fun fact: 'A' is the most common letter in English.",
            "Creative twist: Your text reversed is a mirror image!",
            "Trivia: There are 26 letters in the English alphabet.",
        ]
        import random

        fact = random.choice(facts)
        return f"<p>Fun Fact: {fact}</p>"
    else:
        return "<p style='color: red;'>Invalid operation selected.</p>"

@app.route("/upper")
def convert_upper():
    return redirect(url_for("home"))


@app.route("/lower")
def convert_lower():
    return redirect(url_for("home"))


@app.route("/length")
def name_length():
    return redirect(url_for("home"))


@app.route("/reverse")
def reverse_name():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
