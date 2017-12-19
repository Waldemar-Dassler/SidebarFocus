import sublime
import sublime_plugin

def plugin_reload():
    global close_sidebar_if_opened
    close_sidebar_if_opened = settings_base.get(
        'close_sidebar_if_opened', settings.get('close_sidebar_if_opened'))

class SidebarFocus(sublime_plugin.WindowCommand):
    def run(self):
        if not self.window.is_sidebar_visible():
            self.window.set_sidebar_visible(True)
            self.window.run_command("reveal_in_side_bar")
            sublime.set_timeout(
                lambda: self.window.run_command('focus_side_bar'), 50)
        else:
            if close_sidebar_if_opened:
                self.window.set_sidebar_visible(False)
                self.window.run_command("focus_group",{"group": 0})
                sublime.set_timeout(lambda: refresh_folders(self), 50)
            else:
                self.window.run_command("reveal_in_side_bar")
                self.window.run_command('focus_side_bar')