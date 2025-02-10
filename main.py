import flet as ft
import asyncio


class YouTubeClone(ft.View):
    def __init__(self, page):
        super().__init__(route="/home")
        self.page = page
        self.controls.append(self.build_ui())
    
    def create_video_card(self, title, channel, views, thumbnail):
        return ft.Column([
            ft.Container(
                content=ft.Image(src=thumbnail, width=350, height=200, fit=ft.ImageFit.COVER),
                border_radius=ft.border_radius.all(10),
            ),
            ft.Text(title, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            ft.Text(f"{channel} • {views} views", size=12, color=ft.colors.GREY_400),
        ], spacing=5)
    
    def build_ui(self):
        search_bar = ft.Row([
            ft.TextField(hint_text="Search", expand=True, bgcolor=ft.colors.WHITE, border_radius=10),
            ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE)
        ], alignment=ft.MainAxisAlignment.CENTER, spacing=10)

        video_list = ft.ListView(
            controls=[
                self.create_video_card("Flet UI Tutorial", "Flet Dev", "1.2M", "https://source.unsplash.com/350x200/?coding"),
                self.create_video_card("Python Basics", "Tech Guru", "850K", "https://source.unsplash.com/350x200/?python"),
                self.create_video_card("Godot 4 Game Dev", "GameZone", "500K", "https://source.unsplash.com/350x200/?gaming"),
                self.create_video_card("FastAPI Explained", "DevStack", "400K", "https://source.unsplash.com/350x200/?api"),
            ],
            expand=True
        )

        return ft.Column([
            ft.Container(content=search_bar, padding=10),
            ft.Container(content=video_list, expand=True, padding=10)
        ])

class SplashScreen(ft.View):
    def __init__(self, page):
        super().__init__(route="/")
        self.page = page
        self.controls.append(
            ft.Column([
                ft.Text("Loading YouTube Clone...", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                ft.ProgressRing()
            ], alignment=ft.MainAxisAlignment.CENTER, spacing=20)
        )
        self.page.run_task(self.load_main)

    async def load_main(self):
        await asyncio.sleep(2)  # Fixed sleep issue
        self.page.go("/home")

def main(page: ft.Page):
    page.title = "YouTube Clone"
    page.bgcolor = ft.colors.BLACK
    page.scroll = "adaptive"
    page.window.width = 400  # Mobile-friendly width
    page.window.height = 800  # Mobile-friendly height
    
    def route_change(route):
        page.views.clear()
        if route.route == "/":
            page.views.append(SplashScreen(page))
        elif route.route == "/home":
            page.views.append(YouTubeClone(page))
        page.update()
    
    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)