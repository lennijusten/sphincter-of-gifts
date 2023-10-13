from flask import Flask, render_template, request, jsonify
import tinder_irl

app = Flask(__name__)
alien_profile = None  # Global variable to hold the selected alien profile
conversation_history = "" #Global variable to hold the conversation history

@app.route('/')
def index(): # set counter to zero here
    global alien_profile
    alien_profile = tinder_irl.parse_json()
    tinder_irl.reset_count()
    return render_template('index.html', profile=alien_profile)

@app.route('/process', methods=['POST'])
def process():
    global alien_profile
    data = request.get_json()
    prompt = data.get('text')
    if not prompt:
        return jsonify({'error': 'No message text provided'}), 400

    if tinder_irl.get_count() < tinder_irl.CHAT_TOLERANCE:
        role_prompt = tinder_irl.generate_role_prompt(alien_profile)  # Generate role prompt based on alien profile
        response, end = tinder_irl.respond_to_user(prompt, role_prompt)

        print(response)  # Print the response to console for now

        if (response != None):
            return jsonify({'response': response, 'end': end})
        else:
            return jsonify({'error': 'No message text provided'}), 400

    else: # CAN WE MAKE MESSAGES STOP SENDING HERE
        if not tinder_irl.rejected:
            tinder_irl.print_ticket("hello world")
        return jsonify({'end':end})

if __name__ == '__main__':
    app.run(debug=True)
