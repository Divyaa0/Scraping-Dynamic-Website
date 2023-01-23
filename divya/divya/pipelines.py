# # # Define your item pipelines here
# # #
# # # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# #
# #
# # # useful for handling different item types with a single interface
# # from itemadapter import ItemAdapter
#
# import pymongo
# from scrapy import settings
#
# class DivyaPipeline(object):
#
#
#     def __int__(self):
#         self.conn=pymongo.MongoClient(
#             'localhost',
#             27017
#         )
#         db=self.conn['divyaaa']
#         self.collection=db['leclerc_fr']
#
#
#
#
#
#     def process_item(self, item, spider):
#         self.collection.insert(dict(item))
