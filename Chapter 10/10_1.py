"""
logging模块最简单使用代码示例
"""
import logging

if __name__ == '__main__':
    # 获得一个Logger
    logger = logging.getLogger("Test")

    # logging提供的简单的配置方法，自行配置的话需要手动添加handler
    logging.basicConfig()

    # 设置输出的log级别(大于或等于此级别的才会输出)，默认级别Warning
    logger.setLevel(logging.INFO)
    logger.debug("=== Debug 级别的信息 ===")
    logger.info("=== Info 级别的信息 ===")
    logger.warning("=== Warning 级别的信息 ===")
    logger.error("=== Error 级别的信息 ===")
    logger.critical("=== Critical 级别的信息 ===")
