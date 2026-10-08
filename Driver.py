from web_surf import scrape_webpage
from get_out import generate_out


def prompt(query, web_out):
    return f"""
<|begin_of_text|>
You're a web browsing AI, and you've been asked to elobrate on the following query: {query}

Web browsing result: {web_out}

provide a more detailed and accurate description based on the web search?
<|end_of_text|>
"""


def run(query: any) -> str:
    scraped_text = scrape_webpage(query)
    scraped_text = scraped_text
    final_prompt = prompt(query, scraped_text)
    generated_text = generate_out(final_prompt)
    return generated_text
