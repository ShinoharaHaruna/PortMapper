# PortMapper

>   [English README](README.md)

**都什么年代，还在纠结于将项目部署在哪个端口上？**

这个 Python 脚本将给定的字符串映射到指定阈值内的一个端口号，并调整结果以确保大于阈值。

为了保证生成的端口号在区间[threshold, 65536)上尽可能均匀分布，采用了一致性Hash算法。一致性Hash的bucket数可以通过参数指定，也可以使用默认值。

## 使用方法

1. 克隆仓库：
```shell
git clone https://github.com/intMojIBakE/PortMapper.git
```
2. 进入项目目录：
```shell
cd PortMapper
```
3. 运行脚本：
```shell
python main.py -n <输入字符串> -t <阈值> -c <桶的个数>
```
将 `<输入字符串>` 替换为您要映射到端口号的字符串，将 `<阈值>` 替换为所需的阈值（可选，默认为 4096），将 `<桶的个数>` 替换为合适的桶数（可选，默认为 127）。

4. 脚本将输出给定字符串的映射端口号。

## 示例

将字符串 "PostgreSQL" 映射到一个端口号，默认大于4096，桶的个数为127：
```shell
python main.py -n PostgreSQL
```
输出：
```shell
The string "PostgreSQL" is mapped to port 63505.
```
------
将字符串 "Redis" 映射到大于 2048 的端口号：
```shell
python main.py -n Redis -t 2048
```

输出：
```shell
The string "Redis" is mapped to port 44463.
```

## 许可证

本项目基于 MIT 许可证。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

欢迎通过开启问题或提交拉取请求来做出贡献。任何反馈或建议都受到欢迎！