# CSC23 Hackathon task: LLM-based Documentation bot for RevenueGrid

### Useful links:
* Documentation: https://docs.revenuegrid.com
* Database connection:
  ```
  import weaviate

  client = weaviate.Client(
    url="https://hackaton-cluster-lnypogrq.weaviate.network",
    auth_client_secret=weaviate.AuthApiKey(api_key="Oa46IoB9HwXqOssR8IpwsWgiSFyrjm8IWuZu"),
  )
  ```

### Preprocessing tasks:

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
- [ ] Think about the logic of dialogue (how to save history for the following messages / proposed starting messages)
- [ ] Think about the user's restrictions (number of messages, allowable topics, starting prompt for LLM)
- [ ] Think about auto-messages for the start of a conversation
- [ ] Think about additional data in answers (links to original articles, images/gifs with instructions)
- [x] Deploy the bot
- [ ] Test chatbot on basic questions about RevenueGrid

