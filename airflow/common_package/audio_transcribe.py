# %%
import whisper
import ast


# %%
class AudioTranscribe:
     
    # def __init__(self) -> None:
    #     self.model = whisper.load_model("base")


    def transcribe_adhoc_audio_link(self, **kwargs) -> str:
        model = whisper.load_model("tiny")
        result = model.transcribe(kwargs['dag_run'].conf.get('audio_file_url'))

        print(result)

        return str(result["text"])
    

    def transcribe_batch_audio_link(self, audio_file_urls_string: str, **kwargs) -> str:
        model = whisper.load_model("tiny")
    
        audio_file_urls = ast.literal_eval(audio_file_urls_string)

        result_with_files = dict()
        for i in range(len(audio_file_urls)):
            if "mp3" in audio_file_urls[i]:
                result = model.transcribe(audio_file_urls[i])
                result_with_files[audio_file_urls[i]] = str(result["text"])
            else:
                print("Not a valid file", audio_file_urls[i])

        return str(result_with_files)




# %%
# transcribe = AudioTranscribe()
# %%
# "mp3" in "https://damg-team-5-assignment-4.s3.amazonaws.com/adhoc/podcast_2.mp3"
# transcribe.transcribe_adhoc_audio_link('https://damg-team-5-assignment-4.s3.amazonaws.com/adhoc/podcast_2.mp3')

# %%
