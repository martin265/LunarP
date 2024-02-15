import flet as ft


class SidebarMenu:
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        #  ================ the list for all the pages here =========== //
        self.all_pages = []
        # ============= calling the selected index page function ========= //
        self.select_page_destination()
    
        # =========== the main side navigation for the desktop application will be here ======== //
        self.navigation_rail = ft.NavigationRail(
            leading=ft.FloatingActionButton(
                content=ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Icon(ft.icons.PHONE_ANDROID_ROUNDED, size=30)
                        ]
                    )
                )
            ),
            selected_index=0,
            min_width=80,
            min_extended_width=50,
            expand=False,
            group_alignment=-0.9,
            height=400,
            #  ================ // the navigation destinations will be here ======= //
            destinations=[
                ft.NavigationRailDestination(
                    icon_content=ft.Icon(ft.icons.DASHBOARD_ROUNDED, color=ft.colors.BLACK),
                    label_content=ft.Text(
                        "main dashboard".title(),
                        size=20,
                        color=ft.colors.BLACK,
                    )
                )
            ],
            on_change=self.destination_pages

        )

    #  ================ function to control the transition of the pages here ========== //
    async def select_page_destination(self):
        """the function will be used to control page transitions"""
        try:
            for single_page, index in enumerate(self.all_pages):
                single_page.visible = True if index == self.navigation_rail.selected_index else False
                await self.page.update_async()
        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                bgcolor=ft.colors.RED_ACCENT,
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            self.page.snack_bar.open = True
            await self.page.update_async()

    #  ===================== function will call the selected index function ========== //
    async def destination_pages(self, e):
        try:
            await self.select_page_destination()

        except Exception as ex:
            self.page.snack_bar = ft.SnackBar(
                bgcolor=ft.colors.RED_ACCENT,
                content=ft.Row(
                    controls=[
                        ft.Text(
                            "something went wrong at {}".format(ex)
                        )
                    ]
                )
            )
            self.page.snack_bar.open = True
            await self.page.update_async()

    def build(self):
        return self.navigation_rail
        
