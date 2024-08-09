import scrappers.arvix_scrapper as arvix_scrapper

# arvix_scrapper.get_arxiv_papers()
paper_summary = arvix_scrapper.search_pdf("bot/papers/paper-1.pdf")
vectordb = arvix_scrapper.embed_pdf(paper_summary)
chain_pdf = arvix_scrapper.chain_pdf(vectordb, "What is the best way to train a neural network?")
print(chain_pdf)
