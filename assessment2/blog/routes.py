from flask import render_template, url_for, request, redirect, flash
from blog import app, db, login_manager
from blog.models import User, Post, Comment
from blog.forms import RegistrationForm, LoginForm, PostForm, CommentForm
from flask_login import login_user, logout_user, current_user, login_required

@app.route("/",methods=['GET', 'POST'])

@app.route("/home",methods=['GET', 'POST'])
def home():
  #posts=Post.query.all()
  posts=Post.query.order_by(Post.date.desc())
  num_posts = Post.query.count()
  form = PostForm()
  if form.validate_on_submit():
    if form.post_order.data == 'date_desc':
      posts=Post.query.order_by(Post.date.desc())
    else:
      posts=Post.query.order_by(Post.date.asc())
  return render_template('home.html',posts=posts,form=form,num_posts=num_posts)

@app.route("/post/<int:post_id>", methods=['GET', 'POST'])
def post(post_id):
  post=Post.query.get_or_404(post_id)
  form = CommentForm()
  if form.validate_on_submit():
    if current_user.is_authenticated:
      comment = Comment(title=form.title.data, content=form.content.data, post_id=post_id, author_id=current_user.id, rating=form.rating.data)
      db.session.add(comment)
      db.session.commit()
      flash('Comment submitted successfully!')
    else:
      flash('Please log in to comment!')
  query_result=Comment.query.filter_by(post_id=post_id)
  comments = query_result.all()
  num_comments = query_result.count()
  return render_template('post.html',title=post.title,post=post,comments=comments, num_comments=num_comments, form=form)

@app.route("/register",methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, password=form.password.data, email=form.email.data)
    db.session.add(user)
    db.session.commit()
    flash('Registration successful! Welcome!')
    login_user(user)
    return redirect(url_for('home'))
  return render_template('register.html',title='Register',form=form)

@app.route("/login_fail")
def login_fail():
  return render_template('login_fail.html', title='Login fail!')

@app.route("/login",methods=['GET','POST'])
def login():
 form = LoginForm()
 if form.validate_on_submit():
   user = User.query.filter_by(username=form.username.data).first()
   if user is not None and user.verify_password(form.password.data):
     login_user(user)
     flash('You have successfully logged in,'+' '+ current_user.username +'!')
     return redirect(url_for('home'))
   else:
     return redirect(url_for('login_fail'))
 return render_template('login.html',title='Login', form=form)

@app.route("/logout")
@login_required
def logout():
  logout_user()
  flash('You have been logged out.')
  return redirect(url_for('home'))

@app.route("/contact")
def contact():
  return render_template('contact.html', title='Contact Me')

@app.route("/privacy")
def privacy():
  return render_template('privacy.html', title='Privacy Policy & Disclaimer')

@app.route("/term")
def term():
  return render_template('term.html', title='Terms of Use')


@login_manager.unauthorized_handler
def unauthorized_callback():
  flash('Please log in first!')
  return redirect(url_for('login'))


