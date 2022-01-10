import re

phoneNumRegex = re.compile('((sam)(eer|ir|er))*')

mo = phoneNumRegex.search("s2s")

print(mo.group(2)) if mo else print(mo)
