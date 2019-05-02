from PyQt5 import QtCore
from PyQt5.QtCore import QThread
import os
import time
from sqlite_util import insert_word_data

from aip import AipSpeech

from config import QUEUE_LOCK
from sqlite_util import query


class BaiDuAPIThread(QThread):
    """
    音频数据线程
        该线程是QThread线程，在获取音频文字内容的同时还将向UI界面推送数据。
    """

    signOut = QtCore.pyqtSignal(str)

    def __init__(self, thread_id, name, queue_name_data):
        super(BaiDuAPIThread, self).__init__()
        self.thread_id = thread_id
        self.name = name
        self.queue_name_data = queue_name_data
        beta_data = query()
        self.app_id = beta_data[1]
        self.api_key = beta_data[2]
        self.secret_key = beta_data[3]
        self.client = AipSpeech(self.app_id, self.api_key, self.secret_key)

        self.out = False

    def run(self):
        count = 0
        id = 0
        word_database_name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        while True:
            if self.out:
                break
            if not self.queue_name_data.empty():
                QUEUE_LOCK.acquire()
                save_data = self.queue_name_data.get()
                QUEUE_LOCK.release()
                if len(save_data) > 1:
                    rd = self.__get_file_content(save_data[2], count)
                    if rd is not None:
                        result_line = save_data[0] + " >> " + save_data[1] + "+:+" + rd
                        insert_word_data(word_database_name, str(id), save_data[0], save_data[1], rd)
                        self.signOut.emit(result_line)
                        save_data = None
                        count += 1
                        id += 1
                        if count > 2:
                            count = 0

    def __get_file_content(self, file_path, now_number):
        with open(file_path, 'rb') as fp:
            line = self.client.asr(fp.read(), 'wav', 16000, {
                'dev_pid': 1537,
            })
        os.remove(file_path)
        if line['err_no'] == 0:
            line = line['result'][0]
            print(line)
            return str(now_number) + "+:+" + line
        else:
            # return str(now_number) + ":识别错误。"
            return None
        # 读取文件 识别本地文件

    def stop(self):
        self.out = True
