# Forked from https://gist.github.com/925008
# Makes it work with Ruby on Rails snippets
# https://github.com/tadast/sublime-rails-snippets#sublime-text-2-rails-snippets

import sublime, sublime_plugin
import os


class DetectFileTypeCommand(sublime_plugin.EventListener):
    """ Detects current file type if the file's extension isn't conclusive """
    """ Modified for Ruby on Rails and Sublime Text 2 """
    """ Original pastie here: http://pastie.org/private/kz8gtts0cjcvkec0d4quqa """

    def on_load(self, view):
        filename = view.file_name()
        if not filename:  # buffer has never been saved
            return

        name = os.path.basename(filename.lower())
        if name[-8:] == "_spec.rb":
            set_syntax(view, "Rspec", "User/rspec")
        elif name == "factories.rb":
            set_syntax(view, "Rspec", "User/rspec")
        elif name == "gemfile":
            set_syntax(view, "Ruby on Rails", "Ruby on Rails snippets")
        elif name[-2:] == "rb":
            set_syntax(view, "Ruby on Rails", "Ruby on Rails snippets")


def set_syntax(view, syntax, path=None):
    if path is None:
        path = syntax
        view.settings().set('syntax', 'Packages/' + path + '/' + syntax + '.tmLanguage')
        print "Switched syntax to: " + syntax
