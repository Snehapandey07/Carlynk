from flask import Flask, render_template, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import os
from chatbot_api import apnabot
from Damage_detection import engine
from Dashboard_helper import CarDashboardHelper

app = Flask(__name__)
chat_history = []
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

##############################
CSV_PATH = "car_dasboard_symbol_detection/Symbols23.csv"
EMAIL_USER = "bhushannikhade446@gmail.com"
EMAIL_PASSWORD = "shws xudn blmp tgae"  # Your generated App Password
TO_EMAIL = "bhushannikhade3012@gmail.com"

# Initialize the helper
helper = CarDashboardHelper(CSV_PATH, EMAIL_USER, EMAIL_PASSWORD)

# # Get user input and generate report


################################
# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
def allowed_file(filename):
    """Check if file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')  # This is your "Start" page

@app.route('/dashboard',methods=['GET', 'POST'])
def dashboard():
    return render_template('dashboard.html')  # Your dashboard page
@app.route('/update_label/<int:light_id>', methods=['GET'])
def update_label(light_id):
    # Set the value of x to the corresponding label
    report_status = helper.generate_report(light_id, TO_EMAIL)

    # Return a response with the label message
    return jsonify({
        'success': True,
        'message': f"Warning light clicked: {report_status}"
    })


@app.route('/maintainance', methods=['GET', 'POST'])
def maintenance():
    bot_response = None  # Default response  # Initialize chat history
    global chat_history
    if request.method == 'POST':
        # Capture user message from form
        user_message = request.form.get('user_message', '')
        
        if user_message:
            # Generate bot response using apnabot function
            bot_response, chat_history = apnabot(user_message, chat_history)
    
    # Render maintenance page with the bot response and chat history
    return render_template('maintainance.html', response=bot_response, chat_history=chat_history)

@app.route('/car-detector', methods=['GET', 'POST'])
def car_detector():
    damage_report = None
    uploaded_file_url = None

    if request.method == 'POST':
        # Check if an image is uploaded
        if 'carImage' not in request.files:
            damage_report = "No file uploaded. Please try again."
        else:
            file = request.files['carImage']
            if file and allowed_file(file.filename):
                # Secure the filename and save the file
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)

                # Simulate generating a damage report (replace with your ML model logic)
                damage_report = engine(file_path)
                uploaded_file_url = file_path  # To display the uploaded image

            else:
                damage_report = "Kuch to gadbad Hai re bacchi....."

    return render_template(
        'car-detector.html',
        damage_report=damage_report,
        uploaded_file_url=uploaded_file_url
    )


if __name__ == '__main__':
    app.run(debug=True)