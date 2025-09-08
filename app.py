import gradio as gr
from utils import translate_text, text_to_speech, save_to_drive

def process_file(file):
    # Read Urdu text
    with open(file.name, "r", encoding="utf-8") as f:
        urdu_text = f.read()

    # Translate to English
    english_text = translate_text(urdu_text)

    # Generate audiobook
    mp3_path = text_to_speech(english_text)

    # Save both files to Google Drive
    save_to_drive("translated.txt", english_text)
    save_to_drive("audiobook.mp3", mp3_path, is_file=True)

    return english_text, mp3_path

demo = gr.Interface(
    fn=process_file,
    inputs=gr.File(label="Upload Urdu TXT file"),
    outputs=[gr.Textbox(label="Translated English"), gr.Audio(label="Audiobook (MP3)")],
    title="Urdu → English Translator + Audiobook",
    description="Upload an Urdu .txt file. It will translate to English and generate an audiobook."
)

if __name__ == "__main__":
    demo.launch()