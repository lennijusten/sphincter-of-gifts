from flask import Flask, render_template, request, jsonify
import tinder_irl

app = Flask(__name__)
alien_profile = None  # Global variable to hold the selected alien profile
conversation_history = "" #Global variable to hold the conversation history

@app.route('/')
def index():
    global alien_profile
    alien_profile = tinder_irl.parse_json()
    return render_template('index.html', profile=alien_profile)

@app.route('/process', methods=['POST'])
def process():
    global alien_profile
    data = request.get_json()
    prompt = data.get('text')
    if not prompt:
        return jsonify({'error': 'No message text provided'}), 400

    conversation_history = ""
    role_prompt = tinder_irl.generate_role_prompt(alien_profile)  # Generate role prompt based on alien profile
    response, _ = tinder_irl.respond_to_user(prompt, conversation_history, role_prompt)

    print(response)  # Print the response to console for now

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
