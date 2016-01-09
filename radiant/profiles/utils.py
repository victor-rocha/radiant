from bs4 import BeautifulSoup


def insert_quote(paragraphs, quote):
    """Inserts a quotation in a Story"""
    middle = int(len(paragraphs) / 2)
    soup = BeautifulSoup("""
        <div class='row'>
            <div class='col-md-12 pre-quotation'></div>
        </div>
        <div class='row quotation-wrapper'>
            <div class='col-md-8 col-quotation-left'>

            </div>
            <div class='col-md-4 col-quotation-right'>
                <div class='quotation'>

                </div>
            </div>
        </div>
        <div class='row'>
            <div class='col-md-12 post-quotation'></div>
        </div>
    """, 'html.parser')

    pre_quote_paragraphs = soup.find('div', {'class': 'pre-quotation'})
    post_quote_paragraphs = soup.find('div', {'class': 'post-quotation'})
    col_left = soup.find('div', {'class': 'col-quotation-left'})
    col_right = soup.find('div', {'class': 'quotation'})
    col_right.string = quote

    for index, paragraph in enumerate(paragraphs):
        if middle - 2 < index < middle + 2:
            # we need to add a class to this paragraphs
            col_left.append(paragraph)
        elif index < middle:
            pre_quote_paragraphs.append(paragraph)
        else:
            post_quote_paragraphs.append(paragraph)
    return [soup]
