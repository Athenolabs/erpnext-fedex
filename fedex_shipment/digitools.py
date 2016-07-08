from __future__ import unicode_literals
import frappe, json
import os.path

@frappe.whitelist(allow_guest=True)
def delno_need_submit(should_submit=None):
    fpath = '/tmp/fedex_shipment'
    if should_submit is None:
        if not os.path.isfile(fpath):
            delno_need_submit(False)
        with open(fpath, 'r') as f:
            return json.loads(f.read())
    else:
        with open(fpath, 'w') as f:
            f.write(json.dumps([should_submit]))

#frappe.call({method: 'fedex_shipment.digitools.test', args: {}, callback : function (r) { console.log(r) } })
@frappe.whitelist(allow_guest=True)
def test():
    with open('/tmp/hello', 'w') as f:
        f.write("goodbye")
