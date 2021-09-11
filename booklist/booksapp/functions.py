import requests

def get_book_from_api(keyword):
    url = f"https://www.googleapis.com/books/v1/volumes?q=search+{keyword}"
    get = requests.get(url)
    data = get.json()
    book_list = []

    for item in data['items']:
        book_info = {}
        try:
            book_info.setdefault('title', item['volumeInfo']['title'])
        except KeyError:
            book_info.setdefault('title', 'Unknown')
        #
        try:
            if len(item['volumeInfo']['authors']) == 1:
                book_info.setdefault('authors', item['volumeInfo']['authors'][0])
            else:
                book_info.setdefault('authors', ', '.join(item['volumeInfo']['authors']))

        except KeyError:
            book_info.setdefault('authors', "Unknown")

        try:
            if len(item['volumeInfo']['publishedDate']) == 4:
                book_info.setdefault('date', item['volumeInfo']['publishedDate'])
            else:
                book_info.setdefault('date', item['volumeInfo']['publishedDate'][:4])
        except KeyError:
            book_info.setdefault('date', 0)

        try:
            id = item['volumeInfo']['industryIdentifiers']
            book_info.setdefault('other_id', "Unknown")
            book_info.setdefault('isbn10', "Unknown")
            book_info.setdefault('isbn13', "Unknown")
            for identifier in id:
                if identifier['type'] == 'OTHER':
                    book_info['other_id'] = identifier['identifier']
                if identifier['type'] == 'ISBN_10':
                    book_info['isbn10'] = identifier['identifier']
                if identifier['type'] == 'ISBN_13':
                    book_info['isbn13'] = identifier['identifier']

        except KeyError:
                pass
        try:
            book_info.setdefault('pages', item['volumeInfo']['pageCount'])
        except KeyError:
            book_info.setdefault('pages', 0)

        try:
            book_info.setdefault('language', item['volumeInfo']['language'])
        except KeyError:
            book_info.setdefault('language', 'Unknown')

        try:
            book_info.setdefault('img', item['volumeInfo']['imageLinks']['thumbnail'])
        except KeyError:
            book_info.setdefault('img', "https://thumbs.dreamstime.com/b/no-image-available-icon-flat-vector-no-image-available-icon-flat-vector-illustration-132482953.jpg")

        book_list.append(book_info)

    return book_list
