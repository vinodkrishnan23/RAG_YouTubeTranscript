## Pre-requisite
**Python3** must be installed <br />
<br />
Your need an **Open AI key**<br />
<br />
Create database in your cluster by name - **youtube** <br />
<br />
Create collection in this database by name - **transcripts** <br />
<br />
Create a vector search index as per below definition on above collection by name **vector_index**<br />
```
{
  "fields": [
    {
      "numDimensions": 1536,
      "path": "embedding",
      "similarity": "cosine",
      "type": "vector"
    }
  ]
}
```
## Clone the Repository
```
git clone https://github.com/vinodkrishnan23/RAG_YouTubeTranscript.git
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

## Key in Youtube URL and question you want to ask
```
Youtube URL - https://www.youtube.com/watch?v=QvKMwLjdK-s
Question - What is HNSW
```



