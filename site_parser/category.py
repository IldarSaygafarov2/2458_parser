from .base import BaseParser

class CategoryParser(BaseParser):
    # URL, get_soup
    def get_categories(self):
        # получить html content страницы
        soup = self.get_soup()

        # ищем обертку над категориями
        nav_row = soup.find('div', class_='nav_row').find('ul')
        result = []
        for item in nav_row.find_all('a'):
            name = item.get_text()
            url = self.URL + item.get('href')  # https://upl.uz + /world/
            if name in ['Реклама', 'Контакты']:
                continue
            result.append({
                'name': name,
                'url': url
            })
        return result
        # NoneType.find_all()
        # NoneType object has no attribute .find_all()
