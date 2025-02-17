from google.cloud import language_v1
from dotenv import load_dotenv


def analyze_syntax(text_content):
    client = language_v1.LanguageServiceClient()

    type_ = language_v1.Document.Type.PLAIN_TEXT
    language = "en"
    document = {"content": text_content, "type_": type_, "language": language}

    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_syntax(
            request={"document": document, "encoding_type": encoding_type}
    )
    for token in response.tokens:
        text = token.text
        print(f"Token text: {text.content}")
        print(f"Location of this token in overall document: {text.begin_offset}")

        part_of_speech = token.part_of_speech
        tag = language_v1.PartOfSpeech.Tag(part_of_speech.tag)

        print(f"Part of Speech tag: {tag.name}")

        match tag:
            case language_v1.PartOfSpeech.Tag.VERB:
                print(f"Tense: {language_v1.PartOfSpeech.Tense(part_of_speech.tense).name}")
                print(f"Mood: {language_v1.PartOfSpeech.Mood(part_of_speech.mood).name}")

            case language_v1.PartOfSpeech.Tag.NOUN:
                print(f"Gender: {language_v1.PartOfSpeech.Gender(part_of_speech.gender).name}")
                print(f"Number: {language_v1.PartOfSpeech.Number(part_of_speech.number).name}")

            case language_v1.PartOfSpeech.Tag.PRON:
                print(f"Person: {language_v1.PartOfSpeech.Person(part_of_speech.person).name}")

        print(f"Lemma: {token.lemma}\n")

    print(f"Language of the text: {response.language}")


if __name__ == "__main__":
    load_dotenv()
    text_1 = ("I ask you this: remove the cell from its chamber, and bring it far to the east. "
              "To a friend... if she is somehow still alive.")

    text_2 = ("Thank you. I suppose this makes us... even? "
              "Goodbye, wet mouse. Send my regards.")

    analyze_syntax(text_1)
