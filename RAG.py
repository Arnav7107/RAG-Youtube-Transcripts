from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate


# Indexing (Document Ingestion)

ytt_api = YouTubeTranscriptApi()
splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
# vector_store = FAISS.from_documents(chunks, embeddings)


video_id = "LPZh9BOjkQs"
try:
    transcipt_list = ytt_api.fetch(video_id, languages=["en"])
    transcript = " ".join([chunk.text for chunk in transcipt_list])
    # print(transcipt_list, "\n")
    # print("-------------------------------------------------------------------------------------------------","\n")
    # print(transcript)
    
    
except TranscriptsDisabled:
    print("No captions available for this video")


# Document Splitting

chunks = splitter.create_documents([transcript])
# print(len(chunks))

# Embedding of Splitted Documents 
vector_store = FAISS.from_documents(chunks, embeddings)
print(vector_store.index_to_docstore_id)

doc = vector_store.get_by_ids(["7a7b7e4d-6690-4a60-a3bf-0463a489d3d6"])
print(doc)





