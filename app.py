from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'your_secret_key'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your_email_address'
app.config['MAIL_PASSWORD'] = 'your_email_password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download_cv')
def download_cv():
    return render_template('download_cv.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        msg = Message(subject, sender='your_email_address', recipients=['your_email_address'])
        msg.body = f"Name: {name}\nEmail: {email}\n\n{message}"
        mail.send(msg)
        flash('Your message has been sent successfully!', 'success')
        return render_template('contact.html')
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
