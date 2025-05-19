# Git Tweet

Automatically generate and (optionally) publish tweets based on your latest Git commit messages using a post-commit hook, Gemini, and the X API.

## 🔧 What It Does
This project automates tweeting about your code changes:

* Listens to Git commits via a post-commit hook.

* Improves commit messages into friendly, human-readable tweets using Gemini.

* Optionally posts to Twitter using tweepy and your Twitter developer credentials.

## ✅ Requirements
* Python 3.8+

* Git

* PowerShell (on Windows)

* Gemini API Key

* X Developer Account (if you want to post automaticaly)

## ⚙️ Setup Instructions

### 1. Clone this repo and set up the hooks
Place the scripts in your local repo's .git/hooks/ folder.

Make sure the post-commit hook is executable:

```bash
chmod +x .git/hooks/post-commit
```
### 2. Install Dependencies (or run setup.ps1)
Either install these Python packages:

```bash
pip install tweepy python-dotenv requests
```

or run ```setup.ps1```, that will install every lib you need for this hook to work.

### 3. Add Environment Variables
Create a .env file in your repo root:

#### X API credentials (only necessary if you want to post automaticaly)
```
TWITTER_API_KEY=your_key
TWITTER_API_SECRET=your_secret
TWITTER_ACCESS_TOKEN=your_token
TWITTER_ACCESS_TOKEN_SECRET=your_token_secret
```

#### Gemini API key
```
GEMINI_KEY=your_gemini_api_key
```

#### Auto tweet toggle
```
AUTO_TWEET=TRUE  # or FALSE if you only want to generate without posting
```

If ```AUTO_TWEET``` is false, you don't need to worry about the X API credentials.

## 🧪 Usage
Make a commit in your repo:

```git commit -m "feat: support user contact info"```

Then, the script will either print or tweet the result, depending on the ```AUTO_TWEET``` flag.

## 🧠 Example
Commit: ```git commit -m "fix: address empty response when user not found"```

Generated Tweet: ```No more empty screens when a parking spot isn't found – we fixed it! 🚗```


## 🛠️ Future Improvements
* Add support for Unix environments (replace tweet.ps1 with a Bash alternative)

* Custom templates or tone adjustment options
