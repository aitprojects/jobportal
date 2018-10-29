

import hashlib

from scrapy.spiders import SitemapSpider
from collectdata.items import JobItem
hashings = hashlib.md5()



class JobsdotafSpider(SitemapSpider):

    name = 'jobsdotaf'
    allowed_domains = ['www.jobs.af']
    sitemap_urls = ['http://www.jobs.af/sitemap.xml']
    sitemap_rules = [('/afghanistan/', 'parse_item')]

    def flattext(self , lists):
        loc = ''
        for i in lists:
            loc += i
        return loc


    def parse_item(self, response):
        table = response.xpath('//*[@class="table table-hover details_table"]//tbody')
        main_text = response.css('div.main_text > p *::text').extract()
        main_res = response.css('div.duties > p *::text').extract()
        main_text_filter = list(filter(lambda item: any(c.isalpha() for c in item), main_text))
        main_res_filter = list(filter(lambda item: any(c.isalpha() for c in item), main_res))
        item = JobItem()
        hashings.update(response.url.encode('utf-8'))
        item['item_id'] = hashings.hexdigest()
        item['title'] = response.css('div.details_title h1.faculty::text').extract_first()
        item['organization'] = main_text_filter[0]
        item['about_company'] = self.flattext(main_text_filter[1:main_text_filter.index('Job Summary')])\
            .replace('\uf0b7' , '').replace('\n' , ' ')
        item['job_description'] = self.flattext(main_text_filter[main_text_filter.index('Job Summary'):])\
            .replace('\uf0b7' , '').replace('\n' , ' ')
        item['open_date'] = table.xpath('//tr')[0].xpath('td//text()')[1].extract()
        item['closing_date'] = table.xpath('//tr')[1].xpath('td//text()')[1].extract()
        item['number_vacancies'] = table.xpath('//tr')[2].xpath('td//text()')[1].extract()
        item['functional_area'] = table.xpath('//tr')[3].xpath('td//text()')[1].extract()
        item['nationality'] = table.xpath('//tr')[4].xpath('td//text()')[1].extract()
        item['contract_type'] = table.xpath('//tr')[5].xpath('td//text()')[1].extract()
        item['contract_duration'] = table.xpath('//tr')[6].xpath('td//text()')[1].extract()
        try:
            item['probation_period'] = table.xpath('//tr')[7].xpath('td//text()')[1].extract()
        except:
            item['probation_period'] = ''
        item['reference'] = table.xpath('//tr')[0].xpath('td//text()')[3].extract()
        item['work_type'] = table.xpath('//tr')[1].xpath('td//text()')[3].extract()
        item['gender'] = table.xpath('//tr')[2].xpath('td//text()')[3].extract()
        item['open_ended'] = table.xpath('//tr')[3].xpath('td//text()')[3].extract()
        item['salary_range'] = table.xpath('//tr')[4].xpath('td//text()')[3].extract()
        item['year_of_expirence'] = table.xpath('//tr')[5].xpath('td//text()')[3].extract()
        item['extension_passibility'] = table.xpath('//tr')[6].xpath('td//text()')[3].extract()
        try:
            item['duties_responsibilities'] = self.flattext(main_res_filter[main_res_filter.index(
                'Duties and Responsibilities') + 1:main_res_filter.index('Skills')])\
                .replace('\uf0b7' , '').replace('\n' , ' ')
            item['skills'] = self.flattext(
                main_res_filter[main_res_filter.index('Skills') + 1:main_res_filter.index('Qualifications')])\
                .replace('\uf0b7' , '').replace('\n' , ' ')
        except:
            item['duties_responsibilities'] = self.flattext(main_res_filter[main_res_filter.index(
                'Duties and Responsibilities') + 1:main_res_filter.index('Qualifications')])\
                .replace('\uf0b7' , '').replace('\n' , ' ')
            item['skills'] = "No Skill"
        item['qualification'] = self.flattext(main_res_filter[main_res_filter.index('Qualifications')+1:main_res_filter.index(
            'Job Location')]).replace('\uf0b7' , '').replace('\n' , ' ')
        item['jobs_location'] = self.flattext(main_res_filter[main_res_filter.index('Job Location')+1:main_res_filter.index(
            'Education:')]).replace('\uf0b7' , '').replace('\n' , ' ')
        item['education'] = self.flattext(main_res_filter[main_res_filter.index('Education:')+1:main_res_filter.index(
            'Submission Guideline')]).replace('\uf0b7' , '').replace('\n' , ' ')
        item['submission_guideline'] = self.flattext(main_res_filter[main_res_filter.index(
            'Submission Guideline')+1:main_res_filter.index('Submission Email')])\
            .replace('\uf0b7' , '').replace('\n' , ' ')
        item['submission_email'] = self.flattext(main_res_filter[main_res_filter.index(
            'Submission Email')+1:]).replace('\uf0b7' , '').replace('\n' , ' ')


        yield item
