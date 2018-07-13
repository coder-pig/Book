"""
logging 通过basicConfig函数配置日志输出代码示例
"""
import logging

if __name__ == '__main__':
    logger = logging.getLogger("Test")
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s %(process)d:%(processName)s- %(levelname)s === %(message)s",
                        datefmt="%Y-%m-%d %H:%M:%S %p")

    logger.debug("Debug 级别的信息")
    logger.info("Info 级别的信息")
    logger.warning("Warning 级别的信息")
    logger.error("Error 级别的信息")
    logger.critical("Critical 级别的信息")
