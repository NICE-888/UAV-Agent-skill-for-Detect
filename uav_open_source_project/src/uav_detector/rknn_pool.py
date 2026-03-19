from queue import Queue
from concurrent.futures import ThreadPoolExecutor

try:
    from rknnlite.api import RKNNLite
except Exception:  # pragma: no cover
    RKNNLite = None


class RKNNImportError(RuntimeError):
    pass


def init_rknn(model_path, core_id=0):
    if RKNNLite is None:
        raise RKNNImportError(
            "未检测到 rknnlite.api.RKNNLite。请在 RK3588 设备上安装 Rockchip 运行时后再执行。"
        )

    rknn_lite = RKNNLite()
    ret = rknn_lite.load_rknn(model_path)
    if ret != 0:
        raise RuntimeError(f"Load RKNN model failed: {model_path}, ret={ret}")

    if core_id == 0:
        ret = rknn_lite.init_runtime(core_mask=RKNNLite.NPU_CORE_0)
    elif core_id == 1:
        ret = rknn_lite.init_runtime(core_mask=RKNNLite.NPU_CORE_1)
    elif core_id == 2:
        ret = rknn_lite.init_runtime(core_mask=RKNNLite.NPU_CORE_2)
    elif core_id == -1:
        ret = rknn_lite.init_runtime(core_mask=RKNNLite.NPU_CORE_0_1_2)
    else:
        ret = rknn_lite.init_runtime()

    if ret != 0:
        raise RuntimeError(f"Init runtime environment failed, ret={ret}")

    print(f"{model_path}\t\tdone")
    return rknn_lite


def init_rknns(model_path, tpes=1):
    return [init_rknn(model_path, i % 3) for i in range(tpes)]


class RknnPoolExecutor:
    def __init__(self, model_path, tpes, func):
        self.tpes = tpes
        self.queue = Queue()
        self.rknn_pool = init_rknns(model_path, tpes)
        self.pool = ThreadPoolExecutor(max_workers=tpes)
        self.func = func
        self.num = 0

    def put(self, frame):
        self.queue.put(self.pool.submit(self.func, self.rknn_pool[self.num % self.tpes], frame))
        self.num += 1

    def get(self):
        if self.queue.empty():
            return None, False
        fut = self.queue.get()
        return fut.result(), True

    def release(self):
        self.pool.shutdown()
        for rknn_lite in self.rknn_pool:
            rknn_lite.release()
