import scrapy

class QuoteSpider(scrapy.Spider):
    name= 'quotes'
    start_urls = [
        'https://www.amazon.in/mobile-phones/b?ie=UTF8&node=1389401031&ref_=nav_shopall_sbc_mobcomp_all_mobiles'
    ]

    def parse(self, response):
        all_div_quotes = response.css('div.crwBucket')

        for quotes in all_div_quotes:
            name = quotes.css(".crwTitle a::text").extract()
            # actual_price= all_div_quotes.css(".crwPrice span:nth-child(1) span::text").extract()
            actual_price = quotes.css(".a-text-strike span::text").extract()
            discount_price = quotes.css(".crwActualPrice span::text").extract()
            rating = quotes.css(".a-icon-alt::text").extract()

            yield {
                'name': name,
                'actual_price': actual_price,
                'discount_price': discount_price,
                'rating': rating
            }
