import sublime
import sublime_plugin


class CloseProjectAndExitCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("close_project")
        self.window.run_command("close_window")
