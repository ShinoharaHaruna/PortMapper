# PortMapper

>   [中文文档](README_zh.md)

**What era is this? Still worrying about which port to deploy the project on?**

This Python script maps a given string to a port number within a specified threshold and adjusts the result to ensure it is greater than the threshold.

To ensure that the generated port numbers are evenly distributed in the range [threshold, 65536), a consistent hashing algorithm is used. The number of buckets for consistent hashing can be specified as a parameter or use the default value.

## Usage

1. Clone the repository:
```shell
git clone https://github.com/intMojIBakE/PortMapper.git
```
2. Navigate to the project directory:
```shell
cd PortMapper
```
3. Run the script:
```shell
python main.py -n <input_string> -t <threshold_value> -c <number_of_buckets>
```
Replace `<input_string>` with the string you want to map to a port number, replace `<threshold_value>` with the desired threshold (optional, default is 4096), and replace `<number_of_buckets>` with the appropriate number of buckets (optional, default is 127).

4. The script will output the mapped port number for the given string.

## Example

To map the string "PostgreSQL" to a port number, defaulting to a threshold of 4096 and a number of buckets of 127:
```shell
python main.py -n PostgreSQL
```
Output:
```shell
The string "PostgreSQL" is mapped to port 63505.
```
------
To map the string "Redis" to a port number that is greater than 2048:

```shell
python main.py -n Redis -t 2048
```

Output：
```shell
The string "Redis" is mapped to port 44463.
```
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to contribute by opening issues or submitting pull requests. Any feedback or suggestions are welcome!