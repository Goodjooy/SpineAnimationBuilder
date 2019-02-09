import os

import wx

from frame import main_frame as mf
from mod_act.classes import mod_load
from pygame_work import link_worker


class MainFrame(mf.MyFrame1):
    def __init__(self, parent):
        super(MainFrame, self).__init__(parent)

        self.type_use = 0

        self.tex_path = ''
        self.div_path = ''
        self.work_path = ''

        self.dialog: wx.Dialog = None

        self.model_group = mod_load.Model()

    def __able_work(self):
        if self.type_use == 0:
            return os.path.isfile(self.tex_path) and os.path.isfile(self.div_path)
        else:
            return os.path.isfile(self.work_path)

    # 导入
    def change_in(self, event):
        self.type_use = self.m_radioBox_in_type.GetSelection()

        self.m_simplebook1.SetSelection(self.type_use)

    def get_tex_file(self, event):
        self.tex_path = self.m_filePicker_tex.GetPath()
        if self.__able_work():
            self.model_group = mod_load.Model.open(self.tex_path, self.div_path)
            self.m_listBox_submodel.Set(self.model_group.bilt_sort)

    def get_div_file(self, event):
        self.div_path = self.m_filePicker_txt.GetPath()
        if self.__able_work():
            self.model_group = mod_load.Model.open(self.tex_path, self.div_path)
            self.m_listBox_submodel.Set(self.model_group.bilt_sort)

    def get_work_file(self, event):
        self.model_group = mod_load.Model.load(self.m_filePicker_work.GetPath())
        self.m_listBox_submodel.Set(self.model_group.bilt_sort)

    def save_work(self, event):
        self.dialog = wx.DirDialog(self, '选择保存文件夹（*注意：将会自动新建文件夹哦~）', os.getcwd(),
                                   wx.DD_CHANGE_DIR | wx.DD_NEW_DIR_BUTTON)

        val = self.dialog.ShowModal()

        if val == wx.ID_OK:
            self.model_group.save(self.dialog.GetPath())

    def link(self, event):
        select = self.model_group[self.m_listBox_submodel.GetSelection()]
        self.dialog = LinkWork(self, select, self.model_group)

        self.dialog.ShowModal()


class LinkWork(mf.MyDialog_set_link):
    def __init__(self, parent, mod: mod_load.SubModel, model_group: mod_load.Model):
        super(LinkWork, self).__init__(parent)
        wx.Locale(wx.LANGUAGE_CHINESE)

        self.model = mod

        self.model_group = model_group

        self.view_work: link_worker.LinkWorker = None

        self.m_staticText_mod.SetLabel(f"部件：{self.model.name}")

        var = self.model_group.bilt_sort
        var.remove(self.model.name)
        link = ["固定"]
        link.extend(var)

        self.m_choice_links.Set(link)

    def link_work(self, event):
        select = self.m_choice_links.GetSelection()
        select = self.model_group[select]

        self.view_work = link_worker.LinkWorker(self.model, select)

    def select_be_linked(self, event):
        """
        被连接--》子部件上
        :param event:
        :return:
        """
        self.view_work.change_type(1)
        try:
            self.view_work.start()
        except RuntimeError:
            pass

    def select_link(self, event):
        """连接"""
        self.view_work.change_type(0)
        try:
            self.view_work.start()
        except RuntimeError:
            pass
