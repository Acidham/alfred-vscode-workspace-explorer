#!/usr/bin/python3

import os
import platform
import sys
from pathlib import PurePath

from Alfred3 import Items, Tools


def get_files(r_path):
    file_list = list()
    for root, dirs, files in os.walk(r_path):
        f_lst = ["{0}/{1}".format(root, f) for f in files]
        file_list.extend(f_lst)
    return file_list


def get_dirs(r_path):
    dir_list = list()
    for p in os.listdir(r_path):
        if os.path.isdir(r_path):
            d = "{0}/{1}".format(r_path, p)
            dir_list.append(d)
    return dir_list


Tools.logPyVersion()

f_path = Tools.getEnv('mypath')
# TODO: Debugging line below
Tools.log(f"this is f_path: {f_path}")
ws_home = f_path if f_path else os.path.expanduser(Tools.getEnv('workspaces_home'))
p_path = str(PurePath(f_path).parent) if f_path and f_path != Tools.getEnv('workspaces_home') else str()

query = Tools.getArgv(1)
if query == str():
    it = sorted(get_dirs(ws_home))
else:
    it = sorted(get_files(ws_home))

wf = Items()
if p_path:
    wf.setItem(
        title='Back',
        arg=p_path
    )
    wf.setIcon(m_path='back.png', m_type='image')
    wf.addItem()
if len(it) > 0:
    for i in it:
        # TODO: Remove just for debugging
        pp = PurePath(i).stem.lower()
        if (query == str() or query.lower() in PurePath(i).stem.lower()) and not(os.path.basename(i).startswith('.')):
            ic = 'folder.png' if os.path.isdir(i) else 'workspace.png'
            sub = 'Folder' if os.path.isdir(i) else "Workspace in VSCode"
            title = os.path.basename(i).replace('.code-workspace', '')
            wf.setItem(
                title=title,
                subtitle=f'\u23CE to open {sub}',
                arg=i
            )
            wf.setIcon(m_path=ic, m_type='image')
            wf.addItem()
    if len(wf.getItems(response_type='dict').get('items')) == 0:
        wf.setItem(
            title="Search does not match a workspace",
            subtitle="...try again",
            valid=False
        )
        wf.addItem()
else:
    wf.setItem(
        title="No Workspace files or Folders found",
        valid=False
    )
    wf.addItem()
wf.write()
