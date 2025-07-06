# Medium Blog Website

A beautiful blogging platform built with Flask and Tailwind CSS, inspired by Medium's design and functionality.

## Features

- **Modern UI Design**: Clean, responsive design using Tailwind CSS with Medium-inspired color theme
- **User Authentication**: Register, login, and logout functionality
- **Blog Post Management**: Create, read, and manage blog posts
- **Rich Text Editor**: HTML-based editor with formatting tools
- **Category System**: Organize posts by categories
- **User Profiles**: View user profiles and their published stories
- **Comments System**: Leave comments on posts (basic implementation)
- **Search & Filter**: Search posts and filter by categories
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices

## Color Theme

The application uses a custom Medium-inspired color palette:

```javascript
{
  background: '#FFFFFF',
  primary: '#242424',
  secondary: '#6B6B6B',
  link: '#1A8917',
  accent: '#1A8917',
  muted: '#F2F2F2',
  border: '#E5E5E5',
  highlight: '#FFC017',
}
```

## Installation & Setup

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Step 1: Clone or Download

Download the project files to your local machine.

### Step 2: Set up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install flask
```

### Step 4: Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## Usage

### Demo Accounts

You can use these pre-existing accounts to test the application:

| Username | Password |
|----------|----------|
| alycia662571 | heath123 |
| lesch.blaise5895 | john123 |
| zbradtke7096 | sara123 |
| mattie.batz4359 | mike123 |
| domingo749552 | linda123 |

### Creating a New Account

1. Click "Get started" in the navigation
2. Fill in your username and password
3. Click "Create account"
4. Sign in with your new credentials

### Writing a Blog Post

1. Sign in to your account
2. Click "Write" in the navigation
3. Fill in the post details:
   - Title (required)
   - Subtitle
   - Summary
   - Category (required)
   - Featured image URL
   - Main content (supports HTML formatting)
4. Use the preview button to see how your post will look
5. Click "Publish Story"

### HTML Formatting

The editor supports basic HTML tags for formatting:

- `<h1>`, `<h2>`, `<h3>` for headings
- `<p>` for paragraphs
- `<strong>` for bold text
- `<em>` for italic text
- `<blockquote>` for quotes
- `<ul>`, `<ol>`, `<li>` for lists

## Project Structure

```
├── app.py                 # Main Flask application
├── posts.json            # Blog posts data
├── users.json            # User accounts data
├── tailwind/
│   ├── input.css         # Tailwind CSS input file
│   └── config.js         # Tailwind configuration
├── templates/
│   ├── base.html         # Base template with navigation
│   ├── index.html        # Home page
│   ├── posts.html        # All posts page
│   ├── post_detail.html  # Individual post page
│   ├── login.html        # Login page
│   ├── register.html     # Registration page
│   ├── create_post.html  # Create post page
│   ├── profile.html      # User profile page
│   └── category.html     # Category posts page
└── README.md             # This file
```

## Features in Detail

### Home Page
- Hero section with call-to-action
- Featured stories grid
- Category exploration
- Responsive design

### All Posts Page
- Grid layout of all posts
- Search functionality
- Category filtering
- Load more button

### Post Detail Page
- Full article display
- Author information
- Comments section
- Like and share buttons
- Related posts section

### User Authentication
- Secure login/logout
- User registration
- Session management
- Flash messages for feedback

### Create Post Page
- Rich text editor with toolbar
- Preview functionality
- Form validation
- Draft saving (demo)

### User Profile Page
- User information display
- Published stories list
- Statistics dashboard
- About section

### Category Pages
- Category-specific posts
- Category descriptions
- Related categories
- Empty state handling

## Customization

### Adding New Categories

To add new categories, update the categories list in:
- `templates/index.html`
- `templates/posts.html`
- `templates/create_post.html`
- `templates/category.html`

### Modifying the Color Theme

Edit the color values in:
- `tailwind.config.js`
- `templates/base.html` (in the script tag)

### Adding New Features

The modular structure makes it easy to add new features:
- Add new routes in `app.py`
- Create new templates in `templates/`
- Update navigation in `base.html`

## Data Storage

The application uses JSON files for data storage:
- `posts.json`: Stores all blog posts with metadata
- `users.json`: Stores user account information

For production use, consider migrating to a proper database like PostgreSQL or MySQL.

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Safari
- Edge

## Contributing

Feel free to contribute to this project by:
- Reporting bugs
- Suggesting new features
- Submitting pull requests
- Improving documentation

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues or have questions, please check the documentation or create an issue in the project repository.

---

**Enjoy writing and sharing your stories! 📝✨** 