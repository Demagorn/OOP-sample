import requests
import concurrent.futures


class Extractor:
    def __init__(self, url):
        self.base_url = url

    def __enter__(self):
        self.session = requests.session()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session = None

    def get_page(self, address):
        return self.session.get(address).json()

    def extract_all_data(self, how_many_pages=9, max_requests=5):
        """get all data from API - optional: amount of pages(def 9)  :set amount of simultaneous requests(def 5) """
        my_data = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_requests) as executor:
            # Start the load operations and mark each future with its URL
            future_to_url = {executor.submit(self.get_page, self.base_url.format(page)): self.base_url.format(page)
                             for page in range(1, how_many_pages+1)}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    data = future.result()
                    my_data.append(data)
                except Exception as exc:
                    print('%r generated an exception: %s' % (url, exc))
        return my_data
