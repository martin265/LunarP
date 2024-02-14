import flet as ft


async def main(page: ft.Page):
    await page.add_async(ft.Text("hello world"))
    await page.update_async()

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets", port=9090)
