
import requests
import bs4 as bs
import pandas as pd

class Category:
    def __init__(self, base_url):
        self.base_url = base_url
        

    def categoryBook(self):
        
        page_number = 1
        all_prices = []
        all_book_names = []
        all_book_link = []
        all_author = []

        while True:
            url = f"{self.base_url}?page={page_number}"
            response = requests.get(url).text
            source = bs.BeautifulSoup(response, 'html.parser')
            prices = source.find_all('p', class_='book-price')
            authors = source.find_all('p', class_='book-author')
            tags = source.find_all('h4')
            links = source.find_all("a", class_="btn home-details-btn btn-block")
            
            if not prices:
                break           

            # Removing the first h4 tag which is not a book name
            book_names = [tag.get_text() for tag in tags]
            all_book_names.extend(book_names)
            
            author_data = [author.get_text() for author in authors]
            all_author.extend(author_data)

            price_data = [price.get_text() for price in prices]
            all_prices.extend(price_data)

            book_link = ["https://www.rokomari.com"+link.get("href") for link in links]
            all_book_link.extend(book_link)

            page_number += 1
        
        # print(len(all_book_names), len(all_prices), len(all_book_link))
        print('\n\tThere are {} books found and listed in total.\n'.format(len(all_book_names)))

        # Create a DataFrame with three columns: "Books Name," "Data," and "Tags"
        df = pd.DataFrame({"Books Name": all_book_names, "Author":all_author, "Price": all_prices, "Link": all_book_link})

        # Get the title of the first page and sanitize it for the filename
        first_page_title = source.title.text
        first_page_title = first_page_title.split('-')[0].strip()
        
        # Create an Excel writer object and save the DataFrame to an Excel file
        with pd.ExcelWriter(f"{first_page_title}.xlsx", engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name=first_page_title, index=False)