# RandomTell

[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/) [![Flask 1.0.2](https://img.shields.io/badge/flask-1.0.2-lightgrey.svg)](http://flask.pocoo.org) [![ECharts 4.1.0](https://img.shields.io/badge/echarts-4.1.0-crimson.svg)](https://echarts.baidu.com/)

RandomTell is a randomness test tool based on B/S structure. It can evaluate the randomness of binary sequences with visualization display.

## Screenshot

![homepage](https://blog-1255335783.cos.ap-guangzhou.myqcloud.com/RandomTell/README/homepage.png)

## Installation

Download the RandomTell by cloning the Git repository.

```bash
git clone --depth 1 https://github.com/ciphersaw/RandomTell.git
```

Install the dependency packages.

```bash
pip install Flask==1.0.2 scipy==1.2.0
```

## Usage

1. Enter the RandomTell directory and run the tool.

```bash
python ./RandomTell.py
```

2. Access http://127.0.0.1:5000 on browser.
3. Select a file for testing in **Step 1**.
4. Select the test methods in **Step 2**.
5. Set the parameters for testing in **Step 3**.
6. Click **Start**.

It will be redirected to the results page automatically after the test ending.

## License

RandomTell is licensed under the GNU General Public License v3.0 that should be along with this project all the time. See the [LICENSE](https://github.com/ciphersaw/RandomTell/blob/master/LICENSE) file for details.

## Links

- Project Home: [https://github.com/ciphersaw/RandomTell](https://github.com/ciphersaw/RandomTell)

- NIST SP 800-22 Rev. 1a: [https://csrc.nist.gov/publications/detail/sp/800-22/rev-1a/final](https://csrc.nist.gov/publications/detail/sp/800-22/rev-1a/final)