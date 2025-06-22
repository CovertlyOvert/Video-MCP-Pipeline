from fastapi import FastAPI, Request
from models import gpt_script, image_gen, video_gen, audio_gen

app = FastAPI()

@app.post("/start")
async def start_pipeline(req: Request):
    data = await req.json()
    topic = data["topic"]

    scenes = gpt_script.generate(topic)
    image_paths = image_gen.generate_images(scenes)
    audio_paths = audio_gen.generate_audio(scenes)
    final_video = video_gen.stitch(scenes, image_paths, audio_paths)

    return {"video_path": final_video}
