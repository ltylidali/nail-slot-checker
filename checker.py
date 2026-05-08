import asyncio
from playwright.async_api import async_playwright

MENU_IDS = ["check835584", "check491100"]  # mami定額, yuka定額

async def check_slots():
    print("开始运行...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("https://v7hwg3.b-merit.jp/e9rsha/web/reserve1/?from_coupon=1&redirect=1")
        await page.wait_for_load_state("networkidle")

        # 点击第一个菜单
        await page.click(f"label[for='{MENU_IDS[0]}']")         
        print(f"点击了 {MENU_IDS[0]}")
        
        await page.screenshot(path="debug.png")
        print("截图已保存！")
        
        await asyncio.sleep(3)
        await browser.close()

asyncio.run(check_slots())