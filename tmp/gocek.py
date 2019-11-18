import requests
import json
import csv

if __name__ == "__main__":
    fr = open('tmp/comments - comments.csv', 'r')
    reader = csv.reader(fr, delimiter=',')

    fw = open('tmp/comments - final.csv', 'a')
    writer = csv.writer(fw)

    # skip header
    for i in range(1):
        next(reader, None)

    i = 0
    for row in reader:
        i += 1
        print(i)
        if i <= 1:
            continue

        if (row[0] == ""):
            continue

        payload = {
            "text": row[-2],
            "lang": "id"
        }
        response = requests.post(
            "https://api.repustate.com/v4/0367fe9077a045661eed32a700a79a596052b952/score.json",
            payload,
        )

        json_response = response.json()
        print(json_response)
        if "score" in json_response:
            print("{} {} {}".format(i, row[-2], json_response["score"]))
            writer.writerow([row[-2], json_response["score"]])