# initialize_disk.py

from models import *
from file_pointer import file_func, FilePointer
from utils import *


def _do_initialization(fp):
    """实际的初始化逻辑，使用传入的文件指针 fp"""
    
    # ---- 定义内部辅助函数 ----
    def new_dir(sp, base_dir, name, parent_inode_id):
        inode_id = sp.get_free_inode_id(fp)
        inode = INode(inode_id, ROOT_ID)
        base_dir.add_new_cat(name=name, inode_id=inode_id)
        dir_write_back(sp, inode, bytes(CatalogBlock(name, parent_inode_id)))
        inode.write_back(fp)

    def dir_write_back(sp, inode, dir_b):
        for block in split_serializer(dir_b):
            block_id = sp.get_data_block_id(fp)
            inode.add_block_id(block_id)
            fp.seek((block_id + DATA_BLOCK_START_ID) * BLOCK_SIZE)
            fp.write(block)

    # ---- 正式开始初始化 ----
    # 超级块写入
    sp = SuperBlock()

    # 索引链接写入
    tmp = INODE_BLOCK_NUM
    start = 0
    while tmp > 0:
        sp.inode_unused_cnt -= 1
        if tmp < FREE_NODE_CNT:
            inode_group_link = INodeGroupLink(start, tmp)
        else:
            inode_group_link = INodeGroupLink(start)
        inode_group_link.write_back(fp)
        start += FREE_NODE_CNT
        tmp -= FREE_NODE_CNT

    # 数据块链接写入
    tmp = DATA_BLOCK_NUM
    start = 0
    while tmp > 0:
        sp.block_unused_cnt -= 1
        if tmp < FREE_BLOCK_CNT:
            block_group_link = BlockGroupLink(start, tmp)
        else:
            block_group_link = BlockGroupLink(start)
        block_group_link.write_back(fp)
        start += FREE_BLOCK_CNT
        tmp -= FREE_BLOCK_CNT

    # 初始化根目录
    inode_id = sp.get_free_inode_id(fp)
    inode = INode(inode_id, ROOT_ID)
    base_dir = CatalogBlock(BASE_NAME)

    for file_name in INIT_DIRS:
        new_dir(sp, base_dir, file_name, inode_id)

    # 写回根目录
    dir_write_back(sp, inode, bytes(base_dir))
    inode.write_back(fp)

    # 写入超级块
    sp.base_dir_inode_id = inode_id
    sp.write_back(fp)


@file_func('wb')
def initialization(fp):
    """保留原有的装饰器版本，供独立运行脚本使用"""
    _do_initialization(fp)


# 也可以提供一个直接接受文件指针的公开函数，供文件系统调用
def format_disk(fp):
    """供文件系统调用的格式化接口"""
    _do_initialization(fp)


if __name__ == '__main__':
    initialization()