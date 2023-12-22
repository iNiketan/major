# Major
Major is a Django-based web app that plays a YouTube video and records your expressions using a webcam. It also rates the video based on your expressions using a facial expression detection model trained on the kaggle Face expression recognition dataset. Major can help you provide rating to videos that match your preferences and emotions.

### Features
Play YouTube videos from various categories
Record your facial expressions using a webcam
Detect your emotions using a pre-trained Facial Expression Recognition model
Rate the video based on your expressions
Display the ratings and emotions of other users

#### Installation
To run Major locally, you need to have Python, Django, and OpenCV installed on your machine. Then, follow these steps:

<!-- start:code block -->

Clone this repository
git clone https://github.com/iNiketan/major.git cd major

Install dependencies
pip install -r requirements.txt

Create and apply migrations
python manage.py makemigrations python manage.py migrate

Start the server
python manage.py runserver

Open http://localhost:8000 in your browser
open http://localhost:8000 <!-- end:code block -->
