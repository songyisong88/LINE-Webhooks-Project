from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/")
async def home():
    return PlainTextResponse("Hello, LINE Webhook is running!")

# ไม่ต้องมี `if __name__ == "__main__"` เพราะ Deploy บน Cloud จะรันให้เอง

