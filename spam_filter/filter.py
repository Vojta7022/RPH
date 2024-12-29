from basefilter import BaseFilter
import random
import re

# zdroje spam slov:
# https://github.com/OOPSpam/spam-words/blob/main/spam-words-EN.txt
# https://www.activecampaign.com/blog/spam-words
# https://mailmeteor.com/blog/spam-words
# https://fluentcrm.com/email-spam-trigger-words/


# C:\\Programovani\\Python\\RPH\\HW\\Spam_filtr\\spam-words-EN.txt


class MyFilter(BaseFilter):
    def predict(self, email_text):
        with open(
            "spam-words-EN.txt",
            "r",
            encoding="utf-8",
        ) as file:
            spam_words = file.read().splitlines()
        spam_words_sets = [set(word.lower().split()) for word in spam_words]
        email_text_words = email_text.split()
        if (
            "unsubscribe" in email_text.lower()
            or "opt-out" in email_text.lower()
            or "optout" in email_text.lower()
        ):
            return self.HAM_TAG
        if len(email_text_words) < 5:
            return self.SPAM_TAG
        
        if re.search(r'(<br\s*/?>\s*){3,}', email_text, re.IGNORECASE) or re.search(r'(<\/br\s*>){3,}', email_text, re.IGNORECASE) or re.search(r'(&nbsp;\s*){3,}', email_text, re.IGNORECASE):
            return self.SPAM_TAG

        found_spam_words = 0

        for i in range(len(email_text_words)):
            email_text_words[i] = email_text_words[i].lower().strip(".,!?")
        for i in range(len(email_text_words) - 5):
            if email_text_words[i] in spam_words_sets:
                found_spam_words += 1
            if (
                set([email_text_words[i], email_text_words[i + 1]])
                in spam_words_sets
            ):
                found_spam_words += 2
            if (
                set(
                    [
                        email_text_words[i],
                        email_text_words[i + 1],
                        email_text_words[i + 2],
                    ]
                )
                in spam_words_sets
            ):
                found_spam_words += 3
            if (
                set(
                    [
                        email_text_words[i],
                        email_text_words[i + 1],
                        email_text_words[i + 2],
                        email_text_words[i + 3],
                    ]
                )
                in spam_words_sets
            ):
                found_spam_words += 4
            if (
                set(
                    [
                        email_text_words[i],
                        email_text_words[i + 1],
                        email_text_words[i + 2],
                        email_text_words[i + 3],
                        email_text_words[i + 4],
                    ]
                )
                in spam_words_sets
            ):
                found_spam_words += 5
        if found_spam_words > 2:
            return self.SPAM_TAG
        return self.HAM_TAG


if __name__ == "__main__":
    filter = MyFilter()
    filter.test("C:\\Programovani\\Python\\RPH\\HW\\Spam_filtr\\corpus")
