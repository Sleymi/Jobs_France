import requests
import time
import os
import sys
from datetime import datetime


# ei1 = sys.argv[1]
#this variable is always changes
ei1 ='r_rQXavOBpqGjLsPgs-XgAc'

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0",
    "Accept": "*/*",
    "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive",
    "TE": "Trailers",
}


place = [
    "Paris",
    "Roissy-en-France",
    "Tremblay-en-France",
    "Évry",
    "Boulogne-Billancourt",
    "Nanterre",
    "Lyon",
    "Neuilly-sur-Seine",
    "Courbevoie",
    "Lille",
    "Puteaux",
    "Saint-Denis",
    "Fontenay-sous-Bois",
    "Rueil-Malmaison",
    "Aix-en-Provence",
    "Clichy-sous-Bois",
    "Nainville-les-Roches",
    "Nantes",
    "Bonneuil-en-France",
    "Clamart",
    "Issy-les-Moulineaux",
    "Levallois-Perret",
    "Magny-les-Hameaux",
    "Marseille",
    "Massy",
    "Puiseux-en-France",
    "Saint-Cloud",
    "Toulouse",
    "Bourg-la-Reine",
    "Colombes",
    "Corbeil-Essonnes",
    "La Courneuve",
    "Laon",
    "Montreuil",
    "Pérols",
    "Suresnes",
    "Vélizy-Villacoublay",
    "Ancenis",
    "Asnières-sur-Seine",
    "Athis-Mons",
    "Auxerre",
    "Avranches",
    "Ayzieu",
    "Bagnolet",
    "Barbery",
    "Bordeaux",
    "Bussy-Saint-Martin",
    "Béligneux",
    "Cahors",
    "Carpentras",
    "Champigny-sur-Marne",
    "Cherbourg-en-Cotentin",
    "Cholet",
]

place = [i.replace(" ", "%20") for i in place]
codes = [
    "D7fiBh9u5kdglIxow4ILBA==",
    "A3Nv1oQV5keti4XTF_aDNQ==",
    "z0HtktIV5kdgOotow4ILBA==",
    "c80Aqh7e5Uc5PHmiEprGLw==",
    "YUevEOh65keQPotow4ILBA==",
    "vyXf2YRk5kfiR8FqHO4hew==",
    "l4foalHq9EfwIbvkKqsIBA==",
    "tZbjc2Nl5keXszL1nHU53A==",
    "vccvsApl5kcQPotow4ILBA==",
    "EW4ls3nVwkdgY2SBPvEKBA==",
    "xfUaLBpl5kfgyvJ51T872A==",
    "YW0056pu5kcN6Sj5uuvvxw==",
    "kyBwzV4N5kdAOYtow4ILBA==",
    "K4enU1pj5kcgPYtow4ILBA==",
    "WRK5BKONyRKjiLbIvlO5XA==",
    "p55diNwT5kcgPItow4ILBA==",
    "zScOX8Ho5UfIchdx8t1EYw==",
    "ra6o8IHuBUgw7Q0eUjcNBA==",
    "WyykNRpr5kdwNYtow4ILBA==",
    "IdLsDxV65kdAPotow4ILBA==",
    "xy7Ltot65kehJ24ad9Amiw==",
    "0_88t4Nv5kewPYtow4ILBA==",
    "p5CXOVSA5kcwPYxow4ILBA==",
    "M1PaREO_yRIgApf9pRkIBA==",
    "ASDNmoR35kenA6QiZFUPAw==",
    "zYxi1mg_5kdQLotow4ILBA==",
    "j45beSR75keCz2CwCgehTA==",
    "_1J17G-7rhIwEEEvnPYGBA==",
    "BY5REypx5keAPotow4ILBA==",
    "S0wd8shl5kcgPotow4ILBA==",
    "G1Q8gCrn5UdmR6OjA6W5Lw==",
    "BdU-zHJs5kdAcN87dNluNg==",
    "oRHYeGtL6Eeg5WmBPvEKBA==",
    "he8OU0Vt5kfwW8SwbXyqow==",
    "LwltMi-7thKwwmoWIYgHBA==",
    "584OtMVk5kfgPItow4ILBA==",
    "-acYgeR75kdQNoxow4ILBA==",
    "XahR4kADBkjA8w0eUjcNBA==",
    "KxuhrEJv5kfAPotow4ILBA==",
    "F9_jDZB15kcETB8w0s5hlQ==",
    "4a81tzBP7keRJ6K6elPmLg==",
    "AZD6DRVVCUhwhLlPSBQMBA==",
    "af-3YTD_VQ1gDEEvnPYGBA==",
    "t4xHy29t5kdwPItow4ILBA==",
    "R4Tp-Cgu5kcwTWSBPvEKBA==",
    "gcpR9-gnVQ2Jejl7A4ZjeQ==",
    "FblFpisF5kcwYoxow4ILBA==",
    "VRbYCkqx9Eec2Lh-B7KMdg==",
    "-xR9VFeJrBKgzj8vnPYGBA==",
    "HdklSv6JtRIwxY_9pRkIBA==",
    "L1welrQN5kenwYVWdRZX6g==",
    "4WKqHxKXDEgA-LwYxB_Gfg==",
    "5fDNrRREBkiAlg0eUjcNBA==",
]

all1 = dict(zip(place, codes))


ei = "kkkkkkkkkkk11111"
start = "sssssssssssss"

all = []
for place, code in all1.items():
    main_url = "https://www.google.com/search?vet=10ahUKEwjMsZi7norlAhUeBWMBHY_PCagQ06ACCJEF..i&ei=kkkkkkkkkkk11111&safe=off&yv=3&rciv=jb&nfpr=0&chips=city:{}&schips=city;{}:{}&q=france&start=sssssssssssss&asearch=tl_af&async=_id:gws-horizon-textlists__tl-af,_pms:hts,_jsfs:Ffpdje,_fmt:pc".format(
        code, code, place
    )
    all += [main_url]


now = datetime.now()
dt_string = now.strftime("res_%d_%m_%Y__%H_%M_%S")
#path_glob = "/home/databiz32/Bureau/badcode/test/spider/curl/"
# os.makedirs(path_glob + dt_string)
os.makedirs(dt_string)

for url in all:
    index = all.index(url)
    for i in range(10, 560, 10):
        url1 = url.replace(start, str(i))
        url1 = url1.replace(ei, ei1)

        # ss = dt_string + "/file_{}_{}".format(index, i)
        # okpath = path_glob + ss
        response = requests.get(url1, headers=headers)
        file = dt_string + "/file_{}_{}".format(index, i)
        with open(file, "wb") as f:
            f.write(response.content)
