from datetime import datetime

from pep_parse.settings import BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_count = {}

    def process_item(self, item, spider):
        status = item['status']
        self.status_count[status] = self.status_count.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        time = datetime.strftime(datetime.now(), '%Y-%m-%dT%H-%M-%S')
        path = BASE_DIR / f'results/status_summary_{time}.csv'
        self.csvfile = open(path, mode='w', encoding='utf-8')
        self.csvfile.write('Статус,Количество\n')

        for status, count in self.status_count.items():
            self.csvfile.write(f'{status},{count}\n')

        total = sum(self.status_count.values())
        self.csvfile.write(f'Total,{total}\n')
        self.csvfile.close()
