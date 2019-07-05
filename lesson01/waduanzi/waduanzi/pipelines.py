# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from waduanzi.orm import SqlOrm, Joke


class WaduanziPipeline(object):
    sql_obj = SqlOrm()

    def process_item(self, item, spider):
        query = self.sql_obj.session.query(Joke)
        if self.sql_obj.is_exists(query.filter(Joke.id == item['id'])):
            print('Have exists： id = %s' % item['id'])
        else:
            self.sql_obj.session.add(Joke(**item))
            print('Update one: id = %s' % item['id'])
        self.sql_obj.session.commit()
        return item
