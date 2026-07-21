from flask import Flask,render_template,redirect,url_for,request,flash
from models import db,Product,User
from forms import ProductForm,EditForm,RegisterForm,LoginForm
from flask_ckeditor import CKEditor
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager,current_user,login_user,logout_user,login_required
from werkzeug.security import generate_password_hash,check_password_hash
import os


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///inventory.db")
db.init_app(app)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')

bootstrap = Bootstrap5(app)
login_manager = LoginManager()
login_manager.init_app(app)

with app.app_context():
    db.create_all()

ckeditor = CKEditor(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User,user_id)



@app.route('/')
def home():
    if current_user.is_authenticated:
        result = current_user.products
        return render_template('home.html',products=result)
    return render_template('home.html')

@app.route('/add-product',methods=['POST','GET'])
@login_required
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(
            name = form.name.data,
            selling_price = f"{form.price.data}",
            stock = form.stock.data,
            description = form.desc.data,
            user_id = current_user.id
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_products.html',form=form)


@app.route('/register',methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username = form.username.data.title(),
            email = form.email.data,
            password_hash = generate_password_hash(password=form.password.data,method='pbkdf2:sha256',
                                              salt_length=10)
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home'))
    return render_template('register.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).where(User.email == form.email.data)).scalar()
        if user:
            if check_password_hash(user.password_hash,form.password.data):
                flash('You were successfully logged in')
                login_user(user)
                return redirect(url_for('home'))
            flash('Invalid Password')
        flash('Invalid email, click on register to sign up')

    return render_template('login.html',form=form)


@app.route('/edit/<int:edit_id>',methods=['GET','POST'])
@login_required
def edit(edit_id):
    result = db.get_or_404(Product,edit_id)
    edit_form = EditForm(
        name = result.name,
        price = result.selling_price,
        stock = result.stock,
        desc = result.description
    )
    if edit_form.validate_on_submit():
        result.name = edit_form.name.data
        result.selling_price = edit_form.price.data
        result.stock = edit_form.stock.data
        result.description = edit_form.desc.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',form=edit_form)


@app.route('/search')
@login_required
def search():
    name = request.args.get('product_name')
    product = db.session.execute(db.select(Product).where((Product.name.icontains(name))& (Product.user_id == current_user.id))).scalars().all()
    return render_template('home.html',products=product)


@app.route('/user/<int:delete_id>/delete')
@login_required
def delete(delete_id):
    product = db.get_or_404(Product,delete_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))




if __name__ == "__main__":
    app.run(debug=True)

