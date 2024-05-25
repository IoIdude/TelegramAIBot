import httpx

from openai import AsyncOpenAI
from utils.config import TOKEN_GPT, PROXY
from sources.information import inf

client = AsyncOpenAI(api_key=TOKEN_GPT,
                     http_client=httpx.AsyncClient(
                         proxies=PROXY
                     )
                     )


async def answer(q):
    inf.append({"role": "user", "content": str(q)})
    resp = await client.chat.completions.create(messages=inf, model="gpt-4o")
    inf.append({"role": "user", "content": resp.choices[0].message.content.strip()})
    return resp.choices[0].message.content.strip()
