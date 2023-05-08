import json

def parse_json():
    with open("sample.json") as myfile:
        content = json.load(myfile)

    quesAns = {}

    for i in content["response"]:
        quesAns[tuple(i["question"])] = i["help_text"]

    return quesAns

    # for i in quesAns.keys():
    #     for questionLine in i:
    #         print(questionLine)
    #     choice = input("Would you like to see the answer? (y/n): ")
    #     if choice == "y":
    #         print(quesAns[i])
    #     print()
    #     print("Next question:")

if __name__ == '__main__':
    parse_json()
