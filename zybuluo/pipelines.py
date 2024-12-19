# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class ZybuluoPipeline:
    def __init__(self):
        self.items = []
        self.output_file = 'bintou.md'

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        with open(self.output_file, 'w', encoding='utf-8') as f:
            for item in self.items:
                md_text=item['text']
                f.write(md_text + '\n\n---\n\n')
