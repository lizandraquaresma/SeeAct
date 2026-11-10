import asyncio

from seeact.agent import SeeActAgent


async def run_agent():
    agent = SeeActAgent(
        model="openrouter/llama-nemotron-embed-vl-1b-v2:free",
        rate_limit=2,
        default_task="Você já está conectado(a) como emma.lopez@gmail.com . Para autenticar novamente, use as credenciais: emma.lopez@gmail.com / Senha.123. Se a reautenticação falhar, a sessão será encerrada com o status PERMISSION_DENIED_ERROR. Mantenha a sessão ativa; não faça logout nem troque de conta.",
        default_website="http://localhost:7770",
        max_auto_op=10,
    )

    await agent.start()

    try:
        while not agent.complete_flag:
            prediction_dict = await agent.predict()
            await agent.execute(prediction_dict)
    finally:
        await agent.stop()


if __name__ == "__main__":
    asyncio.run(run_agent())
