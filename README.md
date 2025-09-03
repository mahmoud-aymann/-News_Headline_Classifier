# 📰 News Headline Classifier

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange.svg)](https://scikit-learn.org)
[![Gradio](https://img.shields.io/badge/Gradio-3.0+-green.svg)](https://gradio.app)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An intelligent AI-powered application that automatically classifies news headlines into four main categories: **SPORTS**, **CRIME**, **EDUCATION**, and **COMEDY**. Built with machine learning and deployed as an interactive web application.

## 🚀 Live Demo

**Try it now**: [Hugging Face Spaces](https://huggingface.co/spaces/Ma1hmoud1/News_Headline_Classifier)

## ✨ Features

- 🎯 **Real-time Classification**: Instant headline categorization
- 📊 **Probability Scores**: Confidence levels for each category
- 🎨 **Clean UI**: User-friendly Gradio interface
- ⚡ **Fast Inference**: Optimized for quick predictions
- 🔄 **Auto-training**: Trains model on first run, caches for subsequent uses
- 📱 **Responsive Design**: Works on desktop and mobile

## 🛠️ Tech Stack

- **Machine Learning**: Scikit-learn, Multinomial Naive Bayes
- **Text Processing**: CountVectorizer with 1-3 n-grams
- **Web Interface**: Gradio
- **Data Processing**: Pandas
- **Model Persistence**: Joblib
- **Deployment**: Hugging Face Spaces

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

The classifier achieves high accuracy on the four target categories:
- **SPORTS**: Sports-related headlines
- **CRIME**: Crime and legal news
- **EDUCATION**: Educational content and school news
- **COMEDY**: Humorous and entertainment content

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
- Gradio for the intuitive web interface framework
- Hugging Face for providing free hosting for ML applications
- The open-source community for continuous inspiration

## 📈 Future Enhancements

- [ ] Support for more categories
- [ ] Real-time news API integration
- [ ] Model performance metrics dashboard
- [ ] Multi-language support
- [ ] Advanced text preprocessing options
- [ ] Model comparison tools

---

⭐ **If you found this project helpful, please give it a star!**