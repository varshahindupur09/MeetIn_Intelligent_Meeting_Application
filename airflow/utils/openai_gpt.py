# %%
import openai
from dotenv import load_dotenv
import os

# %%
load_dotenv()


# %%
class OpenAIGPT:

    def __init__(self) -> None:
        openai.api_key = os.environ.get('OPEN_AI_API_KEY')

    def generate_questions_for_transcribed_text(self, text) -> str:
        text = 'content ="'+ text +'."'+ "Ask 4 questions about this given content."

        completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", 
                messages = [
                    {'role': 'user', 'content': text}
                ],
                temperature = 0.75 
            )


        return completion.choices[0].message.content



# %%
gpt = OpenAIGPT()


gpt.generate_questions_for_transcribed_text("The thread is what's the craziest way you found out your partner was cheating on you on obviously responses were someone sent this to me And I'm glad I didn't read it gang. I'm glad I didn't read it. Yeah, go on This is a tweet another reply his waves were her Twitter header He's waves were her Twitter header. Yeah, how how pristine are these ways? I'm fine for them to like oh, that's my man. That's that's James. I know those waves anywhere reply I would have shaved his head while he slept. Oh His ways how can not that's impossible you can't close my waves Like oh bro, also don't ever use my ways as your Twitter header. Don't ever use my ways. I don't care if they're back Their mind also this is a yeah, so yeah took a picture of next man's waves and said this has to be my Twitter header Well, come how paying are these waves? Forlishness brother. All right, here you go My study abroad roommate literally jumped out of a bed and said something is wrong Called her boyfriend back home in the US and said are you cheating on me right now? This man goes And hangs up we panic waiting for him to answer her calls or call back He goes I'm so sorry a girl came over to work on a project and I didn't mean to but we were hooking up when you called My friend fell in a stomach from Italy insane That's that's important. I don't think that's possible bro. It's my said And hung up I'm not calling back and I'm not taking back a long distance team blocked. Yeah, it's a wrap This you live in Italy because I'm not dealing with this confrontation. I just nothing you could do about it Right literally nothing you could do on it. I would have done exactly the same as him. Yeah, I was at the phone about hello Are you cheating on me right now? Hang up and that's the end of it. I'll throw my phone and carry on with my cheek. I'll do it I'm not hard. It's I have to compose myself. It'll take a couple of minutes my thing will be like you Right Don't work the shovel time. Yeah my tool shrewled up because I'll be scared. Yeah, you shake it. Yeah, shake it Rocks kids. Yeah, yeah, I'm not I'm not texting on nothing. Yeah, that's hilarious Next one he sent me a playlist He made for me on Spotify. I knew I already had five likes My sense of five things bro. I made this playlist for you Already and she was last it already had five likes I think that would be my like my gaslight you flip. Yeah, yeah, yeah, yeah, yeah, how has this got five likes? Like I don't understand yeah, how have you waited until it's got five lives to listen to it? Because all the other hosts were listening to it. They click place straight away They all follow the link immediately immediately what what you do it? Yeah, it's got five likes before you've jumped on What does it say about you thanks? Let's say the pressure of me that wasn't actually say about you really on it or not if you're not on it Tell me I'll send it to someone else. Yeah, I'll delete the link That simple straightforward. I'll delete the link Um I pulled in early to his mom's birthday pie to help set up and his mom said he was in the room He was in his room to find out his best friend where he was bending Bending bending Jesus Christ He had a dream. I had a dream. He was she and after he spontaneously told me he was going to leave for work trip to Texas Uh found out he swooped a girl up at Arkansas on his way there the same girl in my dream CREPTAV CREPTA Facebook and found his boots in the back of the mirror selfie in the hotel. I saw red. Oh my god These teams are lies. I'm all these women and the fucking The lion's pro What's the word I'm looking for their their pro um pro this pro something. I'm sure there's a way What premonition premonition is one of the dreams of premonitions these these these visions that they're having Bro is it's jerry. Yeah, yeah, come on like Sandra Bullock. Oh shot. You're a liar. You hacked his phone. You just sat Yeah, yeah, yeah, yeah, yeah, yeah, this dream stuff is all he picked up someone in Arkansas the same girl from my dream shot your mouth Shot your actual mouth, bro. Mad. Mad next one. I was watching her his daughter and she told me about how her had dad and some other chick went to Disney World I didn't even start the conversation. I was just there curling my hair and she was spilling all the beans Wow Watching his daughter She just started spilling the beans He took my dad took. No, no, no, no, no, no, no, no, no, no, no, no, no Keep it in check whose team are you actually? Oh it's tough. I was sat there curling my hair She just started running up. Mouth say stuff. They're gas she knew where she was doing as well. Why would you tell me this yeah? Yeah? Yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, she wouldn't let her out the picture oh facts She went out the pictures the new things bell the new things actually bear the new thing we're doing a Disney Yeah, yeah, yeah, yeah, yeah, yeah, yeah, yeah, who even are you and why are you looking after me facts? Why are you only here when Dave's not here? Question that needs to be answered because when dad is with me There's another thing and we're doing that doing stuff. Yeah, yeah, yeah I'm gas then I'm happy all the time anytime you're here. He leaves He leaves and it's just two of us in these four walls and it's dark Yeah, it's dark and you don't play with me. You just sit there doing your hair Why can't you do your hair at your own house? Why do you have to be here facts? Who are you who even are you? You know what yeah, my dad doesn't even like you. He actually doesn't like you because he's a cheat He told me to tell you he told me to tell you But after today, yeah, be gone before he gets home He's done He got before he gets home Oh last one the girl I went to the same church with befriended one one another and she's showed me a picture of her boyfriend That's so stressful These man need to if they're gonna cheat they need to like international Yeah, yeah, yeah, yeah, yeah International International cheat because you got that's not an eventually this allowed to happen. Yeah, yeah, it's things that I just don't have a picture of my boyfriend Not man")

# %%
