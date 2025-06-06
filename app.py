from flask import Flask, render_template, request, redirect
from models import db, Feedback

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        feedback = Feedback(name=name, message=message)
        db.session.add(feedback)
        db.session.commit()
        return redirect('/')
    
    all_feedback = Feedback.query.all()
    return render_template('index.html', feedback=all_feedback)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
