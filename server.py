from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

def generate_website(template):
    html = ""  # Initialize html with a default value

    if template == 'ecommerce_template':
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome to Our E-commerce Site</title>
            <link rel="stylesheet" href="static/styles.css">
        </head>
        <body>
            <header>
                <h1>Welcome to Our E-commerce Site</h1>
                <nav>
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">Shop</a></li>
                        <li><a href="#">About Us</a></li>
                        <li><a href="#">Contact</a></li>
                    </ul>
                </nav>
            </header>
            <main>
                <section class="hero">
                    <h2>Shop the Latest Trends</h2>
                    <p>Find what you love!</p>
                </section>
                <section class="products">
                    <h3>Featured Products</h3>
                    <ul>
                        <li>Product 1</li>
                        <li>Product 2</li>
                        <li>Product 3</li>
                    </ul>
                </section>
            </main>
            <footer>
                <p>&copy; 2024 Our E-commerce Site. All Rights Reserved.</p>
            </footer>
        </body>
        </html>
        """
    elif template == 'portfolio_template':
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>My Portfolio</title>
            <link rel="stylesheet" href="static/styles.css">
        </head>
        <body>
            <header>
                <h1>My Portfolio</h1>
                <nav>
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">Projects</a></li>
                        <li><a href="#">About Me</a></li>
                        <li><a href="#">Contact</a></li>
                    </ul>
                </nav>
            </header>
            <main>
                <section class="hero">
                    <h2>Welcome to My Portfolio</h2>
                    <p>Showcasing my work and projects.</p>
                </section>
                <section class="projects">
                    <h3>My Projects</h3>
                    <ul>
                        <li>Project A</li>
                        <li>Project B</li>
                        <li>Project C</li>
                    </ul>
                </section>
            </main>
            <footer>
                <p>&copy; 2024 My Portfolio. All Rights Reserved.</p>
            </footer>
        </body>
        </html>
        """
    elif template == 'online_course_template':
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Online Courses</title>
            <link rel="stylesheet" href="static/styles.css">
        </head>
        <body>
            <header>
                <h1>Online Courses</h1>
                <nav>
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">Courses</a></li>
                        <li><a href="#">About Us</a></li>
                        <li><a href="#">Contact</a></li>
                    </ul>
                </nav>
            </header>
            <main>
                <section class="hero">
                    <h2>Learn Anytime, Anywhere</h2>
                    <p>Explore our wide range of online courses.</p>
                </section>
                <section class="courses">
                    <h3>Our Courses</h3>
                    <ul>
                        <li>Course 1</li>
                        <li>Course 2</li>
                        <li>Course 3</li>
                    </ul>
                </section>
            </main>
            <footer>
                <p>&copy; 2024 Online Courses. All Rights Reserved.</p>
            </footer>
        </body>
        </html>
        """
    elif template == 'blog_template':
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>My Blog</title>
            <link rel="stylesheet" href="static/styles.css">
        </head>
        <body>
            <header>
                <h1>Welcome to My Blog</h1>
                <nav>
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">Posts</a></li>
                        <li><a href="#">About</a></li>
                        <li><a href="#">Contact</a></li>
                    </ul>
                </nav>
            </header>
            <main>
                <section class="hero">
                    <h2>Latest Posts</h2>
                    <p>Sharing my thoughts and experiences.</p>
                </section>
                <section class="posts">
                    <h3>Recent Posts</h3>
                    <ul>
                        <li>Post 1</li>
                        <li>Post 2</li>
                        <li>Post 3</li>
                    </ul>
                </section>
            </main>
            <footer>
                <p>&copy; 2024 My Blog. All Rights Reserved.</p>
            </footer>
        </body>
        </html>
        """
    elif template == 'hospital_template':
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Our Hospital</title>
            <link rel="stylesheet" href="static/styles.css">
        </head>
        <body>
            <header>
                <h1>Welcome to Our Hospital</h1>
                <nav>
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">Departments</a></li>
                        <li><a href="#">Doctors</a></li>
                        <li><a href="#">Contact Us</a></li>
                    </ul>
                </nav>
            </header>
            <main>
                <section class="hero">
                    <h2>Providing Quality Healthcare</h2>
                    <p>Your health is our priority!</p>
                </section>
                <section class="departments">
                    <h3>Our Departments</h3>
                    <ul>
                        <li>Emergency</li>
                        <li>Pediatrics</li>
                        <li>Cardiology</li>
                    </ul>
                </section>
            </main>
            <footer>
                <p>&copy; 2024 Our Hospital. All Rights Reserved.</p>
            </footer>
        </body>
        </html>
        """
    elif template == 'restaurant_template':
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome to Our Restaurant</title>
            <link rel="stylesheet" href="static/styles.css">
        </head>
        <body>
            <header>
                <h1>Welcome to Our Restaurant</h1>
                <nav>
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">Menu</a></li>
                        <li><a href="#">About Us</a></li>
                        <li><a href="#">Contact</a></li>
                    </ul>
                </nav>
            </header>
            <main>
                <section class="hero">
                    <h2>Delicious Food Awaits</h2>
                    <p>Come dine with us!</p>
                </section>
                <section class="menu">
                    <h3>Our Menu</h3>
                    <ul>
                        <li>Dish 1</li>
                        <li>Dish 2</li>
                        <li>Dish 3</li>
                    </ul>
                </section>
            </main>
            <footer>
                <p>&copy; 2024 Our Restaurant. All Rights Reserved.</p>
            </footer>
        </body>
        </html>
        """
    elif template == 'fitness_template':
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Your Fitness Journey Begins</title>
            <link rel="stylesheet" href="static/styles.css">
        </head>
        <body>
            <header>
                <h1>Your Fitness Journey Begins Here</h1>
                <nav>
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">Classes</a></li>
                        <li><a href="#">Trainers</a></li>
                        <li><a href="#">Contact</a></li>
                    </ul>
                </nav>
            </header>
            <main>
                <section class="hero">
                    <h2>Join us for the best fitness experience.</h2>
                </section>
                <section class="classes">
                    <h3>Our Classes</h3>
                    <ul>
                        <li>Yoga</li>
                        <li>Cardio</li>
                        <li>Strength Training</li>
                    </ul>
                </section>
            </main>
            <footer>
                <p>&copy; 2024 Our Fitness Center. All Rights Reserved.</p>
            </footer>
        </body>
        </html>
        """
    elif template == 'travel_template':
        html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Welcome to Our Travel Agency</title>
            <link rel="stylesheet" href="static/styles.css">
        </head>
        <body>
            <header>
                <h1>Welcome to Our Travel Agency</h1>
                <nav>
                    <ul>
                        <li><a href="#">Home</a></li>
                        <li><a href="#">Destinations</a></li>
                        <li><a href="#">Packages</a></li>
                        <li><a href="#">Contact</a></li>
                    </ul>
                </nav>
            </header>
            <main>
                <section class="hero">
                    <h2>Explore the World with Us</h2>
                    <p>Your adventure starts here!</p>
                </section>
                <section class="destinations">
                    <h3>Popular Destinations</h3>
                    <ul>
                        <li>Paris</li>
                        <li>New York</li>
                        <li>Tokyo</li>
                    </ul>
                </section>
            </main>
            <footer>
                <p>&copy; 2024 Our Travel Agency. All Rights Reserved.</p>
            </footer>
        </body>
        </html>
        """
    else:
        html = "<h1>Template not recognized.</h1>"

    return html

@app.route('/')
def index():
    return '''
    <h1>Website Generator</h1>
    <form action="/generate" method="post">
        <label for="template">Write your preferred template name (e.g., ecommerce_template, portfolio_template):</label><br>
        <input type="text" name="template" id="template" required>
        <input type="submit" value="Generate">
    </form>
    '''

@app.route('/generate', methods=['POST'])
def generate():
    template = request.form.get('template')
    html_content = generate_website(template)
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

