from .base import BaseParser

class ArticleParser(BaseParser):
    def get_category_articles(self, category_url):
        soup = self.get_soup(category_url)

        total_pages = soup.find('div', class_='navigation').find_all('a')[-1].get_text()
        result = {}

        for page in range(1, int(total_pages)+1)[:5]:  # 2
            print(f'====[LVL-2] Получаем данные из страницы номер: {page}')
            if page == 1:
                page_soup = soup
            else:
                page_soup = self.get_soup(f'{category_url}page/{page}/')

            wrapper = page_soup.find('div', id='content-block')
            # print(wrapper)
            items = wrapper.find_all('div', class_='sh-news')  # 30
            # print(len(items))
            result[page] = []
            for i in items:
                title = i.find('h2').get_text()
                print(title)
                img_url = i.find('img').get('data-src')
                # print(img_url)
                text = i.find('div', class_='sh-text').next.get_text(strip=True)
                # print(text)
                side_date = i.find('div', class_='side-date').find_all('span')
                # print(side_date)
                time = side_date[0].get_text()
                if len(side_date) == 2:
                    comments = side_date[1].get_text()
                else:
                    comments = '0'

                result[page].append({
                    'title': title,
                    'img_url': img_url,
                    'text': text,
                    'time': time,
                    'comments': comments
                })
        return result

    def get_article_detail(self, article_url):
        pass
