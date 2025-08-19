from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate


# Indexing (Document Ingestion)

ytt_api = YouTubeTranscriptApi()
splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)


video_id = "LPZh9BOjkQs"
try:
    transcipt_list = ytt_api.fetch(video_id, languages=["en"])
    transcript = " ".join([chunk.text for chunk in transcipt_list])
    # print(transcipt_list, "\n")
    # print("-------------------------------------------------------------------------------------------------","\n")
    # print(transcript)
    
    
except TranscriptsDisabled:
    print("No captions available for this video")


chunks = splitter.create_documents([transcript])





