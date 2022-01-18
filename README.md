
#  API Key Scraper
Get public API keys from Github and retrieve them 


## Installation

Install requirements

```bash
  pip install -r requirements.txt
```
    
## Demo

Insert gif or link to demo


## Run

Clone the project

```bash
  git clone https://github.com/Loule95450/API-Key-Scraper.git
```

Go to the project directory

```bash
  cd API-Key-Scraper
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the script

```bash
  python3 main.py
```


## FAQ

#### What is API URL ?

To call my api, I have to use a URL (or a line of code).

Let's say I want to call the YouTube API, I use: `https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=1234&type=video&order=date&maxResults=100&key=AIza...`.

So I give as much information as possible to get more results, but not too much information because I would get results that have nothing to do with the API key that I want to scrape.
So I give my program this information: `googleapis.com/youtube/v3/search?part=snippet &key=`. The program will then read that I am looking for a key that is located after the `&key=` and a key that belongs to `googleapis.com`.

#### What is API key start?

The first characters of an API key usually start with same. 

Let's say I want to scrape the Google API. I notice that all Google keys start with `AIzaSy`. So I reply to the `AIzaSy` program

#### What is Github API
To scrape keys. You will need to create a GitHub key.

* Go to the GitHub [key creation page](https://github.com/settings/tokens/new)

* Create a key with the `public_repo` parameter

* Once created, you just have to paste it in the program
## Contributing

Contributions are always welcome!

<a href="https://github.com/Loule95450/API-Key-Scraper/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Loule95450/API-Key-Scraper" />
</a>

Please adhere to this project's `code of conduct`.

