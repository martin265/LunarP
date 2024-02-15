import flet as ft
from Controller.sidebar import SidebarMenu


async def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window_center = True
    await page.update_async()

    side_navigation = SidebarMenu(page=page)

    #  ============== including the side navigation here ===========//
    await page.add_async(
        side_navigation.navigation_rail,
        ft.Row(
            [
                ft.Column(side_navigation.all_pages, alignment=ft.MainAxisAlignment.START, expand=True)
            ],
            expand=True
        )
    )
    #  ================= // updating the ui here ================ //
    await page.update_async()

if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets", port=9090)
