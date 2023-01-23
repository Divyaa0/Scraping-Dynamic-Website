

BOT_NAME = 'divya'
ROBOTSTXT_OBEY = False
SPIDER_MODULES = ['divya.spiders']
NEWSPIDER_MODULE = 'divya.spiders'
# ITEM_PIPELINES = {
#    'divya.pipelines.DivyaPipeline': 300,
# }
# MONGODB_SERVER = "localhost"
# MONGODB_PORT = 27017
# MONGODB_DB = "divyaaa"
# MONGODB_COLLECTION = "leclerc_fr"

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPLASH_URL = 'http://localhost:8050'
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
USER_AGENT = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'






