# AGS Worksheet Generator

A full-stack web application for generating Common Core-aligned mathematics worksheets with automated grading capabilities. Built with Flask, React, and a custom computer algebra engine.

**To check out some of the core logic, [https://github.com/smyu24/AGSWkstGenerator/blob/main/app/logic/AGS1/loader.py](https://github.com/smyu24/AGSWkstGenerator/blob/main/app/logic/AGS1/loader.py)**

[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

## 🚀 Features

- **Custom Problem Generation**: Dynamically generates math problems using a proprietary computer algebra engine
- **Common Core Alignment**: All worksheets align with educational standards
- **Automated Grading**: Fine-tuned TrOCR model for handwriting recognition (94.8% accuracy)
- **LaTeX Integration**: Professional-quality PDF worksheet generation with MathJax rendering
- **User Management**: Complete authentication system with role-based access (students, teachers, parents)
- **Real-time Analytics**: Performance tracking and progress monitoring
- **Classroom Integration**: Multi-classroom support for educators

## 🛠️ Technology Stack

### Backend
- **Framework**: Flask (Python)
- **Database**: MySQL with SQLAlchemy ORM
- **Math Engine**: SymPy, NumPy, SciPy
- **Authentication**: Flask-Login, WTForms
- **PDF Generation**: LaTeX with custom optimization

### Frontend
- **Framework**: React.js
- **Styling**: Bootstrap, Material-UI components
- **Math Rendering**: MathJax for client-side rendering
- **Data Visualization**: Pandas integration

### Machine Learning
- **OCR Model**: Fine-tuned TrOCR on IAM handwriting dataset
- **Performance**: 94.8% character recognition accuracy

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8+
- MySQL Server
- Node.js (for React frontend)

### Backend Setup
```bash
# Clone the repository
git clone https://github.com/smyu24/AGS_Worksheet_Generator.git
cd AGS_Worksheet_Generator

# Install Python dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your database credentials and secret keys

# Initialize database
python init_db.py
```

### Frontend Setup
```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Build for production
npm run build
```

### Running the Application
```bash
# Start the Flask backend
python app.py

# The application will be available at http://localhost:5000
```

## 📁 Project Structure

```
AGS_Worksheet_Generator/
├── app/
│   ├── logic/
│   │   └── AGS1/
│   │       └── loader.py          # Core problem generation engine
│   ├── models/                    # Database models
│   ├── routes/                    # API endpoints
│   └── templates/                 # Jinja2 templates
├── frontend/
│   ├── src/
│   │   ├── components/           # React components
│   │   └── pages/               # Main application pages
│   └── public/
├── ml/
│   └── ocr_model/               # TrOCR fine-tuning scripts
└── docs/                        # Documentation
```

## 🔍 Core Components

### Problem Generation Engine
The heart of the application lies in the custom computer algebra engine ([`loader.py`](https://github.com/smyu24/AGS_Worksheet_Generator/blob/main/app/logic/AGS1/loader.py)) which:
- Generates algebraically diverse problems
- Ensures Common Core alignment
- Implements difficulty scaling algorithms
- Supports multiple problem types and formats

### Database Schema
```sql
-- User Management
CREATE TABLE users (
    uid INTEGER AUTO_INCREMENT PRIMARY KEY,
    username TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    email TEXT,
    role ENUM('student', 'teacher', 'parent'),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Problem Generation
CREATE TABLE learning_targets (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    ccss_standard TEXT NOT NULL,
    difficulty_level INTEGER,
    problem_template TEXT,
    solution_template TEXT
);

-- Performance Tracking
CREATE TABLE student_progress (
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    user_id INTEGER,
    worksheet_id INTEGER,
    completion_rate DECIMAL(5,2),
    accuracy_rate DECIMAL(5,2),
    time_spent INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(uid)
);
```

## 🎯 API Endpoints

### Core Functionality
- `POST /api/generate-worksheet` - Generate custom worksheet
- `POST /api/grade-worksheet` - Submit worksheet for automated grading
- `GET /api/progress/:userId` - Retrieve student progress analytics

### User Management
- `POST /api/auth/register` - User registration
- `POST /api/auth/login` - User authentication
- `GET /api/classrooms` - Retrieve assigned classrooms

## 🧪 Testing

```bash
# Run backend tests
python -m pytest tests/

# Run frontend tests
cd frontend && npm test

# Run integration tests
python -m pytest tests/integration/
```

## 🚀 Deployment

The application is deployed at [ericyu.dev](http://ericyu.dev) using:
- **Hosting**: AWS EC2 with nginx reverse proxy
- **Database**: AWS RDS MySQL instance
- **CDN**: CloudFront for static asset delivery
- **CI/CD**: GitHub Actions for automated deployment

## 📈 Performance Optimizations

- **Lazy Loading**: Implemented for LaTeX compilation and MathJax rendering
- **Database Indexing**: Compound indexes on frequently queried columns
- **Caching**: Redis caching for generated problems and user sessions
- **Asset Optimization**: Minified JavaScript and CSS with gzip compression

## 🛣️ Roadmap

### Short Term (v2.0)
- [ ] Interactive HTML worksheets with live problem solving
- [ ] Enhanced accessibility features (ADHD-friendly fonts, bionic reading)
- [ ] Mobile-responsive redesign
- [ ] Real-time collaborative features

### Long Term (v3.0)
- [ ] Advanced analytics dashboard for educators
- [ ] Integration with popular LMS platforms (Canvas, Blackboard)
- [ ] Multi-language support
- [ ] AI-powered personalized learning paths

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Seung-min Yu**
- GitHub: [@smyu24](https://github.com/smyu24)
- LinkedIn: [seungmin-yu](https://linkedin.com/in/seungmin-yu)
- Email: smyu24@gmail.com

## 🙏 Acknowledgments

- Thanks to the educators at partner high schools for feedback and testing
- IAM Handwriting Dataset contributors for training data
- Open source community for the foundational libraries

---

*Built with ❤️ for educators and students everywhere*
