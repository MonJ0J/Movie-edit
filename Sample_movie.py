import moviepy.editor as mp

# Function to extract a clip from a video
def extract_clip(video_file, start_time, end_time, output_file):
    video = mp.VideoFileClip(video_file)
    clip = video.subclip(start_time, end_time)
    clip.write_videofile(output_file)

# Function to merge multiple video files
def merge_videos(video_files, output_file):
    clips = [mp.VideoFileClip(video_file) for video_file in video_files]
    merged_clip = mp.concatenate_videoclips(clips)
    merged_clip.write_videofile(output_file)

# Function to transcode a video to a different format
def transcode_video(video_file, output_format, output_file):
    video = mp.VideoFileClip(video_file)
    video.write_videofile(output_file, codec=output_format)
# Extract a clip from a video
input_video = "input_video.mp4"
start_time = 10  # seconds
end_time = 20  # seconds
output_clip = "output_clip.mp4"
extract_clip(input_video, start_time, end_time, output_clip)

# Merge multiple video files
video_files = ["video1.mp4", "video2.mp4", "video3.mp4"]
output_merged = "merged_videos.mp4"
merge_videos(video_files, output_merged)

# Transcode a video to a different format (e.g., from MP4 to AVI)
input_video = "input_video.mp4"
output_format = "libx264"  # H.264 codec (for MP4 files)
output_transcoded = "output_video.avi"
transcode_video(input_video, output_format, output_transcoded)
