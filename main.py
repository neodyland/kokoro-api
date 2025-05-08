from fastapi import Query, FastAPI, Response
from src import tts, speakers, available_providers, default_speaker
import asyncio
import uvicorn
import os
from dotenv import load_dotenv

app = FastAPI()


@app.get("/tts", description="Text to Speech. Returns audio in WAV format.")
async def tts_endpoint(
    text,
    speaker: str = Query(default_speaker, enum=speakers),
):
    audiobyte = await tts(text, speaker, with_wav=True)
    if type(audiobyte) == str:
        return Response(
            content=audiobyte,
            media_type="text/plain",
            status_code=500,
        )
    return Response(
        content=audiobyte,
        media_type="audio/wav",
    )


@app.get("/speakers", description="List available speakers.")
async def speakers_endpoint():
    return speakers


async def main():
    load_dotenv()
    print("Available speakers:")
    print(speakers)
    print("Available providers:")
    print(available_providers())
    print("Testing TTS...")
    text = "生麦生米生卵、隣の客はよく書き食う客だ。"
    audiobyte = await tts(text, "alpha", with_wav=True)
    if type(audiobyte) == str:
        print(f"Error: {audiobyte}")
        return
    print(f"TTS test completed with wav length: {len(audiobyte)} bytes")
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))
    print(f"Starting server at {host}:{port}")
    config = uvicorn.Config(app, host=host, port=port)
    server = uvicorn.Server(config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main())
