# Instead of the docs

## Prerequisites 

To run OSADA you need the following:
1. Database - MySQL or PostgreSQL
2. Access to LLM - currently we support OpenAI or Gemini

## Quickstart

Run OSADA with docker. To do it you need to provide a various environment variables. See all supported env variabled below.

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

## Environment variables

| Variable          | Description                                                                                    | Default      |
|-------------------|------------------------------------------------------------------------------------------------|--------------|
| `GOOGLE_API_KEY`  | Google API key to access Gemini models                                                         | `None`       |
| `OPENAI_API_KEY`  | OpenAI API key to access OpenAI models                                                         | `None`       |
| `LLM_PROVIDER`    | Large Language Model provider. Can be `gemini` or `openai`.                                    | `gemini`     |
| `LLM_CHOICE`      | Choose the model. For full list consult with the providers' manuals. Example: `gemini-1.5-pro` | ""           |
| `LLM_TEMPERATURE` | Model temperature                                                                              | 0            |
| `DB_TYPE`         | Database type. Can be `mysql` or `postgresql`.                                                 | `postgresql` |
| `DB_USERNAME`     | Database username                                                                              | ""           |
| `DB_PASSWORD`     | Database password                                                                              | ""           |
| `DB_HOSTNAME`     | Database hostname                                                                              | `localhost`  |
| `DB_NAME`         | Database name                                                                                  | ""           |
| `DB_PORT`         | Database TCP port                                                                              | 5432         |
