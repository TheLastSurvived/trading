from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import ccxt
import asyncio
import uvicorn

app = FastAPI()

# Монтируем статические файлы (HTML, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Подключение к бирже (например, Binance)
exchange = ccxt.binance()

# WebSocket endpoint для передачи данных в реальном времени
@app.websocket("/ws-btc")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            # Получаем данные о цене BTC/USDT
            ticker = exchange.fetch_ticker('BTC/USDT')
            price = ticker['last']
            # Отправляем данные клиенту
            
            await websocket.send_text(str(price))
            # Задержка для обновления данных (например, каждую секунду)
            await asyncio.sleep(1)
        except Exception as e:
            print(f"Ошибка: {e}")
            break
        

# WebSocket endpoint для передачи данных в реальном времени
@app.websocket("/ws-eth")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            # Получаем данные о цене ETH/USDT
            ticker = exchange.fetch_ticker('ETH/USDT')
            price = ticker['last']
            # Отправляем данные клиенту
            
            await websocket.send_text(str(price))
            # Задержка для обновления данных (например, каждую секунду)
            await asyncio.sleep(1)
        except Exception as e:
            print(f"Ошибка: {e}")
            break
        
        
# WebSocket endpoint для передачи данных в реальном времени
@app.websocket("/ws-ltc")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            # Получаем данные о цене LTC/USDT
            ticker = exchange.fetch_ticker('LTC/USDT')
            price = ticker['last']
            # Отправляем данные клиенту
            
            await websocket.send_text(str(price))
            # Задержка для обновления данных (например, каждую секунду)
            await asyncio.sleep(1)
        except Exception as e:
            print(f"Ошибка: {e}")
            break


@app.get("/")
def read_root():
    return FileResponse("static/index.html")


@app.get("/eth")
def read_root():
    return FileResponse("static/eth.html")

@app.get("/ltc")
def read_root():
    return FileResponse("static/ltc.html")


# Запуск сервера
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)