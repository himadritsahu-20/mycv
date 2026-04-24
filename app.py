from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cv')
def cv():
    # Your CV data - customize this section
    cv_data = {
        'personal_info': {
            'name': 'Himadri Tanaya Sahu',
            'title': 'Full Stack Developer',
            'email': 'himadri.tsahu@email.com',
            'phone': '+91 9776464734',
            'location': 'Balasore, Odisha',
            'linkedin': 'https://www.linkedin.com/in/himadri-tanaya-sahu-ba5738379/',
            'github': 'https://github.com/himadritsahu-20'
        },
        'experience': ['Fresher'
     ],
        'education': [
            {
                'degree': 'Computer Science Engineering in Artificial Intelligence and Machine Learning',
                'school': 'Kalinga Institute of Technology',
                'duration': '2024 - 2028',
                'gpa': '8.0/10.0'
            }
        ],
        'skills': [
            'Python', 'Java','JavaScript','Tailwind CSS','Node.js','FastAPI',
            'Django','Flask','MongoDB','PostgreSQL','MySQL','Redis',
            'SQLite','Azure', 'React','Vercel','Jyputer',
            'Numpy','Pandas','Scikit-learn','OpenCV',
            'REST APIs','Postman', 'GitHub',
            'Docker', 'AWS', 
        ],
        'projects': [
            {
                'name': 'E-Commerce Platform',
                'description': 'Full-stack e-commerce solution with payment integration',
                'technologies': 'React, Node.js, MongoDB, Stripe',
                'link': 'https://github.com/himadritsahu-20'
            }
        ]
    }
    return render_template('cv.html', cv=cv_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)