import webbrowser

class Browser:
    def __init__(self, web_browser, path_to_browser_exec):
        self.web_browser = web_browser
        webbrowser.register(
            web_browser,
            None,
            webbrowser.BackgroundBrowser(path_to_browser_exec)
        )

    def open_link(self, link):
        webbrowser.get(self.web_browser).open_new_tab(link)