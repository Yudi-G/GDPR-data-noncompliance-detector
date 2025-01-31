import os
from transformers import DebertaV2Tokenizer, DebertaV2ForSequenceClassification, pipeline


class GDPR:

    def __init__(self):
        self.max_length_ = 512
        self.classifier = pipeline("text-classification", model="BananaFish45/gdpr_personal_data")
        self.max_length = self.max_length_

    def run_GDPR(self, text):
        return self.predict(text)


    def sliding_window(self, text, window_size, overlap):
        tokens = self.classifier.tokenizer.encode(text, truncation=False)
        chunks = []
        for i in range(0, len(tokens), window_size - overlap):
            chunk = tokens[i:i + window_size]
            if len(chunk) < window_size:
                break
            chunks.append(chunk)
        return chunks

    def predict(self, input_text):
        window_size = 128  # Adjust based on your model's max_length
        overlap = 64       # Adjust based on desired overlap

        chunks = self.sliding_window(input_text, window_size, overlap)
        labels = []

        for chunk in chunks:
            truncated_text = self.classifier.tokenizer.decode(chunk, skip_special_tokens=True)
            result = self.classifier(truncated_text)
            label = result[0]['label']
            labels.append(label)

        return labels

if __name__ == '__main__':
    gdpr = GDPR()
    print(gdpr.run_GDPR("Samantha Schultz lives at 5365 Julie Union, Lake Jorgemouth, PA 90372. Contact them at johnsonjames@valencia-boyer.com or 5020153600.,Samantha,Schultz,S,2020-06-20,5365 Julie Union, Lake Jorgemouth, PA 90372,johnsonjames@valencia-boyer.com,5020153600,+1-762-972-3354,042-45-5223,XD20386955,445-92-8929,950-96-6247"))#Personal Data
    print(gdpr.run_GDPR("Food life marriage book if business. Long beat accept tell. Support method field agency several break citizen amount."))#No personal data
    print(gdpr.run_GDPR("John Doe's email is john.doe@example.com and his phone number is 123-456-7890."))#Personal data
    print(gdpr.run_GDPR("Yeshlen Moddley is an Asian business man crooked man indeed"))#Personal data
    print(gdpr.run_GDPR("This document contains general information about the company's financials"))#No personal data
    print(gdpr.run_GDPR("Jonas Motha is a school admin clerk"))#No Ethnicity 
    print(gdpr.run_GDPR("Micheal Simon is an Caucasian programmer "))#Personal data
    print(gdpr.run_GDPR("Nevin Thomas is an Hispanic scammer"))#Personal data
    print(gdpr.run_GDPR("Samantha Williams is an African American"))#Personal data
    