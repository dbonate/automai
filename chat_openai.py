from openai import OpenAI

def conversa_com_openai(openai_client, system_prompt, user_prompt):


	resposta = openai_client.chat.completions.create(
		model = "gpt-4o-2024-08-06",
		messages = [
			{'role': 'system', 'content': system_prompt},
			{'role': 'user', 'content': user_prompt}
		],
		temperature=0.7
		)

	print(resposta.choices[0].message.content)
if __name__ == "__main__":

	openai_client = OpenAI(api_key = 'KEY-OPENAI-CHATGPT')
	system_prompt = "Você é um cientista muito famoso como por exemplo Einstein."
	user_prompt = "Me explique a teoria da relatividade."

	resposta = conversa_com_openai(openai_client, system_prompt, user_prompt)
	print(resposta)