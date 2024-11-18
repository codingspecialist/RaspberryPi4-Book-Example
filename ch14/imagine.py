import openai

openai.api_key = "Your API Key"


response = openai.images.generate(
  model="dall-e-3",
  prompt="핫도그 먹는 고양이 사진 보여줘",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

print(image_url)