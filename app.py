from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///resumes.db'
db = SQLAlchemy(app)

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    resumes = Resume.query.all()
    return render_template('index.html', resumes=resumes)

@app.route('/upload', methods=['POST'])
def upload():
    if 'resume' in request.files:
        resume = request.files['resume']

        if resume.filename != '':
            # Save the uploaded resume to the "uploads" folder
            upload_folder = 'uploads'
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)

            resume_path = os.path.join(upload_folder, resume.filename)
            resume.save(resume_path)

            # Save the resume information to the database
            new_resume = Resume(filename=resume.filename)
            db.session.add(new_resume)
            db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
