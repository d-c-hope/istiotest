from sanic import Sanic
from sanic.response import json
import aiohttp
import os

app = Sanic("App Name")
server2 = os.getenv('SERVER2')

@app.route("/app1")
async def test(request):
    async with aiohttp.ClientSession() as session:
        async with session.get('{}/app1'.format(server2)) as resp:
            resJSON = await resp.json()
            print(resJSON)
            # resJSON.update({"servername": "app1"})
            return json({"name": "app1", "app2Response" : resJSON})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)