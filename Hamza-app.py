from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from forms import PortfolioForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
db = SQLAlchemy(app)

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    profile_picture = db.Column(db.String(150), nullable=False)
    bio = db.Column(db.Text, nullable=False)
    skills = db.Column(db.Text, nullable=False)
    online_links = db.Column(db.Text, nullable=False)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/create-portfolio', methods=['GET', 'POST'])
def create_portfolio():
    form = PortfolioForm()
    if form.validate_on_submit():
        new_portfolio = Portfolio(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone=form.phone.data,
            profile_picture=form.profile_picture.data,
            bio=form.bio.data,
            skills=form.skills.data,
            online_links=form.online_links.data
        )
        db.session.add(new_portfolio)
        db.session.commit()
        return redirect(url_for('view_portfolio', portfolio_id=new_portfolio.id))
    return render_template('create_portfolio.html', form=form)

@app.route('/view-portfolio/<int:portfolio_id>')
def view_portfolio(portfolio_id):
    portfolio = Portfolio.query.get_or_404(portfolio_id)
    return render_template('view_portfolio.html', portfolio=portfolio)

@app.route('/custom-page')
def custom_page():
    return render_template('custom_page.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)