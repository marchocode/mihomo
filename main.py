import logging
from flask import Flask, Response
from config_process import ConfigProcessor
from auto_check import token_check
from config_loader import ConfigLoader

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/subs/<token>')
def convert_subscription(token):
    try:

        config = ConfigLoader("config.yaml")
        config.load()

        token_check(token,config)

        processor = ConfigProcessor(config)
        processor.process()
        yaml_str = processor.dump()

        return Response(yaml_str,mimetype='application/x-yaml')

    except Exception as e:
        return f"处理失败: {str(e)}", 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)