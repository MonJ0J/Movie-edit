from flask import Flask, request, send_from_directory, flash, redirect, url_for
import os
import moviepy.editor as mp

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PROCESSED_FOLDER'] = 'processed'
app.secret_key = 'your_secret_key'

# Video processing functions from previous example

# Route to upload a video file
@app.route('/upload', methods=['POST'])
def upload_video():
    if request.method == 'POST':
        video = request.files['video']
        video.save(os.path.join(app.config['UPLOAD_FOLDER'], video.filename))
        return 'Video uploaded and saved.'

# Route to process a video (e.g., extract a clip)
@app.route('/process', methods=['POST'])
def process_video():
    if request.method == 'POST':
        video_file = request.form['video_file']
        start_time = float(request.form['start_time'])
        end_time = float(request.form['end_time'])
        output_file = request.form['output_file']
        
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], video_file)
        output_path = os.path.join(app.config['PROCESSED_FOLDER'], output_file)
        
        extract_clip(input_path, start_time, end_time, output_path)
        return 'Video processed.'

# Route to serve a processed video
@app.route('/processed/<path:filename>')
def serve_processed_video(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename)

if __name__ == '__main__':
    app.run()
