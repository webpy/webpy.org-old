from infogami import config
from infogami.utils import delegate
from infogami.utils.view import render, public
from infogami.infobase import client

@public
def render_template(name, *a, **kw):
    """Render the template with given name.
    """
    return render[name](*a, **kw)
    
class hooks(client.hook):
    def on_new_version(self, page):
        """Updates the template/macro cache, when a new version is saved or deleted."""
        if page.key.startswith("/user"):
            return

        to = config.get("plugin_webpy", {}).get("notify")
        if to:
            msg = render_template("email/notify", page)
            web.sendmail(config.from_address, to=to, subject=msg.subject.strip(), message=str(msg))