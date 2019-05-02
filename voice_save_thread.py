import threading
import wave

from config import RATE, CHANNELS, FORMAT, QUEUE_LOCK, P


class VoiceSaveThread(threading.Thread):
    """
    声音存储线程
        由于，使用的python接口仅仅支持语音文件识别，所以需要将音频数据暂存为文件
        文件将存在temp目录下
    """
    def __init__(self, thread_id, name, queue_frames_data, queue_name_data):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.queue_frames_data = queue_frames_data
        self.queue_name_data = queue_name_data

        self.exit = False

    def run(self):
        temp_count = 0
        while True:
            if self.exit:
                # print("Over")
                break
            frames_data = None
            if not self.queue_frames_data.empty():
                QUEUE_LOCK.acquire()
                frames_data = self.queue_frames_data.get()
                QUEUE_LOCK.release()
                if len(frames_data) > 1:
                    cap_time_start = frames_data.pop(0)
                    cap_time_end = frames_data.pop(-1)
                    save_data = []
                    save_data.append(cap_time_start)
                    save_data.append(cap_time_end)
                    filename = "temp/temp" + str(temp_count) + ".wav"
                    save_data.append(filename)
                    self.__record(filename, frames_data)
                    temp_count += 1
                    if temp_count > 10:
                        temp_count = 0
                    if not self.queue_name_data.full():
                        QUEUE_LOCK.acquire()
                        self.queue_name_data.put(save_data)
                        QUEUE_LOCK.release()

    def __record(self, filename, frames_data):
        # print("save recording")
        wf = wave.open(filename, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(P.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames_data))
        wf.close()

    def stop(self):
        self.exit = True
