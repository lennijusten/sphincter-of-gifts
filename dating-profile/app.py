from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Sample data for an alien profile
    profile = {
        'image': 'static/img/profile.png',
        'name': 'Zorgon',
        'planet': 'Mars',
        'age': '120',
        'bio': 'Alien from Mars who loves space travel.',
        'interests': ['Space exploration', 'Galactic dance', 'Star gazing']
    }
    return render_template('index.html', profile=profile)

if __name__ == '__main__':
    app.run(debug=True)

