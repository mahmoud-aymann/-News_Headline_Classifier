# 📰 News Headline Classifier

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange.svg)](https://scikit-learn.org)
[![Gradio](https://img.shields.io/badge/Gradio-3.0+-green.svg)](https://gradio.app)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A simple Natural Language Processing (NLP) project that classifies news headlines into four categories: **SPORTS**, **CRIME**, **EDUCATION**, and **COMEDY**. This is a beginner-friendly machine learning project demonstrating basic text classification using traditional ML techniques.

## 🚀 Live Demo

**Try it now**: [Hugging Face Spaces](https://huggingface.co/spaces/Ma1hmoud1/News_Headline_Classifier)

## ✨ Features

- 🎯 **Simple Classification**: Basic headline categorization into 4 categories
- 📊 **Probability Scores**: Shows confidence levels for each category
- 🎨 **Easy-to-use Interface**: Simple Gradio web interface
- ⚡ **Quick Training**: Fast model training on small dataset
- 🔄 **Model Caching**: Saves trained model for faster subsequent runs
- 📚 **Learning Project**: Perfect for NLP beginners

## 🛠️ Tech Stack

- **Machine Learning**: Scikit-learn, Multinomial Naive Bayes (simple baseline model)
- **Text Processing**: CountVectorizer with 1-3 n-grams (basic feature extraction)
- **Web Interface**: Gradio (easy web UI framework)
- **Data Processing**: Pandas (data manipulation)
- **Model Persistence**: Joblib (model saving/loading)
- **Deployment**: Hugging Face Spaces (free hosting)

## 📁 Project Structure

```
news-headline-classifier/
├── 📄 app.py                    # Main Gradio application
├── 🧠 news_classifier.py        # ML pipeline and training logic
├── 📋 requirements.txt          # Python dependencies
├── 📖 README.md                 # Project documentation
├── 🚫 .gitignore               # Git ignore rules
└── 📊 dataset_small.json       # Sample dataset (30 headlines)
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mahmoud-aymann/-News_Headline_Classifier.git
   cd -News_Headline_Classifier
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment**
   
   **Windows:**
   ```powershell
   .\.venv\Scripts\activate
   ```
   
   **macOS/Linux:**
   ```bash
   source .venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   - Navigate to the URL shown in terminal (usually `http://127.0.0.1:7860`)
   - Start classifying headlines!

## 🎯 How It Works

1. **Text Preprocessing**: Headlines are processed using CountVectorizer with 1-3 n-grams
2. **Model Training**: Multinomial Naive Bayes classifier learns from balanced dataset
3. **Prediction**: Real-time classification with probability scores
4. **Caching**: Trained model is saved and reused for faster startup

## 📊 Model Performance

This is a simple baseline model for educational purposes. The classifier works on the four target categories:
- **SPORTS**: Sports-related headlines
- **CRIME**: Crime and legal news  
- **EDUCATION**: Educational content and school news
- **COMEDY**: Humorous and entertainment content

**Note**: This is a basic implementation using traditional ML techniques. For production use, consider more advanced models like transformers or deep learning approaches.

## 🔧 Configuration

### Custom Categories
To modify the classification categories, update the `CATEGORIES` list in `news_classifier.py`:

```python
CATEGORIES = ['SPORTS', 'CRIME', 'EDUCATION', 'COMEDY', 'NEW_CATEGORY']
```

### Dataset
- The app uses a sample dataset (`dataset_small.json`) for demonstration
- For production, replace with your own dataset following the same JSON format
- Each entry should contain `headline` and `category` fields

## 🌐 Deployment

### Hugging Face Spaces
This project is deployed on Hugging Face Spaces for easy access and sharing.

### Local Deployment
For local deployment with custom settings:

```bash
python app.py --server.port 7861 --server.name 0.0.0.0
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Mahmoud Ayman**
- GitHub: [@mahmoud-aymann](https://github.com/mahmoud-aymann)
- Project Link: [News Headline Classifier](https://github.com/mahmoud-aymann/-News_Headline_Classifier)

## 🙏 Acknowledgments

- Thanks to the Scikit-learn team for the excellent ML library
- Gradio for the simple web interface framework
- Hugging Face for providing free hosting for ML applications
- My instructor and the learning community for guidance
- The open-source community for continuous inspiration

## 📈 Future Enhancements

- [ ] Add more categories (POLITICS, TECHNOLOGY, etc.)
- [ ] Implement more advanced models (SVM, Random Forest)
- [ ] Add model evaluation metrics (accuracy, precision, recall)
- [ ] Improve text preprocessing (stop words removal, stemming)
- [ ] Add support for larger datasets
- [ ] Implement cross-validation for better model evaluation

---

⭐ **If you found this project helpful, please give it a star!**
