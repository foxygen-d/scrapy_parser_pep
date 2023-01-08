from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:

    def open_spider(self, spider):
        path = BASE_DIR / f'results/status_summary_{datetime.now()}.csv'
        self.csvfile = open(path, mode='w', encoding='utf-8')
        self.csvfile.write('Статус,Количество\n')
        self.status_count = {}

    def process_item(self, item, spider):
        status = item['status']
        self.status_count[status] = self.status_count.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        for status, count in self.status_count.items():
            self.csvfile.write(f'{status},{count}\n')

        total = sum(self.status_count.values())
        self.csvfile.write(f'Total,{total}\n')
        self.csvfile.close()
