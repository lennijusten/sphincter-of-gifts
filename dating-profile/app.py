from flask import Flask, render_template
import random
import string

app = Flask(__name__)

@app.route('/')
def profile():
    # Generating random name, location, and bio
    name = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=10))
    location = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))
    bio = ' '.join(''.join(random.choices(string.ascii_lowercase, k=5)) for _ in range(20))  # 20 words of 5 letters each

    return render_template('profile.html', name=name, location=location, bio=bio)

if __name__ == '__main__':
    app.run(debug=True)
