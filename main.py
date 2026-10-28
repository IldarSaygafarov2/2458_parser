from site_parser.category import CategoryParser
from site_parser.article import ArticleParser
import json

def main():
    category_parser = CategoryParser()
    article_parser = ArticleParser()

    categories = category_parser.get_categories()
    result = {}
    for category in categories:
        c_name, c_url = category.values()  #
        print(f'[LVL-1] Получаем данные из категории: {c_name}')
        articles = article_parser.get_category_articles(c_url)
        result[c_name] = articles

    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(result, file, ensure_ascii=False, indent=4)



main()