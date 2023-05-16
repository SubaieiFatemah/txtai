class Questions(Data):
    """
    Tokenizes question-answering datasets as input for training question-answering models.
    """

    def __init__(self, tokenizer, columns, maxlength, stride):
        """
        Creates a new instance for tokenizing Questions training data.

        Args:
            tokenizer: model tokenizer
            columns: tuple of columns to use for question/context/answer/answer_start
            maxlength: maximum sequence length
            stride: chunk size for splitting data for QA tasks
        """

        super().__init__(tokenizer, columns, maxlength)

        if not self.columns:
            self.columns = ("question", "context", "answers", "answer_start")

        self.question, self.context, self.answer, self.answer_start = self.columns
        self.stride = stride
        self.rpad = tokenizer.padding_side == "right"

    # Rest of your code...

    def process(self, data):
        # Rest of your code...

        for x, offset in enumerate(offsets):
            # Label NO ANSWER with CLS token
            inputids = tokenized["input_ids"][x]
            clstoken = inputids.index(self.tokenizer.cls_token_id)

            # Sequence ids
            sequences = tokenized.sequence_ids(x)

            # Get and format answer
            answers = self.answers(data, samples[x], index)

            # Rest of your code...

    def answers(self, data, index):
        """
        Gets and formats an answer.

        Args:
            data: input examples
            index: answer index to retrieve

        Returns:
            answers dict
        """

        # Answer mappings
        answers = data[self.answer][index]
        answer_start = data[self.answer_start][index]
        context = data[self.context][index]

        # Handle mapping string answers to dict
        if not isinstance(answers, dict):
            if not answers:
                answers = {"text": [], "answer_start": []}
            else:
                answers = {"text": [answers], "answer_start": [int(answer_start)]} # Note the change here

        return answers
