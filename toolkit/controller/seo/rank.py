from googlesearch import search
import logging


def rank(domain, query, lang='en', tld='com'):
    my_results_list = []
    lang = lang
    tld = tld
    if lang is None:
        lang = 'en'
    if tld is None:
        tld = 'com'

    for i in search(query,        # The query you want to run
                    tld='com',  # The top level domain
                    lang='en',  # The language
                    num=25,     # Number of results per page
                    start=0,    # First result to retrieve
                    stop=50,  # Last result to retrieve
                    pause=2.0,  # Lapse between HTTP requests
                    ):
        my_results_list.append(i)
        logging.debug(str(my_results_list.index(i)) + ": " + str(i))
        if domain in i:
            return {"pos": my_results_list.index(i) + 1, "url": i, "query": query}
    return {"pos": -1, "url": "None", "query": query}




if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.DEBUG, datefmt='%m/%d/%Y %I:%M:%S %p')

    print(rank("primates.dev", "parse xml response python"))
