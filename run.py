from httprunner.api import HttpRunner
from httprunner.report import gen_html_report


runner = HttpRunner(failfast=False)

# summary=runner.run("testcase/")
summary=runner.run("testsuites/")

gen_html_report(summary)