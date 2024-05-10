from langchain_community.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
#from langchain_community.vectorstores import MongoDBAtlasVectorSearch
from langchain_mongodb import MongoDBAtlasVectorSearch
from langchain_openai import OpenAIEmbeddings
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

from dotenv import load_dotenv

load_dotenv()
embeddings = OpenAIEmbeddings()

def create_vectordb_from_youtube_url(video_url:str) -> MongoDBAtlasVectorSearch:
    # Load the transcript from the video
    yt_loader = YoutubeLoader.from_youtube_url(video_url, add_video_info=True)
    transcript = yt_loader.load()

    # Split the transcript into sentences
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    docs=text_splitter.split_documents(transcript)
    # Create a new client and connect to the server
    client = MongoClient(os.getenv("uri"), server_api=ServerApi('1'))
    mdb=client.youtube
    mcollection = mdb.transcripts

    db = MongoDBAtlasVectorSearch.from_documents(
        documents=docs,
        embedding=OpenAIEmbeddings(disallowed_special=()),
        collection=mcollection,
        index_name="vector_index"
    )
    #print(docs)
    return db

def create_db():
    client = MongoClient(os.getenv("uri"), server_api=ServerApi('1'))
    mdb=client.youtube
    mcollection = mdb.transcripts
    return MongoDBAtlasVectorSearch(mcollection,embedding=OpenAIEmbeddings(),text_key="text",index_name="vector_index",relevance_score_fn="cosine")
def get_response_from_query(db,query,k=4):
    # 8192 tokens is the maximum length for the OpenAI API
    #docs = db.similarity_search(query,k=k,post_filter_pipeline=[{"$unset":["embedding","source","title","description","view_count","thumbnail_url","publish_date","length","author"]}])
    docs = db.similarity_search(query,k=k,post_filter_pipeline=[{"$project":{"_id":0,"text":1,"score":1}}])
    #docs_page_content = " ".join([d.page_content for d in docs])
    #llm = OpenAI(model="text-embedding-ada-002")
    llm = OpenAI()
    
    prompt = PromptTemplate(
        input_variables = ["question","docs"],
        template="Answer the following question:{question} By searching the following video transcript:{docs}"
    )
    chain = LLMChain(llm=llm,prompt=prompt)
    response = chain.invoke({"question":query,"docs":docs})
    #response = response.replace("\n","")
    return response

if __name__ == "__main__":
    create_vectordb_from_youtube_url("https://www.youtube.com/watch?v=QvKMwLjdK-s&t=700s")
    #db=create_db()
    #print(get_response_from_query(db,"What is HNSW")['text'])