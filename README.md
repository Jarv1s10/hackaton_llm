# CSC23 Hackathon task: LLM-based Documentation bot for RevenueGrid

# Documentation 

## 1. How to run CHATBOT:

A. Locally run scripts:
   - Open terminal (command+J)
   - Go to api directory
    ```cd api/```
   - Run command
    ```uvicorn main:app --reload```


  - Open one more terminal
  - Go to telegram_bot directory
    ```cd telegram_bot/```
  - Run python script main.py
    ```python main.py```

  - Bot is ready to use! (Check if keys in .env files are still valid)


B. Using Docker-Compose file
  - Open Docker App
  - Right-click on docker-compose.yml and choose 'Compose Up' command. Check Docker Extension: there should be two images and two containers with green marks. 
  - Bot is ready to use! (Check if keys in .env files are still valid)

## 2. GitHub
Repository: https://github.com/Jarv1s10/hackaton_llm/tree/develop

## 3. Useful links:
* Documentation: https://docs.revenuegrid.com

## Preprocessing tasks:

- [x] Create a database
- [x] Think about structuring all articles in a tree
- [x] Extract data from markdown (split article by headers using the allowable number of tokens, delete html-tags)
- [x] Deal with missed 'product_name'
- [x] Preprocess data (delete unnecessary words such as "Click to show" / "1 min to read" / etc)
- [x] Load all data to the database

### Encoding tasks
- [x] Think about summarising text
- [x] Choose the best OpenAI embedding model
- [x] Create and save embeddings for each sub-article

### Chatbot logic:
- [x] Choose an open-source LLM
- [x] Choose apps for integration (Telegram / Slack / Teams / WhatsApp / ...)
- [x] Think about the logic of dialogue (how to save history for the following messages / proposed starting messages)
- [x] Think about the user's restrictions (number of messages, allowable topics, starting prompt for LLM)
- [x] Think about auto-messages for the start of a conversation
- [x] Think about additional data in answers (links to original articles, images/gifs with instructions)
- [x] Deploy the bot
- [x] Test chatbot on basic questions about RevenueGrid

