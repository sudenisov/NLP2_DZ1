def transform_to_yoda_style(answer):
    words = answer.split()
    random.shuffle(words)
    yoda_style_answer = ' '.join(words)
    yoda_style_answer = yoda_style_answer.capitalize()
    yoda_style_answer += ", " + random.choice(["Yes, hmmm", "Difficult question, this is", "Yes, yes, hmmm"])
    return yoda_style_answer


def preprocess_dataset(file_path, tokenizer):
    inputs = []
    labels = []
    question = []
    answer = []

    with open(file_path, 'r', encoding='utf-8') as file, open(output_file_path, 'w', encoding='utf-8') as output_file:
        for line in file:
            question_inp, answer_inp = line.strip().split('\t')
            answer_yoda = transform_to_yoda_style(answer_inp)
            output_file.write(f"{question_inp}\t{answer_yoda}\n")
            # Tokenize вопрос и ответ
            question_tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(question_inp, add_special_tokens=True)))
            answer_tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(answer_yoda, add_special_tokens=True)))

            # Формирование входных и выходных данных
            inputs.append(question_tokens)
            labels.append(answer_tokens)

            question.append(question_inp)
            answer.append(answer_yoda)

    return inputs, labels, question, answer