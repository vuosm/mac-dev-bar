import rumps
import psutil

class DevBar(rumps.App):
    def __init__(self):
        super().__init__("⚡")

        self.cpu_item = rumps.MenuItem("CPU: ...")
        self.ram_item = rumps.MenuItem("RAM: ...")
        self.disk_item = rumps.MenuItem("Disk: ...")

        self.quit_item = rumps.MenuItem("Quit")

        self.menu = [
            self.cpu_item,
            self.ram_item,
            self.disk_item,
            None,
            self.quit_item
        ]

        self.timer = rumps.Timer(self.update_stats, 1)
        self.timer.start()

    def update_stats(self, _=None):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        self.cpu_item.title = f"CPU: {cpu}%"
        self.ram_item.title = f"RAM: {ram}%"
        self.disk_item.title = f"Disk: {disk}%"

    @rumps.clicked("Quit")
    def quit_app(self, _):
        rumps.quit_application()


if __name__ == "__main__":
    DevBar().run()