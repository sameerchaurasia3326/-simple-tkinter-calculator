from flask import Flask, render_template, request

# Create the Flask web app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = ''
    if request.method == 'POST':
        # Get the expression from the web form
        expression = request.form.get('expression', '')
        try:
            # DANGEROUS: eval() is not safe for real production apps
            # but we use it here to match your original code's logic.
            result = eval(expression)
        except:
            result = "Error"
    
    # Render the HTML user interface
    return render_template('index.html', result=result)

# This allows the app to be run by a production server like Gunicorn
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
