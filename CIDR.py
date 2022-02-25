import requests, csv, json, config


apple = {
  "cidr": "",
  "depthLimit": 1, 
  "bogonsOnly": "false", 
  "localityLanguage": "en",
  "key": ''
}

final = []


def use(ipAddress):
  apple["cidr"] = ipAddress + "/32"
  r = requests.get('https://api.bigdatacloud.net/data/network-by-cidr', params=apple)
  appending(r.json())
  

def appending(data):
  dataset = []
  dataset.clear()
  dataset.append(data["cidr"])
  dataset.append(data["network"]["carriers"][0]["asn"])
  dataset.append(data["network"]["subnets"][0]["organisation"])
  final.append(dataset)

def readFile():
  data = []
  with open('ip_test_input.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
      data.append(row[0].replace(" ", ""))
    data.remove(data[0])
    return data



def writeFile():
  listings = []
  for i in final:
    newdict = {
      "CIDR": i[0],
      "ASN": i[1],
      "Organisation": i[2]
    }
    listings.append(newdict)
  with open('test.json', "w+") as file:
    json.dump(listings, file)


def main():
  apple["key"] = config.key
  listings = readFile()
  for ip in listings:
    use(ip)
  writeFile()


main()