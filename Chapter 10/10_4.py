"""
logging 设置自定义Formatter对象定制日志输出格式代码示例
"""
import logging

if __name__ == '__main__':
    logger = logging.getLogger("Test")
    logger.setLevel(logging.INFO)
    # 自定义Formatter对象
    fmt = logging.Formatter("%(asctime)s %(process)d:%(processName)s- %(levelname)s === %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S %p")
    # 输出到控制台
    s_handler = logging.StreamHandler()
    s_handler.setLevel(logging.WARNING)
    s_handler.setFormatter(fmt)
    logger.addHandler(s_handler)

    # 输出到文件
    f_handler = logging.FileHandler('test.log', encoding='UTF-8')
    f_handler.setLevel(logging.DEBUG)
    f_handler.setFormatter(fmt)
    logger.addHandler(f_handler)

    logger.debug("Debug 级别的信息")
    logger.info("Info 级别的信息")
    logger.warning("Warning 级别的信息")
    logger.error("Error 级别的信息")
    logger.critical("Critical 级别的信息")
