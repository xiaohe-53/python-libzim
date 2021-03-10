# -*- coding:utf-8 -*-

from libzim.reader import Archive

zim = Archive("/home/xiaohe/wikiZIM/wikipedia_zh_all.zim")
print(f"Main entry is at {zim.main_entry.get_item().path}")
entry = zim.get_entry_by_path("性交")
print(f"Entry {entry.title} at {entry.path} is {entry.get_item().size}b:")
print(bytes(entry.get_item().content).decode("UTF-8"))