#This script automatically downloads the csv file available
#at this url: https://www.data.gouv.fr/fr/datasets/r/8e5e70fa-c082-45e3-a7b8-20862711b142

import requests

def csv_download():
    #Makes a "get" request to the specified url with a maximum delay of 30ms
    r = requests.get('https://www.data.gouv.fr/fr/datasets/r/8e5e70fa-c082-45e3-a7b8-20862711b142', timeout=30, allow_redirects=True)

    #Writes the query response to a file
    open("vacsi-s-a-reg-2022-03-22-21h01.csv", "wb").write(r.content)



