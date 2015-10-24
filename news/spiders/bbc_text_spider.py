from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from items import NewsItem

class BbcSpider(CrawlSpider):
	name = "bbcnews"
	allowed_domains = ["bbc.co.uk"]
	start_urls = [
	"http://www.bbc.co.uk/news/technology/",
	]

	rules = [Rule(LinkExtractor(allow=['/technology-\d+']), 'parse_story')]

	def parse_story(self, response):

		story = NewsItem()
		#story['url'] = response.url
		story['headline'] = response.xpath("//title/text()").extract()
		#story['intro'] = response.css('p.introduction::text').extract()

		return story	