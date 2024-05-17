# Importing necessary libraries
import newspaper
from gtts import gTTS


# Function to extract text from the provided URL
def extract_text(url):
    article = newspaper.Article(url)
    article.download()
    article.parse()
    return article.text


# Function to convert text to speech and save it as an audio file
def text_to_speech(text, filename):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)


# Main function
def main():
    # URL of the web article
    url = input("Enter the URL of the web article: ")

    try:
        # Extracting text from the web article
        article_text = extract_text(url)

        # Converting text to speech and saving it as an audio file
        filename = 'article_audio.mp3'
        text_to_speech(article_text, filename)

        print(f"Audio file '{filename}' has been created successfully!")

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    main()
