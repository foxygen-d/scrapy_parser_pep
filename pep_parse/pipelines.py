import csv
from datetime import datetime
from itemadapter import ItemAdapter


class PepParseToCSVPipeline:

    def open_spider(self, spider):
        self.csvfile = open(f'results/status_summary_{datetime.now()}.csv', mode='w', encoding='utf-8')
        self.csvfile.write('Статус,Количество\n')
        self.status_count = {}

    def process_item(self, item, spider):
        self.status_count[item['status']] = self.status_count.get(item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        for status, count in self.status_count.items():
            self.csvfile.write(f'{status},{count}\n')

        total = sum(self.status_count.values())
        self.csvfile.write(f'Total,{total}\n')
        self.csvfile.close()
