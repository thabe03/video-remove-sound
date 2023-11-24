from moviepy.editor import VideoFileClip, AudioFileClip

# Charger la vidéo et extraire l'audio existant
video = VideoFileClip("video.mp4")
old_audio = video.audio

# Charger le nouveau son
new_audio = AudioFileClip("new_sound.m4a")

# Ajouter le nouveau son à la vidéo
video = video.set_audio(new_audio)

# Enregistrer la vidéo avec le nouveau son
video.write_videofile("new_video.mp4")

#ffmpeg