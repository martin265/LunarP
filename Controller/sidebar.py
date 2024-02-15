import flet as ft


class SidebarMenu:
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
    
        # =========== the main side navigation for the desktop application will be here ======== //
        self.navigation_rail = ft.NavigationRail(
            
        )

    def build(self):
        
