# PortMapper

>   [English README](README.md)

**都什么年代，还在纠结于将项目部署在哪个端口上？**

这个 Python 脚本将给定的字符串映射到指定阈值内的一个端口号。它计算输入字符串的 ASCII 值总和，执行一个与 65535 的模运算，并调整结果以确保大于阈值。

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
python main.py -n <输入字符串> -t <阈值>
```
将 `<输入字符串>` 替换为您要映射到端口号的字符串，将 `<阈值>` 替换为所需的阈值（可选，默认为 4096）。

4. 脚本将输出给定字符串的映射端口号。

## 示例

将字符串 "PostgreSQL" 映射到大于 4096 的端口号：
```shell
python main.py -n PostgreSQL -t 4096
```
输出：
```shell
The string "PostgreSQL" is mapped to port 5076.
```
## 许可证

本项目基于 MIT 许可证。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

欢迎通过开启问题或提交拉取请求来做出贡献。任何反馈或建议都受到欢迎！