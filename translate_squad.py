from googletrans import Translator
import json


def run(file_name):
    translator = Translator()
    with open(file_name, "r+") as file:
        data = file.read()
        data = json.loads(data)['data']
        for d in data:
            paragraphs = d['paragraphs']
            for page in paragraphs:
                context = page['context']

                context_trans = translator.translate(context, src='en', dest='vi')
                print(context_trans.text)


if __name__ == '__main__':
    run("dataset/train-v2.0.json")
