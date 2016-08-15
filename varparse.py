from sys import argv
import re

__author__ = 'Kelvin Lomboy'

_0x2ed5 = ["use strict", "now", "getTime", "length", "", "substr", "000", "001", "fromCharCode", "concat",
            "hasOwnProperty", "localStorage", "setTime", "; expires=", "toGMTString", "isSupported", "setItem",
            "cookie", "=", "; path=/", "getItem", "true", "false", ";", "split", "substring", "charAt", " ",
            "indexOf", "0.", "replace", "random", "click", "body", "getElementsByTagName", "url", "self", "top",
            "parent", "innerWidth", "availWidth", "window", "clientWidth", "documentElement", "document",
            "innerHeight", "availHeight", "clientHeight", "width", "height", "userAgent", "toLowerCase", "OPR", "opera",
            "test", "compatMode", "undefined", "CSS1Compat", "user_agent", "flash_support",
            "application/x-shockwave-flash", "mimeTypes", "version", "safari", "match", "touchable", "ontouchstart",
            "major_version", "is_mobile", "android", "ios", "blackberry", "ms_mobile", "opera_mini", "swf_file",
            "AdFlash43.swf", "chrome", "AdFlash46.swf", "function", "callback", "jsonp", "round", "?", "&", "script",
            "createElement", "src", "setAttribute", "scripts", "appendChild", "parentNode", "&isopp=1", "opp",
            "&unin=1", "unsold", "pixel_url", "img", "display", "style", "none", "visibility", "hidden", "about:blank",
            "open", "focus", "close", "a", "MouseEvents", "createEvent", "href",
            "data:text/html;charset=utf-8;base64,PHNjcmlwdD53aW5kb3cuY2xvc2UoKTs8L3NjcmlwdD4K", "initMouseEvent",
            "dispatchEvent", "removeChild", "removeEventListener", "on", "detachEvent", "_0xfav3451dft135",
            "addEventListener", "attachEvent", "mousedown", "button", "window_name",
            "toolbar=no,scrollbars=yes,location=yes,statusbar=yes,menubar=no,resizable=1,width=",
            ",height=", ",screenX=", "screenX", ",screenY=", "screenY", "blur", "opener", "firefox", "webkit",
            "elementFromPoint", "toLocaleLowerCase", "tagName", "input", "textarea", "option", "select", "msie",
            "touchstart", "aCsdAh", "object", "refresh_rate", "delay", "mac", "presto", "type", "popunder", "clientX",
            "clientY", "px", "mousemove", "name", "value", "param", "id", "class", "data", "host", "/swf/",
            "position:fixed;visibility:visible;display:auto;left:0;top:0;width:1px;height:1px;z-index:2147483647",
            "flashvars", "funcid=", "wmode", "transparent", "menu", "AllowScriptAccess", "always", "AllowFullScreen",
            "firstChild", "insertBefore", "javascript:window.close()",
            "dialogtop:9710090000;dialogleft:997115104;dialogWidth:1;dialogHeight:1", "showModalDialog", "mouseDown",
            "changedTouches", "tabswap", "get", "tabswap_refresh_rate", "state", "adc", "stringify", "parse",
            "replaceState", "initEvent", "target", "srcElement", "pageX", "pageY", "location", "nodeName", "_blank",
            "set", "title", "pushState", "history", "track_time", "ttc=", "c", "y", "r", "4", "j", "v", "9", "t", "x",
            "p", "position: absolute; top: 0; left:0 ;z-index: 2147483647; width: ", "px; height:",
            "px; background: rgba(54, 25, 25, .001); ", "innerText", "onclick", "oMiniLastEntry", "submit",
            "position: absolute; z-index:2147483647; top: 0; left:0 ;width: ",
            "px; background: rgba(54, 25, 25, .001);", "fb", "tabover", "tabunder", "popover",
            "publisher_onload_callback", "rbd_url", "error", "rtb", "iframe", "position", "absolute", "left",
            "-1000px", "1px", "border", "backgroundColor", "push", "join", "ban", "protected_media_url", "fb_disabled",
            "ttcStart", "NqPnfu", "NqpnfuVfNOrggreArgjbex", "_0x90aa"]


def get_value_to_replace(parsed):
    global _0x2ed5
    item = parsed.group(0)
    return eval(item)


script, filename = argv
with open(filename, 'r') as f:
    string = f.read()

modified = re.sub(r'_0x2ed5\[(.*?)\]', get_value_to_replace, string)

modified_file = filename + ".modified.txt"

with open(modified_file, 'w') as f:
    f.write(modified)

print("Output:\n")
print(modified)
