# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# class TruckingtimePipeline:
#     def process_item(self, item, spider):
#         return item

from itemadapter import ItemAdapter
import sqlite3


class TruckingtimePipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("truckingData.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS truckingData""")
        self.curr.execute("""create table truckingData(
                rank text,
                location text,
                state text,
                averageSpeed text,
                peakAvgSpeed text,
                nonPeakAvgSpeed text,
                deltaChange text
                )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item
    
    def store_db(self, item):
        self.curr.execute("""insert into truckingData values (?,?,?,?,?,?,?)""",(
            item['rank'][0],
            item['location'][0],
            item['state'][0],
            item['averageSpeed'][0],
            item['peakAvgSpeed'][0],
            item['nonPeakAvgSpeed'][0],
            item['deltaChange'][0]
        ))
        self.conn.commit()
