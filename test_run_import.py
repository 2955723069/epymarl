#!/usr/bin/env python
import os
import sys
import yaml
from copy import deepcopy

# 添加src目录到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from utils.logging import get_logger

# 模拟main.py的配置加载过程
def test_run_import():
    logger = get_logger()
    
    # 加载默认配置
    with open(os.path.join('src', 'config', 'default.yaml'), 'r') as f:
        config_dict = yaml.load(f, Loader=yaml.FullLoader)
    
    # 测试1: group算法，应该使用interval_run.py
    logger.info("=== 测试group算法 ===")
    with open(os.path.join('src', 'config', 'algs', 'group.yaml'), 'r') as f:
        alg_config = yaml.load(f, Loader=yaml.FullLoader)
    
    # 合并配置
    for k, v in alg_config.items():
        if isinstance(v, dict) and k in config_dict:
            config_dict[k].update(v)
        else:
            config_dict[k] = v
    
    # 动态导入run函数
    run_module = config_dict.get("run", "run")
    logger.info(f"Using run module: {run_module}")
    if run_module == "interval_run":
        logger.info("✓ group算法将使用interval_run.py")
    else:
        logger.error("✗ group算法没有使用interval_run.py")
    
    # 测试2: qmix算法，应该使用默认的run.py
    logger.info("\n=== 测试qmix算法 ===")
    # 重新加载默认配置
    with open(os.path.join('src', 'config', 'default.yaml'), 'r') as f:
        config_dict = yaml.load(f, Loader=yaml.FullLoader)
    
    with open(os.path.join('src', 'config', 'algs', 'qmix.yaml'), 'r') as f:
        alg_config = yaml.load(f, Loader=yaml.FullLoader)
    
    # 合并配置
    for k, v in alg_config.items():
        if isinstance(v, dict) and k in config_dict:
            config_dict[k].update(v)
        else:
            config_dict[k] = v
    
    # 动态导入run函数
    run_module = config_dict.get("run", "run")
    logger.info(f"Using run module: {run_module}")
    if run_module != "interval_run":
        logger.info("✓ qmix算法将使用默认的run.py")
    else:
        logger.error("✗ qmix算法错误地使用了interval_run.py")

if __name__ == "__main__":
    test_run_import()