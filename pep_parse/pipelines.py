from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:

    def open_spider(self, spider):
        self.csvfile = open(
            f'results/status_summary_{datetime.now()}.csv',
            mode='w',
            encoding='utf-8'
        )
        self.csvfile.write('Статус,Количество\n')
        self.status_count = {}

    def process_item(self, item, spider):
        pep_status = item['status']
        self.status_count[pep_status] = self.status_count.get(pep_status, 0) + 1
        return item

    def close_spider(self, spider):
        for status, count in self.status_count.items():
            self.csvfile.write(f'{status},{count}\n')

        total = sum(self.status_count.values())
        self.csvfile.write(f'Total,{total}\n')
        self.csvfile.close()
