import threading
import time

from config import RATE, CHUNK, RECORD_SECONDS, STREAM, QUEUE_LOCK, P


class VoiceCaptureThread (threading.Thread):
    """
    声音捕捉线程
        当前是3秒为一个阶段进行的捕捉，捕捉完成之后传入处理队列。
    """
    def __init__(self, thread_id, name, queue_frames_data, queue_name_data):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.queue_frame_data = queue_frames_data
        self.queue_name_data = queue_name_data

        self.exit = False

    def run(self):
        while True:
            frames = []
            frames.append(time.strftime("%H:%M:%S", time.localtime()))
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = STREAM.read(CHUNK)
                frames.append(data)
            frames.append(time.strftime("%H:%M:%S", time.localtime()))
            if not self.queue_frame_data.full():
                QUEUE_LOCK.acquire()
                self.queue_frame_data.put(frames)
                QUEUE_LOCK.release()

            if self.exit:
                break

    def stop(self):
        self.exit = True
