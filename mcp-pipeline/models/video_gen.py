from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips

def stitch(scenes, images, audios):
    clips = []
    for img, aud in zip(images, audios):
        clip = ImageClip(img).set_duration(AudioFileClip(aud).duration)
        clip = clip.set_audio(AudioFileClip(aud))
        clips.append(clip)
    final = concatenate_videoclips(clips)
    output_path = "output/final_video.mp4"
    final.write_videofile(output_path)
    return output_path
