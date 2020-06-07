from sanic import Sanic
from sanic.response import json

app = Sanic("App Name")

@app.route("/app2")
async def test(request):
    return json({"name": "app2"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)