import scrapy
import re
import glob


class Sp(scrapy.Spider):
    name = "sp1"
    # path='/home/databiz32/Bureau/badcode/test/spider/curl/all_france3'
    #path = "/home/databiz32/Bureau/badcode/test/spider/curl/res_14_10_2019__09_49_59"
    #path = "res_17_11_2019__08_51_12"
    path = "/home/mohamed/Desktop/Jobs-go/res_17_11_2019__08_51_12"
    
    all = glob.glob(path + "/*")

    def start_requests(self):
        for e in self.all:
            url = "file://{}".format(e)
            req = scrapy.Request(url, callback=self.parse)
            yield req

    def parse(self, response):

        item = {}

        base = response.xpath("//ul/li")
        j = 0
        all_desc = re.findall(
            '(?<=style="line-height:1.5em">)(.*?)(?=</span>)', response.text, flags=re.S
        )
        all_id = re.findall('<div jsname="x5pWN" id="(.*?)"', response.text)
        tt = re.findall("\xc0(.*?temps.*?)</span>", response.text)
        all_temps = [tt[i] for i in range(0, len(tt), 2)]
        dp = re.findall("il y a.*?jours", response.text)
        all_date_pb = [dp[i] for i in range(0, len(dp), 2)]

        for sel in base:
            item = {}
            job_name = sel.xpath(
                "div/div[2]/div[2]/div/div[2]/div[1]/text()"
            ).extract_first()
            company = sel.xpath(
                "div/div[2]/div[2]/div/div[2]/div[2]/div[1]/text()"
            ).extract_first()
            adr = sel.xpath(
                "div/div[2]/div[2]/div/div[2]/div[2]/div[2]/text()"
            ).extract_first()
            site = sel.xpath(
                "div/div[2]/div[2]/div/div[2]/div[2]/div[3]/text()"
            ).extract_first()
            desc = all_desc[j]
            date_publication = sel.xpath(
                "div/div/div/div/div/div/div/span[1]/span[2]/text()"
            ).extract_first()
            temps_de_travail = sel.xpath(
                "div/div/div[2]/div/div[2]/div[2]/div[4]/span[2]/span[2]/text()"
            ).extract_first()
            AnnonceID = all_id[j]
            j += 1

            dispo = sel.xpath(
                "div/div[2]/div[1]/div/div/div/g-scrolling-carousel/div[1]/div/div/span/a/@href"
            ).extract_first()

            item["desc"] = desc.replace("\n", " ")
            item["job_name"] = job_name
            item["company"] = company
            item["adr"] = adr
            item["site"] = site
            item["AnnonceID"] = AnnonceID
            item["temps_de_travail"] = temps_de_travail
            item["date_publication"] = date_publication
            item["Disponible sur"] = dispo

            yield item
