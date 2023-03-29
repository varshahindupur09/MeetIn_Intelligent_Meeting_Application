# %%
import whisper


# %%
class AudioTranscribe:
     
    def __init__(self) -> None:
        self.model = whisper.load_model("base")


    def transcribe_audio_link(self, audio_file_url: str) -> str:
        
        result = self.model.transcribe(audio_file_url)

        print(result)

        return result["text"]




# %%
transcribe = AudioTranscribe()

# %%
transcribe.transcribe_audio_link("https://damg-team-5-assignment-4.s3.amazonaws.com/adhoc/podcast_2.mp3")
# %%
