# Trendyol iPhone Price Tracker & Gemini AI Analyzer

This project is a modular web scraping and artificial intelligence-powered analysis pipeline. It automatically collects iPhone listing data from Trendyol using Selenium, stores it in a local database, and analyzes market trends using Google's Gemini AI.

## 🚀 Features
- **Automated Web Scraping**: Extracts product details, prices, and seller info from Trendyol via Selenium (`trendyol_iphone.py`).
- **Database Management**: Stores and structures historical price data using SQLite (`oku.py`, `analiz.py`).
- **AI-Powered Insights**: Integrates Google Gemini AI to analyze price trends and provide smart summaries (`ai_analiz.py`).
- **Security First**: Sensitive credentials and database files are excluded from version control using `.gitignore`.

## 🛠️ Tech Stack
- **Python** (Core language)
- **Selenium** (Web automation & scraping)
- **Google GenAI SDK** (Gemini AI integration)
- **SQLite** (Local database)

## 📦 Installation & Setup

1. Clone the repository:
   ```bash
   git clone [https://github.com/21deniz13/trendyol-iphone-gemini-analyzer.git](https://github.com/21deniz13/trendyol-iphone-gemini-analyzer.git)