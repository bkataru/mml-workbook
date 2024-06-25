import os

import requests

dir = os.path.dirname(os.path.realpath(__file__))

def download_pdf(url: str, save_path: str):
    final_path = os.path.join(dir, save_path)

    response = requests.get(url)

    with open(final_path, 'wb') as f:
        f.write(response.content)
    
    print(f"PDF downloaded and saved at {final_path}")


pdf_url = "https://mml-book.github.io/book/mml-book.pdf"
save_path = 'mml-book.pdf'

if __name__ == "__main__":
    download_pdf(pdf_url, save_path)


