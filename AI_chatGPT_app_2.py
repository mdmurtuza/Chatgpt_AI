import openai
openai.api_key = "YOUR_API KEY"



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
