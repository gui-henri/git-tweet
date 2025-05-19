import sys
import os
import io
import tweepy
import requests
from dotenv import load_dotenv

load_dotenv()

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

auto_tweet = os.getenv("AUTO_TWEET")
gemini_key = os.getenv("GEMINI_KEY")

if not gemini_key:
    print("Gemini key not found. Terminating...")
    quit()

gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={gemini_key}"

def gemini_improve_tweet(message: str):
    res = requests.post(
        gemini_url,
        headers={
            'Content-Type': "application/json",
        },
        json={
            'system_instruction': {
                'parts': [{
                        'text': "You're a Tweeter manager for an inovative indie developer. Your work is to take commit messages and make tweets from them. They should be simple, feel human, and atract peaple that want to see the indie developer work and inovate. You can use emojis, but avoid them. Dont't ask for feedback. Try making more than three words a tweet. Input example: feat: now Aluguel by proprietario and contratante return data about the Vaga and contact information. Output example: now you're able to get the data about the parking and contact information when you search your Parkings!"
                    }]
            },
            'contents': [{
                'parts': [{
                    'text': message
                }]
            }]
        }
    )
    if res.ok:
        return res.json()['candidates'][0]['content']['parts'][0]['text']
    else:
        print(res.status_code)
        print(res.text)

tweet = sys.argv[1][:280]
tweet = gemini_improve_tweet(tweet)

if not tweet:
    quit()    

print("Generated Tweet: ")
print(tweet)

if auto_tweet == "TRUE":
    api_key = os.getenv("TWITTER_API_KEY")
    api_secret = os.getenv("TWITTER_API_SECRET")
    access_token = os.getenv("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")

    if not access_token or not access_token_secret or not api_key or not api_secret:
        print("Twitter tokens are missing from enviroment variables")
        quit()

    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    client.create_tweet(text=tweet)