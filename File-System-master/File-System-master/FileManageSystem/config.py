# 状态栏颜色
BAR_TIME_F = "33"
BAR_TIME_B = "40"
BAR_USER_F = "36"
BAR_USER_B = "40"
BAR_VERSION_F = "31"
BAR_VERSION_B = "47"
BAR_PATH_F = "37"
BAR_PATH_B = "44"
BAR_PROMPT_F = "32"
BAR_PROMPT_B = "40"

# 系统信息颜色
SYS_INFO_F = "36"
SYS_INFO_B = "40"

# 登录界面颜色
LOGIN_TITLE_F = "33"
LOGIN_LABEL_F = "32"




BLOCK_SIZE = 512  # 磁盘块大小Bytes
BLOCK_NUM = 2560  # 磁盘块总数量

SUPER_BLOCK_NUM = 2  # 超级块占用的块数
INODE_BLOCK_NUM = 256  # 索引占用的块数
DATA_BLOCK_NUM = BLOCK_NUM - SUPER_BLOCK_NUM - INODE_BLOCK_NUM

INODE_BLOCK_START_ID = SUPER_BLOCK_NUM

DATA_BLOCK_START_ID = SUPER_BLOCK_NUM + INODE_BLOCK_NUM + 1  # 数据块的起始地址

INODE_SIZE = 512  # INODE占用的块区大小

DISK_SIZE = BLOCK_SIZE * BLOCK_NUM  # 磁盘大小
DISK_NAME = "../fms.pfs"
DIR_NUM = 128  # 每个目录锁包含的最大文件数
FREE_NODE_CNT = 50  # 超级块中空闲节点的最大块数
FREE_BLOCK_CNT = 100  # 超级块中空闲数据块的最大块数

BASE_NAME = "base"  # 根目录名

FILE_TYPE = 0  # 文件类型
DIR_TYPE = 1  # 目录类型

ROOT_ID = 0
ROOT = 'root'

INIT_DIRS = ['root', 'home', 'etc']

VERSION = "V 1.2"

# color
FILE_COLOR_F = "37"  # 文件名前景色
FILE_COLOR_B = "40"  # 文件名背景色

DIR_COLOR_F = "32"
DIR_COLOR_B = "40"
