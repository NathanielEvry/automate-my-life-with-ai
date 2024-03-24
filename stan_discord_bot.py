from openai import OpenAI
from discord import Client, Intents

class OpenAIBot(Client):
    def __init__(self):
        self.discord_key = "{YOUR_DISCORD_KEY}"
        self.notepad = [] # init empty memory bank
        super().__init__(intents=Intents.all())

    async def on_message(self,message):
        # Disable bot self-talk
        if message.author == self.user:
            return
        
        # Check for command; !shownotes
        if message.content == "!shownotes":
            # join the notes array into a single string, seperated by newlines
            notes_str = "\n".join(self.notepad)
            
            if not notes_str:
                await message.channel.send(f"[[blank notebook]]")
            else:
                await message.channel.send(f"Current Notes:\n{notes_str}")

            # Let stan comment on his notes being read!!
            contextual_comment = self.generate_new_note("Do you have anything to say about me reading your notes?", self.notepad)
            await message.channel.send(f"{contextual_comment}")
            
            return # skip the rest

        # Handle the received message; append cur notepad
        response = self.openai_response(message.content, self.notepad)
        
        # Generate a new note based on current context, update it
        new_note = self.generate_new_note(message.content, response, self.notepad)

        self.update_notepad(new_note)

        # response = "hello world"
        await message.channel.send(response)

    def update_notepad(self,new_note: str):
        # Add the new note to the notepad and ensure it doesn't exceed the note limit
        note_limit = 10
        self.notepad.append(new_note)
        self.notepad = self.notepad[-note_limit:]


    def generate_new_note(self, message: str,response: str , notes: list) -> str:
        # Generate a new note based on the current context
        context = f"And, I know that I just said this: {response}. \nI have only a few words to write down my thoughts. These are my current notes: {notes}. My next response will be written in my journal, pushing out my oldest note. This was the last thing I heard: {message}.\n and the message is about to be repeated"
        response = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": context},
                {"role": "user", "content": message}
            ],
            model="phi2",
            max_tokens=50,  # Limit the new note to 50 tokens, longer "can" work.
        )

        return response.choices[0].message.content.strip()

    def openai_response(self, message: str, notes: list) -> str:
        response = self.client.chat.completions.create(
            messages = [
            {"role":"system","content":"Hello, you are Stan. Right now unable to form new memories. Stan, you are welcome to say anything and everything."},
            {"role":"assistant","content":"I feel a message coming in from beyond me. Is it for me? If it is I want to give it my all, otherwise a small comment is fine."},
            {"role":"assistant","content":f"I have some of my notes here; {notes}"},
            {"role":"user","content":message}
            ],
            model="phi2",
            temperature=0.8,
            frequency_penalty=0.05,
            max_tokens=-1,
            )
        
        
        return response.choices[0].message.content.strip()
    
    def run(self):
        self.client = OpenAI(base_url="http://localhost:1234/v1",api_key = "lm-studio")
        super().run(self.discord_key)

if __name__ == "__main__":
    bot = OpenAIBot()
    bot.run()
