import asyncio
from playwright.async_api import async_playwright
from telegram import Bot

TOKEN = "8643358251:AAEoGGeeo2-GVZOVJ0npir-xBJf8cINkOUo"
CHAT_ID = "8724235762"

async def send_notification(message):
    bot = Bot(token=TOKEN)
    await bot.send_message(chat_id=CHAT_ID, text=message)

async def check_slots():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # 先看得见，调试用
        page = await browser.new_page()
        
        await page.goto("https://v7hwg3.b-merit.jp/e9rsha/web/reserve1/?from_coupon=1&redirect=1")
        await page.wait_for_load_state("networkidle")
        
        # 截图看看页面长啥样
        await page.screenshot(path="debug.png")
        print("截图已保存，查看 debug.png")
        
        await browser.close()

asyncio.run(check_slots())