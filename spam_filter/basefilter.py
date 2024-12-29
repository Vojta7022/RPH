from corpus import Corpus
import os


class BaseFilter:
    def __init__(self):
        self.SPAM_TAG = "SPAM"
        self.HAM_TAG = "OK"

    def test(self, path):
        corpus = Corpus(path)
        with open(
            os.path.join(path, "!prediction.txt"), "w", encoding="utf-8"
        ) as file_prediction:
            for email in corpus.emails():
                email_name = email[0]
                email_text = email[1]
                file_prediction.write(
                    email_name + " " + self.predict(email_text) + "\n"
                )

    def train(self, path):
        pass

    def predict(self, email_text):
        raise NotImplementedError("You must implement the predict method")
