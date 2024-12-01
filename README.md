# Smart Steganography

## Description
A web application for hiding and extracting hidden data from images, videos, and audio using steganographic techniques. Utilizes AWS S3 for storage, DynamoDB for metadata, and Flask for the backend.

## Features
- Image Steganography (LSB Substitution)
- Video and Audio Steganography
- AWS Integration for Secure Storage

## Requirements
- Python 3.9+
- AWS S3 Bucket
- AWS Access Keys

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Set up AWS credentials in `app.py`.
3. Run the Flask server: `python app.py`.
4. Open `frontend.html` in a browser.

## AWS Services Used
- Amazon S3: File storage
- DynamoDB/RDS: Metadata management (Future Implementation)
- Elastic Beanstalk: Deployment
