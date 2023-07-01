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

### Current tasks:

- [x] Create a database
- [ ] Preprocess and extract text from markdown
- [ ] Create a docs knowledge tree
- [ ] Think about summarising text
- [ ] Think about user's restrictions
- [ ] Think about auto-messages for the start of a conversation
- [ ] Think about the logic of dialogue
- [ ] Choose an open-source LLM model
