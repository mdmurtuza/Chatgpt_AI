import openai
openai.api_key = "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"



while True:
    model_engine = "text-davinci-003"
    prompt = input('enter your prompt: ')
    if 'exit' in prompt or 'quit' in prompt:
        break

    completion = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 1024,
        n=1, stop =None,
        temparature=0.5)
    response = completion.choices[0].text
    print(response)