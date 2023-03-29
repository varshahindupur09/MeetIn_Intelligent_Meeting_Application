# %%
import whisper


# %%
class AudioTranscribe:
     
    # def __init__(self) -> None:
    #     self.model = whisper.load_model("base")


    def transcribe_audio_link(self, audio_file_url, **kwargs) -> str:
        print(audio_file_url)

        self.model = whisper.load_model("base")

        result = self.model.transcribe(audio_file_url[1])

        print(result)

        return str(result["text"])




# %%
transcribe = AudioTranscribe()
# %%
transcribe.transcribe_audio_link(['', 'https://damg-team-5-assignment-4.s3.amazonaws.com/adhoc/podcast_2.mp3'])

# %%
