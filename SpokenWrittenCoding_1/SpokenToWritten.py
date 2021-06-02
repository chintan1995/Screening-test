from word2number import w2n
import re


def replace_tuple(text):
    text = re.sub('(double)( *)([A-Za-z])(.*)', '\\3\\3\\4', text, flags=re.IGNORECASE)
    text = re.sub('(triple)( *)([A-Za-z])(.*)', '\\3\\3\\3\\4', text, flags=re.IGNORECASE)
    text = re.sub('(quadruple)( *)([A-Za-z])(.*)', '\\3\\3\\3\\3\\4', text, flags=re.IGNORECASE)
    text = re.sub('(quintuple)( *)([A-Za-z])(.*)', '\\3\\3\\3\\3\\3\\4', text, flags=re.IGNORECASE)
    text = re.sub('(sextuple)( *)([A-Za-z])(.*)', '\\3\\3\\3\\3\\3\\3\\4', text, flags=re.IGNORECASE)
    text = re.sub('(septuple)( *)([A-Za-z])(.*)', '\\3\\3\\3\\3\\3\\3\\3\\4', text, flags=re.IGNORECASE)
    text = re.sub('(octuple)( *)([A-Za-z])(.*)', '\\3\\3\\3\\3\\3\\3\\3\\3\\4', text, flags=re.IGNORECASE)
    return text


def replace_currency(text):
    text = re.sub('([0-9]*)( *)(dollars|dollar)', '$\\1', text, flags=re.IGNORECASE)
    text = re.sub('([0-9]*)( *)(rupees|rupee)', '₹\\1', text, flags=re.IGNORECASE)
    text = re.sub('([0-9]*)( *)(euros|euro)', '€\\1', text, flags=re.IGNORECASE)
    text = re.sub('([0-9]*)( *)(yen)', '¥\\1', text, flags=re.IGNORECASE)
    return text


def replace_numbers(text):
    num_reg = '((one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen|sixteen' \
              '|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|hundred|thousand' \
              '|million|billion|trillion)( (one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen' \
              '|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty' \
              '|ninety|hundred|thousand|million|billion|trillion))*) '

    text = re.sub(num_reg, lambda x: str(w2n.word_to_num(x.group())) + ' ', text, flags=re.IGNORECASE)
    return text


def replace_weight(text):
    text = re.sub('kilograms', 'KG', text, flags=re.IGNORECASE)
    text = re.sub('grams', 'G', text, flags=re.IGNORECASE)
    text = re.sub('pound', 'lbs', text, flags=re.IGNORECASE)
    return text


def replace_abbreviation(text):
    # Inspired by, https://stackoverflow.com/a/45592012/7697658
    text = re.sub(r'\b([A-Za-z]) (?=[A-Za-z]\b)', r'\g<1>', text, flags=re.IGNORECASE)
    return text


def convert(text):
    text = replace_numbers(text)
    text = replace_currency(text)
    text = replace_tuple(text)
    text = replace_weight(text)
    text = replace_abbreviation(text)
    return text


if __name__ == '__main__':
    text = 'I have three hundred TWo dollars in my two pockets. Total six hundred two dollar. Triple H is a wwe star. ' \
           'He weighs aroung 150 pound. He talked about double k. Double k wakes up at twelve P M. He also said that, H T M L is a good markup language.'

    print(convert(text))