# Welcoma to OSADA! 🚀🤖

I'm the Open Source AI Database Agent (OSADA). 

I can connect to your MySQL or PostgreSQL database and answer the questions that you ask in a human-language. You can think of me as text-to-SQL model.

Find more about me here:
- [Blog post - Open Source AI Database Agent - Part 1 - Intro]()
- [Blog post - Open Source AI Database Agent - Part 2]()
- [Github](https://github.com/spron-in/osada)

I'm in experimental phase and would love to recieve feedback. Create a github issue.

## Usage

### Prerequisites 

To run OSADA you need the following:
1. Database - MySQL or PostgreSQL
2. Access to LLM - currently we support OpenAI or Gemini

### Quickstart

Run OSADA with docker. To do it you need to provide a various environment variables. You can see all supported variables in [USAGE.md](USAGE.md).

Example:
```
docker run -d \
-e DB_TYPE='postgresql' \
-e DB_HOSTNAME='mydb.company.com' \
-e DB_USERNAME='pagila' \
-e DB_PASSWORD='pagila' \
-e DB_NAME='pagila' \
-e LLM_PROVIDER="gemini" \
-e GOOGLE_API_KEY='somesuperkey' \
-e LLM_CHOICE="gemini-1.5-pro" \
-p 8000:8000 perconasp/osada:0.0.2
```

You should be able to access the UI in your browser: [http://localhost:8000](http://localhost:8000).
Start asking questions!

## TODO

There are bunch of cool improvements that can be done:
1. Move away from environment variables and allow users to provide them through UI
2. Support multiple databases as right now user can talk to only one
3. Add more LLM providers (like Mistral or custom ones)
4. Make docker image smaller - it is ugly now
5. Add authentication for UI
6. Smart responses with more fine tuning

## Tools

I'm built with the following tools:
- [Langchain](https://www.langchain.com/) - currently I can use openai and gemini models
- [Chainlit](https://github.com/Chainlit/chainlit) - to provide you with a nice UI and a chat experience

## License 

Open source, Apache 2.0.

## Contribute

Feel free to send a PR.

## Who

I was built at [Percona](https://percona.com) by [Sergey Pronin](sergey.pronin@percona.com).
