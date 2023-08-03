# PortMapper

>   [中文文档](README_zh.md)

**What era is this? Still worrying about which port to deploy the project on?**

This Python script maps a given string to a port number within a specified threshold. It calculates the total ASCII value of the input string, performs a modulo operation with 65535, and adjusts the result to ensure it is greater than the threshold value.

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
python main.py -n <input_string> -t <threshold_value>
```
Replace `<input_string>` with the string you want to map to a port number, and `<threshold_value>` with the desired threshold (optional, default is 4096).

4. The script will output the mapped port number for the given string.

## Example

To map the string "PostgreSQL" to a port number greater than 4096:
```shell
python main.py -n PostgreSQL -t 4096
```
Output:
```shell
The string "PostgreSQL" is mapped to port 5076.
```
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to contribute by opening issues or submitting pull requests. Any feedback or suggestions are welcome!