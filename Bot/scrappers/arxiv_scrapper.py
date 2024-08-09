import arxiv
import requests

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_milvus import Milvus, Zilliz
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.document_loaders import PyPDFLoader

def get_arxiv_papers(search_terms=("artificial intelligence", "natural language processing"), max_results=5):
    """
    Get research papers from arxiv, download pdf versions, and return a list of dictionaries containing information from each paper.

    Args:
        search_terms (tuple, optional): Search terms to use for arxiv. Defaults to ("artificial intelligence", "natural language processing").
        max_results (int, optional): Maximum number of results to return from arxiv. Defaults to 5.

    Returns:
        list: List of generated pdf filenames.
        list: List of dictionaries containing the title, date, authors, summary, and link for each paper.
    """

    search_query = " AND ".join(f'"{term}"' for term in search_terms)
    search = arxiv.Search(
        query=search_query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Descending,
    )
    result_pdf_list = []
    result_pdf_dict = []
    for result in search.results():
        result_pdf_list.append(result.pdf_url)
        ds_result = {'title': result.title, 'date': result.published, 'authors': result.authors, 'summary': result.summary, 'link': result.pdf_url}
        result_pdf_dict.append(ds_result)

    pdf_filenames = []
    for count, pdf in enumerate(result_pdf_list):
        print(f"Downloading {count+1} of {len(result_pdf_list)}")
        r = requests.get(pdf, allow_redirects=True)
        with open(f"Bot/papers/paper-{count+1}.pdf", "wb") as f:
            f.write(r.content)
        pdf_filenames.append(f"AI_newsletter/papers/paper-{count+1}.pdf")

    return pdf_filenames, result_pdf_dict

def search_pdf(pdf_filename):
    """
    Read a pdf file and return a list of pages.

    Args:
        pdf_filename (str): Filename of the pdf file to read.

    Returns:
        list: List of pages from the pdf file.
    """

    loader = PyPDFLoader(pdf_filename)
    pages = loader.load_and_split()
    return pages

def embed_pdf(pages):
    """
    Embed the text from a list of pages and store the embeddings in a Milvus database.

    Args:
        pages (list): List of pages to embed.

    Returns:
        Milvus: Milvus database containing the embeddings.
    """

    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vectordb = Milvus.from_documents(pages, embedding=embeddings, collection_name="arxiv_papers", connection_args={
        # "host": "localhost", "port": "19530"
        "uri": "./milvus.db"
    })
    return vectordb

def chain_pdf(vectordb, query):
    """
    Get similar papers from a Milvus database based on a query.

    Args:
        vectordb (Milvus): Milvus database containing the embeddings.
        query (str): Query to search for similar papers.

    Returns:
        list: List of similar papers.
    """

    return vectordb.similarity_search(query, k=10)
