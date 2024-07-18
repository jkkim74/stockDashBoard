from moviepy.editor import AudioFileClip, ImageClip
from PIL import Image
import os

# 오디오 파일 경로 설정
audio_file_path = "D:/movie/acousticbreeze.mp3"  # 오디오 파일 경로
image_file_path = "D:/movie/background_image.jpg"  # 로컬 이미지 파일 경로

# Load the audio file
audio_clip = AudioFileClip(audio_file_path)

# 이미지 파일이 존재하는지 확인
if os.path.exists(image_file_path):
    # Pillow를 사용하여 이미지를 로드
    img = Image.open(image_file_path)
    img.save("corrected_background_image.jpg")

    # 이미지 클립 생성
    image_clip = ImageClip("corrected_background_image.jpg", duration=audio_clip.duration)

    # 비디오 해상도에 맞게 이미지 크기 조정
    image_clip = image_clip.resize(height=720)  # Assuming 720p resolution

    # 오디오와 결합하여 최종 비디오 생성
    final_clip = image_clip.set_audio(audio_clip)

    # 비디오 내보내기
    output_video_path = "D:/movie/acoustic_breeze_video.mp4"
    final_clip.write_videofile(output_video_path, codec='libx264', fps=24)

    print("Video creation successful. Output saved as:", output_video_path)
else:
    print(f"Failed to find the image file at: {image_file_path}")
