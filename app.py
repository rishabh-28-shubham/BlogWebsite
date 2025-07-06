from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import json
import os
from datetime import datetime
import uuid

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'
app.config['DEBUG'] = True

# Load data from JSON files
def load_posts():
    try:
        with open('posts.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def load_users():
    try:
        with open('users.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_posts(posts):
    with open('posts.json', 'w', encoding='utf-8') as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)

def save_users(users):
    with open('users.json', 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=2, ensure_ascii=False)

@app.route("/")
def home():
    posts = load_posts()
    # Sort posts by creation date (newest first)
    posts.sort(key=lambda x: datetime.strptime(x['created_at'], '%a, %m/%d/%Y'), reverse=True)
    return render_template("index.html", posts=posts[:6])  # Show latest 6 posts

@app.route("/posts")
def all_posts():
    posts = load_posts()
    posts.sort(key=lambda x: datetime.strptime(x['created_at'], '%a, %m/%d/%Y'), reverse=True)
    return render_template("posts.html", posts=posts)

@app.route("/post/<post_id>")
def post_detail(post_id):
    posts = load_posts()
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        return render_template("post_detail.html", post=post)
    else:
        flash('Post not found!', 'error')
        return redirect(url_for('home'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        users = load_users()
        user = next((u for u in users if u['username'] == username and u['password'] == password), None)
        
        if user:
            session['user_id'] = user['user_id']
            session['username'] = user['username']
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password!', 'error')
    
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('home'))

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return render_template("register.html")
        
        users = load_users()
        if any(u['username'] == username for u in users):
            flash('Username already exists!', 'error')
            return render_template("register.html")
        
        new_user = {
            "username": username,
            "password": password,
            "user_id": str(uuid.uuid4())
        }
        
        users.append(new_user)
        save_users(users)
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template("register.html")

@app.route("/create-post", methods=['GET', 'POST'])
def create_post():
    if 'user_id' not in session:
        flash('Please login to create a post!', 'error')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        title = request.form['title']
        subtitle = request.form['subtitle']
        summary = request.form['summary']
        category = request.form['category']
        featured_image = request.form['featured_image']
        main_content = request.form['main_content']
        
        # Get user info
        users = load_users()
        user = next((u for u in users if u['user_id'] == session['user_id']), None)
        
        if not user:
            flash('User not found!', 'error')
            return redirect(url_for('login'))
        
        new_post = {
            "id": str(uuid.uuid4()),
            "user_id": session['user_id'],
            "title": title,
            "subtitle": subtitle,
            "summary": summary,
            "category": category,
            "featured_image": featured_image,
            "main_content": main_content,
            "created_at": datetime.now().strftime('%a, %m/%d/%Y'),
            "updated_at": datetime.now().strftime('%a, %m/%d/%Y'),
            "user": {
                "id": user['user_id'],
                "first_name": user.get('first_name', ''),
                "last_name": user.get('last_name', ''),
                "username": user['username'],
                "profile_pic": "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w0OTE2MTF8MHwxfHNlYXJjaHwxNnx8UG9ydHJhaXR8ZW58MHwwfHx8MTY5NzM2Mzk0Nnww&ixlib=rb-4.0.3&q=80&w=400"
            },
            "comments": [],
            "tags": []
        }
        
        posts = load_posts()
        posts.append(new_post)
        save_posts(posts)
        
        flash('Post created successfully!', 'success')
        return redirect(url_for('post_detail', post_id=new_post['id']))
    
    return render_template("create_post.html")

@app.route("/profile")
def profile():
    if 'user_id' not in session:
        flash('Please login to view your profile!', 'error')
        return redirect(url_for('login'))
    
    users = load_users()
    user = next((u for u in users if u['user_id'] == session['user_id']), None)
    
    if not user:
        flash('User not found!', 'error')
        return redirect(url_for('login'))
    
    posts = load_posts()
    user_posts = [p for p in posts if p['user_id'] == session['user_id']]
    
    return render_template("profile.html", user=user, posts=user_posts)

@app.route("/category/<category>")
def category_posts(category):
    posts = load_posts()
    category_posts = [p for p in posts if p['category'].lower() == category.lower()]
    return render_template("category.html", posts=category_posts, category=category)

if __name__ == "__main__":
    app.run(debug=True)
