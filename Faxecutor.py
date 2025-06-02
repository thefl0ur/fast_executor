import subprocess
import tempfile

import sublime_plugin


DEFAULT_EXECUTOR = "python3"
DEFAULT_SUFFIX = ".py"
DEFAULT_SYNTAX = "Packages/Python/Python.sublime-syntax"


class Settings:
    def __init__(self, **kwargs):
        self.suffix = kwargs.get("suffix", DEFAULT_SUFFIX)
        self.executor = kwargs.get("executor", DEFAULT_EXECUTOR)
        self.options = kwargs.get("options")
        self.syntax = kwargs.get("syntax", DEFAULT_SYNTAX)


class FaxecutorCommand(sublime_plugin.TextCommand):
    def _save_if_needed(self):
        if self.view.file_name() and not self.view.is_dirty():
            return

        if not self.view.file_name():
            with tempfile.NamedTemporaryFile(
                delete=False, suffix=self.settings.suffix, mode="w"
            ) as tmp_file:
                self.view.retarget(tmp_file.name)

        self.view.run_command("save")

    def _show_output(self, message):
        output = self.view.window().create_output_panel("faxecutor_result")
        output.run_command("insert", {"characters": message})
        self.view.window().run_command(
            "show_panel", {"panel": "output.faxecutor_result"}
        )

    def _call(self):
        call_args = [self.settings.executor, self.view.file_name()]

        if self.settings.options:
            call_args[1:1] = self.settings.options

        try:
            command_result = subprocess.check_output(
                call_args, universal_newlines=True, stderr=subprocess.STDOUT, timeout=10
            )
        except subprocess.CalledProcessError as e:
            return e.output
        except (Exception, FileNotFoundError) as e:
            return str(e)
        else:
            return command_result

    def run(self, _, **kwargs):
        self.settings = Settings(**kwargs)

        self.view.set_syntax_file(self.settings.syntax)
        self._save_if_needed()
        self._show_output(self._call())
