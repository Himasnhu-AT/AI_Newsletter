import os
from dotenv import load_dotenv

import scrappers.arvix_scrapper as arvix_scrapper
import scrappers.github_scrapper as github_scrapper
import scrappers.news_scrapper as news_scrapper

load_dotenv()

# arvix_scrapper.get_arxiv_papers()
# paper_summary = arvix_scrapper.search_pdf("bot/papers/paper-1.pdf")
# vectordb = arvix_scrapper.embed_pdf(paper_summary)
# chain_pdf = arvix_scrapper.chain_pdf(vectordb, "What is the best way to train a neural network?")
# print(chain_pdf)

# repos = github_scrapper.get_github_repos()
# print(f"Top 10 fastest growing  repositories on Github: {repos}")

news = news_scrapper.get_top_10_ai_news()
print(f"Top 10 news articles: {news}")
