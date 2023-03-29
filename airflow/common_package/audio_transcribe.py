# %%
import whisper


# %%
class AudioTranscribe:
     
    # def __init__(self) -> None:
    #     self.model = whisper.load_model("base")


    def transcribe_adhoc_audio_link(self, audio_file_url, **kwargs) -> str:

        print("audio_file_url", audio_file_url)
        
        self.model = whisper.load_model("tiny")
        result = self.model.transcribe(audio_file_url)

        print(result)

        return str(result["text"])
    

    def transcribe_batch_audio_link(self, audio_file_urls, **kwargs) -> dict:
        self.model = whisper.load_model("tiny")

        result_with_files = {}
        for file in audio_file_urls:

            result = self.model.transcribe(file)
            result_with_files[file] = str(result["text"])

        # print(result)

        return result_with_files




# %%
# transcribe = AudioTranscribe()
# %%
# transcribe.transcribe_adhoc_audio_link('https://damg-team-5-assignment-4.s3.amazonaws.com/adhoc/podcast_2.mp3')

# %%
