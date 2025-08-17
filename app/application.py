from flask import Flask, request, url_for, session, redirect, render_template
from markupsafe import Markup
from app.core.final_retriever import FinalRetriever

import os

app = Flask(__name__)

def nl2br(value):
    return Markup(value.replace('\n', '<br>\n'))

@app.route('/predict', methods=['POST', 'GET'])
def get_response():
    response = None
    error_msg = None

    if request.method == 'POST':
        user_input = request.form.get('prompt')

        if user_input:
            try:
                retriever_instance = FinalRetriever()
                result = retriever_instance.prompt_chaining(question=user_input)
                response = result.get('answer', 'No answer returned.')
            except Exception as e:
                error_msg = f"Error occurred: {str(e)}"
        else:
            error_msg = "No input provided."

    # Always render the template for both GET and POST
    return render_template('index.html', response=response, error=error_msg)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
