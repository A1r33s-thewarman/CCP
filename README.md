# Sinhala Code-Mixed Text Translator and Sentiment Analyzer

> The purpose of this application is to identify mixed language texts, whether it is written in
Singlish or English, and convert it to proper Sinhala sentence while performing a
sentiment analysis and BLEU score evaluation.

### environment 
- Windows 8 or later 
- Python 3.10.5 or later
- NodeJs 16.16.0 or later

##How to run
Navigate to cloned project using command prompt.
####Start Backend Server
- Install python modules
```bash
pip install -r requirements.txt
```
- Start server
```bash
python server.py
```
- If the server properly started, below output will display.
```python
Serving Flask app 'server' (lazy loading)
Environment: production
WARNING: This is a development server. Do not use it in a production deployment.
Use a production WSGI server instead.
Debug mode: off
Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
```

####Run frontend application

- Navigate to *Sinhala-Translator-translator/translate* directory.
```python
cd Sinhala-Translator-translator/translate
```
- Install node modules
```bash
npm install
```
- Start application
```bash
npm start
```
