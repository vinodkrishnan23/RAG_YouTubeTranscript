## Clone the Repository
```
git clone _githuburl_
cd RAG_YouTubeTranscript
```

## Create Python Virtual environment - rag_yt_transcript
```python -m venv ./rag_yt_transcript```

## Activate the python virtual environment
```source ./rag_yt_transcript/bin/activate```

## Install python dependencies in rag_yt_transcript 
```pip install -r requirement.txt```

## Modify .env file to incorporate your open ai key and mongodb connection string
```
OPENAI_API_KEY="ENTER-YOUR-OPEN-AI-KEY"
uri="ENTER MONGODB CONNECTION STRING - CAN USE COMPASS ONE AS WELL"
```

## Run the application

```
streamlit run main.py
```



