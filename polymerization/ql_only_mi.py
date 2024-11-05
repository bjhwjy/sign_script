"""
name : 小米商城签到做任务
cron : 1 9 * * *
脚本兼容 : 青龙
更新时间 : 20241105
环境变量名：mi
环境变量值：cookie
备注：抓小米商城app的包。有黑号风险，请根据自身情况选择是否用。若有新代码，请及时更新。
"""

#!/usr/bin/python3
import lzma, base64
exec(lzma.decompress(base64.b64decode('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')))