from opencve.checks import BaseCheck
from opencve.commands.utils import CveUtil
from opencve.extensions import db
from opencve.utils import convert_cpes, flatten_vendors


class FirstTime(BaseCheck):
    def execute(self):
        old = flatten_vendors(convert_cpes(self.cve_obj.json["configurations"]))
        new = flatten_vendors(convert_cpes(self.cve_json["configurations"]))
        if payload := list(set(new) - set(old)):
            return CveUtil.create_event(
                self.cve_obj, self.cve_json, "first_time", payload
            )


        return None
