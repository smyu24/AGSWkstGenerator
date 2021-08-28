(function() {
    var o, r, l, a, h, e, t, i = function() {
        return this
    }();
    i || "undefined" == typeof window || (i = window),
    "undefined" == typeof requirejs && ((o = function(e, t, i) {
        "string" == typeof e ? (2 == arguments.length && (i = t),
        o.modules[e] || (o.payloads[e] = i,
        o.modules[e] = null)) : o.original ? o.original.apply(this, arguments) : (console.error("dropping module because define wasn't a string."),
        console.trace())
    }
    ).modules = {},
    o.payloads = {},
    r = function(e, t, i) {
        if ("string" == typeof t) {
            var n = h(e, t);
            if (null != n)
                return i && i(),
                n
        } else if ("[object Array]" === Object.prototype.toString.call(t)) {
            for (var s = [], o = 0, r = t.length; o < r; ++o) {
                var a = h(e, t[o]);
                if (null == a && l.original)
                    return;
                s.push(a)
            }
            return i && i.apply(null, s) || !0
        }
    }
    ,
    l = function(e, t) {
        var i = r("", e, t);
        return null == i && l.original ? l.original.apply(this, arguments) : i
    }
    ,
    a = function(e, t) {
        if (-1 !== t.indexOf("!")) {
            var i = t.split("!");
            return a(e, i[0]) + "!" + a(e, i[1])
        }
        if ("." == t.charAt(0))
            for (t = e.split("/").slice(0, -1).join("/") + "/" + t; -1 !== t.indexOf(".") && n != t; ) {
                var n = t;
                t = t.replace(/\/\.\//, "/").replace(/[^\/]+\/\.\.\//, "")
            }
        return t
    }
    ,
    h = function(e, i) {
        i = a(e, i);
        var t, n, s = o.modules[i];
        return s || ("function" == typeof (s = o.payloads[i]) && (t = {
            id: i,
            uri: "",
            exports: n = {},
            packaged: !0
        },
        n = s(function(e, t) {
            return r(i, e, t)
        }, n, t) || t.exports,
        o.modules[i] = n,
        delete o.payloads[i]),
        s = o.modules[i] = n || s),
        s
    }
    ,
    t = i,
    (e = "") && (i[e] || (i[e] = {}),
    t = i[e]),
    t.define && t.define.packaged || (o.original = t.define,
    t.define = o,
    t.define.packaged = !0),
    t.require && t.require.packaged || (l.original = t.require,
    t.require = l,
    t.require.packaged = !0))
}
)(),
define("ace/lib/fixoldbrowsers", ["require", "exports", "module"], function(e, t, i) {
    "use strict";
    "undefined" == typeof Element || Element.prototype.remove || Object.defineProperty(Element.prototype, "remove", {
        enumerable: !1,
        writable: !0,
        configurable: !0,
        value: function() {
            this.parentNode && this.parentNode.removeChild(this)
        }
    })
}),
define("ace/lib/useragent", ["require", "exports", "module"], function(e, t, i) {
    "use strict";
    t.OS = {
        LINUX: "LINUX",
        MAC: "MAC",
        WINDOWS: "WINDOWS"
    },
    t.getOS = function() {
        return t.isMac ? t.OS.MAC : t.isLinux ? t.OS.LINUX : t.OS.WINDOWS
    }
    ;
    var n = "object" == typeof navigator ? navigator : {}
      , s = (/mac|win|linux/i.exec(n.platform) || ["other"])[0].toLowerCase()
      , o = n.userAgent || ""
      , r = n.appName || "";
    t.isWin = "win" == s,
    t.isMac = "mac" == s,
    t.isLinux = "linux" == s,
    t.isIE = "Microsoft Internet Explorer" == r || 0 <= r.indexOf("MSAppHost") ? parseFloat((o.match(/(?:MSIE |Trident\/[0-9]+[\.0-9]+;.*rv:)([0-9]+[\.0-9]+)/) || [])[1]) : parseFloat((o.match(/(?:Trident\/[0-9]+[\.0-9]+;.*rv:)([0-9]+[\.0-9]+)/) || [])[1]),
    t.isOldIE = t.isIE && t.isIE < 9,
    t.isGecko = t.isMozilla = o.match(/ Gecko\/\d+/),
    t.isOpera = "object" == typeof opera && "[object Opera]" == Object.prototype.toString.call(window.opera),
    t.isWebKit = parseFloat(o.split("WebKit/")[1]) || void 0,
    t.isChrome = parseFloat(o.split(" Chrome/")[1]) || void 0,
    t.isEdge = parseFloat(o.split(" Edge/")[1]) || void 0,
    t.isAIR = 0 <= o.indexOf("AdobeAIR"),
    t.isAndroid = 0 <= o.indexOf("Android"),
    t.isChromeOS = 0 <= o.indexOf(" CrOS "),
    t.isIOS = /iPad|iPhone|iPod/.test(o) && !window.MSStream,
    t.isIOS && (t.isMac = !0),
    t.isMobile = t.isIOS || t.isAndroid
}),
define("ace/lib/dom", ["require", "exports", "module", "ace/lib/useragent"], function(e, a, t) {
    "use strict";
    var i, n = e("./useragent");
    a.buildDom = function e(t, i, n) {
        if ("string" == typeof t && t) {
            var s = document.createTextNode(t);
            return i && i.appendChild(s),
            s
        }
        if (!Array.isArray(t))
            return t && t.appendChild && i && i.appendChild(t),
            t;
        if ("string" != typeof t[0] || !t[0]) {
            for (var o = [], r = 0; r < t.length; r++) {
                var a = e(t[r], i, n);
                a && o.push(a)
            }
            return o
        }
        var l = document.createElement(t[0])
          , h = t[1]
          , c = 1;
        h && "object" == typeof h && !Array.isArray(h) && (c = 2);
        for (r = c; r < t.length; r++)
            e(t[r], l, n);
        return 2 == c && Object.keys(h).forEach(function(e) {
            var t = h[e];
            "class" === e ? l.className = Array.isArray(t) ? t.join(" ") : t : "function" == typeof t || "value" == e || "$" == e[0] ? l[e] = t : "ref" === e ? n && (n[t] = l) : null != t && l.setAttribute(e, t)
        }),
        i && i.appendChild(l),
        l
    }
    ,
    a.getDocumentHead = function(e) {
        return (e = e || document).head || e.getElementsByTagName("head")[0] || e.documentElement
    }
    ,
    a.createElement = function(e, t) {
        return document.createElementNS ? document.createElementNS(t || "http://www.w3.org/1999/xhtml", e) : document.createElement(e)
    }
    ,
    a.removeChildren = function(e) {
        e.innerHTML = ""
    }
    ,
    a.createTextNode = function(e, t) {
        return (t ? t.ownerDocument : document).createTextNode(e)
    }
    ,
    a.createFragment = function(e) {
        return (e ? e.ownerDocument : document).createDocumentFragment()
    }
    ,
    a.hasCssClass = function(e, t) {
        return -1 !== (e.className + "").split(/\s+/g).indexOf(t)
    }
    ,
    a.addCssClass = function(e, t) {
        a.hasCssClass(e, t) || (e.className += " " + t)
    }
    ,
    a.removeCssClass = function(e, t) {
        for (var i = e.className.split(/\s+/g); ; ) {
            var n = i.indexOf(t);
            if (-1 == n)
                break;
            i.splice(n, 1)
        }
        e.className = i.join(" ")
    }
    ,
    a.toggleCssClass = function(e, t) {
        for (var i = e.className.split(/\s+/g), n = !0; ; ) {
            var s = i.indexOf(t);
            if (-1 == s)
                break;
            n = !1,
            i.splice(s, 1)
        }
        return n && i.push(t),
        e.className = i.join(" "),
        n
    }
    ,
    a.setCssClass = function(e, t, i) {
        i ? a.addCssClass(e, t) : a.removeCssClass(e, t)
    }
    ,
    a.hasCssString = function(e, t) {
        var i, n = 0;
        if (i = (t = t || document).querySelectorAll("style"))
            for (; n < i.length; )
                if (i[n++].id === e)
                    return !0
    }
    ,
    a.importCssString = function(e, t, i) {
        var n = i;
        i && i.getRootNode && (n = i.getRootNode()) && n != i || (n = document);
        var s = n.ownerDocument || n;
        if (t && a.hasCssString(t, n))
            return null;
        t && (e += "\n/*# sourceURL=ace/css/" + t + " */");
        var o = a.createElement("style");
        o.appendChild(s.createTextNode(e)),
        t && (o.id = t),
        n == s && (n = a.getDocumentHead(s)),
        n.insertBefore(o, n.firstChild)
    }
    ,
    a.importCssStylsheet = function(e, t) {
        a.buildDom(["link", {
            rel: "stylesheet",
            href: e
        }], a.getDocumentHead(t))
    }
    ,
    a.scrollbarWidth = function(e) {
        var t = a.createElement("ace_inner");
        t.style.width = "100%",
        t.style.minWidth = "0px",
        t.style.height = "200px",
        t.style.display = "block";
        var i = a.createElement("ace_outer")
          , n = i.style;
        n.position = "absolute",
        n.left = "-10000px",
        n.overflow = "hidden",
        n.width = "200px",
        n.minWidth = "0px",
        n.height = "150px",
        n.display = "block",
        i.appendChild(t);
        var s = e.documentElement;
        s.appendChild(i);
        var o = t.offsetWidth;
        n.overflow = "scroll";
        var r = t.offsetWidth;
        return o == r && (r = i.clientWidth),
        s.removeChild(i),
        o - r
    }
    ,
    "undefined" == typeof document && (a.importCssString = function() {}
    ),
    a.computedStyle = function(e, t) {
        return window.getComputedStyle(e, "") || {}
    }
    ,
    a.setStyle = function(e, t, i) {
        e[t] !== i && (e[t] = i)
    }
    ,
    a.HAS_CSS_ANIMATION = !1,
    a.HAS_CSS_TRANSFORMS = !1,
    a.HI_DPI = !n.isWin || "undefined" != typeof window && 1.5 <= window.devicePixelRatio,
    "undefined" != typeof document && (i = document.createElement("div"),
    a.HI_DPI && void 0 !== i.style.transform && (a.HAS_CSS_TRANSFORMS = !0),
    n.isEdge || void 0 === i.style.animationName || (a.HAS_CSS_ANIMATION = !0),
    i = null),
    a.HAS_CSS_TRANSFORMS ? a.translate = function(e, t, i) {
        e.style.transform = "translate(" + Math.round(t) + "px, " + Math.round(i) + "px)"
    }
    : a.translate = function(e, t, i) {
        e.style.top = Math.round(i) + "px",
        e.style.left = Math.round(t) + "px"
    }
}),
define("ace/lib/oop", ["require", "exports", "module"], function(e, i, t) {
    "use strict";
    i.inherits = function(e, t) {
        e.super_ = t,
        e.prototype = Object.create(t.prototype, {
            constructor: {
                value: e,
                enumerable: !1,
                writable: !0,
                configurable: !0
            }
        })
    }
    ,
    i.mixin = function(e, t) {
        for (var i in t)
            e[i] = t[i];
        return e
    }
    ,
    i.implement = function(e, t) {
        i.mixin(e, t)
    }
}),
define("ace/lib/keys", ["require", "exports", "module", "ace/lib/oop"], function(e, t, i) {
    "use strict";
    var n = e("./oop")
      , s = function() {
        var e, t, i = {
            MODIFIER_KEYS: {
                16: "Shift",
                17: "Ctrl",
                18: "Alt",
                224: "Meta",
                91: "MetaLeft",
                92: "MetaRight",
                93: "ContextMenu"
            },
            KEY_MODS: {
                ctrl: 1,
                alt: 2,
                option: 2,
                shift: 4,
                super: 8,
                meta: 8,
                command: 8,
                cmd: 8,
                control: 1
            },
            FUNCTION_KEYS: {
                8: "Backspace",
                9: "Tab",
                13: "Return",
                19: "Pause",
                27: "Esc",
                32: "Space",
                33: "PageUp",
                34: "PageDown",
                35: "End",
                36: "Home",
                37: "Left",
                38: "Up",
                39: "Right",
                40: "Down",
                44: "Print",
                45: "Insert",
                46: "Delete",
                96: "Numpad0",
                97: "Numpad1",
                98: "Numpad2",
                99: "Numpad3",
                100: "Numpad4",
                101: "Numpad5",
                102: "Numpad6",
                103: "Numpad7",
                104: "Numpad8",
                105: "Numpad9",
                "-13": "NumpadEnter",
                112: "F1",
                113: "F2",
                114: "F3",
                115: "F4",
                116: "F5",
                117: "F6",
                118: "F7",
                119: "F8",
                120: "F9",
                121: "F10",
                122: "F11",
                123: "F12",
                144: "Numlock",
                145: "Scrolllock"
            },
            PRINTABLE_KEYS: {
                32: " ",
                48: "0",
                49: "1",
                50: "2",
                51: "3",
                52: "4",
                53: "5",
                54: "6",
                55: "7",
                56: "8",
                57: "9",
                59: ";",
                61: "=",
                65: "a",
                66: "b",
                67: "c",
                68: "d",
                69: "e",
                70: "f",
                71: "g",
                72: "h",
                73: "i",
                74: "j",
                75: "k",
                76: "l",
                77: "m",
                78: "n",
                79: "o",
                80: "p",
                81: "q",
                82: "r",
                83: "s",
                84: "t",
                85: "u",
                86: "v",
                87: "w",
                88: "x",
                89: "y",
                90: "z",
                107: "+",
                109: "-",
                110: ".",
                186: ";",
                187: "=",
                188: ",",
                189: "-",
                190: ".",
                191: "/",
                192: "`",
                219: "[",
                220: "\\",
                221: "]",
                222: "'",
                111: "/",
                106: "*"
            }
        };
        for (t in i.FUNCTION_KEYS)
            e = i.FUNCTION_KEYS[t].toLowerCase(),
            i[e] = parseInt(t, 10);
        for (t in i.PRINTABLE_KEYS)
            e = i.PRINTABLE_KEYS[t].toLowerCase(),
            i[e] = parseInt(t, 10);
        return n.mixin(i, i.MODIFIER_KEYS),
        n.mixin(i, i.PRINTABLE_KEYS),
        n.mixin(i, i.FUNCTION_KEYS),
        i.enter = i.return,
        i.escape = i.esc,
        i.del = i.delete,
        i[173] = "-",
        function() {
            for (var e = ["cmd", "ctrl", "alt", "shift"], t = Math.pow(2, e.length); t--; )
                i.KEY_MODS[t] = e.filter(function(e) {
                    return t & i.KEY_MODS[e]
                }).join("-") + "-"
        }(),
        i.KEY_MODS[0] = "",
        i.KEY_MODS[-1] = "input-",
        i
    }();
    n.mixin(t, s),
    t.keyCodeToString = function(e) {
        var t = s[e];
        return "string" != typeof t && (t = String.fromCharCode(e)),
        t.toLowerCase()
    }
}),
define("ace/lib/event", ["require", "exports", "module", "ace/lib/keys", "ace/lib/useragent"], function(e, u, t) {
    "use strict";
    function s() {
        return null == i && function() {
            i = !1;
            try {
                document.createComment("").addEventListener("test", function() {}, {
                    get passive() {
                        i = {
                            passive: !1
                        }
                    }
                })
            } catch (e) {}
        }(),
        i
    }
    function o(e, t, i) {
        this.elem = e,
        this.type = t,
        this.callback = i
    }
    function r(e, t, i) {
        var n, s = m(t);
        if (!d.isMac && h) {
            if (t.getModifierState && (t.getModifierState("OS") || t.getModifierState("Win")) && (s |= 8),
            h.altGr) {
                if (3 == (3 & s))
                    return;
                h.altGr = 0
            }
            18 !== i && 17 !== i || (n = "location"in t ? t.location : t.keyLocation,
            17 === i && 1 === n ? 1 == h[i] && (c = t.timeStamp) : 18 === i && 3 === s && 2 === n && t.timeStamp - c < 50 && (h.altGr = !0))
        }
        if ((i in l.MODIFIER_KEYS && (i = -1),
        !s && 13 === i) && (3 === (n = "location"in t ? t.location : t.keyLocation) && (e(t, s, -i),
        t.defaultPrevented)))
            return;
        if (d.isChromeOS && 8 & s) {
            if (e(t, s, i),
            t.defaultPrevented)
                return;
            s &= -9
        }
        return !!(s || i in l.FUNCTION_KEYS || i in l.PRINTABLE_KEYS) && e(t, s, i)
    }
    function a() {
        h = Object.create(null)
    }
    var i, l = e("./keys"), d = e("./useragent"), h = null, c = 0;
    o.prototype.destroy = function() {
        f(this.elem, this.type, this.callback),
        this.elem = this.type = this.callback = void 0
    }
    ;
    var g = u.addListener = function(e, t, i, n) {
        e.addEventListener(t, i, s()),
        n && n.$toDestroy.push(new o(e,t,i))
    }
      , f = u.removeListener = function(e, t, i) {
        e.removeEventListener(t, i, s())
    }
    ;
    u.stopEvent = function(e) {
        return u.stopPropagation(e),
        u.preventDefault(e),
        !1
    }
    ,
    u.stopPropagation = function(e) {
        e.stopPropagation && e.stopPropagation()
    }
    ,
    u.preventDefault = function(e) {
        e.preventDefault && e.preventDefault()
    }
    ,
    u.getButton = function(e) {
        return "dblclick" == e.type ? 0 : "contextmenu" == e.type || d.isMac && e.ctrlKey && !e.altKey && !e.shiftKey ? 2 : e.button
    }
    ,
    u.capture = function(e, t, i) {
        function n(e) {
            t && t(e),
            i && i(e),
            f(s, "mousemove", t),
            f(s, "mouseup", n),
            f(s, "dragstart", n)
        }
        var s = e && e.ownerDocument || document;
        return g(s, "mousemove", t),
        g(s, "mouseup", n),
        g(s, "dragstart", n),
        n
    }
    ,
    u.addMouseWheelListener = function(e, t, i) {
        "onmousewheel"in e ? g(e, "mousewheel", function(e) {
            void 0 !== e.wheelDeltaX ? (e.wheelX = -e.wheelDeltaX / 8,
            e.wheelY = -e.wheelDeltaY / 8) : (e.wheelX = 0,
            e.wheelY = -e.wheelDelta / 8),
            t(e)
        }, i) : "onwheel"in e ? g(e, "wheel", function(e) {
            switch (e.deltaMode) {
            case e.DOM_DELTA_PIXEL:
                e.wheelX = .35 * e.deltaX || 0,
                e.wheelY = .35 * e.deltaY || 0;
                break;
            case e.DOM_DELTA_LINE:
            case e.DOM_DELTA_PAGE:
                e.wheelX = 5 * (e.deltaX || 0),
                e.wheelY = 5 * (e.deltaY || 0)
            }
            t(e)
        }, i) : g(e, "DOMMouseScroll", function(e) {
            e.axis && e.axis == e.HORIZONTAL_AXIS ? (e.wheelX = 5 * (e.detail || 0),
            e.wheelY = 0) : (e.wheelX = 0,
            e.wheelY = 5 * (e.detail || 0)),
            t(e)
        }, i)
    }
    ,
    u.addMultiMouseDownListener = function(e, i, n, s, t) {
        function o(e) {
            var t;
            if (0 !== u.getButton(e) ? h = 0 : 1 < e.detail ? 4 < ++h && (h = 1) : h = 1,
            d.isIE && (t = 5 < Math.abs(e.clientX - r) || 5 < Math.abs(e.clientY - a),
            l && !t || (h = 1),
            l && clearTimeout(l),
            l = setTimeout(function() {
                l = null
            }, i[h - 1] || 600),
            1 == h && (r = e.clientX,
            a = e.clientY)),
            e._clicks = h,
            n[s]("mousedown", e),
            4 < h)
                h = 0;
            else if (1 < h)
                return n[s](c[h], e)
        }
        var r, a, l, h = 0, c = {
            2: "dblclick",
            3: "tripleclick",
            4: "quadclick"
        };
        Array.isArray(e) || (e = [e]),
        e.forEach(function(e) {
            g(e, "mousedown", o, t)
        })
    }
    ;
    function m(e) {
        return 0 | (e.ctrlKey ? 1 : 0) | (e.altKey ? 2 : 0) | (e.shiftKey ? 4 : 0) | (e.metaKey ? 8 : 0)
    }
    var p;
    u.getModifierString = function(e) {
        return l.KEY_MODS[m(e)]
    }
    ,
    u.addCommandKeyListener = function(e, i, t) {
        var n, s;
        d.isOldGecko || d.isOpera && !("KeyboardEvent"in window) ? (n = null,
        g(e, "keydown", function(e) {
            n = e.keyCode
        }, t),
        g(e, "keypress", function(e) {
            return r(i, e, n)
        }, t)) : (s = null,
        g(e, "keydown", function(e) {
            h[e.keyCode] = (h[e.keyCode] || 0) + 1;
            var t = r(i, e, e.keyCode);
            return s = e.defaultPrevented,
            t
        }, t),
        g(e, "keypress", function(e) {
            s && (e.ctrlKey || e.altKey || e.shiftKey || e.metaKey) && (u.stopEvent(e),
            s = null)
        }, t),
        g(e, "keyup", function(e) {
            h[e.keyCode] = null
        }, t),
        h || (a(),
        g(window, "focus", a)))
    }
    ,
    "object" == typeof window && window.postMessage && !d.isOldIE && (p = 1,
    u.nextTick = function(t, i) {
        i = i || window;
        var n = "zero-timeout-message-" + p++
          , s = function(e) {
            e.data == n && (u.stopPropagation(e),
            f(i, "message", s),
            t())
        };
        g(i, "message", s),
        i.postMessage(n, "*")
    }
    ),
    u.$idleBlocked = !1,
    u.onIdle = function(t, e) {
        return setTimeout(function e() {
            u.$idleBlocked ? setTimeout(e, 100) : t()
        }, e)
    }
    ,
    u.$idleBlockId = null,
    u.blockIdle = function(e) {
        u.$idleBlockId && clearTimeout(u.$idleBlockId),
        u.$idleBlocked = !0,
        u.$idleBlockId = setTimeout(function() {
            u.$idleBlocked = !1
        }, e || 100)
    }
    ,
    u.nextFrame = "object" == typeof window && (window.requestAnimationFrame || window.mozRequestAnimationFrame || window.webkitRequestAnimationFrame || window.msRequestAnimationFrame || window.oRequestAnimationFrame),
    u.nextFrame ? u.nextFrame = u.nextFrame.bind(window) : u.nextFrame = function(e) {
        setTimeout(e, 17)
    }
}),
define("ace/range", ["require", "exports", "module"], function(e, t, i) {
    "use strict";
    function o(e, t, i, n) {
        this.start = {
            row: e,
            column: t
        },
        this.end = {
            row: i,
            column: n
        }
    }
    (function() {
        this.isEqual = function(e) {
            return this.start.row === e.start.row && this.end.row === e.end.row && this.start.column === e.start.column && this.end.column === e.end.column
        }
        ,
        this.toString = function() {
            return "Range: [" + this.start.row + "/" + this.start.column + "] -> [" + this.end.row + "/" + this.end.column + "]"
        }
        ,
        this.contains = function(e, t) {
            return 0 == this.compare(e, t)
        }
        ,
        this.compareRange = function(e) {
            var t = e.end
              , i = e.start
              , n = this.compare(t.row, t.column);
            return 1 == n ? 1 == (n = this.compare(i.row, i.column)) ? 2 : 0 == n ? 1 : 0 : -1 == n ? -2 : -1 == (n = this.compare(i.row, i.column)) ? -1 : 1 == n ? 42 : 0
        }
        ,
        this.comparePoint = function(e) {
            return this.compare(e.row, e.column)
        }
        ,
        this.containsRange = function(e) {
            return 0 == this.comparePoint(e.start) && 0 == this.comparePoint(e.end)
        }
        ,
        this.intersects = function(e) {
            var t = this.compareRange(e);
            return -1 == t || 0 == t || 1 == t
        }
        ,
        this.isEnd = function(e, t) {
            return this.end.row == e && this.end.column == t
        }
        ,
        this.isStart = function(e, t) {
            return this.start.row == e && this.start.column == t
        }
        ,
        this.setStart = function(e, t) {
            "object" == typeof e ? (this.start.column = e.column,
            this.start.row = e.row) : (this.start.row = e,
            this.start.column = t)
        }
        ,
        this.setEnd = function(e, t) {
            "object" == typeof e ? (this.end.column = e.column,
            this.end.row = e.row) : (this.end.row = e,
            this.end.column = t)
        }
        ,
        this.inside = function(e, t) {
            return 0 == this.compare(e, t) && (!this.isEnd(e, t) && !this.isStart(e, t))
        }
        ,
        this.insideStart = function(e, t) {
            return 0 == this.compare(e, t) && !this.isEnd(e, t)
        }
        ,
        this.insideEnd = function(e, t) {
            return 0 == this.compare(e, t) && !this.isStart(e, t)
        }
        ,
        this.compare = function(e, t) {
            return this.isMultiLine() || e !== this.start.row ? e < this.start.row ? -1 : e > this.end.row ? 1 : this.start.row === e ? t >= this.start.column ? 0 : -1 : this.end.row !== e || t <= this.end.column ? 0 : 1 : t < this.start.column ? -1 : t > this.end.column ? 1 : 0
        }
        ,
        this.compareStart = function(e, t) {
            return this.start.row == e && this.start.column == t ? -1 : this.compare(e, t)
        }
        ,
        this.compareEnd = function(e, t) {
            return this.end.row == e && this.end.column == t ? 1 : this.compare(e, t)
        }
        ,
        this.compareInside = function(e, t) {
            return this.end.row == e && this.end.column == t ? 1 : this.start.row == e && this.start.column == t ? -1 : this.compare(e, t)
        }
        ,
        this.clipRows = function(e, t) {
            var i, n;
            return this.end.row > t ? i = {
                row: t + 1,
                column: 0
            } : this.end.row < e && (i = {
                row: e,
                column: 0
            }),
            this.start.row > t ? n = {
                row: t + 1,
                column: 0
            } : this.start.row < e && (n = {
                row: e,
                column: 0
            }),
            o.fromPoints(n || this.start, i || this.end)
        }
        ,
        this.extend = function(e, t) {
            var i, n, s = this.compare(e, t);
            return 0 == s ? this : (-1 == s ? i = {
                row: e,
                column: t
            } : n = {
                row: e,
                column: t
            },
            o.fromPoints(i || this.start, n || this.end))
        }
        ,
        this.isEmpty = function() {
            return this.start.row === this.end.row && this.start.column === this.end.column
        }
        ,
        this.isMultiLine = function() {
            return this.start.row !== this.end.row
        }
        ,
        this.clone = function() {
            return o.fromPoints(this.start, this.end)
        }
        ,
        this.collapseRows = function() {
            return 0 == this.end.column ? new o(this.start.row,0,Math.max(this.start.row, this.end.row - 1),0) : new o(this.start.row,0,this.end.row,0)
        }
        ,
        this.toScreenRange = function(e) {
            var t = e.documentToScreenPosition(this.start)
              , i = e.documentToScreenPosition(this.end);
            return new o(t.row,t.column,i.row,i.column)
        }
        ,
        this.moveBy = function(e, t) {
            this.start.row += e,
            this.start.column += t,
            this.end.row += e,
            this.end.column += t
        }
    }
    ).call(o.prototype),
    o.fromPoints = function(e, t) {
        return new o(e.row,e.column,t.row,t.column)
    }
    ,
    o.comparePoints = function(e, t) {
        return e.row - t.row || e.column - t.column
    }
    ,
    o.comparePoints = function(e, t) {
        return e.row - t.row || e.column - t.column
    }
    ,
    t.Range = o
}),
define("ace/lib/lang", ["require", "exports", "module"], function(e, t, i) {
    "use strict";
    t.last = function(e) {
        return e[e.length - 1]
    }
    ,
    t.stringReverse = function(e) {
        return e.split("").reverse().join("")
    }
    ,
    t.stringRepeat = function(e, t) {
        for (var i = ""; 0 < t; )
            1 & t && (i += e),
            (t >>= 1) && (e += e);
        return i
    }
    ;
    var n = /^\s\s*/
      , s = /\s\s*$/;
    t.stringTrimLeft = function(e) {
        return e.replace(n, "")
    }
    ,
    t.stringTrimRight = function(e) {
        return e.replace(s, "")
    }
    ,
    t.copyObject = function(e) {
        var t = {};
        for (var i in e)
            t[i] = e[i];
        return t
    }
    ,
    t.copyArray = function(e) {
        for (var t = [], i = 0, n = e.length; i < n; i++)
            e[i] && "object" == typeof e[i] ? t[i] = this.copyObject(e[i]) : t[i] = e[i];
        return t
    }
    ,
    t.deepCopy = function e(t) {
        if ("object" != typeof t || !t)
            return t;
        var i;
        if (Array.isArray(t)) {
            i = [];
            for (var n = 0; n < t.length; n++)
                i[n] = e(t[n]);
            return i
        }
        if ("[object Object]" !== Object.prototype.toString.call(t))
            return t;
        for (var n in i = {},
        t)
            i[n] = e(t[n]);
        return i
    }
    ,
    t.arrayToMap = function(e) {
        for (var t = {}, i = 0; i < e.length; i++)
            t[e[i]] = 1;
        return t
    }
    ,
    t.createMap = function(e) {
        var t = Object.create(null);
        for (var i in e)
            t[i] = e[i];
        return t
    }
    ,
    t.arrayRemove = function(e, t) {
        for (var i = 0; i <= e.length; i++)
            t === e[i] && e.splice(i, 1)
    }
    ,
    t.escapeRegExp = function(e) {
        return e.replace(/([.*+?^${}()|[\]\/\\])/g, "\\$1")
    }
    ,
    t.escapeHTML = function(e) {
        return ("" + e).replace(/&/g, "&#38;").replace(/"/g, "&#34;").replace(/'/g, "&#39;").replace(/</g, "&#60;")
    }
    ,
    t.getMatchOffsets = function(e, t) {
        var i = [];
        return e.replace(t, function(e) {
            i.push({
                offset: arguments[arguments.length - 2],
                length: e.length
            })
        }),
        i
    }
    ,
    t.deferredCall = function(e) {
        function t() {
            i = null,
            e()
        }
        var i = null
          , n = function(e) {
            return n.cancel(),
            i = setTimeout(t, e || 0),
            n
        };
        return (n.schedule = n).call = function() {
            return this.cancel(),
            e(),
            n
        }
        ,
        n.cancel = function() {
            return clearTimeout(i),
            i = null,
            n
        }
        ,
        n.isPending = function() {
            return i
        }
        ,
        n
    }
    ,
    t.delayedCall = function(e, t) {
        function i() {
            s = null,
            e()
        }
        function n(e) {
            null == s && (s = setTimeout(i, e || t))
        }
        var s = null;
        return n.delay = function(e) {
            s && clearTimeout(s),
            s = setTimeout(i, e || t)
        }
        ,
        (n.schedule = n).call = function() {
            this.cancel(),
            e()
        }
        ,
        n.cancel = function() {
            s && clearTimeout(s),
            s = null
        }
        ,
        n.isPending = function() {
            return s
        }
        ,
        n
    }
}),
define("ace/clipboard", ["require", "exports", "module"], function(e, t, i) {
    "use strict";
    var n;
    i.exports = {
        lineMode: !1,
        pasteCancelled: function() {
            return !!(n && n > Date.now() - 50) || (n = !1)
        },
        cancel: function() {
            n = Date.now()
        }
    }
}),
define("ace/keyboard/textinput", ["require", "exports", "module", "ace/lib/event", "ace/lib/useragent", "ace/lib/dom", "ace/lib/lang", "ace/clipboard", "ace/lib/keys"], function(e, t, i) {
    "use strict";
    var D = e("../lib/event")
      , B = e("../lib/useragent")
      , H = e("../lib/dom")
      , P = e("../lib/lang")
      , N = e("../clipboard")
      , z = B.isChrome < 18
      , V = B.isIE
      , U = 63 < B.isChrome
      , K = e("../lib/keys")
      , G = K.KEY_MODS
      , j = B.isIOS
      , q = j ? /\s/ : /\n/
      , Y = B.isMobile;
    t.TextInput = function(e, d) {
        function i() {
            t = !0,
            g.blur(),
            g.focus(),
            t = !1
        }
        function l() {
            clearTimeout(T),
            T = setTimeout(function() {
                c && (g.style.cssText = c,
                c = ""),
                d.renderer.$isMousePressed = !1,
                d.renderer.$keepTextAreaAtCursor && d.renderer.$moveTextAreaToCursor()
            }, 0)
        }
        var g = H.createElement("textarea");
        g.className = "ace_text-input",
        g.setAttribute("wrap", "off"),
        g.setAttribute("autocorrect", "off"),
        g.setAttribute("autocapitalize", "off"),
        g.setAttribute("spellcheck", !1),
        g.style.opacity = "0",
        e.insertBefore(g, e.firstChild);
        var r = !1
          , f = !1
          , h = !1
          , m = !1
          , c = "";
        Y || (g.style.fontSize = "1px");
        var p = !1
          , t = !1
          , w = ""
          , v = 0
          , $ = 0
          , b = 0;
        try {
            var u = document.activeElement === g
        } catch (e) {}
        D.addListener(g, "blur", function(e) {
            t || (d.onBlur(e),
            u = !1)
        }, d),
        D.addListener(g, "focus", function(e) {
            if (!t) {
                if (u = !0,
                B.isEdge)
                    try {
                        if (!document.hasFocus())
                            return
                    } catch (e) {}
                d.onFocus(e),
                B.isEdge ? setTimeout(y) : y()
            }
        }, d),
        this.$focusScroll = !1,
        this.focus = function() {
            if (c || U || "browser" == this.$focusScroll)
                return g.focus({
                    preventScroll: !0
                });
            var e = g.style.top;
            g.style.position = "fixed",
            g.style.top = "0px";
            try {
                var t = 0 != g.getBoundingClientRect().top
            } catch (e) {
                return
            }
            var i = [];
            if (t)
                for (var n = g.parentElement; n && 1 == n.nodeType; )
                    i.push(n),
                    n.setAttribute("ace_nocontext", !0),
                    n = !n.parentElement && n.getRootNode ? n.getRootNode().host : n.parentElement;
            g.focus({
                preventScroll: !0
            }),
            t && i.forEach(function(e) {
                e.removeAttribute("ace_nocontext")
            }),
            setTimeout(function() {
                g.style.position = "",
                "0px" == g.style.top && (g.style.top = e)
            }, 0)
        }
        ,
        this.blur = function() {
            g.blur()
        }
        ,
        this.isFocused = function() {
            return u
        }
        ,
        d.on("beforeEndOperation", function() {
            var e, t = d.curOp, i = t && t.command && t.command.name;
            "insertstring" != i && (e = i && (t.docChanged || t.selectionChanged),
            h && e && (w = g.value = "",
            R()),
            y())
        });
        var y = j ? function(e) {
            var t, i;
            !u || r && !e || m || ((t = "\n ab" + (e = e || "") + "cde fg\n") != g.value && (g.value = w = t),
            i = 4 + (e.length || (d.selection.isEmpty() ? 0 : 1)),
            4 == v && $ == i || g.setSelectionRange(4, i),
            v = 4,
            $ = i)
        }
        : function() {
            if (!h && !m && (u || k)) {
                h = !0;
                var e, t, i, n, s, o = 0, r = 0, a = "";
                d.session && (t = (e = d.selection).getRange(),
                i = e.cursor.row,
                o = t.start.column,
                r = t.end.column,
                a = d.session.getLine(i),
                t.start.row != i ? (n = d.session.getLine(i - 1),
                o = t.start.row < i - 1 ? 0 : o,
                r += n.length + 1,
                a = n + "\n" + a) : t.end.row != i ? (s = d.session.getLine(i + 1),
                r = t.end.row > i + 1 ? s.length : r,
                r += a.length + 1,
                a = a + "\n" + s) : Y && 0 < i && (a = "\n" + a,
                r += 1,
                o += 1),
                400 < a.length && (o < 400 && r < 400 ? a = a.slice(0, 400) : (a = "\n",
                o == r ? o = r = 0 : (o = 0,
                r = 1))));
                var l = a + "\n\n";
                if (l != w && (g.value = w = l,
                v = $ = l.length),
                k && (v = g.selectionStart,
                $ = g.selectionEnd),
                $ != r || v != o || g.selectionEnd != $)
                    try {
                        g.setSelectionRange(o, r),
                        v = o,
                        $ = r
                    } catch (e) {}
                h = !1
            }
        }
        ;
        this.resetSelection = y,
        u && d.onFocus();
        var n = null;
        this.setInputHandler = function(e) {
            n = e
        }
        ;
        function s(e, t) {
            if (k = k && !1,
            f)
                return y(),
                e && d.onPaste(e),
                f = !1,
                "";
            for (var i = g.selectionStart, n = g.selectionEnd, s = v, o = w.length - $, r = e, a = e.length - i, l = e.length - n, h = 0; 0 < s && w[h] == e[h]; )
                h++,
                s--;
            for (r = r.slice(h),
            h = 1; 0 < o && w.length - h > v - 1 && w[w.length - h] == e[e.length - h]; )
                h++,
                o--;
            a -= h - 1,
            l -= h - 1;
            var c = r.length - h + 1;
            if (c < 0 && (s = -c,
            c = 0),
            r = r.slice(0, c),
            !(t || r || a || s || o || l))
                return "";
            var u = !(m = !0);
            return B.isAndroid && ". " == r && (r = "  ",
            u = !0),
            r && !s && !o && !a && !l || p ? d.onTextInput(r) : d.onTextInput(r, {
                extendLeft: s,
                extendRight: o,
                restoreStart: a,
                restoreEnd: l
            }),
            m = !1,
            w = e,
            v = i,
            $ = n,
            b = l,
            u ? "\n" : r
        }
        function o(e) {
            if (h)
                return L();
            if (e && e.inputType) {
                if ("historyUndo" == e.inputType)
                    return d.execCommand("undo");
                if ("historyRedo" == e.inputType)
                    return d.execCommand("redo")
            }
            var t = g.value
              , i = s(t, !0);
            (500 < t.length || q.test(i) || Y && v < 1 && v == $) && y()
        }
        function a(e, t) {
            var i = d.getCopyText();
            if (!i)
                return D.preventDefault(e);
            A(e, i) ? (j && (y(i),
            r = i,
            setTimeout(function() {
                r = !1
            }, 10)),
            t ? d.onCut() : d.onCopy(),
            D.preventDefault(e)) : (r = !0,
            g.value = i,
            g.select(),
            setTimeout(function() {
                r = !1,
                y(),
                t ? d.onCut() : d.onCopy()
            }))
        }
        function C(e) {
            a(e, !0)
        }
        function S(e) {
            a(e, !1)
        }
        function x(e) {
            var t = A(e);
            N.pasteCancelled() || ("string" == typeof t ? (t && d.onPaste(t, e),
            B.isIE && setTimeout(y),
            D.preventDefault(e)) : (g.value = "",
            f = !0))
        }
        var k = !(this.getInputHandler = function() {
            return n
        }
        )
          , A = function(e, t, i) {
            var n = e.clipboardData || window.clipboardData;
            if (n && !z) {
                var s = V || i ? "Text" : "text/plain";
                try {
                    return t ? !1 !== n.setData(s, t) : n.getData(s)
                } catch (e) {
                    if (!i)
                        return A(e, t, !0)
                }
            }
        };
        D.addCommandKeyListener(g, d.onCommandKey.bind(d), d),
        D.addListener(g, "select", function(e) {
            var t;
            h || (r ? r = !1 : 0 === (t = g).selectionStart && t.selectionEnd >= w.length && t.value === w && w && t.selectionEnd !== $ ? (d.selectAll(),
            y()) : Y && g.selectionStart != v && y())
        }, d),
        D.addListener(g, "input", o, d),
        D.addListener(g, "cut", C, d),
        D.addListener(g, "copy", S, d),
        D.addListener(g, "paste", x, d),
        "oncut"in g && "oncopy"in g && "onpaste"in g || D.addListener(e, "keydown", function(e) {
            if ((!B.isMac || e.metaKey) && e.ctrlKey)
                switch (e.keyCode) {
                case 67:
                    S(e);
                    break;
                case 86:
                    x(e);
                    break;
                case 88:
                    C(e)
                }
        }, d);
        var L = function() {
            var e;
            if (h && d.onCompositionUpdate && !d.$readOnly)
                return p ? i() : void (h.useTextareaForIME ? d.onCompositionUpdate(g.value) : (e = g.value,
                s(e),
                h.markerRange && (h.context && (h.markerRange.start.column = h.selectionStart = h.context.compositionStartOffset),
                h.markerRange.end.column = h.markerRange.start.column + $ - h.selectionStart + b)))
        }
          , R = function(e) {
            d.onCompositionEnd && !d.$readOnly && (h = !1,
            d.onCompositionEnd(),
            d.off("mousedown", i),
            e && o())
        }
          , M = P.delayedCall(L, 50).schedule.bind(null, null);
        D.addListener(g, "compositionstart", function(e) {
            var t;
            h || !d.onCompositionStart || d.$readOnly || (h = {},
            p || (e.data && (h.useTextareaForIME = !1),
            setTimeout(L, 0),
            d._signal("compositionStart"),
            d.on("mousedown", i),
            (t = d.getSelectionRange()).end.row = t.start.row,
            t.end.column = t.start.column,
            h.markerRange = t,
            h.selectionStart = v,
            d.onCompositionStart(h),
            h.useTextareaForIME ? (w = g.value = "",
            $ = v = 0) : (g.msGetInputContext && (h.context = g.msGetInputContext()),
            g.getInputContext && (h.context = g.getInputContext()))))
        }, d),
        D.addListener(g, "compositionupdate", L, d),
        D.addListener(g, "keyup", function(e) {
            27 == e.keyCode && g.value.length < g.selectionStart && (h || (w = g.value),
            v = $ = -1,
            y()),
            M()
        }, d),
        D.addListener(g, "keydown", M, d),
        D.addListener(g, "compositionend", R, d),
        this.getElement = function() {
            return g
        }
        ,
        this.setCommandMode = function(e) {
            p = e,
            g.readOnly = !1
        }
        ,
        this.setReadOnly = function(e) {
            p || (g.readOnly = e)
        }
        ,
        this.setCopyWithEmptySelection = function(e) {}
        ,
        this.onContextMenu = function(e) {
            k = !0,
            y(),
            d._emit("nativecontextmenu", {
                target: d,
                domEvent: e
            }),
            this.moveToMouse(e, !0)
        }
        ,
        this.moveToMouse = function(e, t) {
            c = c || g.style.cssText,
            g.style.cssText = (t ? "z-index:100000;" : "") + (B.isIE ? "opacity:0.1;" : "") + "text-indent: -" + (v + $) * d.renderer.characterWidth * .5 + "px;";
            function i(e) {
                H.translate(g, e.clientX - r - 2, Math.min(e.clientY - o - 2, a))
            }
            var n = d.container.getBoundingClientRect()
              , s = H.computedStyle(d.container)
              , o = n.top + (parseInt(s.borderTopWidth) || 0)
              , r = n.left + (parseInt(n.borderLeftWidth) || 0)
              , a = n.bottom - o - g.clientHeight - 2;
            i(e),
            "mousedown" == e.type && (d.renderer.$isMousePressed = !0,
            clearTimeout(T),
            B.isWin && D.capture(d.container, i, l))
        }
        ,
        this.onContextMenuClose = l;
        function E(e) {
            d.textInput.onContextMenu(e),
            l()
        }
        var T, _, F, O, I;
        function W(e) {
            var t, i, n, s, o;
            document.activeElement === F && (I || h || _.$mouseHandler.isMousePressed || r || (t = F.selectionStart,
            i = F.selectionEnd,
            n = null,
            (s = 0) == t ? n = K.up : 1 == t ? n = K.home : $ < i && "\n" == w[i] ? n = K.end : t < v && " " == w[t - 1] ? (n = K.left,
            s = G.option) : t < v || t == v && $ != v && t == i ? n = K.left : $ < i && 2 < w.slice(0, i).split("\n").length ? n = K.down : $ < i && " " == w[i - 1] ? (n = K.right,
            s = G.option) : ($ < i || i == $ && $ != v && t == i) && (n = K.right),
            t !== i && (s |= G.shift),
            n && (!_.onCommandKey({}, s, n) && _.commands && (n = K.keyCodeToString(n),
            (o = _.commands.findKeyCommand(s, n)) && _.execCommand(o)),
            v = t,
            $ = i,
            y(""))))
        }
        D.addListener(g, "mouseup", E, d),
        D.addListener(g, "mousedown", function(e) {
            e.preventDefault(),
            l()
        }, d),
        D.addListener(d.renderer.scroller, "contextmenu", E, d),
        D.addListener(g, "contextmenu", E, d),
        j && (_ = d,
        O = null,
        I = !1,
        (F = g).addEventListener("keydown", function(e) {
            O && clearTimeout(O),
            I = !0
        }, !0),
        F.addEventListener("keyup", function(e) {
            O = setTimeout(function() {
                I = !1
            }, 100)
        }, !0),
        document.addEventListener("selectionchange", W),
        _.on("destroy", function() {
            document.removeEventListener("selectionchange", W)
        }))
    }
    ,
    t.$setUserAgentForTests = function(e, t) {
        Y = e,
        j = t
    }
}),
define("ace/mouse/default_handlers", ["require", "exports", "module", "ace/lib/useragent"], function(e, t, i) {
    "use strict";
    function n(t) {
        t.$clickSelection = null;
        var e = t.editor;
        e.setDefaultHandler("mousedown", this.onMouseDown.bind(t)),
        e.setDefaultHandler("dblclick", this.onDoubleClick.bind(t)),
        e.setDefaultHandler("tripleclick", this.onTripleClick.bind(t)),
        e.setDefaultHandler("quadclick", this.onQuadClick.bind(t)),
        e.setDefaultHandler("mousewheel", this.onMouseWheel.bind(t));
        ["select", "startSelect", "selectEnd", "selectAllEnd", "selectByWordsEnd", "selectByLinesEnd", "dragWait", "dragWaitEnd", "focusWait"].forEach(function(e) {
            t[e] = this[e]
        }, this),
        t.selectByLines = this.extendSelectionBy.bind(t, "getLineRange"),
        t.selectByWords = this.extendSelectionBy.bind(t, "getWordRange")
    }
    function l(e, t) {
        return (e.start.row == e.end.row ? 2 * t.column - e.start.column - e.end.column : e.start.row != e.end.row - 1 || e.start.column || e.end.column ? 2 * t.row - e.start.row - e.end.row : t.column - 4) < 0 ? {
            cursor: e.start,
            anchor: e.end
        } : {
            cursor: e.end,
            anchor: e.start
        }
    }
    var o = e("../lib/useragent");
    (function() {
        this.onMouseDown = function(e) {
            var t = e.inSelection()
              , i = e.getDocumentPosition();
            this.mousedownEvent = e;
            var n = this.editor
              , s = e.getButton();
            return 0 !== s ? (!n.getSelectionRange().isEmpty() && 1 != s || n.selection.moveToPosition(i),
            void (2 == s && (n.textInput.onContextMenu(e.domEvent),
            o.isMozilla || e.preventDefault()))) : (this.mousedownEvent.time = Date.now(),
            !t || n.isFocused() || (n.focus(),
            !this.$focusTimeout || this.$clickSelection || n.inMultiSelectMode) ? (this.captureMouse(e),
            this.startSelect(i, 1 < e.domEvent._clicks),
            e.preventDefault()) : (this.setState("focusWait"),
            void this.captureMouse(e)))
        }
        ,
        this.startSelect = function(e, t) {
            e = e || this.editor.renderer.screenToTextCoordinates(this.x, this.y);
            var i = this.editor;
            this.mousedownEvent && (this.mousedownEvent.getShiftKey() ? i.selection.selectToPosition(e) : t || i.selection.moveToPosition(e),
            t || this.select(),
            i.renderer.scroller.setCapture && i.renderer.scroller.setCapture(),
            i.setStyle("ace_selecting"),
            this.setState("select"))
        }
        ,
        this.select = function() {
            var e, t, i, n = this.editor, s = n.renderer.screenToTextCoordinates(this.x, this.y);
            this.$clickSelection && (i = -1 == (e = this.$clickSelection.comparePoint(s)) ? this.$clickSelection.end : 1 == e ? this.$clickSelection.start : (s = (t = l(this.$clickSelection, s)).cursor,
            t.anchor),
            n.selection.setSelectionAnchor(i.row, i.column)),
            n.selection.selectToPosition(s),
            n.renderer.scrollCursorIntoView()
        }
        ,
        this.extendSelectionBy = function(e) {
            var t, i, n, s, o = this.editor, r = o.renderer.screenToTextCoordinates(this.x, this.y), a = o.selection[e](r.row, r.column);
            this.$clickSelection && (t = this.$clickSelection.comparePoint(a.start),
            i = this.$clickSelection.comparePoint(a.end),
            -1 == t && i <= 0 ? (s = this.$clickSelection.end,
            a.end.row == r.row && a.end.column == r.column || (r = a.start)) : 1 == i && 0 <= t ? (s = this.$clickSelection.start,
            a.start.row == r.row && a.start.column == r.column || (r = a.end)) : s = -1 == t && 1 == i ? (r = a.end,
            a.start) : (r = (n = l(this.$clickSelection, r)).cursor,
            n.anchor),
            o.selection.setSelectionAnchor(s.row, s.column)),
            o.selection.selectToPosition(r),
            o.renderer.scrollCursorIntoView()
        }
        ,
        this.selectEnd = this.selectAllEnd = this.selectByWordsEnd = this.selectByLinesEnd = function() {
            this.$clickSelection = null,
            this.editor.unsetStyle("ace_selecting"),
            this.editor.renderer.scroller.releaseCapture && this.editor.renderer.scroller.releaseCapture()
        }
        ,
        this.focusWait = function() {
            var e, t, i, n, s = (e = this.mousedownEvent.x,
            t = this.mousedownEvent.y,
            i = this.x,
            n = this.y,
            Math.sqrt(Math.pow(i - e, 2) + Math.pow(n - t, 2))), o = Date.now();
            (0 < s || o - this.mousedownEvent.time > this.$focusTimeout) && this.startSelect(this.mousedownEvent.getDocumentPosition())
        }
        ,
        this.onDoubleClick = function(e) {
            var t = e.getDocumentPosition()
              , i = this.editor
              , n = i.session.getBracketRange(t);
            n ? (n.isEmpty() && (n.start.column--,
            n.end.column++),
            this.setState("select")) : (n = i.selection.getWordRange(t.row, t.column),
            this.setState("selectByWords")),
            this.$clickSelection = n,
            this.select()
        }
        ,
        this.onTripleClick = function(e) {
            var t = e.getDocumentPosition()
              , i = this.editor;
            this.setState("selectByLines");
            var n = i.getSelectionRange();
            n.isMultiLine() && n.contains(t.row, t.column) ? (this.$clickSelection = i.selection.getLineRange(n.start.row),
            this.$clickSelection.end = i.selection.getLineRange(n.end.row).end) : this.$clickSelection = i.selection.getLineRange(t.row),
            this.select()
        }
        ,
        this.onQuadClick = function(e) {
            var t = this.editor;
            t.selectAll(),
            this.$clickSelection = t.getSelectionRange(),
            this.setState("selectAll")
        }
        ,
        this.onMouseWheel = function(e) {
            if (!e.getAccelKey()) {
                e.getShiftKey() && e.wheelY && !e.wheelX && (e.wheelX = e.wheelY,
                e.wheelY = 0);
                var t = this.editor;
                this.$lastScroll || (this.$lastScroll = {
                    t: 0,
                    vx: 0,
                    vy: 0,
                    allowed: 0
                });
                var i = this.$lastScroll
                  , n = e.domEvent.timeStamp
                  , s = n - i.t
                  , o = s ? e.wheelX / s : i.vx
                  , r = s ? e.wheelY / s : i.vy;
                s < 550 && (o = (o + i.vx) / 2,
                r = (r + i.vy) / 2);
                var a = Math.abs(o / r)
                  , l = !1;
                return 1 <= a && t.renderer.isScrollableBy(e.wheelX * e.speed, 0) && (l = !0),
                a <= 1 && t.renderer.isScrollableBy(0, e.wheelY * e.speed) && (l = !0),
                l ? i.allowed = n : n - i.allowed < 550 && (Math.abs(o) <= 1.5 * Math.abs(i.vx) && Math.abs(r) <= 1.5 * Math.abs(i.vy) ? (l = !0,
                i.allowed = n) : i.allowed = 0),
                i.t = n,
                i.vx = o,
                i.vy = r,
                l ? (t.renderer.scrollBy(e.wheelX * e.speed, e.wheelY * e.speed),
                e.stop()) : void 0
            }
        }
    }
    ).call(n.prototype),
    t.DefaultHandlers = n
}),
define("ace/tooltip", ["require", "exports", "module", "ace/lib/oop", "ace/lib/dom"], function(e, t, i) {
    "use strict";
    function n(e) {
        this.isOpen = !1,
        this.$element = null,
        this.$parentNode = e
    }
    e("./lib/oop");
    var s = e("./lib/dom");
    (function() {
        this.$init = function() {
            return this.$element = s.createElement("div"),
            this.$element.className = "ace_tooltip",
            this.$element.style.display = "none",
            this.$parentNode.appendChild(this.$element),
            this.$element
        }
        ,
        this.getElement = function() {
            return this.$element || this.$init()
        }
        ,
        this.setText = function(e) {
            this.getElement().textContent = e
        }
        ,
        this.setHtml = function(e) {
            this.getElement().innerHTML = e
        }
        ,
        this.setPosition = function(e, t) {
            this.getElement().style.left = e + "px",
            this.getElement().style.top = t + "px"
        }
        ,
        this.setClassName = function(e) {
            s.addCssClass(this.getElement(), e)
        }
        ,
        this.show = function(e, t, i) {
            null != e && this.setText(e),
            null != t && null != i && this.setPosition(t, i),
            this.isOpen || (this.getElement().style.display = "block",
            this.isOpen = !0)
        }
        ,
        this.hide = function() {
            this.isOpen && (this.getElement().style.display = "none",
            this.isOpen = !1)
        }
        ,
        this.getHeight = function() {
            return this.getElement().offsetHeight
        }
        ,
        this.getWidth = function() {
            return this.getElement().offsetWidth
        }
        ,
        this.destroy = function() {
            this.isOpen = !1,
            this.$element && this.$element.parentNode && this.$element.parentNode.removeChild(this.$element)
        }
    }
    ).call(n.prototype),
    t.Tooltip = n
}),
define("ace/mouse/default_gutter_handler", ["require", "exports", "module", "ace/lib/dom", "ace/lib/oop", "ace/lib/event", "ace/tooltip"], function(e, t, i) {
    "use strict";
    function n(e) {
        r.call(this, e)
    }
    var s = e("../lib/dom")
      , o = e("../lib/oop")
      , f = e("../lib/event")
      , r = e("../tooltip").Tooltip;
    o.inherits(n, r),
    function() {
        this.setPosition = function(e, t) {
            var i = window.innerWidth || document.documentElement.clientWidth
              , n = window.innerHeight || document.documentElement.clientHeight
              , s = this.getWidth()
              , o = this.getHeight();
            i < (e += 15) + s && (e -= e + s - i),
            n < (t += 15) + o && (t -= 20 + o),
            r.prototype.setPosition.call(this, e, t)
        }
    }
    .call(n.prototype),
    t.GutterHandler = function(r) {
        function a() {
            i = i && clearTimeout(i),
            c && (g.hide(),
            c = null,
            u._signal("hideGutterTooltip", g),
            u.off("mousewheel", a))
        }
        function l(e) {
            g.setPosition(e.x, e.y)
        }
        var i, h, c, u = r.editor, d = u.renderer.$gutterLayer, g = new n(u.container);
        r.editor.setDefaultHandler("guttermousedown", function(e) {
            if (u.isFocused() && 0 == e.getButton() && "foldWidgets" != d.getRegion(e)) {
                var t = e.getDocumentPosition().row
                  , i = u.session.selection;
                if (e.getShiftKey())
                    i.selectTo(t, 0);
                else {
                    if (2 == e.domEvent.detail)
                        return u.selectAll(),
                        e.preventDefault();
                    r.$clickSelection = u.selection.getLineRange(t)
                }
                return r.setState("selectByLines"),
                r.captureMouse(e),
                e.preventDefault()
            }
        }),
        r.editor.setDefaultHandler("guttermousemove", function(e) {
            var t = e.domEvent.target || e.domEvent.srcElement;
            if (s.hasCssClass(t, "ace_fold-widget"))
                return a();
            c && r.$tooltipFollowsMouse && l(e),
            h = e,
            i = i || setTimeout(function() {
                i = null,
                (h && !r.isMousePressed ? function() {
                    var e, t, i = h.getDocumentPosition().row, n = d.$annotations[i];
                    if (!n)
                        return a();
                    if (i == u.session.getLength()) {
                        var s = u.renderer.pixelToScreenCoordinates(0, h.y).row
                          , o = h.$pos;
                        if (s > u.session.documentToScreenRow(o.row, o.column))
                            return a()
                    }
                    c != n && (c = n.text.join("<br/>"),
                    g.setHtml(c),
                    g.show(),
                    u._signal("showGutterTooltip", g),
                    u.on("mousewheel", a),
                    r.$tooltipFollowsMouse ? l(h) : (e = h.domEvent.target.getBoundingClientRect(),
                    (t = g.getElement().style).left = e.right + "px",
                    t.top = e.bottom + "px"))
                }
                : a)()
            }, 50)
        }),
        f.addListener(u.renderer.$gutter, "mouseout", function(e) {
            h = null,
            c && !i && (i = setTimeout(function() {
                i = null,
                a()
            }, 50))
        }, u),
        u.on("changeSession", a)
    }
}),
define("ace/mouse/mouse_event", ["require", "exports", "module", "ace/lib/event", "ace/lib/useragent"], function(e, t, i) {
    "use strict";
    var n = e("../lib/event")
      , s = e("../lib/useragent")
      , o = t.MouseEvent = function(e, t) {
        this.domEvent = e,
        this.editor = t,
        this.x = this.clientX = e.clientX,
        this.y = this.clientY = e.clientY,
        this.$pos = null,
        this.$inSelection = null,
        this.propagationStopped = !1,
        this.defaultPrevented = !1
    }
    ;
    (function() {
        this.stopPropagation = function() {
            n.stopPropagation(this.domEvent),
            this.propagationStopped = !0
        }
        ,
        this.preventDefault = function() {
            n.preventDefault(this.domEvent),
            this.defaultPrevented = !0
        }
        ,
        this.stop = function() {
            this.stopPropagation(),
            this.preventDefault()
        }
        ,
        this.getDocumentPosition = function() {
            return this.$pos || (this.$pos = this.editor.renderer.screenToTextCoordinates(this.clientX, this.clientY)),
            this.$pos
        }
        ,
        this.inSelection = function() {
            if (null !== this.$inSelection)
                return this.$inSelection;
            var e, t = this.editor.getSelectionRange();
            return t.isEmpty() ? this.$inSelection = !1 : (e = this.getDocumentPosition(),
            this.$inSelection = t.contains(e.row, e.column)),
            this.$inSelection
        }
        ,
        this.getButton = function() {
            return n.getButton(this.domEvent)
        }
        ,
        this.getShiftKey = function() {
            return this.domEvent.shiftKey
        }
        ,
        this.getAccelKey = s.isMac ? function() {
            return this.domEvent.metaKey
        }
        : function() {
            return this.domEvent.ctrlKey
        }
    }
    ).call(o.prototype)
}),
define("ace/mouse/dragdrop_handler", ["require", "exports", "module", "ace/lib/dom", "ace/lib/event", "ace/lib/useragent"], function(e, t, i) {
    "use strict";
    function n(t) {
        function e() {
            var e, t, i, n, s, o = u;
            u = g.renderer.screenToTextCoordinates(f, m),
            e = u,
            t = o,
            i = Date.now(),
            n = !t || e.row != t.row,
            s = !t || e.column != t.column,
            !v || n || s ? (g.moveCursorToPosition(e),
            v = i,
            $ = {
                x: f,
                y: m
            }) : 5 < S($.x, $.y, f, m) ? v = null : 200 <= i - v && (g.renderer.scrollCursorIntoView(),
            v = null),
            function(e, t) {
                var i = Date.now()
                  , n = g.renderer.layerConfig.lineHeight
                  , s = g.renderer.layerConfig.characterWidth
                  , o = g.renderer.scroller.getBoundingClientRect()
                  , r = {
                    x: {
                        left: f - o.left,
                        right: o.right - f
                    },
                    y: {
                        top: m - o.top,
                        bottom: o.bottom - m
                    }
                }
                  , a = Math.min(r.x.left, r.x.right)
                  , l = Math.min(r.y.top, r.y.bottom)
                  , h = {
                    row: e.row,
                    column: e.column
                };
                a / s <= 2 && (h.column += r.x.left < r.x.right ? -3 : 2),
                l / n <= 1 && (h.row += r.y.top < r.y.bottom ? -1 : 1);
                var c = e.row != h.row
                  , u = e.column != h.column
                  , d = !t || e.row != t.row;
                c || u && !d ? w ? 200 <= i - w && g.renderer.scrollCursorIntoView(h) : w = i : w = null
            }(u, o)
        }
        function i() {
            c = g.selection.toOrientedRange(),
            l = g.session.addMarker(c, "ace_selection", g.getSelectionStyle()),
            g.clearSelection(),
            g.isFocused() && g.renderer.$cursorLayer.setBlinking(!1),
            clearInterval(h),
            e(),
            h = setInterval(e, 20),
            y = 0,
            k.addListener(document, "mousemove", s)
        }
        function n() {
            clearInterval(h),
            g.session.removeMarker(l),
            l = null,
            g.selection.fromOrientedRange(c),
            g.isFocused() && !p && g.$resetCursorStyle(),
            y = 0,
            v = w = u = c = null,
            k.removeListener(document, "mousemove", s)
        }
        function s() {
            null == C && (C = setTimeout(function() {
                null != C && l && n()
            }, 20))
        }
        function o(e) {
            var t = e.types;
            return !t || Array.prototype.some.call(t, function(e) {
                return "text/plain" == e || "Text" == e
            })
        }
        function r(e) {
            var t = ["copy", "copymove", "all", "uninitialized"]
              , i = A.isMac ? e.altKey : e.ctrlKey
              , n = "uninitialized";
            try {
                n = e.dataTransfer.effectAllowed.toLowerCase()
            } catch (e) {}
            var s = "none";
            return i && 0 <= t.indexOf(n) ? s = "copy" : 0 <= ["move", "copymove", "linkmove", "all", "uninitialized"].indexOf(n) ? s = "move" : 0 <= t.indexOf(n) && (s = "copy"),
            s
        }
        var g = t.editor
          , a = x.createElement("img");
        a.src = "data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==",
        A.isOpera && (a.style.cssText = "width:1px;height:1px;position:fixed;top:0;left:0;z-index:2147483647;opacity:0;");
        ["dragWait", "dragWaitEnd", "startDrag", "dragReadyEnd", "onMouseDrag"].forEach(function(e) {
            t[e] = this[e]
        }, this),
        g.on("mousedown", this.onMouseDown.bind(t));
        var l, f, m, h, c, u, d, p, w, v, $, b = g.container, y = 0;
        this.onDragStart = function(e) {
            if (this.cancelDrag || !b.draggable) {
                var t = this;
                return setTimeout(function() {
                    t.startSelect(),
                    t.captureMouse(e)
                }, 0),
                e.preventDefault()
            }
            c = g.getSelectionRange();
            var i = e.dataTransfer;
            i.effectAllowed = g.getReadOnly() ? "copy" : "copyMove",
            A.isOpera && (g.container.appendChild(a),
            a.scrollTop = 0),
            i.setDragImage && i.setDragImage(a, 0, 0),
            A.isOpera && g.container.removeChild(a),
            i.clearData(),
            i.setData("Text", g.session.getTextRange()),
            p = !0,
            this.setState("drag")
        }
        ,
        this.onDragEnd = function(e) {
            var t;
            b.draggable = !1,
            p = !1,
            this.setState(null),
            g.getReadOnly() || (t = e.dataTransfer.dropEffect,
            d || "move" != t || g.session.remove(g.getSelectionRange()),
            g.$resetCursorStyle()),
            this.editor.unsetStyle("ace_dragging"),
            this.editor.renderer.setCursorStyle("")
        }
        ,
        this.onDragEnter = function(e) {
            if (!g.getReadOnly() && o(e.dataTransfer))
                return f = e.clientX,
                m = e.clientY,
                l || i(),
                y++,
                e.dataTransfer.dropEffect = d = r(e),
                k.preventDefault(e)
        }
        ,
        this.onDragOver = function(e) {
            if (!g.getReadOnly() && o(e.dataTransfer))
                return f = e.clientX,
                m = e.clientY,
                l || (i(),
                y++),
                null !== C && (C = null),
                e.dataTransfer.dropEffect = d = r(e),
                k.preventDefault(e)
        }
        ,
        this.onDragLeave = function(e) {
            if (--y <= 0 && l)
                return n(),
                d = null,
                k.preventDefault(e)
        }
        ,
        this.onDrop = function(e) {
            if (u) {
                var t = e.dataTransfer;
                if (p)
                    switch (d) {
                    case "move":
                        c = c.contains(u.row, u.column) ? {
                            start: u,
                            end: u
                        } : g.moveText(c, u);
                        break;
                    case "copy":
                        c = g.moveText(c, u, !0)
                    }
                else {
                    var i = t.getData("Text");
                    c = {
                        start: u,
                        end: g.session.insert(u, i)
                    },
                    g.focus(),
                    d = null
                }
                return n(),
                k.preventDefault(e)
            }
        }
        ,
        k.addListener(b, "dragstart", this.onDragStart.bind(t), g),
        k.addListener(b, "dragend", this.onDragEnd.bind(t), g),
        k.addListener(b, "dragenter", this.onDragEnter.bind(t), g),
        k.addListener(b, "dragover", this.onDragOver.bind(t), g),
        k.addListener(b, "dragleave", this.onDragLeave.bind(t), g),
        k.addListener(b, "drop", this.onDrop.bind(t), g);
        var C = null
    }
    function S(e, t, i, n) {
        return Math.sqrt(Math.pow(i - e, 2) + Math.pow(n - t, 2))
    }
    var x = e("../lib/dom")
      , k = e("../lib/event")
      , A = e("../lib/useragent");
    (function() {
        this.dragWait = function() {
            Date.now() - this.mousedownEvent.time > this.editor.getDragDelay() && this.startDrag()
        }
        ,
        this.dragWaitEnd = function() {
            this.editor.container.draggable = !1,
            this.startSelect(this.mousedownEvent.getDocumentPosition()),
            this.selectEnd()
        }
        ,
        this.dragReadyEnd = function(e) {
            this.editor.$resetCursorStyle(),
            this.editor.unsetStyle("ace_dragging"),
            this.editor.renderer.setCursorStyle(""),
            this.dragWaitEnd()
        }
        ,
        this.startDrag = function() {
            this.cancelDrag = !1;
            var e = this.editor;
            e.container.draggable = !0,
            e.renderer.$cursorLayer.setBlinking(!1),
            e.setStyle("ace_dragging");
            var t = A.isWin ? "default" : "move";
            e.renderer.setCursorStyle(t),
            this.setState("dragReady")
        }
        ,
        this.onMouseDrag = function(e) {
            var t = this.editor.container;
            A.isIE && "dragReady" == this.state && 3 < S(this.mousedownEvent.x, this.mousedownEvent.y, this.x, this.y) && t.dragDrop(),
            "dragWait" === this.state && 0 < S(this.mousedownEvent.x, this.mousedownEvent.y, this.x, this.y) && (t.draggable = !1,
            this.startSelect(this.mousedownEvent.getDocumentPosition()))
        }
        ,
        this.onMouseDown = function(e) {
            if (this.$dragEnabled) {
                this.mousedownEvent = e;
                var t = this.editor
                  , i = e.inSelection()
                  , n = e.getButton();
                if (1 === (e.domEvent.detail || 1) && 0 === n && i) {
                    if (e.editor.inMultiSelectMode && (e.getAccelKey() || e.getShiftKey()))
                        return;
                    this.mousedownEvent.time = Date.now();
                    var s = e.domEvent.target || e.domEvent.srcElement;
                    "unselectable"in s && (s.unselectable = "on"),
                    t.getDragDelay() ? (A.isWebKit && (this.cancelDrag = !0,
                    t.container.draggable = !0),
                    this.setState("dragWait")) : this.startDrag(),
                    this.captureMouse(e, this.onMouseDrag.bind(this)),
                    e.defaultPrevented = !0
                }
            }
        }
    }
    ).call(n.prototype),
    t.DragdropHandler = n
}),
define("ace/mouse/touch_handler", ["require", "exports", "module", "ace/mouse/mouse_event", "ace/lib/event", "ace/lib/dom"], function(e, t, i) {
    "use strict";
    var F = e("./mouse_event").MouseEvent
      , n = e("../lib/event")
      , l = e("../lib/dom");
    t.addTouchListeners = function(e, $) {
        function o() {
            function t(e) {
                var t, i, n = e.target.getAttribute("action");
                if ("more" == n || !o)
                    return o = !o,
                    t = $.getCopyText(),
                    i = $.session.getUndoManager().hasUndo(),
                    void a.replaceChild(l.buildDom(o ? ["span", !t && ["span", {
                        class: "ace_mobile-button",
                        action: "selectall"
                    }, "Select All"], t && ["span", {
                        class: "ace_mobile-button",
                        action: "copy"
                    }, "Copy"], t && ["span", {
                        class: "ace_mobile-button",
                        action: "cut"
                    }, "Cut"], s && ["span", {
                        class: "ace_mobile-button",
                        action: "paste"
                    }, "Paste"], i && ["span", {
                        class: "ace_mobile-button",
                        action: "undo"
                    }, "Undo"], ["span", {
                        class: "ace_mobile-button",
                        action: "find"
                    }, "Find"], ["span", {
                        class: "ace_mobile-button",
                        action: "openCommandPallete"
                    }, "Pallete"]] : ["span"]), a.firstChild);
                "paste" == n ? s.readText().then(function(e) {
                    $.execCommand(n, e)
                }) : n && ("cut" != n && "copy" != n || (s ? s.writeText($.getCopyText()) : document.execCommand("copy")),
                $.execCommand(n)),
                a.firstChild.style.display = "none",
                o = !1,
                "openCommandPallete" != n && $.focus()
            }
            var s = window.navigator && window.navigator.clipboard
              , o = !1;
            a = l.buildDom(["div", {
                class: "ace_mobile-menu",
                ontouchstart: function(e) {
                    R = "menu",
                    e.stopPropagation(),
                    e.preventDefault(),
                    $.textInput.focus()
                },
                ontouchend: function(e) {
                    e.stopPropagation(),
                    e.preventDefault(),
                    t(e)
                },
                onclick: t
            }, ["span"], ["span", {
                class: "ace_mobile-button",
                action: "more"
            }, "..."]], $.container)
        }
        function i() {
            a || o();
            var e = $.selection.cursor
              , t = $.renderer.textToScreenCoordinates(e.row, e.column)
              , i = $.renderer.textToScreenCoordinates(0, 0).pageX
              , n = $.renderer.scrollLeft
              , s = $.container.getBoundingClientRect();
            a.style.top = t.pageY - s.top - 3 + "px",
            t.pageX - s.left < s.width - 70 ? (a.style.left = "",
            a.style.right = "10px") : (a.style.right = "",
            a.style.left = i + n - s.left + "px"),
            a.style.display = "",
            a.firstChild.style.display = "none",
            $.on("input", r)
        }
        function r(e) {
            a && (a.style.display = "none"),
            $.off("input", r)
        }
        function b() {
            k = null,
            clearTimeout(k);
            var e = $.selection.getRange()
              , t = e.contains(A.row, A.column);
            !e.isEmpty() && t || ($.selection.moveToPosition(A),
            $.selection.selectWord()),
            R = "wait",
            i()
        }
        var y, C, S, x, k, t, A, L, a, R = "scroll", M = 0, E = 0, T = 0, _ = 0;
        n.addListener(e, "contextmenu", function(e) {
            L && $.textInput.getElement().focus()
        }, $),
        n.addListener(e, "touchstart", function(e) {
            var t = e.touches;
            if (k || 1 < t.length)
                return clearTimeout(k),
                k = null,
                S = -1,
                void (R = "zoom");
            L = $.$mouseHandler.isMousePressed = !0;
            var i = $.renderer.layerConfig.lineHeight
              , n = $.renderer.layerConfig.lineHeight
              , s = e.timeStamp;
            x = s;
            var o = t[0]
              , r = o.clientX
              , a = o.clientY;
            Math.abs(y - r) + Math.abs(C - a) > i && (S = -1),
            y = e.clientX = r,
            C = e.clientY = a,
            T = _ = 0;
            var l = new F(e,$);
            if (A = l.getDocumentPosition(),
            s - S < 500 && 1 == t.length && !M)
                E++,
                e.preventDefault(),
                e.button = 0,
                function() {
                    k = null,
                    clearTimeout(k),
                    $.selection.moveToPosition(A);
                    var e = 2 <= E ? $.selection.getLineRange(A.row) : $.session.getBracketRange(A);
                    e && !e.isEmpty() ? $.selection.setRange(e) : $.selection.selectWord(),
                    R = "wait"
                }();
            else {
                E = 0;
                var h = $.selection.cursor
                  , c = $.selection.isEmpty() ? h : $.selection.anchor
                  , u = $.renderer.$cursorLayer.getPixelPosition(h, !0)
                  , d = $.renderer.$cursorLayer.getPixelPosition(c, !0)
                  , g = $.renderer.scroller.getBoundingClientRect()
                  , f = $.renderer.layerConfig.offset
                  , m = $.renderer.scrollLeft
                  , p = function(e, t) {
                    return (e /= n) * e + (t = t / i - .75) * t
                };
                if (e.clientX < g.left)
                    return void (R = "zoom");
                var w = p(e.clientX - g.left - u.left + m, e.clientY - g.top - u.top + f)
                  , v = p(e.clientX - g.left - d.left + m, e.clientY - g.top - d.top + f);
                w < 3.5 && v < 3.5 && (R = v < w ? "cursor" : "anchor"),
                R = v < 3.5 ? "anchor" : w < 3.5 ? "cursor" : "scroll",
                k = setTimeout(b, 450)
            }
            S = s
        }, $),
        n.addListener(e, "touchend", function(e) {
            L = $.$mouseHandler.isMousePressed = !1,
            t && clearInterval(t),
            "zoom" == R ? (R = "",
            M = 0) : k ? ($.selection.moveToPosition(A),
            M = 0,
            i()) : "scroll" == R ? (M += 60,
            t = setInterval(function() {
                M-- <= 0 && (clearInterval(t),
                t = null),
                Math.abs(T) < .01 && (T = 0),
                Math.abs(_) < .01 && (_ = 0),
                M < 20 && (T *= .9),
                M < 20 && (_ *= .9);
                var e = $.session.getScrollTop();
                $.renderer.scrollBy(10 * T, 10 * _),
                e == $.session.getScrollTop() && (M = 0)
            }, 10),
            r()) : i(),
            clearTimeout(k),
            k = null
        }, $),
        n.addListener(e, "touchmove", function(e) {
            k && (clearTimeout(k),
            k = null);
            var t = e.touches;
            if (!(1 < t.length || "zoom" == R)) {
                var i = t[0]
                  , n = y - i.clientX
                  , s = C - i.clientY;
                if ("wait" == R) {
                    if (!(4 < n * n + s * s))
                        return e.preventDefault();
                    R = "cursor"
                }
                y = i.clientX,
                C = i.clientY,
                e.clientX = i.clientX,
                e.clientY = i.clientY;
                var o, r, a = e.timeStamp, l = a - x;
                x = a,
                "scroll" == R ? ((o = new F(e,$)).speed = 1,
                o.wheelX = n,
                o.wheelY = s,
                10 * Math.abs(n) < Math.abs(s) && (n = 0),
                10 * Math.abs(s) < Math.abs(n) && (s = 0),
                0 != l && (T = n / l,
                _ = s / l),
                $._emit("mousewheel", o),
                o.propagationStopped || (T = _ = 0)) : (r = new F(e,$).getDocumentPosition(),
                "cursor" == R ? $.selection.moveCursorToPosition(r) : "anchor" == R && $.selection.setSelectionAnchor(r.row, r.column),
                $.renderer.scrollCursorIntoView(r),
                e.preventDefault())
            }
        }, $)
    }
}),
define("ace/lib/net", ["require", "exports", "module", "ace/lib/dom"], function(e, t, i) {
    "use strict";
    var s = e("./dom");
    t.get = function(e, t) {
        var i = new XMLHttpRequest;
        i.open("GET", e, !0),
        i.onreadystatechange = function() {
            4 === i.readyState && t(i.responseText)
        }
        ,
        i.send(null)
    }
    ,
    t.loadScript = function(e, i) {
        var t = s.getDocumentHead()
          , n = document.createElement("script");
        n.src = e,
        t.appendChild(n),
        n.onload = n.onreadystatechange = function(e, t) {
            !t && n.readyState && "loaded" != n.readyState && "complete" != n.readyState || (n = n.onload = n.onreadystatechange = null,
            t || i())
        }
    }
    ,
    t.qualifyURL = function(e) {
        var t = document.createElement("a");
        return t.href = e,
        t.href
    }
}),
define("ace/lib/event_emitter", ["require", "exports", "module"], function(e, t, i) {
    "use strict";
    function o() {
        this.propagationStopped = !0
    }
    function r() {
        this.defaultPrevented = !0
    }
    var n = {};
    n._emit = n._dispatchEvent = function(e, t) {
        this._eventRegistry || (this._eventRegistry = {}),
        this._defaultHandlers || (this._defaultHandlers = {});
        var i = this._eventRegistry[e] || []
          , n = this._defaultHandlers[e];
        if (i.length || n) {
            "object" == typeof t && t || (t = {}),
            t.type || (t.type = e),
            t.stopPropagation || (t.stopPropagation = o),
            t.preventDefault || (t.preventDefault = r),
            i = i.slice();
            for (var s = 0; s < i.length && (i[s](t, this),
            !t.propagationStopped); s++)
                ;
            return n && !t.defaultPrevented ? n(t, this) : void 0
        }
    }
    ,
    n._signal = function(e, t) {
        var i = (this._eventRegistry || {})[e];
        if (i) {
            i = i.slice();
            for (var n = 0; n < i.length; n++)
                i[n](t, this)
        }
    }
    ,
    n.once = function(t, i) {
        var n = this;
        if (this.on(t, function e() {
            n.off(t, e),
            i.apply(null, arguments)
        }),
        !i)
            return new Promise(function(e) {
                i = e
            }
            )
    }
    ,
    n.setDefaultHandler = function(e, t) {
        var i, n, s, o = this._defaultHandlers;
        (o = o || (this._defaultHandlers = {
            _disabled_: {}
        }))[e] && (i = o[e],
        (n = o._disabled_[e]) || (o._disabled_[e] = n = []),
        n.push(i),
        -1 != (s = n.indexOf(t)) && n.splice(s, 1)),
        o[e] = t
    }
    ,
    n.removeDefaultHandler = function(e, t) {
        var i, n, s = this._defaultHandlers;
        s && (i = s._disabled_[e],
        s[e] == t ? i && this.setDefaultHandler(e, i.pop()) : !i || -1 != (n = i.indexOf(t)) && i.splice(n, 1))
    }
    ,
    n.on = n.addEventListener = function(e, t, i) {
        this._eventRegistry = this._eventRegistry || {};
        var n = this._eventRegistry[e];
        return -1 == (n = n || (this._eventRegistry[e] = [])).indexOf(t) && n[i ? "unshift" : "push"](t),
        t
    }
    ,
    n.off = n.removeListener = n.removeEventListener = function(e, t) {
        this._eventRegistry = this._eventRegistry || {};
        var i, n = this._eventRegistry[e];
        !n || -1 !== (i = n.indexOf(t)) && n.splice(i, 1)
    }
    ,
    n.removeAllListeners = function(e) {
        e || (this._eventRegistry = this._defaultHandlers = void 0),
        this._eventRegistry && (this._eventRegistry[e] = void 0),
        this._defaultHandlers && (this._defaultHandlers[e] = void 0)
    }
    ,
    t.EventEmitter = n
}),
define("ace/lib/app_config", ["require", "exports", "module", "ace/lib/oop", "ace/lib/event_emitter"], function(e, t, i) {
    function n(e) {
        "undefined" != typeof console && console.warn && console.warn.apply(console, arguments)
    }
    function s(e, t) {
        var i = new Error(e);
        i.data = t,
        "object" == typeof console && console.error && console.error(i),
        setTimeout(function() {
            throw i
        })
    }
    function o() {
        this.$defaultOptions = {}
    }
    var r = e("./oop")
      , a = e("./event_emitter").EventEmitter
      , l = {
        setOptions: function(t) {
            Object.keys(t).forEach(function(e) {
                this.setOption(e, t[e])
            }, this)
        },
        getOptions: function(e) {
            var t, i = {};
            return e ? Array.isArray(e) || (i = e,
            e = Object.keys(i)) : (t = this.$options,
            e = Object.keys(t).filter(function(e) {
                return !t[e].hidden
            })),
            e.forEach(function(e) {
                i[e] = this.getOption(e)
            }, this),
            i
        },
        setOption: function(e, t) {
            if (this["$" + e] !== t) {
                var i = this.$options[e];
                return i ? i.forwardTo ? this[i.forwardTo] && this[i.forwardTo].setOption(e, t) : (i.handlesSet || (this["$" + e] = t),
                void (i && i.set && i.set.call(this, t))) : n('misspelled option "' + e + '"')
            }
        },
        getOption: function(e) {
            var t = this.$options[e];
            return t ? t.forwardTo ? this[t.forwardTo] && this[t.forwardTo].getOption(e) : t && t.get ? t.get.call(this) : this["$" + e] : n('misspelled option "' + e + '"')
        }
    };
    (function() {
        r.implement(this, a),
        this.defineOptions = function(i, e, n) {
            return i.$options || (this.$defaultOptions[e] = i.$options = {}),
            Object.keys(n).forEach(function(e) {
                var t = n[e];
                "string" == typeof t && (t = {
                    forwardTo: t
                }),
                t.name || (t.name = e),
                "initialValue"in (i.$options[t.name] = t) && (i["$" + t.name] = t.initialValue)
            }),
            r.implement(i, l),
            this
        }
        ,
        this.resetOptions = function(i) {
            Object.keys(i.$options).forEach(function(e) {
                var t = i.$options[e];
                "value"in t && i.setOption(e, t.value)
            })
        }
        ,
        this.setDefaultValue = function(e, t, i) {
            if (!e) {
                for (e in this.$defaultOptions)
                    if (this.$defaultOptions[e][t])
                        break;
                if (!this.$defaultOptions[e][t])
                    return !1
            }
            var n = this.$defaultOptions[e] || (this.$defaultOptions[e] = {});
            n[t] && (n.forwardTo ? this.setDefaultValue(n.forwardTo, t, i) : n[t].value = i)
        }
        ,
        this.setDefaultValues = function(t, i) {
            Object.keys(i).forEach(function(e) {
                this.setDefaultValue(t, e, i[e])
            }, this)
        }
        ,
        this.warn = n,
        this.reportError = s
    }
    ).call(o.prototype),
    t.AppConfig = o
}),
define("ace/config", ["require", "exports", "module", "ace/lib/lang", "ace/lib/oop", "ace/lib/net", "ace/lib/app_config"], function(f, m, p) {
    var e = f("./lib/lang")
      , o = (f("./lib/oop"),
    f("./lib/net"))
      , t = f("./lib/app_config").AppConfig;
    p.exports = m = new t;
    var w = function() {
        return this || "undefined" != typeof window && window
    }()
      , v = {
        packaged: !1,
        workerPath: null,
        modePath: null,
        themePath: null,
        basePath: "",
        suffix: ".js",
        $moduleUrls: {},
        loadWorkerFromBlob: !0,
        sharedPopups: !1
    };
    m.get = function(e) {
        if (!v.hasOwnProperty(e))
            throw new Error("Unknown config key: " + e);
        return v[e]
    }
    ,
    m.set = function(e, t) {
        if (v.hasOwnProperty(e))
            v[e] = t;
        else if (0 == this.setDefaultValue("", e, t))
            throw new Error("Unknown config key: " + e)
    }
    ,
    m.all = function() {
        return e.copyObject(v)
    }
    ,
    m.$modes = {},
    m.moduleUrl = function(e, t) {
        if (v.$moduleUrls[e])
            return v.$moduleUrls[e];
        var i, n = e.split("/"), s = "snippets" == (t = t || n[n.length - 2] || "") ? "/" : "-", o = n[n.length - 1];
        "worker" == t && "-" == s && (i = new RegExp("^" + t + "[\\-_]|[\\-_]" + t + "$","g"),
        o = o.replace(i, "")),
        (!o || o == t) && 1 < n.length && (o = n[n.length - 2]);
        var r = v[t + "Path"];
        return null == r ? r = v.basePath : "/" == s && (t = s = ""),
        r && "/" != r.slice(-1) && (r += "/"),
        r + t + s + o + this.get("suffix")
    }
    ,
    m.setModuleUrl = function(e, t) {
        return v.$moduleUrls[e] = t
    }
    ,
    m.$loading = {},
    m.loadModule = function(i, e) {
        var t, n;
        Array.isArray(i) && (n = i[0],
        i = i[1]);
        try {
            t = f(i)
        } catch (e) {}
        if (t && !m.$loading[i])
            return e && e(t);
        if (m.$loading[i] || (m.$loading[i] = []),
        m.$loading[i].push(e),
        !(1 < m.$loading[i].length)) {
            function s() {
                f([i], function(t) {
                    m._emit("load.module", {
                        name: i,
                        module: t
                    });
                    var e = m.$loading[i];
                    m.$loading[i] = null,
                    e.forEach(function(e) {
                        e && e(t)
                    })
                })
            }
            if (!m.get("packaged"))
                return s();
            o.loadScript(m.moduleUrl(i, n), s),
            r()
        }
    }
    ;
    var r = function() {
        v.basePath || v.workerPath || v.modePath || v.themePath || Object.keys(v.$moduleUrls).length || (console.error("Unable to infer path to ace from script src,", "use ace.config.set('basePath', 'path') to enable dynamic loading of modes and themes", "or with webpack use ace/webpack-resolver"),
        r = function() {}
        )
    };
    m.init = function(e) {
        if (w && w.document) {
            v.packaged = e || f.packaged || p.packaged || w.define && define.packaged;
            for (var t = {}, i = "", n = document.currentScript || document._currentScript, s = (n && n.ownerDocument || document).getElementsByTagName("script"), o = 0; o < s.length; o++) {
                var r = s[o]
                  , a = r.src || r.getAttribute("src");
                if (a) {
                    for (var l = r.attributes, h = 0, c = l.length; h < c; h++) {
                        var u = l[h];
                        0 === u.name.indexOf("data-ace-") && (t[u.name.replace(/^data-ace-/, "").replace(/-(.)/g, function(e, t) {
                            return t.toUpperCase()
                        })] = u.value)
                    }
                    var d = a.match(/^(.*)\/ace(\-\w+)?\.js(\?|$)/);
                    d && (i = d[1])
                }
            }
            for (var g in i && (t.base = t.base || i,
            t.packaged = !0),
            t.basePath = t.base,
            t.workerPath = t.workerPath || t.base,
            t.modePath = t.modePath || t.base,
            t.themePath = t.themePath || t.base,
            delete t.base,
            t)
                void 0 !== t[g] && m.set(g, t[g])
        }
    }
    ,
    m.version = "1.4.12"
}),
define("ace/mouse/mouse_handler", ["require", "exports", "module", "ace/lib/event", "ace/lib/useragent", "ace/mouse/default_handlers", "ace/mouse/default_gutter_handler", "ace/mouse/mouse_event", "ace/mouse/dragdrop_handler", "ace/mouse/touch_handler", "ace/config"], function(e, t, i) {
    "use strict";
    function n(s) {
        var o = this;
        function e(e) {
            document.hasFocus && document.hasFocus() && (s.isFocused() || document.activeElement != (s.textInput && s.textInput.getElement())) || window.focus(),
            s.focus()
        }
        this.editor = s,
        new r(this),
        new a(this),
        new l(this);
        var t = s.renderer.getMouseEventTarget();
        c.addListener(t, "click", this.onMouseEvent.bind(this, "click"), s),
        c.addListener(t, "mousemove", this.onMouseMove.bind(this, "mousemove"), s),
        c.addMultiMouseDownListener([t, s.renderer.scrollBarV && s.renderer.scrollBarV.inner, s.renderer.scrollBarH && s.renderer.scrollBarH.inner, s.textInput && s.textInput.getElement()].filter(Boolean), [400, 300, 250], this, "onMouseEvent", s),
        c.addMouseWheelListener(s.container, this.onMouseWheel.bind(this, "mousewheel"), s),
        h(s.container, s);
        var i = s.renderer.$gutter;
        c.addListener(i, "mousedown", this.onMouseEvent.bind(this, "guttermousedown"), s),
        c.addListener(i, "click", this.onMouseEvent.bind(this, "gutterclick"), s),
        c.addListener(i, "dblclick", this.onMouseEvent.bind(this, "gutterdblclick"), s),
        c.addListener(i, "mousemove", this.onMouseEvent.bind(this, "guttermousemove"), s),
        c.addListener(t, "mousedown", e, s),
        c.addListener(i, "mousedown", e, s),
        u.isIE && s.renderer.scrollBarV && (c.addListener(s.renderer.scrollBarV.element, "mousedown", e, s),
        c.addListener(s.renderer.scrollBarH.element, "mousedown", e, s)),
        s.on("mousemove", function(e) {
            var t, i, n;
            o.state || o.$dragDelay || !o.$dragEnabled || (t = s.renderer.screenToTextCoordinates(e.x, e.y),
            i = s.session.selection.getRange(),
            n = s.renderer,
            !i.isEmpty() && i.insideStart(t.row, t.column) ? n.setCursorStyle("default") : n.setCursorStyle(""))
        }, s)
    }
    var c = e("../lib/event")
      , u = e("../lib/useragent")
      , r = e("./default_handlers").DefaultHandlers
      , a = e("./default_gutter_handler").GutterHandler
      , d = e("./mouse_event").MouseEvent
      , l = e("./dragdrop_handler").DragdropHandler
      , h = e("./touch_handler").addTouchListeners
      , s = e("../config");
    (function() {
        this.onMouseEvent = function(e, t) {
            this.editor._emit(e, new d(t,this.editor))
        }
        ,
        this.onMouseMove = function(e, t) {
            var i = this.editor._eventRegistry && this.editor._eventRegistry.mousemove;
            i && i.length && this.editor._emit(e, new d(t,this.editor))
        }
        ,
        this.onMouseWheel = function(e, t) {
            var i = new d(t,this.editor);
            i.speed = 2 * this.$scrollSpeed,
            i.wheelX = t.wheelX,
            i.wheelY = t.wheelY,
            this.editor._emit(e, i)
        }
        ,
        this.setState = function(e) {
            this.state = e
        }
        ,
        this.captureMouse = function(e, t) {
            this.x = e.x,
            this.y = e.y,
            this.isMousePressed = !0;
            var i = this.editor
              , n = this.editor.renderer;
            n.$isMousePressed = !0;
            function s(e) {
                if (e)
                    return u.isWebKit && !e.which && r.releaseMouse ? r.releaseMouse() : (r.x = e.clientX,
                    r.y = e.clientY,
                    t && t(e),
                    r.mouseEvent = new d(e,r.editor),
                    void (r.$mouseMoved = !0))
            }
            function o(e) {
                i.off("beforeEndOperation", l),
                clearInterval(h),
                a(),
                r[r.state + "End"] && r[r.state + "End"](e),
                r.state = "",
                r.isMousePressed = n.$isMousePressed = !1,
                n.$keepTextAreaAtCursor && n.$moveTextAreaToCursor(),
                r.$onCaptureMouseMove = r.releaseMouse = null,
                e && r.onMouseEvent("mouseup", e),
                i.endOperation()
            }
            var r = this
              , a = function() {
                r[r.state] && r[r.state](),
                r.$mouseMoved = !1
            };
            if (u.isOldIE && "dblclick" == e.domEvent.type)
                return setTimeout(function() {
                    o(e)
                });
            var l = function(e) {
                r.releaseMouse && i.curOp.command.name && i.curOp.selectionChanged && (r[r.state + "End"] && r[r.state + "End"](),
                r.state = "",
                r.releaseMouse())
            };
            i.on("beforeEndOperation", l),
            i.startOperation({
                command: {
                    name: "mouse"
                }
            }),
            r.$onCaptureMouseMove = s,
            r.releaseMouse = c.capture(this.editor.container, s, o);
            var h = setInterval(a, 20)
        }
        ,
        this.releaseMouse = null,
        this.cancelContextMenu = function() {
            var t = function(e) {
                e && e.domEvent && "contextmenu" != e.domEvent.type || (this.editor.off("nativecontextmenu", t),
                e && e.domEvent && c.stopEvent(e.domEvent))
            }
            .bind(this);
            setTimeout(t, 10),
            this.editor.on("nativecontextmenu", t)
        }
        ,
        this.destroy = function() {
            this.releaseMouse && this.releaseMouse()
        }
    }
    ).call(n.prototype),
    s.defineOptions(n.prototype, "mouseHandler", {
        scrollSpeed: {
            initialValue: 2
        },
        dragDelay: {
            initialValue: u.isMac ? 150 : 0
        },
        dragEnabled: {
            initialValue: !0
        },
        focusTimeout: {
            initialValue: 0
        },
        tooltipFollowsMouse: {
            initialValue: !0
        }
    }),
    t.MouseHandler = n
}),
define("ace/mouse/fold_handler", ["require", "exports", "module", "ace/lib/dom"], function(e, t, i) {
    "use strict";
    var o = e("../lib/dom");
    t.FoldHandler = function(r) {
        r.on("click", function(e) {
            var t = e.getDocumentPosition()
              , i = r.session
              , n = i.getFoldAt(t.row, t.column, 1);
            n && (e.getAccelKey() ? i.removeFold(n) : i.expandFold(n),
            e.stop());
            var s = e.domEvent && e.domEvent.target;
            s && o.hasCssClass(s, "ace_inline_button") && o.hasCssClass(s, "ace_toggle_wrap") && (i.setOption("wrap", !i.getUseWrapMode()),
            r.renderer.scrollCursorIntoView())
        }),
        r.on("gutterclick", function(e) {
            var t, i;
            "foldWidgets" == r.renderer.$gutterLayer.getRegion(e) && (t = e.getDocumentPosition().row,
            (i = r.session).foldWidgets && i.foldWidgets[t] && r.session.onFoldWidgetClick(t, e),
            r.isFocused() || r.focus(),
            e.stop())
        }),
        r.on("gutterdblclick", function(e) {
            var t, i, n, s, o;
            "foldWidgets" == r.renderer.$gutterLayer.getRegion(e) && (t = e.getDocumentPosition().row,
            (s = (n = (i = r.session).getParentFoldRangeData(t, !0)).range || n.firstRange) && (t = s.start.row,
            (o = i.getFoldAt(t, i.getLine(t).length, 1)) ? i.removeFold(o) : (i.addFold("...", s),
            r.renderer.scrollCursorIntoView({
                row: s.start.row,
                column: 0
            }))),
            e.stop())
        })
    }
}),
define("ace/keyboard/keybinding", ["require", "exports", "module", "ace/lib/keys", "ace/lib/event"], function(e, t, i) {
    "use strict";
    function n(e) {
        this.$editor = e,
        this.$data = {
            editor: e
        },
        this.$handlers = [],
        this.setDefaultHandler(e.commands)
    }
    var s = e("../lib/keys")
      , l = e("../lib/event");
    (function() {
        this.setDefaultHandler = function(e) {
            this.removeKeyboardHandler(this.$defaultHandler),
            this.$defaultHandler = e,
            this.addKeyboardHandler(e, 0)
        }
        ,
        this.setKeyboardHandler = function(e) {
            var t = this.$handlers;
            if (t[t.length - 1] != e) {
                for (; t[t.length - 1] && t[t.length - 1] != this.$defaultHandler; )
                    this.removeKeyboardHandler(t[t.length - 1]);
                this.addKeyboardHandler(e, 1)
            }
        }
        ,
        this.addKeyboardHandler = function(e, t) {
            var i;
            e && ("function" != typeof e || e.handleKeyboard || (e.handleKeyboard = e),
            -1 != (i = this.$handlers.indexOf(e)) && this.$handlers.splice(i, 1),
            null == t ? this.$handlers.push(e) : this.$handlers.splice(t, 0, e),
            -1 == i && e.attach && e.attach(this.$editor))
        }
        ,
        this.removeKeyboardHandler = function(e) {
            var t = this.$handlers.indexOf(e);
            return -1 != t && (this.$handlers.splice(t, 1),
            e.detach && e.detach(this.$editor),
            !0)
        }
        ,
        this.getKeyboardHandler = function() {
            return this.$handlers[this.$handlers.length - 1]
        }
        ,
        this.getStatusText = function() {
            var t = this.$data
              , i = t.editor;
            return this.$handlers.map(function(e) {
                return e.getStatusText && e.getStatusText(i, t) || ""
            }).filter(Boolean).join(" ")
        }
        ,
        this.$callKeyboardHandlers = function(e, t, i, n) {
            for (var s, o = !1, r = this.$editor.commands, a = this.$handlers.length; a-- && !((s = this.$handlers[a].handleKeyboard(this.$data, e, t, i, n)) && s.command && ((o = "null" == s.command || r.exec(s.command, this.$editor, s.args, n)) && n && -1 != e && 1 != s.passEvent && 1 != s.command.passEvent && l.stopEvent(n),
            o)); )
                ;
            return o || -1 != e || (s = {
                command: "insertstring"
            },
            o = r.exec("insertstring", this.$editor, t)),
            o && this.$editor._signal && this.$editor._signal("keyboardActivity", s),
            o
        }
        ,
        this.onCommandKey = function(e, t, i) {
            var n = s.keyCodeToString(i);
            return this.$callKeyboardHandlers(t, n, i, e)
        }
        ,
        this.onTextInput = function(e) {
            return this.$callKeyboardHandlers(-1, e)
        }
    }
    ).call(n.prototype),
    t.KeyBinding = n
}),
define("ace/lib/bidiutil", ["require", "exports", "module"], function(e, l, t) {
    "use strict";
    function h(e, t, i) {
        if (!(v < e))
            if (1 != e || 1 != w || b)
                for (var n, s, o, r, a = i.length, l = 0; l < a; ) {
                    if (t[l] >= e) {
                        for (n = l + 1; n < a && t[n] >= e; )
                            n++;
                        for (s = l,
                        o = n - 1; s < o; s++,
                        o--)
                            r = i[s],
                            i[s] = i[o],
                            i[o] = r;
                        l = n
                    }
                    l++
                }
            else
                i.reverse()
    }
    function m(e, t, i, n) {
        var s, o, r, a = t[n];
        switch (a) {
        case u:
        case d:
            $ = !1;
        case x:
        case f:
            return a;
        case g:
            return $ ? f : g;
        case L:
            return $ = !0,
            d;
        case R:
            return x;
        case M:
            return n < 1 || n + 1 >= t.length || (c = i[n - 1]) != g && c != f || (s = t[n + 1]) != g && s != f ? x : ($ && (s = f),
            s == c ? s : x);
        case E:
            return (c = 0 < n ? i[n - 1] : k) == g && n + 1 < t.length && t[n + 1] == g ? g : x;
        case T:
            if (0 < n && i[n - 1] == g)
                return g;
            if ($)
                return x;
            for (r = n + 1,
            o = t.length; r < o && t[r] == T; )
                r++;
            return r < o && t[r] == g ? g : x;
        case _:
            for (o = t.length,
            r = n + 1; r < o && t[r] == _; )
                r++;
            if (r < o) {
                var l = e[n]
                  , h = 1425 <= l && l <= 2303 || 64286 == l
                  , c = t[r];
                if (h && (c == d || c == L))
                    return d
            }
            return n < 1 || (c = t[n - 1]) == k ? x : i[n - 1];
        case k:
            return b = !($ = !1),
            w;
        case A:
            return y = !0,
            x;
        case F:
        case O:
        case W:
        case D:
        case I:
            $ = !1;
        case B:
            return x
        }
    }
    function p(e) {
        var t = e.charCodeAt(0)
          , i = t >> 8;
        return 0 == i ? 191 < t ? u : n[t] : 5 == i ? /[\u0591-\u05f4]/.test(e) ? d : u : 6 == i ? /[\u0610-\u061a\u064b-\u065f\u06d6-\u06e4\u06e7-\u06ed]/.test(e) ? _ : /[\u0660-\u0669\u066b-\u066c]/.test(e) ? f : 1642 == t ? T : /[\u06f0-\u06f9]/.test(e) ? g : L : 32 == i && t <= 8287 ? s[255 & t] : 254 == i && 65136 <= t ? L : x
    }
    var w = 0
      , v = 0
      , $ = !1
      , b = !1
      , y = !1
      , C = [[0, 3, 0, 1, 0, 0, 0], [0, 3, 0, 1, 2, 2, 0], [0, 3, 0, 17, 2, 0, 1], [0, 3, 5, 5, 4, 1, 0], [0, 3, 21, 21, 4, 0, 1], [0, 3, 5, 5, 4, 2, 0]]
      , S = [[2, 0, 1, 1, 0, 1, 0], [2, 0, 1, 1, 0, 2, 0], [2, 0, 2, 1, 3, 2, 0], [2, 0, 2, 33, 3, 1, 1]]
      , u = 0
      , d = 1
      , g = 2
      , f = 3
      , x = 4
      , k = 5
      , A = 6
      , L = 7
      , R = 8
      , M = 9
      , E = 10
      , T = 11
      , _ = 12
      , F = 13
      , O = 14
      , I = 15
      , W = 16
      , D = 17
      , B = 18
      , n = [B, B, B, B, B, B, B, B, B, A, k, A, R, k, B, B, B, B, B, B, B, B, B, B, B, B, B, B, k, k, k, A, R, x, x, T, T, T, x, x, x, x, x, E, M, E, M, M, g, g, g, g, g, g, g, g, g, g, M, x, x, x, x, x, x, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, x, x, x, x, x, x, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, u, x, x, x, x, B, B, B, B, B, B, k, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, B, M, x, T, T, T, T, x, x, x, x, u, x, x, B, x, x, T, T, g, g, x, u, x, x, x, g, u, x, x, x, x, x]
      , s = [R, R, R, R, R, R, R, R, R, R, R, B, B, B, u, d, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, R, k, F, O, I, W, D, M, T, T, T, T, T, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, M, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, x, R];
    l.L = u,
    l.R = d,
    l.EN = g,
    l.ON_R = 3,
    l.AN = 4,
    l.R_H = 5,
    l.B = 6,
    l.RLE = 7,
    l.DOT = "·",
    l.doBidiReorder = function(e, t, i) {
        if (e.length < 2)
            return {};
        var n = e.split("")
          , s = new Array(n.length)
          , o = new Array(n.length)
          , r = [];
        w = i ? 1 : 0,
        function(e, t, i, n) {
            var s = w ? S : C
              , o = null
              , r = null
              , a = null
              , l = 0
              , h = null
              , c = -1
              , u = null
              , d = null
              , g = [];
            if (!n)
                for (u = 0,
                n = []; u < i; u++)
                    n[u] = p(e[u]);
            for (v = w,
            y = b = $ = !1,
            d = 0; d < i; d++) {
                if (o = l,
                g[d] = r = m(e, n, g, d),
                h = 240 & (l = s[o][r]),
                l &= 15,
                t[d] = a = s[l][5],
                0 < h)
                    if (16 == h) {
                        for (u = c; u < d; u++)
                            t[u] = 1;
                        c = -1
                    } else
                        c = -1;
                if (s[l][6])
                    -1 == c && (c = d);
                else if (-1 < c) {
                    for (u = c; u < d; u++)
                        t[u] = a;
                    c = -1
                }
                n[d] == k && (t[d] = 0),
                v |= a
            }
            if (y)
                for (u = 0; u < i; u++)
                    if (n[u] == A) {
                        t[u] = w;
                        for (var f = u - 1; 0 <= f && n[f] == R; f--)
                            t[f] = w
                    }
        }(n, r, n.length, t);
        for (var a = 0; a < s.length; s[a] = a,
        a++)
            ;
        h(2, r, s),
        h(1, r, s);
        for (a = 0; a < s.length - 1; a++)
            t[a] === f ? r[a] = l.AN : r[a] === d && (t[a] > L && t[a] < F || t[a] === x || t[a] === B) ? r[a] = l.ON_R : 0 < a && "ل" === n[a - 1] && /\u0622|\u0623|\u0625|\u0627/.test(n[a]) && (r[a - 1] = r[a] = l.R_H,
            a++);
        n[n.length - 1] === l.DOT && (r[n.length - 1] = l.B),
        "‫" === n[0] && (r[0] = l.RLE);
        for (a = 0; a < s.length; a++)
            o[a] = r[s[a]];
        return {
            logicalFromVisual: s,
            bidiLevels: o
        }
    }
    ,
    l.hasBidiCharacters = function(e, t) {
        for (var i = !1, n = 0; n < e.length; n++)
            t[n] = p(e.charAt(n)),
            i || t[n] != d && t[n] != L && t[n] != f || (i = !0);
        return i
    }
    ,
    l.getVisualFromLogicalIdx = function(e, t) {
        for (var i = 0; i < t.logicalFromVisual.length; i++)
            if (t.logicalFromVisual[i] == e)
                return i;
        return 0
    }
}),
define("ace/bidihandler", ["require", "exports", "module", "ace/lib/bidiutil", "ace/lib/lang"], function(e, t, i) {
    "use strict";
    function n(e) {
        this.session = e,
        this.bidiMap = {},
        this.currentRow = null,
        this.bidiUtil = a,
        this.charWidths = [],
        this.EOL = "¬",
        this.showInvisibles = !0,
        this.isRtlDir = !1,
        this.$isRtl = !1,
        this.line = "",
        this.wrapIndent = 0,
        this.EOF = "¶",
        this.RLE = "‫",
        this.contentWidth = 0,
        this.fontMetrics = null,
        this.rtlLineOffset = 0,
        this.wrapOffset = 0,
        this.isMoveLeftOperation = !1,
        this.seenBidi = s.test(e.getValue())
    }
    var a = e("./lib/bidiutil")
      , l = e("./lib/lang")
      , s = /[\u0590-\u05f4\u0600-\u06ff\u0700-\u08ac\u202B]/;
    (function() {
        this.isBidiRow = function(e, t, i) {
            return !!this.seenBidi && (e !== this.currentRow && (this.currentRow = e,
            this.updateRowLine(t, i),
            this.updateBidiMap()),
            this.bidiMap.bidiLevels)
        }
        ,
        this.onChange = function(e) {
            this.seenBidi ? this.currentRow = null : "insert" == e.action && s.test(e.lines.join("\n")) && (this.seenBidi = !0,
            this.currentRow = null)
        }
        ,
        this.getDocumentRow = function() {
            var e, t = 0, i = this.session.$screenRowCache;
            return !i.length || 0 <= (e = this.session.$getRowCacheIndex(i, this.currentRow)) && (t = this.session.$docRowCache[e]),
            t
        }
        ,
        this.getSplitIndex = function() {
            var e = 0
              , t = this.session.$screenRowCache;
            if (t.length)
                for (var i, n = this.session.$getRowCacheIndex(t, this.currentRow); 0 < this.currentRow - e && (i = this.session.$getRowCacheIndex(t, this.currentRow - e - 1)) === n; )
                    n = i,
                    e++;
            else
                e = this.currentRow;
            return e
        }
        ,
        this.updateRowLine = function(e, t) {
            void 0 === e && (e = this.getDocumentRow());
            var i, n = e === this.session.getLength() - 1 ? this.EOF : this.EOL;
            this.wrapIndent = 0,
            this.line = this.session.getLine(e),
            this.isRtlDir = this.$isRtl || this.line.charAt(0) === this.RLE,
            this.session.$useWrapMode ? ((i = this.session.$wrapData[e]) && (void 0 === t && (t = this.getSplitIndex()),
            0 < t && i.length ? (this.wrapIndent = i.indent,
            this.wrapOffset = this.wrapIndent * this.charWidths[a.L],
            this.line = t < i.length ? this.line.substring(i[t - 1], i[t]) : this.line.substring(i[i.length - 1])) : this.line = this.line.substring(0, i[t])),
            t == i.length && (this.line += this.showInvisibles ? n : a.DOT)) : this.line += this.showInvisibles ? n : a.DOT;
            var s, o = this.session, r = 0;
            this.line = this.line.replace(/\t|[\u1100-\u2029, \u202F-\uFFE6]/g, function(e, t) {
                return "\t" === e || o.isFullWidth(e.charCodeAt(0)) ? (s = "\t" === e ? o.getScreenTabSize(t + r) : 2,
                r += s - 1,
                l.stringRepeat(a.DOT, s)) : e
            }),
            this.isRtlDir && (this.fontMetrics.$main.textContent = this.line.charAt(this.line.length - 1) == a.DOT ? this.line.substr(0, this.line.length - 1) : this.line,
            this.rtlLineOffset = this.contentWidth - this.fontMetrics.$main.getBoundingClientRect().width)
        }
        ,
        this.updateBidiMap = function() {
            var e = [];
            a.hasBidiCharacters(this.line, e) || this.isRtlDir ? this.bidiMap = a.doBidiReorder(this.line, e, this.isRtlDir) : this.bidiMap = {}
        }
        ,
        this.markAsDirty = function() {
            this.currentRow = null
        }
        ,
        this.updateCharacterWidths = function(e) {
            var t, i;
            this.characterWidth !== e.$characterSize.width && (this.fontMetrics = e,
            t = this.characterWidth = e.$characterSize.width,
            i = e.$measureCharWidth("ה"),
            this.charWidths[a.L] = this.charWidths[a.EN] = this.charWidths[a.ON_R] = t,
            this.charWidths[a.R] = this.charWidths[a.AN] = i,
            this.charWidths[a.R_H] = .45 * i,
            this.charWidths[a.B] = this.charWidths[a.RLE] = 0,
            this.currentRow = null)
        }
        ,
        this.setShowInvisibles = function(e) {
            this.showInvisibles = e,
            this.currentRow = null
        }
        ,
        this.setEolChar = function(e) {
            this.EOL = e
        }
        ,
        this.setContentWidth = function(e) {
            this.contentWidth = e
        }
        ,
        this.isRtlLine = function(e) {
            return !!this.$isRtl || (null != e ? this.session.getLine(e).charAt(0) == this.RLE : this.isRtlDir)
        }
        ,
        this.setRtlDirection = function(e, t) {
            for (var i = e.getCursorPosition(), n = e.selection.getSelectionAnchor().row; n <= i.row; n++)
                t || e.session.getLine(n).charAt(0) !== e.session.$bidiHandler.RLE ? t && e.session.getLine(n).charAt(0) !== e.session.$bidiHandler.RLE && e.session.doc.insert({
                    column: 0,
                    row: n
                }, e.session.$bidiHandler.RLE) : e.session.doc.removeInLine(n, 0, 1)
        }
        ,
        this.getPosLeft = function(e) {
            e -= this.wrapIndent;
            var t = this.line.charAt(0) === this.RLE ? 1 : 0
              , i = t < e ? this.session.getOverwrite() ? e : e - 1 : t
              , n = a.getVisualFromLogicalIdx(i, this.bidiMap)
              , s = this.bidiMap.bidiLevels
              , o = 0;
            !this.session.getOverwrite() && e <= t && s[n] % 2 != 0 && n++;
            for (var r = 0; r < n; r++)
                o += this.charWidths[s[r]];
            return !this.session.getOverwrite() && t < e && s[n] % 2 == 0 && (o += this.charWidths[s[n]]),
            this.wrapIndent && (o += this.isRtlDir ? -1 * this.wrapOffset : this.wrapOffset),
            this.isRtlDir && (o += this.rtlLineOffset),
            o
        }
        ,
        this.getSelections = function(e, t) {
            var i, n = this.bidiMap, s = n.bidiLevels, o = [], r = 0, a = Math.min(e, t) - this.wrapIndent, l = Math.max(e, t) - this.wrapIndent, h = !1, c = !1, u = 0;
            this.wrapIndent && (r += this.isRtlDir ? -1 * this.wrapOffset : this.wrapOffset);
            for (var d, g = 0; g < s.length; g++)
                d = n.logicalFromVisual[g],
                i = s[g],
                (h = a <= d && d < l) && !c ? u = r : !h && c && o.push({
                    left: u,
                    width: r - u
                }),
                r += this.charWidths[i],
                c = h;
            if (h && g === s.length && o.push({
                left: u,
                width: r - u
            }),
            this.isRtlDir)
                for (var f = 0; f < o.length; f++)
                    o[f].left += this.rtlLineOffset;
            return o
        }
        ,
        this.offsetToCol = function(e) {
            this.isRtlDir && (e -= this.rtlLineOffset);
            var t = 0
              , e = Math.max(e, 0)
              , i = 0
              , n = 0
              , s = this.bidiMap.bidiLevels
              , o = this.charWidths[s[n]];
            for (this.wrapIndent && (e -= this.isRtlDir ? -1 * this.wrapOffset : this.wrapOffset); i + o / 2 < e; ) {
                if (i += o,
                n === s.length - 1) {
                    o = 0;
                    break
                }
                o = this.charWidths[s[++n]]
            }
            return 0 === (t = 0 < n && s[n - 1] % 2 != 0 && s[n] % 2 == 0 ? (e < i && n--,
            this.bidiMap.logicalFromVisual[n]) : 0 < n && s[n - 1] % 2 == 0 && s[n] % 2 != 0 ? 1 + (i < e ? this.bidiMap.logicalFromVisual[n] : this.bidiMap.logicalFromVisual[n - 1]) : this.isRtlDir && n === s.length - 1 && 0 === o && s[n - 1] % 2 == 0 || !this.isRtlDir && 0 === n && s[n] % 2 != 0 ? 1 + this.bidiMap.logicalFromVisual[n] : (0 < n && s[n - 1] % 2 != 0 && 0 !== o && n--,
            this.bidiMap.logicalFromVisual[n])) && this.isRtlDir && t++,
            t + this.wrapIndent
        }
    }
    ).call(n.prototype),
    t.BidiHandler = n
}),
define("ace/selection", ["require", "exports", "module", "ace/lib/oop", "ace/lib/lang", "ace/lib/event_emitter", "ace/range"], function(e, t, i) {
    "use strict";
    function n(e) {
        this.session = e,
        this.doc = e.getDocument(),
        this.clearSelection(),
        this.cursor = this.lead = this.doc.createAnchor(0, 0),
        this.anchor = this.doc.createAnchor(0, 0),
        this.$silent = !1;
        var t = this;
        this.cursor.on("change", function(e) {
            t.$cursorChanged = !0,
            t.$silent || t._emit("changeCursor"),
            t.$isEmpty || t.$silent || t._emit("changeSelection"),
            t.$keepDesiredColumnOnChange || e.old.column == e.value.column || (t.$desiredColumn = null)
        }),
        this.anchor.on("change", function() {
            t.$anchorChanged = !0,
            t.$isEmpty || t.$silent || t._emit("changeSelection")
        })
    }
    var s = e("./lib/oop")
      , r = e("./lib/lang")
      , o = e("./lib/event_emitter").EventEmitter
      , a = e("./range").Range;
    (function() {
        s.implement(this, o),
        this.isEmpty = function() {
            return this.$isEmpty || this.anchor.row == this.lead.row && this.anchor.column == this.lead.column
        }
        ,
        this.isMultiLine = function() {
            return !this.$isEmpty && this.anchor.row != this.cursor.row
        }
        ,
        this.getCursor = function() {
            return this.lead.getPosition()
        }
        ,
        this.setSelectionAnchor = function(e, t) {
            this.$isEmpty = !1,
            this.anchor.setPosition(e, t)
        }
        ,
        this.getAnchor = this.getSelectionAnchor = function() {
            return this.$isEmpty ? this.getSelectionLead() : this.anchor.getPosition()
        }
        ,
        this.getSelectionLead = function() {
            return this.lead.getPosition()
        }
        ,
        this.isBackwards = function() {
            var e = this.anchor
              , t = this.lead;
            return e.row > t.row || e.row == t.row && e.column > t.column
        }
        ,
        this.getRange = function() {
            var e = this.anchor
              , t = this.lead;
            return this.$isEmpty ? a.fromPoints(t, t) : this.isBackwards() ? a.fromPoints(t, e) : a.fromPoints(e, t)
        }
        ,
        this.clearSelection = function() {
            this.$isEmpty || (this.$isEmpty = !0,
            this._emit("changeSelection"))
        }
        ,
        this.selectAll = function() {
            this.$setSelection(0, 0, Number.MAX_VALUE, Number.MAX_VALUE)
        }
        ,
        this.setRange = this.setSelectionRange = function(e, t) {
            var i = t ? e.end : e.start
              , n = t ? e.start : e.end;
            this.$setSelection(i.row, i.column, n.row, n.column)
        }
        ,
        this.$setSelection = function(e, t, i, n) {
            var s, o;
            this.$silent || (s = this.$isEmpty,
            o = this.inMultiSelectMode,
            this.$silent = !0,
            this.$cursorChanged = this.$anchorChanged = !1,
            this.anchor.setPosition(e, t),
            this.cursor.setPosition(i, n),
            this.$isEmpty = !a.comparePoints(this.anchor, this.cursor),
            this.$silent = !1,
            this.$cursorChanged && this._emit("changeCursor"),
            (this.$cursorChanged || this.$anchorChanged || s != this.$isEmpty || o) && this._emit("changeSelection"))
        }
        ,
        this.$moveSelection = function(e) {
            var t = this.lead;
            this.$isEmpty && this.setSelectionAnchor(t.row, t.column),
            e.call(this)
        }
        ,
        this.selectTo = function(e, t) {
            this.$moveSelection(function() {
                this.moveCursorTo(e, t)
            })
        }
        ,
        this.selectToPosition = function(e) {
            this.$moveSelection(function() {
                this.moveCursorToPosition(e)
            })
        }
        ,
        this.moveTo = function(e, t) {
            this.clearSelection(),
            this.moveCursorTo(e, t)
        }
        ,
        this.moveToPosition = function(e) {
            this.clearSelection(),
            this.moveCursorToPosition(e)
        }
        ,
        this.selectUp = function() {
            this.$moveSelection(this.moveCursorUp)
        }
        ,
        this.selectDown = function() {
            this.$moveSelection(this.moveCursorDown)
        }
        ,
        this.selectRight = function() {
            this.$moveSelection(this.moveCursorRight)
        }
        ,
        this.selectLeft = function() {
            this.$moveSelection(this.moveCursorLeft)
        }
        ,
        this.selectLineStart = function() {
            this.$moveSelection(this.moveCursorLineStart)
        }
        ,
        this.selectLineEnd = function() {
            this.$moveSelection(this.moveCursorLineEnd)
        }
        ,
        this.selectFileEnd = function() {
            this.$moveSelection(this.moveCursorFileEnd)
        }
        ,
        this.selectFileStart = function() {
            this.$moveSelection(this.moveCursorFileStart)
        }
        ,
        this.selectWordRight = function() {
            this.$moveSelection(this.moveCursorWordRight)
        }
        ,
        this.selectWordLeft = function() {
            this.$moveSelection(this.moveCursorWordLeft)
        }
        ,
        this.getWordRange = function(e, t) {
            var i;
            return void 0 === t && (e = (i = e || this.lead).row,
            t = i.column),
            this.session.getWordRange(e, t)
        }
        ,
        this.selectWord = function() {
            this.setSelectionRange(this.getWordRange())
        }
        ,
        this.selectAWord = function() {
            var e = this.getCursor()
              , t = this.session.getAWordRange(e.row, e.column);
            this.setSelectionRange(t)
        }
        ,
        this.getLineRange = function(e, t) {
            var i = "number" == typeof e ? e : this.lead.row
              , n = this.session.getFoldLine(i)
              , s = n ? (i = n.start.row,
            n.end.row) : i;
            return !0 === t ? new a(i,0,s,this.session.getLine(s).length) : new a(i,0,s + 1,0)
        }
        ,
        this.selectLine = function() {
            this.setSelectionRange(this.getLineRange())
        }
        ,
        this.moveCursorUp = function() {
            this.moveCursorBy(-1, 0)
        }
        ,
        this.moveCursorDown = function() {
            this.moveCursorBy(1, 0)
        }
        ,
        this.wouldMoveIntoSoftTab = function(e, t, i) {
            var n = e.column
              , s = e.column + t;
            return i < 0 && (n = e.column - t,
            s = e.column),
            this.session.isTabStop(e) && this.doc.getLine(e.row).slice(n, s).split(" ").length - 1 == t
        }
        ,
        this.moveCursorLeft = function() {
            var e, t, i = this.lead.getPosition();
            (e = this.session.getFoldAt(i.row, i.column, -1)) ? this.moveCursorTo(e.start.row, e.start.column) : 0 === i.column ? 0 < i.row && this.moveCursorTo(i.row - 1, this.doc.getLine(i.row - 1).length) : (t = this.session.getTabSize(),
            this.wouldMoveIntoSoftTab(i, t, -1) && !this.session.getNavigateWithinSoftTabs() ? this.moveCursorBy(0, -t) : this.moveCursorBy(0, -1))
        }
        ,
        this.moveCursorRight = function() {
            var e, t, i = this.lead.getPosition();
            (e = this.session.getFoldAt(i.row, i.column, 1)) ? this.moveCursorTo(e.end.row, e.end.column) : this.lead.column == this.doc.getLine(this.lead.row).length ? this.lead.row < this.doc.getLength() - 1 && this.moveCursorTo(this.lead.row + 1, 0) : (t = this.session.getTabSize(),
            i = this.lead,
            this.wouldMoveIntoSoftTab(i, t, 1) && !this.session.getNavigateWithinSoftTabs() ? this.moveCursorBy(0, t) : this.moveCursorBy(0, 1))
        }
        ,
        this.moveCursorLineStart = function() {
            var e = this.lead.row
              , t = this.lead.column
              , i = this.session.documentToScreenRow(e, t)
              , n = this.session.screenToDocumentPosition(i, 0)
              , s = this.session.getDisplayLine(e, null, n.row, n.column).match(/^\s*/);
            s[0].length == t || this.session.$useEmacsStyleLineStart || (n.column += s[0].length),
            this.moveCursorToPosition(n)
        }
        ,
        this.moveCursorLineEnd = function() {
            var e, t, i = this.lead, n = this.session.getDocumentLastRowColumnPosition(i.row, i.column);
            this.lead.column == n.column && (e = this.session.getLine(n.row),
            n.column != e.length || 0 < (t = e.search(/\s+$/)) && (n.column = t)),
            this.moveCursorTo(n.row, n.column)
        }
        ,
        this.moveCursorFileEnd = function() {
            var e = this.doc.getLength() - 1
              , t = this.doc.getLine(e).length;
            this.moveCursorTo(e, t)
        }
        ,
        this.moveCursorFileStart = function() {
            this.moveCursorTo(0, 0)
        }
        ,
        this.moveCursorLongWordRight = function() {
            var e = this.lead.row
              , t = this.lead.column
              , i = this.doc.getLine(e)
              , n = i.substring(t);
            this.session.nonTokenRe.lastIndex = 0,
            this.session.tokenRe.lastIndex = 0;
            var s = this.session.getFoldAt(e, t, 1);
            if (s)
                this.moveCursorTo(s.end.row, s.end.column);
            else {
                if (this.session.nonTokenRe.exec(n) && (t += this.session.nonTokenRe.lastIndex,
                this.session.nonTokenRe.lastIndex = 0,
                n = i.substring(t)),
                t >= i.length)
                    return this.moveCursorTo(e, i.length),
                    this.moveCursorRight(),
                    void (e < this.doc.getLength() - 1 && this.moveCursorWordRight());
                this.session.tokenRe.exec(n) && (t += this.session.tokenRe.lastIndex,
                this.session.tokenRe.lastIndex = 0),
                this.moveCursorTo(e, t)
            }
        }
        ,
        this.moveCursorLongWordLeft = function() {
            var e, t = this.lead.row, i = this.lead.column;
            if (e = this.session.getFoldAt(t, i, -1))
                this.moveCursorTo(e.start.row, e.start.column);
            else {
                var n = this.session.getFoldStringAt(t, i, -1);
                null == n && (n = this.doc.getLine(t).substring(0, i));
                var s = r.stringReverse(n);
                if (this.session.nonTokenRe.lastIndex = 0,
                this.session.tokenRe.lastIndex = 0,
                this.session.nonTokenRe.exec(s) && (i -= this.session.nonTokenRe.lastIndex,
                s = s.slice(this.session.nonTokenRe.lastIndex),
                this.session.nonTokenRe.lastIndex = 0),
                i <= 0)
                    return this.moveCursorTo(t, 0),
                    this.moveCursorLeft(),
                    void (0 < t && this.moveCursorWordLeft());
                this.session.tokenRe.exec(s) && (i -= this.session.tokenRe.lastIndex,
                this.session.tokenRe.lastIndex = 0),
                this.moveCursorTo(t, i)
            }
        }
        ,
        this.$shortWordEndIndex = function(e) {
            var t, i = 0, n = /\s/, s = this.session.tokenRe;
            if (s.lastIndex = 0,
            this.session.tokenRe.exec(e))
                i = this.session.tokenRe.lastIndex;
            else {
                for (; (t = e[i]) && n.test(t); )
                    i++;
                if (i < 1)
                    for (s.lastIndex = 0; (t = e[i]) && !s.test(t); )
                        if (s.lastIndex = 0,
                        i++,
                        n.test(t)) {
                            if (2 < i) {
                                i--;
                                break
                            }
                            for (; (t = e[i]) && n.test(t); )
                                i++;
                            if (2 < i)
                                break
                        }
            }
            return s.lastIndex = 0,
            i
        }
        ,
        this.moveCursorShortWordRight = function() {
            var e = this.lead.row
              , t = this.lead.column
              , i = this.doc.getLine(e)
              , n = i.substring(t)
              , s = this.session.getFoldAt(e, t, 1);
            if (s)
                return this.moveCursorTo(s.end.row, s.end.column);
            if (t == i.length) {
                for (var o = this.doc.getLength(); e++,
                n = this.doc.getLine(e),
                e < o && /^\s*$/.test(n); )
                    ;
                /^\s+/.test(n) || (n = ""),
                t = 0
            }
            var r = this.$shortWordEndIndex(n);
            this.moveCursorTo(e, t + r)
        }
        ,
        this.moveCursorShortWordLeft = function() {
            var e, t = this.lead.row, i = this.lead.column;
            if (e = this.session.getFoldAt(t, i, -1))
                return this.moveCursorTo(e.start.row, e.start.column);
            var n = this.session.getLine(t).substring(0, i);
            if (0 === i) {
                for (; t--,
                n = this.doc.getLine(t),
                0 < t && /^\s*$/.test(n); )
                    ;
                i = n.length,
                /\s+$/.test(n) || (n = "")
            }
            var s = r.stringReverse(n)
              , o = this.$shortWordEndIndex(s);
            return this.moveCursorTo(t, i - o)
        }
        ,
        this.moveCursorWordRight = function() {
            this.session.$selectLongWords ? this.moveCursorLongWordRight() : this.moveCursorShortWordRight()
        }
        ,
        this.moveCursorWordLeft = function() {
            this.session.$selectLongWords ? this.moveCursorLongWordLeft() : this.moveCursorShortWordLeft()
        }
        ,
        this.moveCursorBy = function(e, t) {
            var i, n, s = this.session.documentToScreenPosition(this.lead.row, this.lead.column);
            0 === t && (0 !== e && (this.session.$bidiHandler.isBidiRow(s.row, this.lead.row) ? (i = this.session.$bidiHandler.getPosLeft(s.column),
            s.column = Math.round(i / this.session.$bidiHandler.charWidths[0])) : i = s.column * this.session.$bidiHandler.charWidths[0]),
            this.$desiredColumn ? s.column = this.$desiredColumn : this.$desiredColumn = s.column),
            0 != e && this.session.lineWidgets && this.session.lineWidgets[this.lead.row] && (n = this.session.lineWidgets[this.lead.row],
            e < 0 ? e -= n.rowsAbove || 0 : 0 < e && (e += n.rowCount - (n.rowsAbove || 0)));
            var o = this.session.screenToDocumentPosition(s.row + e, s.column, i);
            0 !== e && 0 === t && o.row === this.lead.row && (o.column,
            this.lead.column),
            this.moveCursorTo(o.row, o.column + t, 0 === t)
        }
        ,
        this.moveCursorToPosition = function(e) {
            this.moveCursorTo(e.row, e.column)
        }
        ,
        this.moveCursorTo = function(e, t, i) {
            var n = this.session.getFoldAt(e, t, 1);
            n && (e = n.start.row,
            t = n.start.column),
            this.$keepDesiredColumnOnChange = !0;
            var s = this.session.getLine(e);
            /[\uDC00-\uDFFF]/.test(s.charAt(t)) && s.charAt(t - 1) && (this.lead.row == e && this.lead.column == t + 1 ? --t : t += 1),
            this.lead.setPosition(e, t),
            this.$keepDesiredColumnOnChange = !1,
            i || (this.$desiredColumn = null)
        }
        ,
        this.moveCursorToScreen = function(e, t, i) {
            var n = this.session.screenToDocumentPosition(e, t);
            this.moveCursorTo(n.row, n.column, i)
        }
        ,
        this.detach = function() {
            this.lead.detach(),
            this.anchor.detach(),
            this.session = this.doc = null
        }
        ,
        this.fromOrientedRange = function(e) {
            this.setSelectionRange(e, e.cursor == e.start),
            this.$desiredColumn = e.desiredColumn || this.$desiredColumn
        }
        ,
        this.toOrientedRange = function(e) {
            var t = this.getRange();
            return e ? (e.start.column = t.start.column,
            e.start.row = t.start.row,
            e.end.column = t.end.column,
            e.end.row = t.end.row) : e = t,
            e.cursor = this.isBackwards() ? e.start : e.end,
            e.desiredColumn = this.$desiredColumn,
            e
        }
        ,
        this.getRangeOfMovements = function(e) {
            var t = this.getCursor();
            try {
                e(this);
                var i = this.getCursor();
                return a.fromPoints(t, i)
            } catch (e) {
                return a.fromPoints(t, t)
            } finally {
                this.moveCursorToPosition(t)
            }
        }
        ,
        this.toJSON = function() {
            var e;
            return this.rangeCount ? e = this.ranges.map(function(e) {
                var t = e.clone();
                return t.isBackwards = e.cursor == e.start,
                t
            }) : (e = this.getRange()).isBackwards = this.isBackwards(),
            e
        }
        ,
        this.fromJSON = function(e) {
            if (null == e.start) {
                if (this.rangeList && 1 < e.length) {
                    this.toSingleRange(e[0]);
                    for (var t = e.length; t--; ) {
                        var i = a.fromPoints(e[t].start, e[t].end);
                        e[t].isBackwards && (i.cursor = i.start),
                        this.addRange(i, !0)
                    }
                    return
                }
                e = e[0]
            }
            this.rangeList && this.toSingleRange(e),
            this.setSelectionRange(e, e.isBackwards)
        }
        ,
        this.isEqual = function(e) {
            if ((e.length || this.rangeCount) && e.length != this.rangeCount)
                return !1;
            if (!e.length || !this.ranges)
                return this.getRange().isEqual(e);
            for (var t = this.ranges.length; t--; )
                if (!this.ranges[t].isEqual(e[t]))
                    return !1;
            return !0
        }
    }
    ).call(n.prototype),
    t.Selection = n
}),
define("ace/tokenizer", ["require", "exports", "module", "ace/config"], function(e, t, i) {
    "use strict";
    function n(e) {
        for (var t in this.states = e,
        this.regExps = {},
        this.matchMappings = {},
        this.states) {
            for (var i = this.states[t], n = [], s = 0, o = this.matchMappings[t] = {
                defaultToken: "text"
            }, r = "g", a = [], l = 0; l < i.length; l++) {
                var h, c, u = i[l];
                u.defaultToken && (o.defaultToken = u.defaultToken),
                u.caseInsensitive && (r = "gi"),
                null != u.regex && (u.regex instanceof RegExp && (u.regex = u.regex.toString().slice(1, -1)),
                h = u.regex,
                c = new RegExp("(?:(" + h + ")|(.))").exec("a").length - 2,
                Array.isArray(u.token) ? 1 == u.token.length || 1 == c ? u.token = u.token[0] : c - 1 != u.token.length ? (this.reportError("number of classes and regexp groups doesn't match", {
                    rule: u,
                    groupCount: c - 1
                }),
                u.token = u.token[0]) : (u.tokenArray = u.token,
                u.token = null,
                u.onMatch = this.$arrayTokens) : "function" != typeof u.token || u.onMatch || (u.onMatch = 1 < c ? this.$applyToken : u.token),
                1 < c && (h = /\\\d/.test(u.regex) ? u.regex.replace(/\\([0-9]+)/g, function(e, t) {
                    return "\\" + (parseInt(t, 10) + s + 1)
                }) : (c = 1,
                this.removeCapturingGroups(u.regex)),
                u.splitRegex || "string" == typeof u.token || a.push(u)),
                o[s] = l,
                s += c,
                n.push(h),
                u.onMatch || (u.onMatch = null))
            }
            n.length || (o[0] = 0,
            n.push("$")),
            a.forEach(function(e) {
                e.splitRegex = this.createSplitterRegexp(e.regex, r)
            }, this),
            this.regExps[t] = new RegExp("(" + n.join(")|(") + ")|($)",r)
        }
    }
    var s = e("./config")
      , v = 2e3;
    (function() {
        this.$setMaxTokenCount = function(e) {
            v = 0 | e
        }
        ,
        this.$applyToken = function(e) {
            var t = this.splitRegex.exec(e).slice(1)
              , i = this.token.apply(this, t);
            if ("string" == typeof i)
                return [{
                    type: i,
                    value: e
                }];
            for (var n = [], s = 0, o = i.length; s < o; s++)
                t[s] && (n[n.length] = {
                    type: i[s],
                    value: t[s]
                });
            return n
        }
        ,
        this.$arrayTokens = function(e) {
            if (!e)
                return [];
            var t = this.splitRegex.exec(e);
            if (!t)
                return "text";
            for (var i = [], n = this.tokenArray, s = 0, o = n.length; s < o; s++)
                t[s + 1] && (i[i.length] = {
                    type: n[s],
                    value: t[s + 1]
                });
            return i
        }
        ,
        this.removeCapturingGroups = function(e) {
            return e.replace(/\\.|\[(?:\\.|[^\\\]])*|\(\?[:=!]|(\()/g, function(e, t) {
                return t ? "(?:" : e
            })
        }
        ,
        this.createSplitterRegexp = function(e, t) {
            var r, a, l;
            return -1 != e.indexOf("(?=") && (r = 0,
            a = !1,
            l = {},
            e.replace(/(\\.)|(\((?:\?[=!])?)|(\))|([\[\]])/g, function(e, t, i, n, s, o) {
                return a ? a = "]" != s : s ? a = !0 : n ? (r == l.stack && (l.end = o + 1,
                l.stack = -1),
                r--) : i && (r++,
                1 != i.length && (l.stack = r,
                l.start = o)),
                e
            }),
            null != l.end && /^\)*$/.test(e.substr(l.end)) && (e = e.substring(0, l.start) + e.substr(l.end))),
            "^" != e.charAt(0) && (e = "^" + e),
            "$" != e.charAt(e.length - 1) && (e += "$"),
            new RegExp(e,(t || "").replace("g", ""))
        }
        ,
        this.getLineTokens = function(e, t) {
            var i;
            t && "string" != typeof t ? "#tmp" === (t = (i = t.slice(0))[0]) && (i.shift(),
            t = i.shift()) : i = [];
            var n = t || "start"
              , s = this.states[n];
            s || (n = "start",
            s = this.states[n]);
            for (var o, r = this.matchMappings[n], a = this.regExps[n], l = [], h = a.lastIndex = 0, c = 0, u = {
                type: null,
                value: ""
            }; o = a.exec(e); ) {
                var d, g = r.defaultToken, f = null, m = o[0], p = a.lastIndex;
                p - m.length > h && (d = e.substring(h, p - m.length),
                u.type == g ? u.value += d : (u.type && l.push(u),
                u = {
                    type: g,
                    value: d
                }));
                for (var w = 0; w < o.length - 2; w++)
                    if (void 0 !== o[w + 1]) {
                        g = (f = s[r[w]]).onMatch ? f.onMatch(m, n, i, e) : f.token,
                        f.next && (n = "string" == typeof f.next ? f.next : f.next(n, i),
                        (s = this.states[n]) || (this.reportError("state doesn't exist", n),
                        n = "start",
                        s = this.states[n]),
                        r = this.matchMappings[n],
                        h = p,
                        (a = this.regExps[n]).lastIndex = p),
                        f.consumeLineEnd && (h = p);
                        break
                    }
                if (m)
                    if ("string" == typeof g)
                        f && !1 === f.merge || u.type !== g ? (u.type && l.push(u),
                        u = {
                            type: g,
                            value: m
                        }) : u.value += m;
                    else if (g) {
                        u.type && l.push(u),
                        u = {
                            type: null,
                            value: ""
                        };
                        for (w = 0; w < g.length; w++)
                            l.push(g[w])
                    }
                if (h == e.length)
                    break;
                if (h = p,
                c++ > v) {
                    for (c > 2 * e.length && this.reportError("infinite loop with in ace tokenizer", {
                        startState: t,
                        line: e
                    }); h < e.length; )
                        u.type && l.push(u),
                        u = {
                            value: e.substring(h, h += 500),
                            type: "overflow"
                        };
                    n = "start",
                    i = [];
                    break
                }
            }
            return u.type && l.push(u),
            1 < i.length && i[0] !== n && i.unshift("#tmp", n),
            {
                tokens: l,
                state: i.length ? i : n
            }
        }
        ,
        this.reportError = s.reportError
    }
    ).call(n.prototype),
    t.Tokenizer = n
}),
define("ace/mode/text_highlight_rules", ["require", "exports", "module", "ace/lib/lang"], function(e, t, i) {
    "use strict";
    function n() {
        this.$rules = {
            start: [{
                token: "empty_line",
                regex: "^$"
            }, {
                defaultToken: "text"
            }]
        }
    }
    var h = e("../lib/lang");
    (function() {
        this.addRules = function(e, t) {
            if (t)
                for (var i in e) {
                    for (var n = e[i], s = 0; s < n.length; s++) {
                        var o = n[s];
                        (o.next || o.onMatch) && ("string" == typeof o.next && 0 !== o.next.indexOf(t) && (o.next = t + o.next),
                        o.nextState && 0 !== o.nextState.indexOf(t) && (o.nextState = t + o.nextState))
                    }
                    this.$rules[t + i] = n
                }
            else
                for (var i in e)
                    this.$rules[i] = e[i]
        }
        ,
        this.getRules = function() {
            return this.$rules
        }
        ,
        this.embedRules = function(e, t, i, n, s) {
            var o = "function" == typeof e ? (new e).getRules() : e;
            if (n)
                for (var r = 0; r < n.length; r++)
                    n[r] = t + n[r];
            else
                for (var a in n = [],
                o)
                    n.push(t + a);
            if (this.addRules(o, t),
            i)
                for (var l = Array.prototype[s ? "push" : "unshift"], r = 0; r < n.length; r++)
                    l.apply(this.$rules[n[r]], h.deepCopy(i));
            this.$embeds || (this.$embeds = []),
            this.$embeds.push(t)
        }
        ,
        this.getEmbeds = function() {
            return this.$embeds
        }
        ;
        function g(e, t) {
            return "start" == e && !t.length || t.unshift(this.nextState, e),
            this.nextState
        }
        function f(e, t) {
            return t.shift(),
            t.shift() || "start"
        }
        this.normalizeRules = function() {
            var u = 0
              , d = this.$rules;
            Object.keys(d).forEach(function e(t) {
                var i = d[t];
                i.processed = !0;
                for (var n = 0; n < i.length; n++) {
                    var s = i[n]
                      , o = null;
                    Array.isArray(s) && (o = s,
                    s = {}),
                    !s.regex && s.start && (s.regex = s.start,
                    s.next || (s.next = []),
                    s.next.push({
                        defaultToken: s.token
                    }, {
                        token: s.token + ".end",
                        regex: s.end || s.start,
                        next: "pop"
                    }),
                    s.token = s.token + ".start",
                    s.push = !0);
                    var r, a = s.next || s.push;
                    if (a && Array.isArray(a) ? ((r = s.stateName) || ("string" != typeof (r = s.token) && (r = r[0] || ""),
                    d[r] && (r += u++)),
                    d[r] = a,
                    e(s.next = r)) : "pop" == a && (s.next = f),
                    s.push && (s.nextState = s.next || s.push,
                    s.next = g,
                    delete s.push),
                    s.rules)
                        for (var l in s.rules)
                            d[l] ? d[l].push && d[l].push.apply(d[l], s.rules[l]) : d[l] = s.rules[l];
                    var h, c = "string" == typeof s ? s : s.include;
                    c && (o = Array.isArray(c) ? c.map(function(e) {
                        return d[e]
                    }) : d[c]),
                    o && (h = [n, 1].concat(o),
                    s.noEscape && (h = h.filter(function(e) {
                        return !e.next
                    })),
                    i.splice.apply(i, h),
                    n--),
                    s.keywordMap && (s.token = this.createKeywordMapper(s.keywordMap, s.defaultToken || "text", s.caseInsensitive),
                    delete s.defaultToken)
                }
            }, this)
        }
        ,
        this.createKeywordMapper = function(s, t, o, r) {
            var a = Object.create(null);
            return this.$keywordList = [],
            Object.keys(s).forEach(function(e) {
                for (var t = s[e].split(r || "|"), i = t.length; i--; ) {
                    var n = t[i];
                    this.$keywordList.push(n),
                    o && (n = n.toLowerCase()),
                    a[n] = e
                }
            }, this),
            s = null,
            o ? function(e) {
                return a[e.toLowerCase()] || t
            }
            : function(e) {
                return a[e] || t
            }
        }
        ,
        this.getKeywords = function() {
            return this.$keywords
        }
    }
    ).call(n.prototype),
    t.TextHighlightRules = n
}),
define("ace/mode/behaviour", ["require", "exports", "module"], function(e, t, i) {
    "use strict";
    function n() {
        this.$behaviours = {}
    }
    (function() {
        this.add = function(e, t, i) {
            switch (void 0) {
            case this.$behaviours:
                this.$behaviours = {};
            case this.$behaviours[e]:
                this.$behaviours[e] = {}
            }
            this.$behaviours[e][t] = i
        }
        ,
        this.addBehaviours = function(e) {
            for (var t in e)
                for (var i in e[t])
                    this.add(t, i, e[t][i])
        }
        ,
        this.remove = function(e) {
            this.$behaviours && this.$behaviours[e] && delete this.$behaviours[e]
        }
        ,
        this.inherit = function(e, t) {
            var i;
            i = "function" == typeof e ? (new e).getBehaviours(t) : e.getBehaviours(t),
            this.addBehaviours(i)
        }
        ,
        this.getBehaviours = function(e) {
            if (!e)
                return this.$behaviours;
            for (var t = {}, i = 0; i < e.length; i++)
                this.$behaviours[e[i]] && (t[e[i]] = this.$behaviours[e[i]]);
            return t
        }
    }
    ).call(n.prototype),
    t.Behaviour = n
}),
define("ace/token_iterator", ["require", "exports", "module", "ace/range"], function(e, t, i) {
    "use strict";
    function n(e, t, i) {
        this.$session = e,
        this.$row = t,
        this.$rowTokens = e.getTokens(t);
        var n = e.getTokenAt(t, i);
        this.$tokenIndex = n ? n.index : -1
    }
    var s = e("./range").Range;
    (function() {
        this.stepBackward = function() {
            for (--this.$tokenIndex; this.$tokenIndex < 0; ) {
                if (--this.$row,
                this.$row < 0)
                    return this.$row = 0,
                    null;
                this.$rowTokens = this.$session.getTokens(this.$row),
                this.$tokenIndex = this.$rowTokens.length - 1
            }
            return this.$rowTokens[this.$tokenIndex]
        }
        ,
        this.stepForward = function() {
            var e;
            for (this.$tokenIndex += 1; this.$tokenIndex >= this.$rowTokens.length; ) {
                if (this.$row += 1,
                e = e || this.$session.getLength(),
                this.$row >= e)
                    return this.$row = e - 1,
                    null;
                this.$rowTokens = this.$session.getTokens(this.$row),
                this.$tokenIndex = 0
            }
            return this.$rowTokens[this.$tokenIndex]
        }
        ,
        this.getCurrentToken = function() {
            return this.$rowTokens[this.$tokenIndex]
        }
        ,
        this.getCurrentTokenRow = function() {
            return this.$row
        }
        ,
        this.getCurrentTokenColumn = function() {
            var e = this.$rowTokens
              , t = this.$tokenIndex
              , i = e[t].start;
            if (void 0 !== i)
                return i;
            for (i = 0; 0 < t; )
                i += e[--t].value.length;
            return i
        }
        ,
        this.getCurrentTokenPosition = function() {
            return {
                row: this.$row,
                column: this.getCurrentTokenColumn()
            }
        }
        ,
        this.getCurrentTokenRange = function() {
            var e = this.$rowTokens[this.$tokenIndex]
              , t = this.getCurrentTokenColumn();
            return new s(this.$row,t,this.$row,t + e.value.length)
        }
    }
    ).call(n.prototype),
    t.TokenIterator = n
}),
define("ace/mode/behaviour/cstyle", ["require", "exports", "module", "ace/lib/oop", "ace/mode/behaviour", "ace/token_iterator", "ace/lib/lang"], function(e, t, i) {
    "use strict";
    function C(e) {
        var t = -1;
        if (e.multiSelect && (t = e.selection.index,
        l.rangeCount != e.multiSelect.rangeCount && (l = {
            rangeCount: e.multiSelect.rangeCount
        })),
        l[t])
            return f = l[t];
        f = l[t] = {
            autoInsertedBrackets: 0,
            autoInsertedRow: -1,
            autoInsertedLineEnd: "",
            maybeInsertedBrackets: 0,
            maybeInsertedRow: -1,
            maybeInsertedLineStart: "",
            maybeInsertedLineEnd: ""
        }
    }
    function S(e, t, i, n) {
        var s = e.end.row - e.start.row;
        return {
            text: i + t + n,
            selection: [0, e.start.column + 1, s, e.end.column + (s ? 0 : 1)]
        }
    }
    var f, n = e("../../lib/oop"), s = e("../behaviour").Behaviour, o = e("../../token_iterator").TokenIterator, m = e("../../lib/lang"), r = ["text", "paren.rparen", "rparen", "paren", "punctuation.operator"], a = ["text", "paren.rparen", "rparen", "paren", "punctuation.operator", "comment"], l = {}, x = {
        '"': '"',
        "'": "'"
    }, p = function(g) {
        this.add("braces", "insertion", function(e, t, i, n, s) {
            var o = i.getCursorPosition()
              , r = n.doc.getLine(o.row);
            if ("{" == s) {
                C(i);
                var a = i.getSelectionRange()
                  , l = n.doc.getTextRange(a);
                if ("" !== l && "{" !== l && i.getWrapBehavioursEnabled())
                    return S(a, l, "{", "}");
                if (p.isSaneInsertion(i, n))
                    return /[\]\}\)]/.test(r[o.column]) || i.inMultiSelectMode || g && g.braces ? (p.recordAutoInsert(i, n, "}"),
                    {
                        text: "{}",
                        selection: [1, 1]
                    }) : (p.recordMaybeInsert(i, n, "{"),
                    {
                        text: "{",
                        selection: [1, 1]
                    })
            } else if ("}" == s) {
                if (C(i),
                "}" == r.substring(o.column, o.column + 1))
                    if (null !== n.$findOpeningBracket("}", {
                        column: o.column + 1,
                        row: o.row
                    }) && p.isAutoInsertedClosing(o, r, s))
                        return p.popAutoInsertedClosing(),
                        {
                            text: "",
                            selection: [1, 1]
                        }
            } else {
                if ("\n" == s || "\r\n" == s) {
                    C(i);
                    var h = "";
                    if (p.isMaybeInsertedClosing(o, r) && (h = m.stringRepeat("}", f.maybeInsertedBrackets),
                    p.clearMaybeInsertedClosing()),
                    "}" === r.substring(o.column, o.column + 1)) {
                        var c = n.findMatchingBracket({
                            row: o.row,
                            column: o.column + 1
                        }, "}");
                        if (!c)
                            return null;
                        var u = this.$getIndent(n.getLine(c.row))
                    } else {
                        if (!h)
                            return void p.clearMaybeInsertedClosing();
                        u = this.$getIndent(r)
                    }
                    var d = u + n.getTabString();
                    return {
                        text: "\n" + d + "\n" + u + h,
                        selection: [1, d.length, 1, d.length]
                    }
                }
                p.clearMaybeInsertedClosing()
            }
        }),
        this.add("braces", "deletion", function(e, t, i, n, s) {
            var o = n.doc.getTextRange(s);
            if (!s.isMultiLine() && "{" == o) {
                if (C(i),
                "}" == n.doc.getLine(s.start.row).substring(s.end.column, s.end.column + 1))
                    return s.end.column++,
                    s;
                f.maybeInsertedBrackets--
            }
        }),
        this.add("parens", "insertion", function(e, t, i, n, s) {
            if ("(" == s) {
                C(i);
                var o = i.getSelectionRange()
                  , r = n.doc.getTextRange(o);
                if ("" !== r && i.getWrapBehavioursEnabled())
                    return S(o, r, "(", ")");
                if (p.isSaneInsertion(i, n))
                    return p.recordAutoInsert(i, n, ")"),
                    {
                        text: "()",
                        selection: [1, 1]
                    }
            } else if (")" == s) {
                C(i);
                var a = i.getCursorPosition()
                  , l = n.doc.getLine(a.row);
                if (")" == l.substring(a.column, a.column + 1))
                    if (null !== n.$findOpeningBracket(")", {
                        column: a.column + 1,
                        row: a.row
                    }) && p.isAutoInsertedClosing(a, l, s))
                        return p.popAutoInsertedClosing(),
                        {
                            text: "",
                            selection: [1, 1]
                        }
            }
        }),
        this.add("parens", "deletion", function(e, t, i, n, s) {
            var o = n.doc.getTextRange(s);
            if (!s.isMultiLine() && "(" == o && (C(i),
            ")" == n.doc.getLine(s.start.row).substring(s.start.column + 1, s.start.column + 2)))
                return s.end.column++,
                s
        }),
        this.add("brackets", "insertion", function(e, t, i, n, s) {
            if ("[" == s) {
                C(i);
                var o = i.getSelectionRange()
                  , r = n.doc.getTextRange(o);
                if ("" !== r && i.getWrapBehavioursEnabled())
                    return S(o, r, "[", "]");
                if (p.isSaneInsertion(i, n))
                    return p.recordAutoInsert(i, n, "]"),
                    {
                        text: "[]",
                        selection: [1, 1]
                    }
            } else if ("]" == s) {
                C(i);
                var a = i.getCursorPosition()
                  , l = n.doc.getLine(a.row);
                if ("]" == l.substring(a.column, a.column + 1))
                    if (null !== n.$findOpeningBracket("]", {
                        column: a.column + 1,
                        row: a.row
                    }) && p.isAutoInsertedClosing(a, l, s))
                        return p.popAutoInsertedClosing(),
                        {
                            text: "",
                            selection: [1, 1]
                        }
            }
        }),
        this.add("brackets", "deletion", function(e, t, i, n, s) {
            var o = n.doc.getTextRange(s);
            if (!s.isMultiLine() && "[" == o && (C(i),
            "]" == n.doc.getLine(s.start.row).substring(s.start.column + 1, s.start.column + 2)))
                return s.end.column++,
                s
        }),
        this.add("string_dquotes", "insertion", function(e, t, i, n, s) {
            var o = n.$mode.$quotes || x;
            if (1 == s.length && o[s]) {
                if (this.lineCommentStart && -1 != this.lineCommentStart.indexOf(s))
                    return;
                C(i);
                var r = s
                  , a = i.getSelectionRange()
                  , l = n.doc.getTextRange(a);
                if ("" !== l && (1 != l.length || !o[l]) && i.getWrapBehavioursEnabled())
                    return S(a, l, r, r);
                if (!l) {
                    var h = i.getCursorPosition()
                      , c = n.doc.getLine(h.row)
                      , u = c.substring(h.column - 1, h.column)
                      , d = c.substring(h.column, h.column + 1)
                      , g = n.getTokenAt(h.row, h.column)
                      , f = n.getTokenAt(h.row, h.column + 1);
                    if ("\\" == u && g && /escape/.test(g.type))
                        return null;
                    var m, p = g && /string|escape/.test(g.type), w = !f || /string|escape/.test(f.type);
                    if (d == r)
                        (m = p !== w) && /string\.end/.test(f.type) && (m = !1);
                    else {
                        if (p && !w)
                            return null;
                        if (p && w)
                            return null;
                        var v = n.$mode.tokenRe;
                        v.lastIndex = 0;
                        var $ = v.test(u);
                        v.lastIndex = 0;
                        var b = v.test(u);
                        if ($ || b)
                            return null;
                        if (d && !/[\s;,.})\]\\]/.test(d))
                            return null;
                        var y = c[h.column - 2];
                        if (u == r && (y == r || v.test(y)))
                            return null;
                        m = !0
                    }
                    return {
                        text: m ? r + r : "",
                        selection: [1, 1]
                    }
                }
            }
        }),
        this.add("string_dquotes", "deletion", function(e, t, i, n, s) {
            var o = n.$mode.$quotes || x
              , r = n.doc.getTextRange(s);
            if (!s.isMultiLine() && o.hasOwnProperty(r) && (C(i),
            n.doc.getLine(s.start.row).substring(s.start.column + 1, s.start.column + 2) == r))
                return s.end.column++,
                s
        })
    };
    p.isSaneInsertion = function(e, t) {
        var i = e.getCursorPosition()
          , n = new o(t,i.row,i.column);
        if (!this.$matchTokenType(n.getCurrentToken() || "text", r)) {
            if (/[)}\]]/.test(e.session.getLine(i.row)[i.column]))
                return !0;
            var s = new o(t,i.row,i.column + 1);
            if (!this.$matchTokenType(s.getCurrentToken() || "text", r))
                return !1
        }
        return n.stepForward(),
        n.getCurrentTokenRow() !== i.row || this.$matchTokenType(n.getCurrentToken() || "text", a)
    }
    ,
    p.$matchTokenType = function(e, t) {
        return -1 < t.indexOf(e.type || e)
    }
    ,
    p.recordAutoInsert = function(e, t, i) {
        var n = e.getCursorPosition()
          , s = t.doc.getLine(n.row);
        this.isAutoInsertedClosing(n, s, f.autoInsertedLineEnd[0]) || (f.autoInsertedBrackets = 0),
        f.autoInsertedRow = n.row,
        f.autoInsertedLineEnd = i + s.substr(n.column),
        f.autoInsertedBrackets++
    }
    ,
    p.recordMaybeInsert = function(e, t, i) {
        var n = e.getCursorPosition()
          , s = t.doc.getLine(n.row);
        this.isMaybeInsertedClosing(n, s) || (f.maybeInsertedBrackets = 0),
        f.maybeInsertedRow = n.row,
        f.maybeInsertedLineStart = s.substr(0, n.column) + i,
        f.maybeInsertedLineEnd = s.substr(n.column),
        f.maybeInsertedBrackets++
    }
    ,
    p.isAutoInsertedClosing = function(e, t, i) {
        return 0 < f.autoInsertedBrackets && e.row === f.autoInsertedRow && i === f.autoInsertedLineEnd[0] && t.substr(e.column) === f.autoInsertedLineEnd
    }
    ,
    p.isMaybeInsertedClosing = function(e, t) {
        return 0 < f.maybeInsertedBrackets && e.row === f.maybeInsertedRow && t.substr(e.column) === f.maybeInsertedLineEnd && t.substr(0, e.column) == f.maybeInsertedLineStart
    }
    ,
    p.popAutoInsertedClosing = function() {
        f.autoInsertedLineEnd = f.autoInsertedLineEnd.substr(1),
        f.autoInsertedBrackets--
    }
    ,
    p.clearMaybeInsertedClosing = function() {
        f && (f.maybeInsertedBrackets = 0,
        f.maybeInsertedRow = -1)
    }
    ,
    n.inherits(p, s),
    t.CstyleBehaviour = p
}),
define("ace/unicode", ["require", "exports", "module"], function(e, t, i) {
    "use strict";
    for (var n = [48, 9, 8, 25, 5, 0, 2, 25, 48, 0, 11, 0, 5, 0, 6, 22, 2, 30, 2, 457, 5, 11, 15, 4, 8, 0, 2, 0, 18, 116, 2, 1, 3, 3, 9, 0, 2, 2, 2, 0, 2, 19, 2, 82, 2, 138, 2, 4, 3, 155, 12, 37, 3, 0, 8, 38, 10, 44, 2, 0, 2, 1, 2, 1, 2, 0, 9, 26, 6, 2, 30, 10, 7, 61, 2, 9, 5, 101, 2, 7, 3, 9, 2, 18, 3, 0, 17, 58, 3, 100, 15, 53, 5, 0, 6, 45, 211, 57, 3, 18, 2, 5, 3, 11, 3, 9, 2, 1, 7, 6, 2, 2, 2, 7, 3, 1, 3, 21, 2, 6, 2, 0, 4, 3, 3, 8, 3, 1, 3, 3, 9, 0, 5, 1, 2, 4, 3, 11, 16, 2, 2, 5, 5, 1, 3, 21, 2, 6, 2, 1, 2, 1, 2, 1, 3, 0, 2, 4, 5, 1, 3, 2, 4, 0, 8, 3, 2, 0, 8, 15, 12, 2, 2, 8, 2, 2, 2, 21, 2, 6, 2, 1, 2, 4, 3, 9, 2, 2, 2, 2, 3, 0, 16, 3, 3, 9, 18, 2, 2, 7, 3, 1, 3, 21, 2, 6, 2, 1, 2, 4, 3, 8, 3, 1, 3, 2, 9, 1, 5, 1, 2, 4, 3, 9, 2, 0, 17, 1, 2, 5, 4, 2, 2, 3, 4, 1, 2, 0, 2, 1, 4, 1, 4, 2, 4, 11, 5, 4, 4, 2, 2, 3, 3, 0, 7, 0, 15, 9, 18, 2, 2, 7, 2, 2, 2, 22, 2, 9, 2, 4, 4, 7, 2, 2, 2, 3, 8, 1, 2, 1, 7, 3, 3, 9, 19, 1, 2, 7, 2, 2, 2, 22, 2, 9, 2, 4, 3, 8, 2, 2, 2, 3, 8, 1, 8, 0, 2, 3, 3, 9, 19, 1, 2, 7, 2, 2, 2, 22, 2, 15, 4, 7, 2, 2, 2, 3, 10, 0, 9, 3, 3, 9, 11, 5, 3, 1, 2, 17, 4, 23, 2, 8, 2, 0, 3, 6, 4, 0, 5, 5, 2, 0, 2, 7, 19, 1, 14, 57, 6, 14, 2, 9, 40, 1, 2, 0, 3, 1, 2, 0, 3, 0, 7, 3, 2, 6, 2, 2, 2, 0, 2, 0, 3, 1, 2, 12, 2, 2, 3, 4, 2, 0, 2, 5, 3, 9, 3, 1, 35, 0, 24, 1, 7, 9, 12, 0, 2, 0, 2, 0, 5, 9, 2, 35, 5, 19, 2, 5, 5, 7, 2, 35, 10, 0, 58, 73, 7, 77, 3, 37, 11, 42, 2, 0, 4, 328, 2, 3, 3, 6, 2, 0, 2, 3, 3, 40, 2, 3, 3, 32, 2, 3, 3, 6, 2, 0, 2, 3, 3, 14, 2, 56, 2, 3, 3, 66, 5, 0, 33, 15, 17, 84, 13, 619, 3, 16, 2, 25, 6, 74, 22, 12, 2, 6, 12, 20, 12, 19, 13, 12, 2, 2, 2, 1, 13, 51, 3, 29, 4, 0, 5, 1, 3, 9, 34, 2, 3, 9, 7, 87, 9, 42, 6, 69, 11, 28, 4, 11, 5, 11, 11, 39, 3, 4, 12, 43, 5, 25, 7, 10, 38, 27, 5, 62, 2, 28, 3, 10, 7, 9, 14, 0, 89, 75, 5, 9, 18, 8, 13, 42, 4, 11, 71, 55, 9, 9, 4, 48, 83, 2, 2, 30, 14, 230, 23, 280, 3, 5, 3, 37, 3, 5, 3, 7, 2, 0, 2, 0, 2, 0, 2, 30, 3, 52, 2, 6, 2, 0, 4, 2, 2, 6, 4, 3, 3, 5, 5, 12, 6, 2, 2, 6, 67, 1, 20, 0, 29, 0, 14, 0, 17, 4, 60, 12, 5, 0, 4, 11, 18, 0, 5, 0, 3, 9, 2, 0, 4, 4, 7, 0, 2, 0, 2, 0, 2, 3, 2, 10, 3, 3, 6, 4, 5, 0, 53, 1, 2684, 46, 2, 46, 2, 132, 7, 6, 15, 37, 11, 53, 10, 0, 17, 22, 10, 6, 2, 6, 2, 6, 2, 6, 2, 6, 2, 6, 2, 6, 2, 6, 2, 31, 48, 0, 470, 1, 36, 5, 2, 4, 6, 1, 5, 85, 3, 1, 3, 2, 2, 89, 2, 3, 6, 40, 4, 93, 18, 23, 57, 15, 513, 6581, 75, 20939, 53, 1164, 68, 45, 3, 268, 4, 27, 21, 31, 3, 13, 13, 1, 2, 24, 9, 69, 11, 1, 38, 8, 3, 102, 3, 1, 111, 44, 25, 51, 13, 68, 12, 9, 7, 23, 4, 0, 5, 45, 3, 35, 13, 28, 4, 64, 15, 10, 39, 54, 10, 13, 3, 9, 7, 22, 4, 1, 5, 66, 25, 2, 227, 42, 2, 1, 3, 9, 7, 11171, 13, 22, 5, 48, 8453, 301, 3, 61, 3, 105, 39, 6, 13, 4, 6, 11, 2, 12, 2, 4, 2, 0, 2, 1, 2, 1, 2, 107, 34, 362, 19, 63, 3, 53, 41, 11, 5, 15, 17, 6, 13, 1, 25, 2, 33, 4, 2, 134, 20, 9, 8, 25, 5, 0, 2, 25, 12, 88, 4, 5, 3, 5, 3, 5, 3, 2], s = 0, o = [], r = 0; r < n.length; r += 2)
        o.push(s += n[r]),
        n[r + 1] && o.push(45, s += n[r + 1]);
    t.wordChars = String.fromCharCode.apply(null, o)
}),
define("ace/mode/text", ["require", "exports", "module", "ace/config", "ace/tokenizer", "ace/mode/text_highlight_rules", "ace/mode/behaviour/cstyle", "ace/unicode", "ace/lib/lang", "ace/token_iterator", "ace/range"], function(e, t, i) {
    "use strict";
    function n() {
        this.HighlightRules = o
    }
    var r = e("../config")
      , s = e("../tokenizer").Tokenizer
      , o = e("./text_highlight_rules").TextHighlightRules
      , a = e("./behaviour/cstyle").CstyleBehaviour
      , l = e("../unicode")
      , y = e("../lib/lang")
      , m = e("../token_iterator").TokenIterator
      , p = e("../range").Range;
    (function() {
        this.$defaultBehaviour = new a,
        this.tokenRe = new RegExp("^[" + l.wordChars + "\\$_]+","g"),
        this.nonTokenRe = new RegExp("^(?:[^" + l.wordChars + "\\$_]|\\s])+","g"),
        this.getTokenizer = function() {
            return this.$tokenizer || (this.$highlightRules = this.$highlightRules || new this.HighlightRules(this.$highlightRuleConfig),
            this.$tokenizer = new s(this.$highlightRules.getRules())),
            this.$tokenizer
        }
        ,
        this.lineCommentStart = "",
        this.blockComment = "",
        this.toggleCommentLines = function(e, s, i, n) {
            function t(e) {
                for (var t = i; t <= n; t++)
                    e(o.getLine(t), t)
            }
            var o = s.doc
              , r = !0
              , a = !0
              , l = 1 / 0
              , h = s.getTabSize()
              , c = !1;
            if (this.lineCommentStart) {
                p = Array.isArray(this.lineCommentStart) ? (v = this.lineCommentStart.map(y.escapeRegExp).join("|"),
                this.lineCommentStart[0]) : (v = y.escapeRegExp(this.lineCommentStart),
                this.lineCommentStart),
                v = new RegExp("^(\\s*)(?:" + v + ") ?"),
                c = s.getUseSoftTabs();
                var u = function(e, t) {
                    var i, n, s = e.match(v);
                    s && (i = s[1].length,
                    n = s[0].length,
                    m(e, i, n) || " " != s[0][n - 1] || n--,
                    o.removeInLine(t, i, n))
                }
                  , d = p + " "
                  , g = function(e, t) {
                    r && !/\S/.test(e) || (m(e, l, l) ? o.insertInLine({
                        row: t,
                        column: l
                    }, d) : o.insertInLine({
                        row: t,
                        column: l
                    }, p))
                }
                  , f = function(e, t) {
                    return v.test(e)
                }
                  , m = function(e, t, i) {
                    for (var n = 0; t-- && " " == e.charAt(t); )
                        n++;
                    if (n % h != 0)
                        return !1;
                    for (n = 0; " " == e.charAt(i++); )
                        n++;
                    return 2 < h ? n % h != h - 1 : n % h == 0
                }
            } else {
                if (!this.blockComment)
                    return !1;
                var p = this.blockComment.start
                  , w = this.blockComment.end
                  , v = new RegExp("^(\\s*)(?:" + y.escapeRegExp(p) + ")")
                  , $ = new RegExp("(?:" + y.escapeRegExp(w) + ")\\s*$")
                  , g = function(e, t) {
                    f(e, t) || r && !/\S/.test(e) || (o.insertInLine({
                        row: t,
                        column: e.length
                    }, w),
                    o.insertInLine({
                        row: t,
                        column: l
                    }, p))
                }
                  , u = function(e, t) {
                    var i;
                    (i = e.match($)) && o.removeInLine(t, e.length - i[0].length, e.length),
                    (i = e.match(v)) && o.removeInLine(t, i[1].length, i[0].length)
                }
                  , f = function(e, t) {
                    if (v.test(e))
                        return !0;
                    for (var i = s.getTokens(t), n = 0; n < i.length; n++)
                        if ("comment" === i[n].type)
                            return !0
                }
            }
            var b = 1 / 0;
            t(function(e, t) {
                var i = e.search(/\S/);
                -1 !== i ? (i < l && (l = i),
                a && !f(e, t) && (a = !1)) : b > e.length && (b = e.length)
            }),
            l == 1 / 0 && (l = b,
            a = r = !1),
            c && l % h != 0 && (l = Math.floor(l / h) * h),
            t(a ? u : g)
        }
        ,
        this.toggleBlockComment = function(e, t, i, n) {
            var s = this.blockComment;
            if (s) {
                !s.start && s[0] && (s = s[0]);
                var o, r, a = (d = new m(t,n.row,n.column)).getCurrentToken(), l = (t.selection,
                t.selection.toOrientedRange());
                if (a && /comment/.test(a.type)) {
                    for (; a && /comment/.test(a.type); ) {
                        if (-1 != (g = a.value.indexOf(s.start))) {
                            var h = d.getCurrentTokenRow()
                              , c = d.getCurrentTokenColumn() + g
                              , u = new p(h,c,h,c + s.start.length);
                            break
                        }
                        a = d.stepBackward()
                    }
                    for (var d, g, a = (d = new m(t,n.row,n.column)).getCurrentToken(); a && /comment/.test(a.type); ) {
                        if (-1 != (g = a.value.indexOf(s.end))) {
                            var h = d.getCurrentTokenRow()
                              , c = d.getCurrentTokenColumn() + g
                              , f = new p(h,c,h,c + s.end.length);
                            break
                        }
                        a = d.stepForward()
                    }
                    f && t.remove(f),
                    u && (t.remove(u),
                    o = u.start.row,
                    r = -s.start.length)
                } else
                    r = s.start.length,
                    o = i.start.row,
                    t.insert(i.end, s.end),
                    t.insert(i.start, s.start);
                l.start.row == o && (l.start.column += r),
                l.end.row == o && (l.end.column += r),
                t.selection.fromOrientedRange(l)
            }
        }
        ,
        this.getNextLineIndent = function(e, t, i) {
            return this.$getIndent(t)
        }
        ,
        this.checkOutdent = function(e, t, i) {
            return !1
        }
        ,
        this.autoOutdent = function(e, t, i) {}
        ,
        this.$getIndent = function(e) {
            return e.match(/^\s*/)[0]
        }
        ,
        this.createWorker = function(e) {
            return null
        }
        ,
        this.createModeDelegates = function(e) {
            for (var n in this.$embeds = [],
            this.$modes = {},
            e) {
                var t, i, s;
                e[n] && (i = (t = e[n]).prototype.$id,
                (s = r.$modes[i]) || (r.$modes[i] = s = new t),
                r.$modes[n] || (r.$modes[n] = s),
                this.$embeds.push(n),
                this.$modes[n] = s)
            }
            for (var o = ["toggleBlockComment", "toggleCommentLines", "getNextLineIndent", "checkOutdent", "autoOutdent", "transformAction", "getCompletions"], n = 0; n < o.length; n++)
                !function(e) {
                    var t = o[n]
                      , i = e[t];
                    e[o[n]] = function() {
                        return this.$delegator(t, arguments, i)
                    }
                }(this)
        }
        ,
        this.$delegator = function(e, t, i) {
            var n = t[0] || "start";
            if ("string" != typeof n) {
                if (Array.isArray(n[2])) {
                    var s = n[2][n[2].length - 1];
                    if (r = this.$modes[s])
                        return r[e].apply(r, [n[1]].concat([].slice.call(t, 1)))
                }
                n = n[0] || "start"
            }
            for (var o = 0; o < this.$embeds.length; o++)
                if (this.$modes[this.$embeds[o]]) {
                    var r, a = n.split(this.$embeds[o]);
                    if (!a[0] && a[1])
                        return t[0] = a[1],
                        (r = this.$modes[this.$embeds[o]])[e].apply(r, t)
                }
            var l = i.apply(this, t);
            return i ? l : void 0
        }
        ,
        this.transformAction = function(e, t, i, n, s) {
            if (this.$behaviour) {
                var o = this.$behaviour.getBehaviours();
                for (var r in o)
                    if (o[r][t]) {
                        var a = o[r][t].apply(this, arguments);
                        if (a)
                            return a
                    }
            }
        }
        ,
        this.getKeywords = function(e) {
            if (!this.completionKeywords) {
                var t = this.$tokenizer.rules
                  , i = [];
                for (var n in t)
                    for (var s = t[n], o = 0, r = s.length; o < r; o++)
                        if ("string" == typeof s[o].token)
                            /keyword|support|storage/.test(s[o].token) && i.push(s[o].regex);
                        else if ("object" == typeof s[o].token)
                            for (var a = 0, l = s[o].token.length; a < l; a++) {
                                /keyword|support|storage/.test(s[o].token[a]) && (n = s[o].regex.match(/\(.+?\)/g)[a],
                                i.push(n.substr(1, n.length - 2)))
                            }
                this.completionKeywords = i
            }
            return e ? i.concat(this.$keywordList || []) : this.$keywordList
        }
        ,
        this.$createKeywordList = function() {
            return this.$highlightRules || this.getTokenizer(),
            this.$keywordList = this.$highlightRules.$keywordList || []
        }
        ,
        this.getCompletions = function(e, t, i, n) {
            return (this.$keywordList || this.$createKeywordList()).map(function(e) {
                return {
                    name: e,
                    value: e,
                    score: 0,
                    meta: "keyword"
                }
            })
        }
        ,
        this.$id = "ace/mode/text"
    }
    ).call(n.prototype),
    t.Mode = n
}),
define("ace/apply_delta", ["require", "exports", "module"], function(e, t, i) {
    "use strict";
    t.applyDelta = function(e, t, i) {
        var n, s = t.start.row, o = t.start.column, r = e[s] || "";
        switch (t.action) {
        case "insert":
            1 === t.lines.length ? e[s] = r.substring(0, o) + t.lines[0] + r.substring(o) : (n = [s, 1].concat(t.lines),
            e.splice.apply(e, n),
            e[s] = r.substring(0, o) + e[s],
            e[s + t.lines.length - 1] += r.substring(o));
            break;
        case "remove":
            var a = t.end.column
              , l = t.end.row;
            s === l ? e[s] = r.substring(0, o) + r.substring(a) : e.splice(s, l - s + 1, r.substring(0, o) + e[l].substring(a))
        }
    }
}),
define("ace/anchor", ["require", "exports", "module", "ace/lib/oop", "ace/lib/event_emitter"], function(e, t, i) {
    "use strict";
    var n = e("./lib/oop")
      , s = e("./lib/event_emitter").EventEmitter
      , o = t.Anchor = function(e, t, i) {
        this.$onChange = this.onChange.bind(this),
        this.attach(e),
        void 0 === i ? this.setPosition(t.row, t.column) : this.setPosition(t, i)
    }
    ;
    (function() {
        function c(e, t, i) {
            var n = i ? e.column <= t.column : e.column < t.column;
            return e.row < t.row || e.row == t.row && n
        }
        n.implement(this, s),
        this.getPosition = function() {
            return this.$clipPositionToDocument(this.row, this.column)
        }
        ,
        this.getDocument = function() {
            return this.document
        }
        ,
        this.$insertRight = !1,
        this.onChange = function(e) {
            var t, i, n, s, o, r, a, l, h;
            e.start.row == e.end.row && e.start.row != this.row || e.start.row > this.row || (i = e,
            n = {
                row: this.row,
                column: this.column
            },
            s = this.$insertRight,
            o = "insert" == i.action,
            r = (o ? 1 : -1) * (i.end.row - i.start.row),
            a = (o ? 1 : -1) * (i.end.column - i.start.column),
            l = i.start,
            h = o ? l : i.end,
            t = c(n, l, s) ? {
                row: n.row,
                column: n.column
            } : c(h, n, !s) ? {
                row: n.row + r,
                column: n.column + (n.row == h.row ? a : 0)
            } : {
                row: l.row,
                column: l.column
            },
            this.setPosition(t.row, t.column, !0))
        }
        ,
        this.setPosition = function(e, t, i) {
            var n, s = i ? {
                row: e,
                column: t
            } : this.$clipPositionToDocument(e, t);
            this.row == s.row && this.column == s.column || (n = {
                row: this.row,
                column: this.column
            },
            this.row = s.row,
            this.column = s.column,
            this._signal("change", {
                old: n,
                value: s
            }))
        }
        ,
        this.detach = function() {
            this.document.off("change", this.$onChange)
        }
        ,
        this.attach = function(e) {
            this.document = e || this.document,
            this.document.on("change", this.$onChange)
        }
        ,
        this.$clipPositionToDocument = function(e, t) {
            var i = {};
            return e >= this.document.getLength() ? (i.row = Math.max(0, this.document.getLength() - 1),
            i.column = this.document.getLine(i.row).length) : e < 0 ? (i.row = 0,
            i.column = 0) : (i.row = e,
            i.column = Math.min(this.document.getLine(i.row).length, Math.max(0, t))),
            t < 0 && (i.column = 0),
            i
        }
    }
    ).call(o.prototype)
}),
define("ace/document", ["require", "exports", "module", "ace/lib/oop", "ace/apply_delta", "ace/lib/event_emitter", "ace/range", "ace/anchor"], function(e, t, i) {
    "use strict";
    function n(e) {
        this.$lines = [""],
        0 === e.length ? this.$lines = [""] : Array.isArray(e) ? this.insertMergedLines({
            row: 0,
            column: 0
        }, e) : this.insert({
            row: 0,
            column: 0
        }, e)
    }
    var s = e("./lib/oop")
      , o = e("./apply_delta").applyDelta
      , r = e("./lib/event_emitter").EventEmitter
      , c = e("./range").Range
      , a = e("./anchor").Anchor;
    (function() {
        s.implement(this, r),
        this.setValue = function(e) {
            var t = this.getLength() - 1;
            this.remove(new c(0,0,t,this.getLine(t).length)),
            this.insert({
                row: 0,
                column: 0
            }, e)
        }
        ,
        this.getValue = function() {
            return this.getAllLines().join(this.getNewLineCharacter())
        }
        ,
        this.createAnchor = function(e, t) {
            return new a(this,e,t)
        }
        ,
        0 === "aaa".split(/a/).length ? this.$split = function(e) {
            return e.replace(/\r\n|\r/g, "\n").split("\n")
        }
        : this.$split = function(e) {
            return e.split(/\r\n|\r|\n/)
        }
        ,
        this.$detectNewLine = function(e) {
            var t = e.match(/^.*?(\r\n|\r|\n)/m);
            this.$autoNewLine = t ? t[1] : "\n",
            this._signal("changeNewLineMode")
        }
        ,
        this.getNewLineCharacter = function() {
            switch (this.$newLineMode) {
            case "windows":
                return "\r\n";
            case "unix":
                return "\n";
            default:
                return this.$autoNewLine || "\n"
            }
        }
        ,
        this.$autoNewLine = "",
        this.$newLineMode = "auto",
        this.setNewLineMode = function(e) {
            this.$newLineMode !== e && (this.$newLineMode = e,
            this._signal("changeNewLineMode"))
        }
        ,
        this.getNewLineMode = function() {
            return this.$newLineMode
        }
        ,
        this.isNewLine = function(e) {
            return "\r\n" == e || "\r" == e || "\n" == e
        }
        ,
        this.getLine = function(e) {
            return this.$lines[e] || ""
        }
        ,
        this.getLines = function(e, t) {
            return this.$lines.slice(e, t + 1)
        }
        ,
        this.getAllLines = function() {
            return this.getLines(0, this.getLength())
        }
        ,
        this.getLength = function() {
            return this.$lines.length
        }
        ,
        this.getTextRange = function(e) {
            return this.getLinesForRange(e).join(this.getNewLineCharacter())
        }
        ,
        this.getLinesForRange = function(e) {
            var t, i;
            return e.start.row === e.end.row ? t = [this.getLine(e.start.row).substring(e.start.column, e.end.column)] : ((t = this.getLines(e.start.row, e.end.row))[0] = (t[0] || "").substring(e.start.column),
            i = t.length - 1,
            e.end.row - e.start.row == i && (t[i] = t[i].substring(0, e.end.column))),
            t
        }
        ,
        this.insertLines = function(e, t) {
            return console.warn("Use of document.insertLines is deprecated. Use the insertFullLines method instead."),
            this.insertFullLines(e, t)
        }
        ,
        this.removeLines = function(e, t) {
            return console.warn("Use of document.removeLines is deprecated. Use the removeFullLines method instead."),
            this.removeFullLines(e, t)
        }
        ,
        this.insertNewLine = function(e) {
            return console.warn("Use of document.insertNewLine is deprecated. Use insertMergedLines(position, ['', '']) instead."),
            this.insertMergedLines(e, ["", ""])
        }
        ,
        this.insert = function(e, t) {
            return this.getLength() <= 1 && this.$detectNewLine(t),
            this.insertMergedLines(e, this.$split(t))
        }
        ,
        this.insertInLine = function(e, t) {
            var i = this.clippedPos(e.row, e.column)
              , n = this.pos(e.row, e.column + t.length);
            return this.applyDelta({
                start: i,
                end: n,
                action: "insert",
                lines: [t]
            }, !0),
            this.clonePos(n)
        }
        ,
        this.clippedPos = function(e, t) {
            var i = this.getLength();
            void 0 === e ? e = i : e < 0 ? e = 0 : i <= e && (e = i - 1,
            t = void 0);
            var n = this.getLine(e);
            return null == t && (t = n.length),
            {
                row: e,
                column: t = Math.min(Math.max(t, 0), n.length)
            }
        }
        ,
        this.clonePos = function(e) {
            return {
                row: e.row,
                column: e.column
            }
        }
        ,
        this.pos = function(e, t) {
            return {
                row: e,
                column: t
            }
        }
        ,
        this.$clipPosition = function(e) {
            var t = this.getLength();
            return e.row >= t ? (e.row = Math.max(0, t - 1),
            e.column = this.getLine(t - 1).length) : (e.row = Math.max(0, e.row),
            e.column = Math.min(Math.max(e.column, 0), this.getLine(e.row).length)),
            e
        }
        ,
        this.insertFullLines = function(e, t) {
            var i = 0
              , i = (e = Math.min(Math.max(e, 0), this.getLength())) < this.getLength() ? (t = t.concat([""]),
            0) : (t = [""].concat(t),
            e--,
            this.$lines[e].length);
            this.insertMergedLines({
                row: e,
                column: i
            }, t)
        }
        ,
        this.insertMergedLines = function(e, t) {
            var i = this.clippedPos(e.row, e.column)
              , n = {
                row: i.row + t.length - 1,
                column: (1 == t.length ? i.column : 0) + t[t.length - 1].length
            };
            return this.applyDelta({
                start: i,
                end: n,
                action: "insert",
                lines: t
            }),
            this.clonePos(n)
        }
        ,
        this.remove = function(e) {
            var t = this.clippedPos(e.start.row, e.start.column)
              , i = this.clippedPos(e.end.row, e.end.column);
            return this.applyDelta({
                start: t,
                end: i,
                action: "remove",
                lines: this.getLinesForRange({
                    start: t,
                    end: i
                })
            }),
            this.clonePos(t)
        }
        ,
        this.removeInLine = function(e, t, i) {
            var n = this.clippedPos(e, t)
              , s = this.clippedPos(e, i);
            return this.applyDelta({
                start: n,
                end: s,
                action: "remove",
                lines: this.getLinesForRange({
                    start: n,
                    end: s
                })
            }, !0),
            this.clonePos(n)
        }
        ,
        this.removeFullLines = function(e, t) {
            e = Math.min(Math.max(0, e), this.getLength() - 1);
            var i = (t = Math.min(Math.max(0, t), this.getLength() - 1)) == this.getLength() - 1 && 0 < e
              , n = t < this.getLength() - 1
              , s = i ? e - 1 : e
              , o = i ? this.getLine(s).length : 0
              , r = n ? t + 1 : t
              , a = n ? 0 : this.getLine(r).length
              , l = new c(s,o,r,a)
              , h = this.$lines.slice(e, t + 1);
            return this.applyDelta({
                start: l.start,
                end: l.end,
                action: "remove",
                lines: this.getLinesForRange(l)
            }),
            h
        }
        ,
        this.removeNewLine = function(e) {
            e < this.getLength() - 1 && 0 <= e && this.applyDelta({
                start: this.pos(e, this.getLine(e).length),
                end: this.pos(e + 1, 0),
                action: "remove",
                lines: ["", ""]
            })
        }
        ,
        this.replace = function(e, t) {
            return e instanceof c || (e = c.fromPoints(e.start, e.end)),
            0 === t.length && e.isEmpty() ? e.start : t == this.getTextRange(e) ? e.end : (this.remove(e),
            t ? this.insert(e.start, t) : e.start)
        }
        ,
        this.applyDeltas = function(e) {
            for (var t = 0; t < e.length; t++)
                this.applyDelta(e[t])
        }
        ,
        this.revertDeltas = function(e) {
            for (var t = e.length - 1; 0 <= t; t--)
                this.revertDelta(e[t])
        }
        ,
        this.applyDelta = function(e, t) {
            var i = "insert" == e.action;
            (i ? e.lines.length <= 1 && !e.lines[0] : !c.comparePoints(e.start, e.end)) || (i && 2e4 < e.lines.length ? this.$splitAndapplyLargeDelta(e, 2e4) : (o(this.$lines, e, t),
            this._signal("change", e)))
        }
        ,
        this.$safeApplyDelta = function(e) {
            var t = this.$lines.length;
            ("remove" == e.action && e.start.row < t && e.end.row < t || "insert" == e.action && e.start.row <= t) && this.applyDelta(e)
        }
        ,
        this.$splitAndapplyLargeDelta = function(e, t) {
            for (var i = e.lines, n = i.length - t + 1, s = e.start.row, o = e.start.column, r = 0, a = 0; r < n; r = a) {
                a += t - 1;
                var l = i.slice(r, a);
                l.push(""),
                this.applyDelta({
                    start: this.pos(s + r, o),
                    end: this.pos(s + a, o = 0),
                    action: e.action,
                    lines: l
                }, !0)
            }
            e.lines = i.slice(r),
            e.start.row = s + r,
            e.start.column = o,
            this.applyDelta(e, !0)
        }
        ,
        this.revertDelta = function(e) {
            this.$safeApplyDelta({
                start: this.clonePos(e.start),
                end: this.clonePos(e.end),
                action: "insert" == e.action ? "remove" : "insert",
                lines: e.lines.slice()
            })
        }
        ,
        this.indexToPosition = function(e, t) {
            for (var i = this.$lines || this.getAllLines(), n = this.getNewLineCharacter().length, s = t || 0, o = i.length; s < o; s++)
                if ((e -= i[s].length + n) < 0)
                    return {
                        row: s,
                        column: e + i[s].length + n
                    };
            return {
                row: o - 1,
                column: e + i[o - 1].length + n
            }
        }
        ,
        this.positionToIndex = function(e, t) {
            for (var i = this.$lines || this.getAllLines(), n = this.getNewLineCharacter().length, s = 0, o = Math.min(e.row, i.length), r = t || 0; r < o; ++r)
                s += i[r].length + n;
            return s + e.column
        }
    }
    ).call(n.prototype),
    t.Document = n
}),
define("ace/background_tokenizer", ["require", "exports", "module", "ace/lib/oop", "ace/lib/event_emitter"], function(e, t, i) {
    "use strict";
    function n(e, t) {
        this.running = !1,
        this.lines = [],
        this.states = [],
        this.currentLine = 0,
        this.tokenizer = e;
        var a = this;
        this.$worker = function() {
            if (a.running) {
                for (var e = new Date, t = a.currentLine, i = -1, n = a.doc, s = t; a.lines[t]; )
                    t++;
                var o = n.getLength()
                  , r = 0;
                for (a.running = !1; t < o; ) {
                    for (a.$tokenizeRow(t),
                    i = t; t++,
                    a.lines[t]; )
                        ;
                    if (++r % 5 == 0 && 20 < new Date - e) {
                        a.running = setTimeout(a.$worker, 20);
                        break
                    }
                }
                a.currentLine = t,
                -1 == i && (i = t),
                s <= i && a.fireUpdateEvent(s, i)
            }
        }
    }
    var s = e("./lib/oop")
      , o = e("./lib/event_emitter").EventEmitter;
    (function() {
        s.implement(this, o),
        this.setTokenizer = function(e) {
            this.tokenizer = e,
            this.lines = [],
            this.states = [],
            this.start(0)
        }
        ,
        this.setDocument = function(e) {
            this.doc = e,
            this.lines = [],
            this.states = [],
            this.stop()
        }
        ,
        this.fireUpdateEvent = function(e, t) {
            var i = {
                first: e,
                last: t
            };
            this._signal("update", {
                data: i
            })
        }
        ,
        this.start = function(e) {
            this.currentLine = Math.min(e || 0, this.currentLine, this.doc.getLength()),
            this.lines.splice(this.currentLine, this.lines.length),
            this.states.splice(this.currentLine, this.states.length),
            this.stop(),
            this.running = setTimeout(this.$worker, 700)
        }
        ,
        this.scheduleStart = function() {
            this.running || (this.running = setTimeout(this.$worker, 700))
        }
        ,
        this.$updateOnChange = function(e) {
            var t, i = e.start.row, n = e.end.row - i;
            0 == n ? this.lines[i] = null : "remove" == e.action ? (this.lines.splice(i, 1 + n, null),
            this.states.splice(i, 1 + n, null)) : ((t = Array(1 + n)).unshift(i, 1),
            this.lines.splice.apply(this.lines, t),
            this.states.splice.apply(this.states, t)),
            this.currentLine = Math.min(i, this.currentLine, this.doc.getLength()),
            this.stop()
        }
        ,
        this.stop = function() {
            this.running && clearTimeout(this.running),
            this.running = !1
        }
        ,
        this.getTokens = function(e) {
            return this.lines[e] || this.$tokenizeRow(e)
        }
        ,
        this.getState = function(e) {
            return this.currentLine == e && this.$tokenizeRow(e),
            this.states[e] || "start"
        }
        ,
        this.$tokenizeRow = function(e) {
            var t = this.doc.getLine(e)
              , i = this.states[e - 1]
              , n = this.tokenizer.getLineTokens(t, i, e);
            return this.states[e] + "" != n.state + "" ? (this.states[e] = n.state,
            this.lines[e + 1] = null,
            this.currentLine > e + 1 && (this.currentLine = e + 1)) : this.currentLine == e && (this.currentLine = e + 1),
            this.lines[e] = n.tokens
        }
    }
    ).call(n.prototype),
    t.BackgroundTokenizer = n
}),
define("ace/search_highlight", ["require", "exports", "module", "ace/lib/lang", "ace/lib/oop", "ace/range"], function(e, t, i) {
    "use strict";
    function n(e, t, i) {
        this.setRegexp(e),
        this.clazz = t,
        this.type = i || "text"
    }
    var h = e("./lib/lang")
      , c = (e("./lib/oop"),
    e("./range").Range);
    (function() {
        this.MAX_RANGES = 500,
        this.setRegexp = function(e) {
            this.regExp + "" != e + "" && (this.regExp = e,
            this.cache = [])
        }
        ,
        this.update = function(e, t, i, n) {
            if (this.regExp)
                for (var s = n.firstRow, o = n.lastRow, r = s; r <= o; r++) {
                    var a = this.cache[r];
                    null == a && ((a = h.getMatchOffsets(i.getLine(r), this.regExp)).length > this.MAX_RANGES && (a = a.slice(0, this.MAX_RANGES)),
                    a = a.map(function(e) {
                        return new c(r,e.offset,r,e.offset + e.length)
                    }),
                    this.cache[r] = a.length ? a : "");
                    for (var l = a.length; l--; )
                        t.drawSingleLineMarker(e, a[l].toScreenRange(i), this.clazz, n)
                }
        }
    }
    ).call(n.prototype),
    t.SearchHighlight = n
}),
define("ace/edit_session/fold_line", ["require", "exports", "module", "ace/range"], function(e, t, i) {
    "use strict";
    function h(e, t) {
        this.foldData = e,
        Array.isArray(t) ? this.folds = t : t = this.folds = [t];
        var i = t[t.length - 1];
        this.range = new n(t[0].start.row,t[0].start.column,i.end.row,i.end.column),
        this.start = this.range.start,
        this.end = this.range.end,
        this.folds.forEach(function(e) {
            e.setFoldLine(this)
        }, this)
    }
    var n = e("../range").Range;
    (function() {
        this.shiftRow = function(t) {
            this.start.row += t,
            this.end.row += t,
            this.folds.forEach(function(e) {
                e.start.row += t,
                e.end.row += t
            })
        }
        ,
        this.addFold = function(e) {
            if (e.sameRow) {
                if (e.start.row < this.startRow || e.endRow > this.endRow)
                    throw new Error("Can't add a fold to this FoldLine as it has no connection");
                this.folds.push(e),
                this.folds.sort(function(e, t) {
                    return -e.range.compareEnd(t.start.row, t.start.column)
                }),
                0 < this.range.compareEnd(e.start.row, e.start.column) ? (this.end.row = e.end.row,
                this.end.column = e.end.column) : this.range.compareStart(e.end.row, e.end.column) < 0 && (this.start.row = e.start.row,
                this.start.column = e.start.column)
            } else if (e.start.row == this.end.row)
                this.folds.push(e),
                this.end.row = e.end.row,
                this.end.column = e.end.column;
            else {
                if (e.end.row != this.start.row)
                    throw new Error("Trying to add fold to FoldRow that doesn't have a matching row");
                this.folds.unshift(e),
                this.start.row = e.start.row,
                this.start.column = e.start.column
            }
            e.foldLine = this
        }
        ,
        this.containsRow = function(e) {
            return e >= this.start.row && e <= this.end.row
        }
        ,
        this.walk = function(e, t, i) {
            var n, s, o = 0, r = this.folds, a = !0;
            null == t && (t = this.end.row,
            i = this.end.column);
            for (var l = 0; l < r.length; l++) {
                if (-1 == (s = (n = r[l]).range.compareStart(t, i)))
                    return void e(null, t, i, o, a);
                if (!e(null, n.start.row, n.start.column, o, a) && e(n.placeholder, n.start.row, n.start.column, o) || 0 === s)
                    return;
                a = !n.sameRow,
                o = n.end.column
            }
            e(null, t, i, o, a)
        }
        ,
        this.getNextFoldTo = function(e, t) {
            for (var i, n, s = 0; s < this.folds.length; s++) {
                if (-1 == (n = (i = this.folds[s]).range.compareEnd(e, t)))
                    return {
                        fold: i,
                        kind: "after"
                    };
                if (0 === n)
                    return {
                        fold: i,
                        kind: "inside"
                    }
            }
            return null
        }
        ,
        this.addRemoveChars = function(e, t, i) {
            var n, s, o = this.getNextFoldTo(e, t);
            if (o)
                if (n = o.fold,
                "inside" == o.kind && n.start.column != t && n.start.row != e)
                    window.console && window.console.log(e, t, n);
                else if (n.start.row == e) {
                    var r = (s = this.folds).indexOf(n);
                    for (0 === r && (this.start.column += i); r < s.length; r++) {
                        if ((n = s[r]).start.column += i,
                        !n.sameRow)
                            return;
                        n.end.column += i
                    }
                    this.end.column += i
                }
        }
        ,
        this.split = function(e, t) {
            var i = this.getNextFoldTo(e, t);
            if (!i || "inside" == i.kind)
                return null;
            var n = i.fold
              , s = this.folds
              , o = this.foldData
              , r = s.indexOf(n)
              , a = s[r - 1];
            this.end.row = a.end.row,
            this.end.column = a.end.column;
            var l = new h(o,s = s.splice(r, s.length - r));
            return o.splice(o.indexOf(this) + 1, 0, l),
            l
        }
        ,
        this.merge = function(e) {
            for (var t = e.folds, i = 0; i < t.length; i++)
                this.addFold(t[i]);
            var n = this.foldData;
            n.splice(n.indexOf(e), 1)
        }
        ,
        this.toString = function() {
            var t = [this.range.toString() + ": ["];
            return this.folds.forEach(function(e) {
                t.push("  " + e.toString())
            }),
            t.push("]"),
            t.join("\n")
        }
        ,
        this.idxToPosition = function(e) {
            for (var t = 0, i = 0; i < this.folds.length; i++) {
                var n = this.folds[i];
                if ((e -= n.start.column - t) < 0)
                    return {
                        row: n.start.row,
                        column: n.start.column + e
                    };
                if ((e -= n.placeholder.length) < 0)
                    return n.start;
                t = n.end.column
            }
            return {
                row: this.end.row,
                column: this.end.column + e
            }
        }
    }
    ).call(h.prototype),
    t.FoldLine = h
}),
define("ace/range_list", ["require", "exports", "module", "ace/range"], function(e, t, i) {
    "use strict";
    function n() {
        this.ranges = [],
        this.$bias = 1
    }
    var l = e("./range").Range.comparePoints;
    (function() {
        this.comparePoints = l,
        this.pointIndex = function(e, t, i) {
            for (var n = this.ranges, s = i || 0; s < n.length; s++) {
                var o = n[s]
                  , r = l(e, o.end);
                if (!(0 < r)) {
                    var a = l(e, o.start);
                    return 0 === r ? t && 0 !== a ? -s - 2 : s : 0 < a || 0 === a && !t ? s : -s - 1
                }
            }
            return -s - 1
        }
        ,
        this.add = function(e) {
            var t = !e.isEmpty()
              , i = this.pointIndex(e.start, t);
            i < 0 && (i = -i - 1);
            var n = this.pointIndex(e.end, t, i);
            return n < 0 ? n = -n - 1 : n++,
            this.ranges.splice(i, n - i, e)
        }
        ,
        this.addList = function(e) {
            for (var t = [], i = e.length; i--; )
                t.push.apply(t, this.add(e[i]));
            return t
        }
        ,
        this.substractPoint = function(e) {
            var t = this.pointIndex(e);
            if (0 <= t)
                return this.ranges.splice(t, 1)
        }
        ,
        this.merge = function() {
            for (var e, t = [], i = this.ranges, n = (i = i.sort(function(e, t) {
                return l(e.start, t.start)
            }))[0], s = 1; s < i.length; s++) {
                e = n,
                n = i[s];
                var o = l(e.end, n.start);
                o < 0 || (0 != o || e.isEmpty() || n.isEmpty()) && (l(e.end, n.end) < 0 && (e.end.row = n.end.row,
                e.end.column = n.end.column),
                i.splice(s, 1),
                t.push(n),
                n = e,
                s--)
            }
            return this.ranges = i,
            t
        }
        ,
        this.contains = function(e, t) {
            return 0 <= this.pointIndex({
                row: e,
                column: t
            })
        }
        ,
        this.containsPoint = function(e) {
            return 0 <= this.pointIndex(e)
        }
        ,
        this.rangeAtPoint = function(e) {
            var t = this.pointIndex(e);
            if (0 <= t)
                return this.ranges[t]
        }
        ,
        this.clipRows = function(e, t) {
            var i = this.ranges;
            if (i[0].start.row > t || i[i.length - 1].start.row < e)
                return [];
            var n = this.pointIndex({
                row: e,
                column: 0
            });
            n < 0 && (n = -n - 1);
            var s = this.pointIndex({
                row: t,
                column: 0
            }, n);
            s < 0 && (s = -s - 1);
            for (var o = [], r = n; r < s; r++)
                o.push(i[r]);
            return o
        }
        ,
        this.removeAll = function() {
            return this.ranges.splice(0, this.ranges.length)
        }
        ,
        this.attach = function(e) {
            this.session && this.detach(),
            this.session = e,
            this.onChange = this.$onChange.bind(this),
            this.session.on("change", this.onChange)
        }
        ,
        this.detach = function() {
            this.session && (this.session.removeListener("change", this.onChange),
            this.session = null)
        }
        ,
        this.$onChange = function(e) {
            for (var t = e.start, i = e.end, n = t.row, s = i.row, o = this.ranges, r = 0, a = o.length; r < a; r++) {
                if ((c = o[r]).end.row >= n)
                    break
            }
            if ("insert" == e.action)
                for (var l = s - n, h = -t.column + i.column; r < a; r++) {
                    if ((c = o[r]).start.row > n)
                        break;
                    if (c.start.row == n && c.start.column >= t.column && (c.start.column == t.column && this.$bias <= 0 || (c.start.column += h,
                    c.start.row += l)),
                    c.end.row == n && c.end.column >= t.column) {
                        if (c.end.column == t.column && this.$bias < 0)
                            continue;
                        c.end.column == t.column && 0 < h && r < a - 1 && c.end.column > c.start.column && c.end.column == o[r + 1].start.column && (c.end.column -= h),
                        c.end.column += h,
                        c.end.row += l
                    }
                }
            else
                for (var c, l = n - s, h = t.column - i.column; r < a; r++) {
                    if ((c = o[r]).start.row > s)
                        break;
                    c.end.row < s && (n < c.end.row || n == c.end.row && t.column < c.end.column) ? (c.end.row = n,
                    c.end.column = t.column) : c.end.row == s ? c.end.column <= i.column ? (l || c.end.column > t.column) && (c.end.column = t.column,
                    c.end.row = t.row) : (c.end.column += h,
                    c.end.row += l) : c.end.row > s && (c.end.row += l),
                    c.start.row < s && (n < c.start.row || n == c.start.row && t.column < c.start.column) ? (c.start.row = n,
                    c.start.column = t.column) : c.start.row == s ? c.start.column <= i.column ? (l || c.start.column > t.column) && (c.start.column = t.column,
                    c.start.row = t.row) : (c.start.column += h,
                    c.start.row += l) : c.start.row > s && (c.start.row += l)
                }
            if (0 != l && r < a)
                for (; r < a; r++) {
                    (c = o[r]).start.row += l,
                    c.end.row += l
                }
        }
    }
    ).call(n.prototype),
    t.RangeList = n
}),
define("ace/edit_session/fold", ["require", "exports", "module", "ace/range_list", "ace/lib/oop"], function(e, t, i) {
    "use strict";
    function g(e, t) {
        e.row -= t.row,
        0 == e.row && (e.column -= t.column)
    }
    function n(e, t) {
        0 == e.row && (e.column += t.column),
        e.row += t.row
    }
    var s = e("../range_list").RangeList
      , o = e("../lib/oop")
      , r = t.Fold = function(e, t) {
        this.foldLine = null,
        this.placeholder = t,
        this.range = e,
        this.start = e.start,
        this.end = e.end,
        this.sameRow = e.start.row == e.end.row,
        this.subFolds = this.ranges = []
    }
    ;
    o.inherits(r, s),
    function() {
        this.toString = function() {
            return '"' + this.placeholder + '" ' + this.range.toString()
        }
        ,
        this.setFoldLine = function(t) {
            this.foldLine = t,
            this.subFolds.forEach(function(e) {
                e.setFoldLine(t)
            })
        }
        ,
        this.clone = function() {
            var e = this.range.clone()
              , t = new r(e,this.placeholder);
            return this.subFolds.forEach(function(e) {
                t.subFolds.push(e.clone())
            }),
            t.collapseChildren = this.collapseChildren,
            t
        }
        ,
        this.addSubFold = function(e) {
            if (!this.range.isEqual(e)) {
                var t, i;
                t = e,
                i = this.start,
                g(t.start, i),
                g(t.end, i);
                for (var n = e.start.row, s = e.start.column, o = 0, r = -1; o < this.subFolds.length && 1 == (r = this.subFolds[o].range.compare(n, s)); o++)
                    ;
                var a = this.subFolds[o]
                  , l = 0;
                if (0 == r) {
                    if (a.range.containsRange(e))
                        return a.addSubFold(e);
                    l = 1
                }
                for (var n = e.range.end.row, s = e.range.end.column, h = o, r = -1; h < this.subFolds.length && 1 == (r = this.subFolds[h].range.compare(n, s)); h++)
                    ;
                0 == r && h++;
                for (var c = this.subFolds.splice(o, h - o, e), u = 0 == r ? c.length - 1 : c.length, d = l; d < u; d++)
                    e.addSubFold(c[d]);
                return e.setFoldLine(this.foldLine),
                e
            }
        }
        ,
        this.restoreRange = function(e) {
            return t = e,
            i = this.start,
            n(t.start, i),
            void n(t.end, i);
            var t, i
        }
    }
    .call(r.prototype)
}),
define("ace/edit_session/folding", ["require", "exports", "module", "ace/range", "ace/edit_session/fold_line", "ace/edit_session/fold", "ace/token_iterator"], function(e, t, i) {
    "use strict";
    var c = e("../range").Range
      , m = e("./fold_line").FoldLine
      , p = e("./fold").Fold
      , u = e("../token_iterator").TokenIterator;
    t.Folding = function() {
        this.getFoldAt = function(e, t, i) {
            var n = this.getFoldLine(e);
            if (!n)
                return null;
            for (var s = n.folds, o = 0; o < s.length; o++) {
                var r = s[o].range;
                if (r.contains(e, t)) {
                    if (1 == i && r.isEnd(e, t) && !r.isEmpty())
                        continue;
                    if (-1 == i && r.isStart(e, t) && !r.isEmpty())
                        continue;
                    return s[o]
                }
            }
        }
        ,
        this.getFoldsInRange = function(e) {
            var t = e.start
              , i = e.end
              , n = this.$foldData
              , s = [];
            t.column += 1,
            --i.column;
            for (var o = 0; o < n.length; o++) {
                if (2 != (l = n[o].range.compareRange(e))) {
                    if (-2 == l)
                        break;
                    for (var r = n[o].folds, a = 0; a < r.length; a++) {
                        var l, h = r[a];
                        if (-2 == (l = h.range.compareRange(e)))
                            break;
                        if (2 != l) {
                            if (42 == l)
                                break;
                            s.push(h)
                        }
                    }
                }
            }
            return --t.column,
            i.column += 1,
            s
        }
        ,
        this.getFoldsInRangeList = function(e) {
            var t;
            return Array.isArray(e) ? (t = [],
            e.forEach(function(e) {
                t = t.concat(this.getFoldsInRange(e))
            }, this)) : t = this.getFoldsInRange(e),
            t
        }
        ,
        this.getAllFolds = function() {
            for (var e = [], t = this.$foldData, i = 0; i < t.length; i++)
                for (var n = 0; n < t[i].folds.length; n++)
                    e.push(t[i].folds[n]);
            return e
        }
        ,
        this.getFoldStringAt = function(e, t, i, n) {
            if (!(n = n || this.getFoldLine(e)))
                return null;
            for (var s, o, r = {
                end: {
                    column: 0
                }
            }, a = 0; a < n.folds.length; a++) {
                var l = (o = n.folds[a]).range.compareEnd(e, t);
                if (-1 == l) {
                    s = this.getLine(o.start.row).substring(r.end.column, o.start.column);
                    break
                }
                if (0 === l)
                    return null;
                r = o
            }
            return s = s || this.getLine(o.start.row).substring(r.end.column),
            -1 == i ? s.substring(0, t - r.end.column) : 1 == i ? s.substring(t - r.end.column) : s
        }
        ,
        this.getFoldLine = function(e, t) {
            var i = this.$foldData
              , n = 0;
            for (t && (n = i.indexOf(t)),
            -1 == n && (n = 0); n < i.length; n++) {
                var s = i[n];
                if (s.start.row <= e && s.end.row >= e)
                    return s;
                if (s.end.row > e)
                    return null
            }
            return null
        }
        ,
        this.getNextFoldLine = function(e, t) {
            var i = this.$foldData
              , n = 0;
            for (t && (n = i.indexOf(t)),
            -1 == n && (n = 0); n < i.length; n++) {
                var s = i[n];
                if (s.end.row >= e)
                    return s
            }
            return null
        }
        ,
        this.getFoldedRowCount = function(e, t) {
            for (var i = this.$foldData, n = t - e + 1, s = 0; s < i.length; s++) {
                var o = i[s]
                  , r = o.end.row
                  , a = o.start.row;
                if (t <= r) {
                    a < t && (e <= a ? n -= t - a : n = 0);
                    break
                }
                e <= r && (n -= e <= a ? r - a : r - e + 1)
            }
            return n
        }
        ,
        this.$addFoldLine = function(e) {
            return this.$foldData.push(e),
            this.$foldData.sort(function(e, t) {
                return e.start.row - t.start.row
            }),
            e
        }
        ,
        this.addFold = function(e, t) {
            var i, n = this.$foldData, s = !1;
            e instanceof p ? i = e : (i = new p(t,e)).collapseChildren = t.collapseChildren,
            this.$clipRangeToDocument(i.range);
            var o = i.start.row
              , r = i.start.column
              , a = i.end.row
              , l = i.end.column
              , h = this.getFoldAt(o, r, 1)
              , c = this.getFoldAt(a, l, -1);
            if (h && c == h)
                return h.addSubFold(i);
            h && !h.range.isStart(o, r) && this.removeFold(h),
            c && !c.range.isEnd(a, l) && this.removeFold(c);
            var u = this.getFoldsInRange(i.range);
            0 < u.length && (this.removeFolds(u),
            i.collapseChildren || u.forEach(function(e) {
                i.addSubFold(e)
            }));
            for (var d = 0; d < n.length; d++) {
                var g = n[d];
                if (a == g.start.row) {
                    g.addFold(i),
                    s = !0;
                    break
                }
                if (o == g.end.row) {
                    if (g.addFold(i),
                    s = !0,
                    !i.sameRow) {
                        var f = n[d + 1];
                        if (f && f.start.row == a) {
                            g.merge(f);
                            break
                        }
                    }
                    break
                }
                if (a <= g.start.row)
                    break
            }
            return s || (g = this.$addFoldLine(new m(this.$foldData,i))),
            this.$useWrapMode ? this.$updateWrapData(g.start.row, g.start.row) : this.$updateRowLengthCache(g.start.row, g.start.row),
            this.$modified = !0,
            this._signal("changeFold", {
                data: i,
                action: "add"
            }),
            i
        }
        ,
        this.addFolds = function(e) {
            e.forEach(function(e) {
                this.addFold(e)
            }, this)
        }
        ,
        this.removeFold = function(e) {
            var t, i = e.foldLine, n = i.start.row, s = i.end.row, o = this.$foldData, r = i.folds;
            1 == r.length ? o.splice(o.indexOf(i), 1) : i.range.isEnd(e.end.row, e.end.column) ? (r.pop(),
            i.end.row = r[r.length - 1].end.row,
            i.end.column = r[r.length - 1].end.column) : i.range.isStart(e.start.row, e.start.column) ? (r.shift(),
            i.start.row = r[0].start.row,
            i.start.column = r[0].start.column) : e.sameRow ? r.splice(r.indexOf(e), 1) : ((r = (t = i.split(e.start.row, e.start.column)).folds).shift(),
            t.start.row = r[0].start.row,
            t.start.column = r[0].start.column),
            this.$updating || (this.$useWrapMode ? this.$updateWrapData(n, s) : this.$updateRowLengthCache(n, s)),
            this.$modified = !0,
            this._signal("changeFold", {
                data: e,
                action: "remove"
            })
        }
        ,
        this.removeFolds = function(e) {
            for (var t = [], i = 0; i < e.length; i++)
                t.push(e[i]);
            t.forEach(function(e) {
                this.removeFold(e)
            }, this),
            this.$modified = !0
        }
        ,
        this.expandFold = function(t) {
            this.removeFold(t),
            t.subFolds.forEach(function(e) {
                t.restoreRange(e),
                this.addFold(e)
            }, this),
            0 < t.collapseChildren && this.foldAll(t.start.row + 1, t.end.row, t.collapseChildren - 1),
            t.subFolds = []
        }
        ,
        this.expandFolds = function(e) {
            e.forEach(function(e) {
                this.expandFold(e)
            }, this)
        }
        ,
        this.unfold = function(e, t) {
            var i, n;
            if (null == e ? (i = new c(0,0,this.getLength(),0),
            null == t && (t = !0)) : i = "number" == typeof e ? new c(e,0,e,this.getLine(e).length) : "row"in e ? c.fromPoints(e, e) : e,
            n = this.getFoldsInRangeList(i),
            0 != t ? this.removeFolds(n) : this.expandFolds(n),
            n.length)
                return n
        }
        ,
        this.isRowFolded = function(e, t) {
            return !!this.getFoldLine(e, t)
        }
        ,
        this.getRowFoldEnd = function(e, t) {
            var i = this.getFoldLine(e, t);
            return i ? i.end.row : e
        }
        ,
        this.getRowFoldStart = function(e, t) {
            var i = this.getFoldLine(e, t);
            return i ? i.start.row : e
        }
        ,
        this.getFoldDisplayLine = function(e, t, i, s, o) {
            null == s && (s = e.start.row),
            null == o && (o = 0),
            null == t && (t = e.end.row),
            null == i && (i = this.getLine(t).length);
            var r = this.doc
              , a = "";
            return e.walk(function(e, t, i, n) {
                if (!(t < s)) {
                    if (t == s) {
                        if (i < o)
                            return;
                        n = Math.max(o, n)
                    }
                    a += null != e ? e : r.getLine(t).substring(n, i)
                }
            }, t, i),
            a
        }
        ,
        this.getDisplayLine = function(e, t, i, n) {
            var s = this.getFoldLine(e);
            if (s)
                return this.getFoldDisplayLine(s, e, t, i, n);
            var o = this.doc.getLine(e);
            return o.substring(n || 0, t || o.length)
        }
        ,
        this.$cloneFoldData = function() {
            var i = [];
            return i = this.$foldData.map(function(e) {
                var t = e.folds.map(function(e) {
                    return e.clone()
                });
                return new m(i,t)
            })
        }
        ,
        this.toggleFold = function(e) {
            var t, i = this.selection.getRange();
            if (i.isEmpty()) {
                var n, s = i.start;
                if (n = this.getFoldAt(s.row, s.column))
                    return void this.expandFold(n);
                (t = this.findMatchingBracket(s)) ? 1 == i.comparePoint(t) ? i.end = t : (i.start = t,
                i.start.column++,
                i.end.column--) : (t = this.findMatchingBracket({
                    row: s.row,
                    column: s.column + 1
                })) ? (1 == i.comparePoint(t) ? i.end = t : i.start = t,
                i.start.column++) : i = this.getCommentFoldRange(s.row, s.column) || i
            } else {
                var o = this.getFoldsInRange(i);
                if (e && o.length)
                    return void this.expandFolds(o);
                1 == o.length && (n = o[0])
            }
            if ((n = n || this.getFoldAt(i.start.row, i.start.column)) && n.range.toString() == i.toString())
                this.expandFold(n);
            else {
                var r = "...";
                if (!i.isMultiLine()) {
                    if ((r = this.getTextRange(i)).length < 4)
                        return;
                    r = r.trim().substring(0, 2) + ".."
                }
                this.addFold(r, i)
            }
        }
        ,
        this.getCommentFoldRange = function(e, t, i) {
            var n = new u(this,e,t)
              , s = n.getCurrentToken()
              , o = s && s.type;
            if (s && /^comment|string/.test(o)) {
                "comment" == (o = o.match(/comment|string/)[0]) && (o += "|doc-start");
                var r = new RegExp(o)
                  , a = new c;
                if (1 != i) {
                    for (; (s = n.stepBackward()) && r.test(s.type); )
                        ;
                    n.stepForward()
                }
                if (a.start.row = n.getCurrentTokenRow(),
                a.start.column = n.getCurrentTokenColumn() + 2,
                n = new u(this,e,t),
                -1 != i) {
                    var l = -1;
                    do {
                        if (s = n.stepForward(),
                        -1 == l) {
                            var h = this.getState(n.$row);
                            r.test(h) || (l = n.$row)
                        } else if (n.$row > l)
                            break
                    } while (s && r.test(s.type));
                    s = n.stepBackward()
                } else
                    s = n.getCurrentToken();
                return a.end.row = n.getCurrentTokenRow(),
                a.end.column = n.getCurrentTokenColumn() + s.value.length - 2,
                a
            }
        }
        ,
        this.foldAll = function(e, t, i, n) {
            null == i && (i = 1e5);
            var s = this.foldWidgets;
            if (s) {
                t = t || this.getLength();
                for (var o, r = e = e || 0; r < t; r++) {
                    null == s[r] && (s[r] = this.getFoldWidget(r)),
                    "start" == s[r] && (n && !n(r) || (o = this.getFoldWidgetRange(r)) && o.isMultiLine() && o.end.row <= t && o.start.row >= e && (r = o.end.row,
                    o.collapseChildren = i,
                    this.addFold("...", o)))
                }
            }
        }
        ,
        this.foldToLevel = function(e) {
            for (this.foldAll(); 0 < e--; )
                this.unfold(null, !1)
        }
        ,
        this.foldAllComments = function() {
            var s = this;
            this.foldAll(null, null, null, function(e) {
                for (var t = s.getTokens(e), i = 0; i < t.length; i++) {
                    var n = t[i];
                    if ("text" != n.type || !/^\s+$/.test(n.value))
                        return !!/comment/.test(n.type)
                }
            })
        }
        ,
        this.$foldStyles = {
            manual: 1,
            markbegin: 1,
            markbeginend: 1
        },
        this.$foldStyle = "markbegin",
        this.setFoldStyle = function(e) {
            if (!this.$foldStyles[e])
                throw new Error("invalid fold style: " + e + "[" + Object.keys(this.$foldStyles).join(", ") + "]");
            var t;
            this.$foldStyle != e && ("manual" == (this.$foldStyle = e) && this.unfold(),
            t = this.$foldMode,
            this.$setFolding(null),
            this.$setFolding(t))
        }
        ,
        this.$setFolding = function(e) {
            this.$foldMode != e && (this.$foldMode = e,
            this.off("change", this.$updateFoldWidgets),
            this.off("tokenizerUpdate", this.$tokenizerUpdateFoldWidgets),
            this._signal("changeAnnotation"),
            e && "manual" != this.$foldStyle ? (this.foldWidgets = [],
            this.getFoldWidget = e.getFoldWidget.bind(e, this, this.$foldStyle),
            this.getFoldWidgetRange = e.getFoldWidgetRange.bind(e, this, this.$foldStyle),
            this.$updateFoldWidgets = this.updateFoldWidgets.bind(this),
            this.$tokenizerUpdateFoldWidgets = this.tokenizerUpdateFoldWidgets.bind(this),
            this.on("change", this.$updateFoldWidgets),
            this.on("tokenizerUpdate", this.$tokenizerUpdateFoldWidgets)) : this.foldWidgets = null)
        }
        ,
        this.getParentFoldRangeData = function(e, t) {
            var i = this.foldWidgets;
            if (!i || t && i[e])
                return {};
            for (var n = e - 1; 0 <= n; ) {
                var s = i[n];
                if (null == s && (s = i[n] = this.getFoldWidget(n)),
                "start" == s) {
                    var o = this.getFoldWidgetRange(n)
                      , r = r || o;
                    if (o && o.end.row >= e)
                        break
                }
                n--
            }
            return {
                range: -1 !== n && o,
                firstRange: r
            }
        }
        ,
        this.onFoldWidgetClick = function(e, t) {
            var i, n = {
                children: (t = t.domEvent).shiftKey,
                all: t.ctrlKey || t.metaKey,
                siblings: t.altKey
            };
            this.$toggleFoldWidget(e, n) || (i = t.target || t.srcElement) && /ace_fold-widget/.test(i.className) && (i.className += " ace_invalid")
        }
        ,
        this.$toggleFoldWidget = function(e, t) {
            if (this.getFoldWidget) {
                var i = this.getFoldWidget(e)
                  , n = this.getLine(e)
                  , s = "end" === i ? -1 : 1
                  , o = this.getFoldAt(e, -1 == s ? 0 : n.length, s);
                if (o)
                    return t.children || t.all ? this.removeFold(o) : this.expandFold(o),
                    o;
                var r, a, l, h = this.getFoldWidgetRange(e, !0);
                return h && !h.isMultiLine() && (o = this.getFoldAt(h.start.row, h.start.column, 1)) && h.isEqual(o.range) ? (this.removeFold(o),
                o) : (t.siblings ? ((r = this.getParentFoldRangeData(e)).range && (a = r.range.start.row + 1,
                l = r.range.end.row),
                this.foldAll(a, l, t.all ? 1e4 : 0)) : t.children ? (l = h ? h.end.row : this.getLength(),
                this.foldAll(e + 1, l, t.all ? 1e4 : 0)) : h && (t.all && (h.collapseChildren = 1e4),
                this.addFold("...", h)),
                h)
            }
        }
        ,
        this.toggleFoldWidget = function(e) {
            var t, i, n = this.selection.getCursor().row, n = this.getRowFoldStart(n), s = this.$toggleFoldWidget(n, {});
            s || (s = (t = this.getParentFoldRangeData(n, !0)).range || t.firstRange) && (n = s.start.row,
            (i = this.getFoldAt(n, this.getLine(n).length, 1)) ? this.removeFold(i) : this.addFold("...", s))
        }
        ,
        this.updateFoldWidgets = function(e) {
            var t, i = e.start.row, n = e.end.row - i;
            0 == n ? this.foldWidgets[i] = null : "remove" == e.action ? this.foldWidgets.splice(i, 1 + n, null) : ((t = Array(1 + n)).unshift(i, 1),
            this.foldWidgets.splice.apply(this.foldWidgets, t))
        }
        ,
        this.tokenizerUpdateFoldWidgets = function(e) {
            var t = e.data;
            t.first != t.last && this.foldWidgets.length > t.first && this.foldWidgets.splice(t.first, this.foldWidgets.length)
        }
    }
}),
define("ace/edit_session/bracket_match", ["require", "exports", "module", "ace/token_iterator", "ace/range"], function(e, t, i) {
    "use strict";
    var u = e("../token_iterator").TokenIterator
      , a = e("../range").Range;
    t.BracketMatch = function() {
        this.findMatchingBracket = function(e, t) {
            if (0 == e.column)
                return null;
            var i = t || this.getLine(e.row).charAt(e.column - 1);
            if ("" == i)
                return null;
            var n = i.match(/([\(\[\{])|([\)\]\}])/);
            return n ? n[1] ? this.$findClosingBracket(n[1], e) : this.$findOpeningBracket(n[2], e) : null
        }
        ,
        this.getBracketRange = function(e) {
            var t, i, n = this.getLine(e.row), s = !0, o = n.charAt(e.column - 1), r = o && o.match(/([\(\[\{])|([\)\]\}])/);
            if (r || (o = n.charAt(e.column),
            e = {
                row: e.row,
                column: e.column + 1
            },
            r = o && o.match(/([\(\[\{])|([\)\]\}])/),
            s = !1),
            !r)
                return null;
            if (r[1]) {
                if (!(i = this.$findClosingBracket(r[1], e)))
                    return null;
                t = a.fromPoints(e, i),
                s || (t.end.column++,
                t.start.column--),
                t.cursor = t.end
            } else {
                if (!(i = this.$findOpeningBracket(r[2], e)))
                    return null;
                t = a.fromPoints(i, e),
                s || (t.start.column++,
                t.end.column--),
                t.cursor = t.start
            }
            return t
        }
        ,
        this.getMatchingBracketRanges = function(e) {
            var t = this.getLine(e.row)
              , i = t.charAt(e.column - 1)
              , n = i && i.match(/([\(\[\{])|([\)\]\}])/);
            if (n || (i = t.charAt(e.column),
            e = {
                row: e.row,
                column: e.column + 1
            },
            n = i && i.match(/([\(\[\{])|([\)\]\}])/)),
            !n)
                return null;
            var s = new a(e.row,e.column - 1,e.row,e.column)
              , o = n[1] ? this.$findClosingBracket(n[1], e) : this.$findOpeningBracket(n[2], e);
            return o ? [s, new a(o.row,o.column,o.row,o.column + 1)] : [s]
        }
        ,
        this.$brackets = {
            ")": "(",
            "(": ")",
            "]": "[",
            "[": "]",
            "{": "}",
            "}": "{",
            "<": ">",
            ">": "<"
        },
        this.$findOpeningBracket = function(e, t, i) {
            var n = this.$brackets[e]
              , s = 1
              , o = new u(this,t.row,t.column)
              , r = o.getCurrentToken();
            if (r = r || o.stepForward()) {
                i = i || new RegExp("(\\.?" + r.type.replace(".", "\\.").replace("rparen", ".paren").replace(/\b(?:end)\b/, "(?:start|begin|end)") + ")+");
                for (var a = t.column - o.getCurrentTokenColumn() - 2, l = r.value; ; ) {
                    for (; 0 <= a; ) {
                        var h = l.charAt(a);
                        if (h == n) {
                            if (0 == --s)
                                return {
                                    row: o.getCurrentTokenRow(),
                                    column: a + o.getCurrentTokenColumn()
                                }
                        } else
                            h == e && (s += 1);
                        --a
                    }
                    for (; (r = o.stepBackward()) && !i.test(r.type); )
                        ;
                    if (null == r)
                        break;
                    a = (l = r.value).length - 1
                }
                return null
            }
        }
        ,
        this.$findClosingBracket = function(e, t, i) {
            var n = this.$brackets[e]
              , s = 1
              , o = new u(this,t.row,t.column)
              , r = o.getCurrentToken();
            if (r = r || o.stepForward()) {
                i = i || new RegExp("(\\.?" + r.type.replace(".", "\\.").replace("lparen", ".paren").replace(/\b(?:start|begin)\b/, "(?:start|begin|end)") + ")+");
                for (var a = t.column - o.getCurrentTokenColumn(); ; ) {
                    for (var l = r.value, h = l.length; a < h; ) {
                        var c = l.charAt(a);
                        if (c == n) {
                            if (0 == --s)
                                return {
                                    row: o.getCurrentTokenRow(),
                                    column: a + o.getCurrentTokenColumn()
                                }
                        } else
                            c == e && (s += 1);
                        a += 1
                    }
                    for (; (r = o.stepForward()) && !i.test(r.type); )
                        ;
                    if (null == r)
                        break;
                    a = 0
                }
                return null
            }
        }
    }
}),
define("ace/edit_session", ["require", "exports", "module", "ace/lib/oop", "ace/lib/lang", "ace/bidihandler", "ace/config", "ace/lib/event_emitter", "ace/selection", "ace/mode/text", "ace/range", "ace/document", "ace/background_tokenizer", "ace/search_highlight", "ace/edit_session/folding", "ace/edit_session/bracket_match"], function(e, t, i) {
    "use strict";
    var n = e("./lib/oop")
      , s = e("./lib/lang")
      , o = e("./bidihandler").BidiHandler
      , r = e("./config")
      , l = e("./lib/event_emitter").EventEmitter
      , a = e("./selection").Selection
      , h = e("./mode/text").Mode
      , c = e("./range").Range
      , u = e("./document").Document
      , d = e("./background_tokenizer").BackgroundTokenizer
      , g = e("./search_highlight").SearchHighlight
      , f = function(e, t) {
        this.$breakpoints = [],
        this.$decorations = [],
        this.$frontMarkers = {},
        this.$backMarkers = {},
        this.$markerId = 1,
        this.$undoSelect = !0,
        this.$foldData = [],
        this.id = "session" + ++f.$uid,
        this.$foldData.toString = function() {
            return this.join("\n")
        }
        ,
        this.on("changeFold", this.onChangeFold.bind(this)),
        this.$onChange = this.onChange.bind(this),
        "object" == typeof e && e.getLine || (e = new u(e)),
        this.setDocument(e),
        this.selection = new a(this),
        this.$bidiHandler = new o(this),
        r.resetOptions(this),
        this.setMode(t),
        r._signal("session", this)
    };
    f.$uid = 0,
    function() {
        function a(e) {
            return !(e < 4352) && (4352 <= e && e <= 4447 || 4515 <= e && e <= 4519 || 4602 <= e && e <= 4607 || 9001 <= e && e <= 9002 || 11904 <= e && e <= 11929 || 11931 <= e && e <= 12019 || 12032 <= e && e <= 12245 || 12272 <= e && e <= 12283 || 12288 <= e && e <= 12350 || 12353 <= e && e <= 12438 || 12441 <= e && e <= 12543 || 12549 <= e && e <= 12589 || 12593 <= e && e <= 12686 || 12688 <= e && e <= 12730 || 12736 <= e && e <= 12771 || 12784 <= e && e <= 12830 || 12832 <= e && e <= 12871 || 12880 <= e && e <= 13054 || 13056 <= e && e <= 19903 || 19968 <= e && e <= 42124 || 42128 <= e && e <= 42182 || 43360 <= e && e <= 43388 || 44032 <= e && e <= 55203 || 55216 <= e && e <= 55238 || 55243 <= e && e <= 55291 || 63744 <= e && e <= 64255 || 65040 <= e && e <= 65049 || 65072 <= e && e <= 65106 || 65108 <= e && e <= 65126 || 65128 <= e && e <= 65131 || 65281 <= e && e <= 65376 || 65504 <= e && e <= 65510)
        }
        n.implement(this, l),
        this.setDocument = function(e) {
            this.doc && this.doc.removeListener("change", this.$onChange),
            (this.doc = e).on("change", this.$onChange),
            this.bgTokenizer && this.bgTokenizer.setDocument(this.getDocument()),
            this.resetCaches()
        }
        ,
        this.getDocument = function() {
            return this.doc
        }
        ,
        this.$resetRowCache = function(e) {
            if (!e)
                return this.$docRowCache = [],
                void (this.$screenRowCache = []);
            var t = this.$docRowCache.length
              , i = this.$getRowCacheIndex(this.$docRowCache, e) + 1;
            i < t && (this.$docRowCache.splice(i, t),
            this.$screenRowCache.splice(i, t))
        }
        ,
        this.$getRowCacheIndex = function(e, t) {
            for (var i = 0, n = e.length - 1; i <= n; ) {
                var s = i + n >> 1
                  , o = e[s];
                if (o < t)
                    i = 1 + s;
                else {
                    if (!(t < o))
                        return s;
                    n = s - 1
                }
            }
            return i - 1
        }
        ,
        this.resetCaches = function() {
            this.$modified = !0,
            this.$wrapData = [],
            this.$rowLengthCache = [],
            this.$resetRowCache(0),
            this.bgTokenizer && this.bgTokenizer.start(0)
        }
        ,
        this.onChangeFold = function(e) {
            var t = e.data;
            this.$resetRowCache(t.start.row)
        }
        ,
        this.onChange = function(e) {
            this.$modified = !0,
            this.$bidiHandler.onChange(e),
            this.$resetRowCache(e.start.row);
            var t = this.$updateInternalDataOnChange(e);
            !this.$fromUndo && this.$undoManager && (t && t.length && (this.$undoManager.add({
                action: "removeFolds",
                folds: t
            }, this.mergeUndoDeltas),
            this.mergeUndoDeltas = !0),
            this.$undoManager.add(e, this.mergeUndoDeltas),
            this.mergeUndoDeltas = !0,
            this.$informUndoManager.schedule()),
            this.bgTokenizer && this.bgTokenizer.$updateOnChange(e),
            this._signal("change", e)
        }
        ,
        this.setValue = function(e) {
            this.doc.setValue(e),
            this.selection.moveTo(0, 0),
            this.$resetRowCache(0),
            this.setUndoManager(this.$undoManager),
            this.getUndoManager().reset()
        }
        ,
        this.getValue = this.toString = function() {
            return this.doc.getValue()
        }
        ,
        this.getSelection = function() {
            return this.selection
        }
        ,
        this.getState = function(e) {
            return this.bgTokenizer.getState(e)
        }
        ,
        this.getTokens = function(e) {
            return this.bgTokenizer.getTokens(e)
        }
        ,
        this.getTokenAt = function(e, t) {
            var i, n = this.bgTokenizer.getTokens(e), s = 0;
            if (null == t)
                var o = n.length - 1
                  , s = this.getLine(e).length;
            else
                for (o = 0; o < n.length && !(t <= (s += n[o].value.length)); o++)
                    ;
            return (i = n[o]) ? (i.index = o,
            i.start = s - i.value.length,
            i) : null
        }
        ,
        this.setUndoManager = function(e) {
            var t;
            this.$undoManager = e,
            this.$informUndoManager && this.$informUndoManager.cancel(),
            e ? (t = this,
            e.addSession(this),
            this.$syncInformUndoManager = function() {
                t.$informUndoManager.cancel(),
                t.mergeUndoDeltas = !1
            }
            ,
            this.$informUndoManager = s.delayedCall(this.$syncInformUndoManager)) : this.$syncInformUndoManager = function() {}
        }
        ,
        this.markUndoGroup = function() {
            this.$syncInformUndoManager && this.$syncInformUndoManager()
        }
        ,
        this.$defaultUndoManager = {
            undo: function() {},
            redo: function() {},
            hasUndo: function() {},
            hasRedo: function() {},
            reset: function() {},
            add: function() {},
            addSelection: function() {},
            startNewGroup: function() {},
            addSession: function() {}
        },
        this.getUndoManager = function() {
            return this.$undoManager || this.$defaultUndoManager
        }
        ,
        this.getTabString = function() {
            return this.getUseSoftTabs() ? s.stringRepeat(" ", this.getTabSize()) : "\t"
        }
        ,
        this.setUseSoftTabs = function(e) {
            this.setOption("useSoftTabs", e)
        }
        ,
        this.getUseSoftTabs = function() {
            return this.$useSoftTabs && !this.$mode.$indentWithTabs
        }
        ,
        this.setTabSize = function(e) {
            this.setOption("tabSize", e)
        }
        ,
        this.getTabSize = function() {
            return this.$tabSize
        }
        ,
        this.isTabStop = function(e) {
            return this.$useSoftTabs && e.column % this.$tabSize == 0
        }
        ,
        this.setNavigateWithinSoftTabs = function(e) {
            this.setOption("navigateWithinSoftTabs", e)
        }
        ,
        this.getNavigateWithinSoftTabs = function() {
            return this.$navigateWithinSoftTabs
        }
        ,
        this.$overwrite = !1,
        this.setOverwrite = function(e) {
            this.setOption("overwrite", e)
        }
        ,
        this.getOverwrite = function() {
            return this.$overwrite
        }
        ,
        this.toggleOverwrite = function() {
            this.setOverwrite(!this.$overwrite)
        }
        ,
        this.addGutterDecoration = function(e, t) {
            this.$decorations[e] || (this.$decorations[e] = ""),
            this.$decorations[e] += " " + t,
            this._signal("changeBreakpoint", {})
        }
        ,
        this.removeGutterDecoration = function(e, t) {
            this.$decorations[e] = (this.$decorations[e] || "").replace(" " + t, ""),
            this._signal("changeBreakpoint", {})
        }
        ,
        this.getBreakpoints = function() {
            return this.$breakpoints
        }
        ,
        this.setBreakpoints = function(e) {
            this.$breakpoints = [];
            for (var t = 0; t < e.length; t++)
                this.$breakpoints[e[t]] = "ace_breakpoint";
            this._signal("changeBreakpoint", {})
        }
        ,
        this.clearBreakpoints = function() {
            this.$breakpoints = [],
            this._signal("changeBreakpoint", {})
        }
        ,
        this.setBreakpoint = function(e, t) {
            void 0 === t && (t = "ace_breakpoint"),
            t ? this.$breakpoints[e] = t : delete this.$breakpoints[e],
            this._signal("changeBreakpoint", {})
        }
        ,
        this.clearBreakpoint = function(e) {
            delete this.$breakpoints[e],
            this._signal("changeBreakpoint", {})
        }
        ,
        this.addMarker = function(e, t, i, n) {
            var s = this.$markerId++
              , o = {
                range: e,
                type: i || "line",
                renderer: "function" == typeof i ? i : null,
                clazz: t,
                inFront: !!n,
                id: s
            };
            return n ? (this.$frontMarkers[s] = o,
            this._signal("changeFrontMarker")) : (this.$backMarkers[s] = o,
            this._signal("changeBackMarker")),
            s
        }
        ,
        this.addDynamicMarker = function(e, t) {
            if (e.update) {
                var i = this.$markerId++;
                return e.id = i,
                e.inFront = !!t,
                t ? (this.$frontMarkers[i] = e,
                this._signal("changeFrontMarker")) : (this.$backMarkers[i] = e,
                this._signal("changeBackMarker")),
                e
            }
        }
        ,
        this.removeMarker = function(e) {
            var t = this.$frontMarkers[e] || this.$backMarkers[e];
            t && (delete (t.inFront ? this.$frontMarkers : this.$backMarkers)[e],
            this._signal(t.inFront ? "changeFrontMarker" : "changeBackMarker"))
        }
        ,
        this.getMarkers = function(e) {
            return e ? this.$frontMarkers : this.$backMarkers
        }
        ,
        this.highlight = function(e) {
            var t;
            this.$searchHighlight || (t = new g(null,"ace_selected-word","text"),
            this.$searchHighlight = this.addDynamicMarker(t)),
            this.$searchHighlight.setRegexp(e)
        }
        ,
        this.highlightLines = function(e, t, i, n) {
            "number" != typeof t && (i = t,
            t = e),
            i = i || "ace_step";
            var s = new c(e,0,t,1 / 0);
            return s.id = this.addMarker(s, i, "fullLine", n),
            s
        }
        ,
        this.setAnnotations = function(e) {
            this.$annotations = e,
            this._signal("changeAnnotation", {})
        }
        ,
        this.getAnnotations = function() {
            return this.$annotations || []
        }
        ,
        this.clearAnnotations = function() {
            this.setAnnotations([])
        }
        ,
        this.$detectNewLine = function(e) {
            var t = e.match(/^.*?(\r?\n)/m);
            this.$autoNewLine = t ? t[1] : "\n"
        }
        ,
        this.getWordRange = function(e, t) {
            var i, n = this.getLine(e), s = !1;
            0 < t && (s = !!n.charAt(t - 1).match(this.tokenRe)),
            i = (s = s || !!n.charAt(t).match(this.tokenRe)) ? this.tokenRe : /^\s+$/.test(n.slice(t - 1, t + 1)) ? /\s/ : this.nonTokenRe;
            var o = t;
            if (0 < o) {
                for (; 0 <= --o && n.charAt(o).match(i); )
                    ;
                o++
            }
            for (var r = t; r < n.length && n.charAt(r).match(i); )
                r++;
            return new c(e,o,e,r)
        }
        ,
        this.getAWordRange = function(e, t) {
            for (var i = this.getWordRange(e, t), n = this.getLine(i.end.row); n.charAt(i.end.column).match(/[ \t]/); )
                i.end.column += 1;
            return i
        }
        ,
        this.setNewLineMode = function(e) {
            this.doc.setNewLineMode(e)
        }
        ,
        this.getNewLineMode = function() {
            return this.doc.getNewLineMode()
        }
        ,
        this.setUseWorker = function(e) {
            this.setOption("useWorker", e)
        }
        ,
        this.getUseWorker = function() {
            return this.$useWorker
        }
        ,
        this.onReloadTokenizer = function(e) {
            var t = e.data;
            this.bgTokenizer.start(t.first),
            this._signal("tokenizerUpdate", e)
        }
        ,
        this.$modes = r.$modes,
        this.$mode = null,
        this.$modeId = null,
        this.setMode = function(e, t) {
            if (e && "object" == typeof e) {
                if (e.getTokenizer)
                    return this.$onChangeMode(e);
                var i = e
                  , n = i.path
            } else
                n = e || "ace/mode/text";
            if (this.$modes["ace/mode/text"] || (this.$modes["ace/mode/text"] = new h),
            this.$modes[n] && !i)
                return this.$onChangeMode(this.$modes[n]),
                void (t && t());
            this.$modeId = n,
            r.loadModule(["mode", n], function(e) {
                if (this.$modeId !== n)
                    return t && t();
                this.$modes[n] && !i ? this.$onChangeMode(this.$modes[n]) : e && e.Mode && (e = new e.Mode(i),
                i || ((this.$modes[n] = e).$id = n),
                this.$onChangeMode(e)),
                t && t()
            }
            .bind(this)),
            this.$mode || this.$onChangeMode(this.$modes["ace/mode/text"], !0)
        }
        ,
        this.$onChangeMode = function(e, t) {
            var i, n, s, o;
            t || (this.$modeId = e.$id),
            this.$mode !== e && (i = this.$mode,
            this.$mode = e,
            this.$stopWorker(),
            this.$useWorker && this.$startWorker(),
            void 0 !== (n = e.getTokenizer()).on && (s = this.onReloadTokenizer.bind(this),
            n.on("update", s)),
            this.bgTokenizer ? this.bgTokenizer.setTokenizer(n) : (this.bgTokenizer = new d(n),
            (o = this).bgTokenizer.on("update", function(e) {
                o._signal("tokenizerUpdate", e)
            })),
            this.bgTokenizer.setDocument(this.getDocument()),
            this.tokenRe = e.tokenRe,
            this.nonTokenRe = e.nonTokenRe,
            t || (e.attachToSession && e.attachToSession(this),
            this.$options.wrapMethod.set.call(this, this.$wrapMethod),
            this.$setFolding(e.foldingRules),
            this.bgTokenizer.start(0),
            this._emit("changeMode", {
                oldMode: i,
                mode: e
            })))
        }
        ,
        this.$stopWorker = function() {
            this.$worker && (this.$worker.terminate(),
            this.$worker = null)
        }
        ,
        this.$startWorker = function() {
            try {
                this.$worker = this.$mode.createWorker(this)
            } catch (e) {
                r.warn("Could not load worker", e),
                this.$worker = null
            }
        }
        ,
        this.getMode = function() {
            return this.$mode
        }
        ,
        this.$scrollTop = 0,
        this.setScrollTop = function(e) {
            this.$scrollTop === e || isNaN(e) || (this.$scrollTop = e,
            this._signal("changeScrollTop", e))
        }
        ,
        this.getScrollTop = function() {
            return this.$scrollTop
        }
        ,
        this.$scrollLeft = 0,
        this.setScrollLeft = function(e) {
            this.$scrollLeft === e || isNaN(e) || (this.$scrollLeft = e,
            this._signal("changeScrollLeft", e))
        }
        ,
        this.getScrollLeft = function() {
            return this.$scrollLeft
        }
        ,
        this.getScreenWidth = function() {
            return this.$computeWidth(),
            this.lineWidgets ? Math.max(this.getLineWidgetMaxWidth(), this.screenWidth) : this.screenWidth
        }
        ,
        this.getLineWidgetMaxWidth = function() {
            if (null != this.lineWidgetsWidth)
                return this.lineWidgetsWidth;
            var t = 0;
            return this.lineWidgets.forEach(function(e) {
                e && e.screenWidth > t && (t = e.screenWidth)
            }),
            this.lineWidgetWidth = t
        }
        ,
        this.$computeWidth = function(e) {
            if (this.$modified || e) {
                if (this.$modified = !1,
                this.$useWrapMode)
                    return this.screenWidth = this.$wrapLimit;
                for (var t = this.doc.getAllLines(), i = this.$rowLengthCache, n = 0, s = 0, o = this.$foldData[s], r = o ? o.start.row : 1 / 0, a = t.length, l = 0; l < a; l++) {
                    if (r < l) {
                        if (a <= (l = o.end.row + 1))
                            break;
                        r = (o = this.$foldData[s++]) ? o.start.row : 1 / 0
                    }
                    null == i[l] && (i[l] = this.$getStringScreenWidth(t[l])[0]),
                    i[l] > n && (n = i[l])
                }
                this.screenWidth = n
            }
        }
        ,
        this.getLine = function(e) {
            return this.doc.getLine(e)
        }
        ,
        this.getLines = function(e, t) {
            return this.doc.getLines(e, t)
        }
        ,
        this.getLength = function() {
            return this.doc.getLength()
        }
        ,
        this.getTextRange = function(e) {
            return this.doc.getTextRange(e || this.selection.getRange())
        }
        ,
        this.insert = function(e, t) {
            return this.doc.insert(e, t)
        }
        ,
        this.remove = function(e) {
            return this.doc.remove(e)
        }
        ,
        this.removeFullLines = function(e, t) {
            return this.doc.removeFullLines(e, t)
        }
        ,
        this.undoChanges = function(e, t) {
            if (e.length) {
                this.$fromUndo = !0;
                for (var i = e.length - 1; -1 != i; i--) {
                    var n = e[i];
                    "insert" == n.action || "remove" == n.action ? this.doc.revertDelta(n) : n.folds && this.addFolds(n.folds)
                }
                !t && this.$undoSelect && (e.selectionBefore ? this.selection.fromJSON(e.selectionBefore) : this.selection.setRange(this.$getUndoSelection(e, !0))),
                this.$fromUndo = !1
            }
        }
        ,
        this.redoChanges = function(e, t) {
            if (e.length) {
                this.$fromUndo = !0;
                for (var i = 0; i < e.length; i++) {
                    var n = e[i];
                    "insert" != n.action && "remove" != n.action || this.doc.$safeApplyDelta(n)
                }
                !t && this.$undoSelect && (e.selectionAfter ? this.selection.fromJSON(e.selectionAfter) : this.selection.setRange(this.$getUndoSelection(e, !1))),
                this.$fromUndo = !1
            }
        }
        ,
        this.setUndoSelect = function(e) {
            this.$undoSelect = e
        }
        ,
        this.$getUndoSelection = function(e, t) {
            function i(e) {
                return t ? "insert" !== e.action : "insert" === e.action
            }
            for (var n, s, o = 0; o < e.length; o++) {
                var r = e[o];
                r.start && (n ? i(r) ? (s = r.start,
                -1 == n.compare(s.row, s.column) && n.setStart(s),
                s = r.end,
                1 == n.compare(s.row, s.column) && n.setEnd(s)) : (s = r.start,
                -1 == n.compare(s.row, s.column) && (n = c.fromPoints(r.start, r.start))) : n = i(r) ? c.fromPoints(r.start, r.end) : c.fromPoints(r.start, r.start))
            }
            return n
        }
        ,
        this.replace = function(e, t) {
            return this.doc.replace(e, t)
        }
        ,
        this.moveText = function(e, t, i) {
            var n, s, o, r, a = this.getTextRange(e), l = this.getFoldsInRange(e), h = c.fromPoints(t, t);
            return i || (this.remove(e),
            o = e.start.row - e.end.row,
            (r = o ? -e.end.column : e.start.column - e.end.column) && (h.start.row == e.end.row && h.start.column > e.end.column && (h.start.column += r),
            h.end.row == e.end.row && h.end.column > e.end.column && (h.end.column += r)),
            o && h.start.row >= e.end.row && (h.start.row += o,
            h.end.row += o)),
            h.end = this.insert(h.start, a),
            l.length && (n = e.start,
            s = h.start,
            o = s.row - n.row,
            r = s.column - n.column,
            this.addFolds(l.map(function(e) {
                return (e = e.clone()).start.row == n.row && (e.start.column += r),
                e.end.row == n.row && (e.end.column += r),
                e.start.row += o,
                e.end.row += o,
                e
            }))),
            h
        }
        ,
        this.indentRows = function(e, t, i) {
            i = i.replace(/\t/g, this.getTabString());
            for (var n = e; n <= t; n++)
                this.doc.insertInLine({
                    row: n,
                    column: 0
                }, i)
        }
        ,
        this.outdentRows = function(e) {
            for (var t = e.collapseRows(), i = new c(0,0,0,0), n = this.getTabSize(), s = t.start.row; s <= t.end.row; ++s) {
                var o = this.getLine(s);
                i.start.row = s,
                i.end.row = s;
                for (var r = 0; r < n && " " == o.charAt(r); ++r)
                    ;
                r < n && "\t" == o.charAt(r) ? (i.start.column = r,
                i.end.column = r + 1) : (i.start.column = 0,
                i.end.column = r),
                this.remove(i)
            }
        }
        ,
        this.$moveLines = function(e, t, i) {
            if (e = this.getRowFoldStart(e),
            t = this.getRowFoldEnd(t),
            i < 0) {
                if ((s = this.getRowFoldStart(e + i)) < 0)
                    return 0;
                var n = s - e
            } else if (0 < i) {
                var s;
                if ((s = this.getRowFoldEnd(t + i)) > this.doc.getLength() - 1)
                    return 0;
                n = s - t
            } else {
                e = this.$clipRowToDocument(e);
                n = (t = this.$clipRowToDocument(t)) - e + 1
            }
            var o = new c(e,0,t,Number.MAX_VALUE)
              , r = this.getFoldsInRange(o).map(function(e) {
                return (e = e.clone()).start.row += n,
                e.end.row += n,
                e
            })
              , a = 0 == i ? this.doc.getLines(e, t) : this.doc.removeFullLines(e, t);
            return this.doc.insertFullLines(e + n, a),
            r.length && this.addFolds(r),
            n
        }
        ,
        this.moveLinesUp = function(e, t) {
            return this.$moveLines(e, t, -1)
        }
        ,
        this.moveLinesDown = function(e, t) {
            return this.$moveLines(e, t, 1)
        }
        ,
        this.duplicateLines = function(e, t) {
            return this.$moveLines(e, t, 0)
        }
        ,
        this.$clipRowToDocument = function(e) {
            return Math.max(0, Math.min(e, this.doc.getLength() - 1))
        }
        ,
        this.$clipColumnToRow = function(e, t) {
            return t < 0 ? 0 : Math.min(this.doc.getLine(e).length, t)
        }
        ,
        this.$clipPositionToDocument = function(e, t) {
            var i;
            return t = Math.max(0, t),
            t = e < 0 ? e = 0 : (i = this.doc.getLength()) <= e ? (e = i - 1,
            this.doc.getLine(i - 1).length) : Math.min(this.doc.getLine(e).length, t),
            {
                row: e,
                column: t
            }
        }
        ,
        this.$clipRangeToDocument = function(e) {
            e.start.row < 0 ? (e.start.row = 0,
            e.start.column = 0) : e.start.column = this.$clipColumnToRow(e.start.row, e.start.column);
            var t = this.doc.getLength() - 1;
            return e.end.row > t ? (e.end.row = t,
            e.end.column = this.doc.getLine(t).length) : e.end.column = this.$clipColumnToRow(e.end.row, e.end.column),
            e
        }
        ,
        this.$wrapLimit = 80,
        this.$useWrapMode = !1,
        this.$wrapLimitRange = {
            min: null,
            max: null
        },
        this.setUseWrapMode = function(e) {
            var t;
            e != this.$useWrapMode && (this.$useWrapMode = e,
            this.$modified = !0,
            this.$resetRowCache(0),
            e && (t = this.getLength(),
            this.$wrapData = Array(t),
            this.$updateWrapData(0, t - 1)),
            this._signal("changeWrapMode"))
        }
        ,
        this.getUseWrapMode = function() {
            return this.$useWrapMode
        }
        ,
        this.setWrapLimitRange = function(e, t) {
            this.$wrapLimitRange.min === e && this.$wrapLimitRange.max === t || (this.$wrapLimitRange = {
                min: e,
                max: t
            },
            this.$modified = !0,
            this.$bidiHandler.markAsDirty(),
            this.$useWrapMode && this._signal("changeWrapMode"))
        }
        ,
        this.adjustWrapLimit = function(e, t) {
            var i = this.$wrapLimitRange;
            i.max < 0 && (i = {
                min: t,
                max: t
            });
            var n = this.$constrainWrapLimit(e, i.min, i.max);
            return n != this.$wrapLimit && 1 < n && (this.$wrapLimit = n,
            this.$modified = !0,
            this.$useWrapMode && (this.$updateWrapData(0, this.getLength() - 1),
            this.$resetRowCache(0),
            this._signal("changeWrapLimit")),
            !0)
        }
        ,
        this.$constrainWrapLimit = function(e, t, i) {
            return t && (e = Math.max(t, e)),
            i && (e = Math.min(i, e)),
            e
        }
        ,
        this.getWrapLimit = function() {
            return this.$wrapLimit
        }
        ,
        this.setWrapLimit = function(e) {
            this.setWrapLimitRange(e, e)
        }
        ,
        this.getWrapLimitRange = function() {
            return {
                min: this.$wrapLimitRange.min,
                max: this.$wrapLimitRange.max
            }
        }
        ,
        this.$updateInternalDataOnChange = function(e) {
            var t = this.$useWrapMode
              , i = e.action
              , n = e.start
              , s = e.end
              , o = n.row
              , r = s.row
              , a = r - o
              , l = null;
            if (this.$updating = !0,
            0 != a)
                if ("remove" === i) {
                    this[t ? "$wrapData" : "$rowLengthCache"].splice(o, a);
                    var h = this.$foldData
                      , l = this.getFoldsInRange(e);
                    this.removeFolds(l);
                    var c, u = 0;
                    for ((m = this.getFoldLine(s.row)) && (m.addRemoveChars(s.row, s.column, n.column - s.column),
                    m.shiftRow(-a),
                    (c = this.getFoldLine(o)) && c !== m && (c.merge(m),
                    m = c),
                    u = h.indexOf(m) + 1); u < h.length; u++) {
                        (m = h[u]).start.row >= s.row && m.shiftRow(-a)
                    }
                    r = o
                } else {
                    var d = Array(a);
                    d.unshift(o, 0);
                    var g = t ? this.$wrapData : this.$rowLengthCache;
                    g.splice.apply(g, d);
                    var f, h = this.$foldData, u = 0;
                    for ((m = this.getFoldLine(o)) && (0 == (f = m.range.compareInside(n.row, n.column)) ? (m = m.split(n.row, n.column)) && (m.shiftRow(a),
                    m.addRemoveChars(r, 0, s.column - n.column)) : -1 == f && (m.addRemoveChars(o, 0, s.column - n.column),
                    m.shiftRow(a)),
                    u = h.indexOf(m) + 1); u < h.length; u++) {
                        (m = h[u]).start.row >= o && m.shiftRow(a)
                    }
                }
            else {
                var m, a = Math.abs(e.start.column - e.end.column);
                "remove" === i && (l = this.getFoldsInRange(e),
                this.removeFolds(l),
                a = -a),
                (m = this.getFoldLine(o)) && m.addRemoveChars(o, n.column, a)
            }
            return t && this.$wrapData.length != this.doc.getLength() && console.error("doc.getLength() and $wrapData.length have to be the same!"),
            this.$updating = !1,
            t ? this.$updateWrapData(o, r) : this.$updateRowLengthCache(o, r),
            l
        }
        ,
        this.$updateRowLengthCache = function(e, t, i) {
            this.$rowLengthCache[e] = null,
            this.$rowLengthCache[t] = null
        }
        ,
        this.$updateWrapData = function(e, t) {
            var r, i, a = this.doc.getAllLines(), n = this.getTabSize(), s = this.$wrapData, o = this.$wrapLimit, l = e;
            for (t = Math.min(t, a.length - 1); l <= t; )
                (i = this.getFoldLine(l, i)) ? (r = [],
                i.walk(function(e, t, i, n) {
                    var s;
                    if (null != e) {
                        (s = this.$getDisplayTokens(e, r.length))[0] = f;
                        for (var o = 1; o < s.length; o++)
                            s[o] = m
                    } else
                        s = this.$getDisplayTokens(a[t].substring(n, i), r.length);
                    r = r.concat(s)
                }
                .bind(this), i.end.row, a[i.end.row].length + 1),
                s[i.start.row] = this.$computeWrapSplits(r, o, n),
                l = i.end.row + 1) : (r = this.$getDisplayTokens(a[l]),
                s[l] = this.$computeWrapSplits(r, o, n),
                l++)
        }
        ;
        var f = 3
          , m = 4;
        this.$computeWrapSplits = function(s, e, o) {
            function t(e) {
                for (var t = e - a, i = a; i < e; i++) {
                    var n = s[i];
                    12 !== n && 2 !== n || --t
                }
                r.length || (d = function() {
                    var e = 0;
                    if (0 === u)
                        return e;
                    if (c)
                        for (var t = 0; t < s.length; t++) {
                            var i = s[t];
                            if (10 == i)
                                e += 1;
                            else {
                                if (11 != i) {
                                    if (12 == i)
                                        continue;
                                    break
                                }
                                e += o
                            }
                        }
                    return h && !1 !== c && (e += o),
                    Math.min(e, u)
                }(),
                r.indent = d),
                l += t,
                r.push(l),
                a = e
            }
            if (0 == s.length)
                return [];
            for (var r = [], i = s.length, a = 0, l = 0, h = this.$wrapAsCode, c = this.$indentedSoftWrap, u = e <= Math.max(2 * o, 8) || !1 === c ? 0 : Math.floor(e / 2), d = 0; e - d < i - a; ) {
                var n = a + e - d;
                if (10 <= s[n - 1] && 10 <= s[n])
                    t(n);
                else if (s[n] != f && s[n] != m) {
                    for (var g = Math.max(n - (e - (e >> 2)), a - 1); g < n && s[n] < f; )
                        n--;
                    if (h) {
                        for (; g < n && s[n] < f; )
                            n--;
                        for (; g < n && 9 == s[n]; )
                            n--
                    } else
                        for (; g < n && s[n] < 10; )
                            n--;
                    g < n ? t(++n) : (2 == s[n = a + e] && n--,
                    t(n - d))
                } else {
                    for (; n != a - 1 && s[n] != f; n--)
                        ;
                    if (a < n) {
                        t(n);
                        continue
                    }
                    for (n = a + e; n < s.length && s[n] == m; n++)
                        ;
                    if (n == s.length)
                        break;
                    t(n)
                }
            }
            return r
        }
        ,
        this.$getDisplayTokens = function(e, t) {
            var i, n = [];
            t = t || 0;
            for (var s = 0; s < e.length; s++) {
                var o = e.charCodeAt(s);
                if (9 == o) {
                    i = this.getScreenTabSize(n.length + t),
                    n.push(11);
                    for (var r = 1; r < i; r++)
                        n.push(12)
                } else
                    32 == o ? n.push(10) : 39 < o && o < 48 || 57 < o && o < 64 ? n.push(9) : 4352 <= o && a(o) ? n.push(1, 2) : n.push(1)
            }
            return n
        }
        ,
        this.$getStringScreenWidth = function(e, t, i) {
            if (0 == t)
                return [0, 0];
            var n, s;
            for (null == t && (t = 1 / 0),
            i = i || 0,
            s = 0; s < e.length && (9 == (n = e.charCodeAt(s)) ? i += this.getScreenTabSize(i) : 4352 <= n && a(n) ? i += 2 : i += 1,
            !(t < i)); s++)
                ;
            return [i, s]
        }
        ,
        this.lineWidgets = null,
        this.getRowLength = function(e) {
            var t = 1;
            return this.lineWidgets && (t += this.lineWidgets[e] && this.lineWidgets[e].rowCount || 0),
            this.$useWrapMode && this.$wrapData[e] ? this.$wrapData[e].length + t : t
        }
        ,
        this.getRowLineCount = function(e) {
            return this.$useWrapMode && this.$wrapData[e] ? this.$wrapData[e].length + 1 : 1
        }
        ,
        this.getRowWrapIndent = function(e) {
            if (this.$useWrapMode) {
                var t = this.screenToDocumentPosition(e, Number.MAX_VALUE)
                  , i = this.$wrapData[t.row];
                return i.length && i[0] < t.column ? i.indent : 0
            }
            return 0
        }
        ,
        this.getScreenLastRowColumn = function(e) {
            var t = this.screenToDocumentPosition(e, Number.MAX_VALUE);
            return this.documentToScreenColumn(t.row, t.column)
        }
        ,
        this.getDocumentLastRowColumn = function(e, t) {
            var i = this.documentToScreenRow(e, t);
            return this.getScreenLastRowColumn(i)
        }
        ,
        this.getDocumentLastRowColumnPosition = function(e, t) {
            var i = this.documentToScreenRow(e, t);
            return this.screenToDocumentPosition(i, Number.MAX_VALUE / 10)
        }
        ,
        this.getRowSplitData = function(e) {
            return this.$useWrapMode ? this.$wrapData[e] : void 0
        }
        ,
        this.getScreenTabSize = function(e) {
            return this.$tabSize - (e % this.$tabSize | 0)
        }
        ,
        this.screenToDocumentRow = function(e, t) {
            return this.screenToDocumentPosition(e, t).row
        }
        ,
        this.screenToDocumentColumn = function(e, t) {
            return this.screenToDocumentPosition(e, t).column
        }
        ,
        this.screenToDocumentPosition = function(e, t, i) {
            if (e < 0)
                return {
                    row: 0,
                    column: 0
                };
            var n, s, o, r = 0, a = 0, l = 0, h = 0, c = this.$screenRowCache, u = this.$getRowCacheIndex(c, e), d = c.length;
            o = d && 0 <= u ? (l = c[u],
            r = this.$docRowCache[u],
            e > c[d - 1]) : !d;
            for (var g = this.getLength() - 1, f = this.getNextFoldLine(r), m = f ? f.start.row : 1 / 0; l <= e && !(e < l + (h = this.getRowLength(r)) || g <= r); )
                l += h,
                m < ++r && (r = f.end.row + 1,
                m = (f = this.getNextFoldLine(r, f)) ? f.start.row : 1 / 0),
                o && (this.$docRowCache.push(r),
                this.$screenRowCache.push(l));
            if (f && f.start.row <= r)
                n = this.getFoldDisplayLine(f),
                r = f.start.row;
            else {
                if (l + h <= e || g < r)
                    return {
                        row: g,
                        column: this.getLine(g).length
                    };
                n = this.getLine(r),
                f = null
            }
            var p, w = 0, v = Math.floor(e - l);
            return !this.$useWrapMode || (p = this.$wrapData[r]) && (s = p[v],
            0 < v && p.length && (w = p.indent,
            a = p[v - 1] || p[p.length - 1],
            n = n.substring(a))),
            void 0 !== i && this.$bidiHandler.isBidiRow(l + v, r, v) && (t = this.$bidiHandler.offsetToCol(i)),
            a += this.$getStringScreenWidth(n, t - w)[1],
            this.$useWrapMode && s <= a && (a = s - 1),
            f ? f.idxToPosition(a) : {
                row: r,
                column: a
            }
        }
        ,
        this.documentToScreenPosition = function(e, t) {
            var i = void 0 === t ? this.$clipPositionToDocument(e.row, e.column) : this.$clipPositionToDocument(e, t);
            e = i.row,
            t = i.column;
            var n, s = 0, o = null;
            (n = this.getFoldAt(e, t, 1)) && (e = n.start.row,
            t = n.start.column);
            var r, a, l = 0, h = this.$docRowCache, c = this.$getRowCacheIndex(h, e), u = h.length;
            a = u && 0 <= c ? (l = h[c],
            s = this.$screenRowCache[c],
            e > h[u - 1]) : !u;
            for (var d = this.getNextFoldLine(l), g = d ? d.start.row : 1 / 0; l < e; ) {
                if (g <= l) {
                    if (e < (r = d.end.row + 1))
                        break;
                    g = (d = this.getNextFoldLine(r, d)) ? d.start.row : 1 / 0
                } else
                    r = l + 1;
                s += this.getRowLength(l),
                l = r,
                a && (this.$docRowCache.push(l),
                this.$screenRowCache.push(s))
            }
            var f = ""
              , o = d && g <= l ? (f = this.getFoldDisplayLine(d, e, t),
            d.start.row) : (f = this.getLine(e).substring(0, t),
            e)
              , m = 0;
            if (this.$useWrapMode) {
                var p = this.$wrapData[o];
                if (p) {
                    for (var w = 0; f.length >= p[w]; )
                        s++,
                        w++;
                    f = f.substring(p[w - 1] || 0, f.length),
                    m = 0 < w ? p.indent : 0
                }
            }
            return this.lineWidgets && this.lineWidgets[l] && this.lineWidgets[l].rowsAbove && (s += this.lineWidgets[l].rowsAbove),
            {
                row: s,
                column: m + this.$getStringScreenWidth(f)[0]
            }
        }
        ,
        this.documentToScreenColumn = function(e, t) {
            return this.documentToScreenPosition(e, t).column
        }
        ,
        this.documentToScreenRow = function(e, t) {
            return this.documentToScreenPosition(e, t).row
        }
        ,
        this.getScreenLength = function() {
            var e = 0
              , t = null;
            if (this.$useWrapMode)
                for (var i = this.$wrapData.length, n = 0, s = 0, o = (t = this.$foldData[s++]) ? t.start.row : 1 / 0; n < i; ) {
                    var r = this.$wrapData[n];
                    e += r ? r.length + 1 : 1,
                    o < ++n && (n = t.end.row + 1,
                    o = (t = this.$foldData[s++]) ? t.start.row : 1 / 0)
                }
            else {
                e = this.getLength();
                for (var a = this.$foldData, s = 0; s < a.length; s++)
                    e -= (t = a[s]).end.row - t.start.row
            }
            return this.lineWidgets && (e += this.$getWidgetScreenLength()),
            e
        }
        ,
        this.$setFontMetrics = function(o) {
            this.$enableVarChar && (this.$getStringScreenWidth = function(e, t, i) {
                if (0 === t)
                    return [0, 0];
                var n, s;
                for (t = t || 1 / 0,
                i = i || 0,
                s = 0; s < e.length && !(t < (i += "\t" === (n = e.charAt(s)) ? this.getScreenTabSize(i) : o.getCharacterWidth(n))); s++)
                    ;
                return [i, s]
            }
            )
        }
        ,
        this.destroy = function() {
            this.bgTokenizer && (this.bgTokenizer.setDocument(null),
            this.bgTokenizer = null),
            this.$stopWorker(),
            this.removeAllListeners(),
            this.selection.detach()
        }
        ,
        this.isFullWidth = a
    }
    .call(f.prototype),
    e("./edit_session/folding").Folding.call(f.prototype),
    e("./edit_session/bracket_match").BracketMatch.call(f.prototype),
    r.defineOptions(f.prototype, "session", {
        wrap: {
            set: function(e) {
                var t;
                e && "off" != e ? "free" == e ? e = !0 : "printMargin" == e ? e = -1 : "string" == typeof e && (e = parseInt(e, 10) || !1) : e = !1,
                this.$wrap != e && ((this.$wrap = e) ? (t = "number" == typeof e ? e : null,
                this.setWrapLimitRange(t, t),
                this.setUseWrapMode(!0)) : this.setUseWrapMode(!1))
            },
            get: function() {
                return this.getUseWrapMode() ? -1 == this.$wrap ? "printMargin" : this.getWrapLimitRange().min ? this.$wrap : "free" : "off"
            },
            handlesSet: !0
        },
        wrapMethod: {
            set: function(e) {
                (e = "auto" == e ? "text" != this.$mode.type : "text" != e) != this.$wrapAsCode && (this.$wrapAsCode = e,
                this.$useWrapMode && (this.$useWrapMode = !1,
                this.setUseWrapMode(!0)))
            },
            initialValue: "auto"
        },
        indentedSoftWrap: {
            set: function() {
                this.$useWrapMode && (this.$useWrapMode = !1,
                this.setUseWrapMode(!0))
            },
            initialValue: !0
        },
        firstLineNumber: {
            set: function() {
                this._signal("changeBreakpoint")
            },
            initialValue: 1
        },
        useWorker: {
            set: function(e) {
                this.$useWorker = e,
                this.$stopWorker(),
                e && this.$startWorker()
            },
            initialValue: !0
        },
        useSoftTabs: {
            initialValue: !0
        },
        tabSize: {
            set: function(e) {
                0 < (e = parseInt(e)) && this.$tabSize !== e && (this.$modified = !0,
                this.$rowLengthCache = [],
                this.$tabSize = e,
                this._signal("changeTabSize"))
            },
            initialValue: 4,
            handlesSet: !0
        },
        navigateWithinSoftTabs: {
            initialValue: !1
        },
        foldStyle: {
            set: function(e) {
                this.setFoldStyle(e)
            },
            handlesSet: !0
        },
        overwrite: {
            set: function(e) {
                this._signal("changeOverwrite")
            },
            initialValue: !1
        },
        newLineMode: {
            set: function(e) {
                this.doc.setNewLineMode(e)
            },
            get: function() {
                return this.doc.getNewLineMode()
            },
            handlesSet: !0
        },
        mode: {
            set: function(e) {
                this.setMode(e)
            },
            get: function() {
                return this.$modeId
            },
            handlesSet: !0
        }
    }),
    t.EditSession = f
}),
define("ace/search", ["require", "exports", "module", "ace/lib/lang", "ace/lib/oop", "ace/range"], function(e, t, i) {
    "use strict";
    function n() {
        this.$options = {}
    }
    var b = e("./lib/lang")
      , s = e("./lib/oop")
      , y = e("./range").Range;
    (function() {
        this.set = function(e) {
            return s.mixin(this.$options, e),
            this
        }
        ,
        this.getOptions = function() {
            return b.copyObject(this.$options)
        }
        ,
        this.setOptions = function(e) {
            this.$options = e
        }
        ,
        this.find = function(e) {
            var s = this.$options
              , t = this.$matchIterator(e, s);
            if (!t)
                return !1;
            var o = null;
            return t.forEach(function(e, t, i, n) {
                return o = new y(e,t,i,n),
                !(t == n && s.start && s.start.start && 0 != s.skipCurrent && o.isEqual(s.start)) || (o = null,
                !1)
            }),
            o
        }
        ,
        this.findAll = function(e) {
            var t = this.$options;
            if (!t.needle)
                return [];
            this.$assembleRegExp(t);
            var i = t.range
              , n = i ? e.getLines(i.start.row, i.end.row) : e.doc.getAllLines()
              , s = []
              , o = t.re;
            if (t.$isMultiLine) {
                var r, a = o.length, l = n.length - a;
                e: for (var h = o.offset || 0; h <= l; h++) {
                    for (var c = 0; c < a; c++)
                        if (-1 == n[h + c].search(o[c]))
                            continue e;
                    var u = n[h]
                      , d = n[h + a - 1]
                      , g = u.length - u.match(o[0])[0].length
                      , f = d.match(o[a - 1])[0].length;
                    r && r.end.row === h && r.end.column > g || (s.push(r = new y(h,g,h + a - 1,f)),
                    2 < a && (h = h + a - 2))
                }
            } else
                for (var m = 0; m < n.length; m++)
                    for (var p = b.getMatchOffsets(n[m], o), c = 0; c < p.length; c++) {
                        var w = p[c];
                        s.push(new y(m,w.offset,m,w.offset + w.length))
                    }
            if (i) {
                for (var v = i.start.column, $ = i.start.column, m = 0, c = s.length - 1; m < c && s[m].start.column < v && s[m].start.row == i.start.row; )
                    m++;
                for (; m < c && s[c].end.column > $ && s[c].end.row == i.end.row; )
                    c--;
                for (s = s.slice(m, c + 1),
                m = 0,
                c = s.length; m < c; m++)
                    s[m].start.row += i.start.row,
                    s[m].end.row += i.start.row
            }
            return s
        }
        ,
        this.replace = function(e, t) {
            var i = this.$options
              , n = this.$assembleRegExp(i);
            if (i.$isMultiLine)
                return t;
            if (n) {
                var s = n.exec(e);
                if (!s || s[0].length != e.length)
                    return null;
                if (t = e.replace(n, t),
                i.preserveCase) {
                    t = t.split("");
                    for (var o = Math.min(e.length, e.length); o--; ) {
                        var r = e[o];
                        r && r.toLowerCase() != r ? t[o] = t[o].toUpperCase() : t[o] = t[o].toLowerCase()
                    }
                    t = t.join("")
                }
                return t
            }
        }
        ,
        this.$assembleRegExp = function(e, t) {
            if (e.needle instanceof RegExp)
                return e.re = e.needle;
            var i, n, s = e.needle;
            if (!e.needle)
                return e.re = !1;
            function o(e) {
                return /\w/.test(e) || n.regExp ? "\\b" : ""
            }
            e.regExp || (s = b.escapeRegExp(s)),
            e.wholeWord && (n = e,
            s = o((i = s)[0]) + i + o(i[i.length - 1]));
            var r = e.caseSensitive ? "gm" : "gmi";
            if (e.$isMultiLine = !t && /[\n\r]/.test(s),
            e.$isMultiLine)
                return e.re = this.$assembleMultilineRegExp(s, r);
            try {
                var a = new RegExp(s,r)
            } catch (e) {
                a = !1
            }
            return e.re = a
        }
        ,
        this.$assembleMultilineRegExp = function(e, t) {
            for (var i = e.replace(/\r\n|\r|\n/g, "$\n^").split("\n"), n = [], s = 0; s < i.length; s++)
                try {
                    n.push(new RegExp(i[s],t))
                } catch (e) {
                    return !1
                }
            return n
        }
        ,
        this.$matchIterator = function(c, i) {
            var u = this.$assembleRegExp(i);
            if (!u)
                return !1;
            var l = 1 == i.backwards
              , e = 0 != i.skipCurrent
              , t = i.range
              , n = i.start;
            (n = n || (t ? t[l ? "end" : "start"] : c.selection.getRange())).start && (n = n[e != l ? "end" : "start"]);
            var s, h, o, r = t ? t.start.row : 0, a = t ? t.end.row : c.getLength() - 1;
            return s = l ? function(e) {
                var t = n.row;
                if (!o(t, n.column, e)) {
                    for (t--; r <= t; t--)
                        if (o(t, Number.MAX_VALUE, e))
                            return;
                    if (0 != i.wrap)
                        for (t = a,
                        r = n.row; r <= t; t--)
                            if (o(t, Number.MAX_VALUE, e))
                                return
                }
            }
            : function(e) {
                var t = n.row;
                if (!o(t, n.column, e)) {
                    for (t += 1; t <= a; t++)
                        if (o(t, 0, e))
                            return;
                    if (0 != i.wrap)
                        for (t = r,
                        a = n.row; t <= a; t++)
                            if (o(t, 0, e))
                                return
                }
            }
            ,
            o = i.$isMultiLine ? (h = u.length,
            function(e, t, i) {
                var n = l ? e - h + 1 : e;
                if (!(n < 0)) {
                    var s = c.getLine(n)
                      , o = s.search(u[0]);
                    if (!(!l && o < t || -1 === o)) {
                        for (var r = 1; r < h; r++)
                            if (-1 == (s = c.getLine(n + r)).search(u[r]))
                                return;
                        var a = s.match(u[h - 1])[0].length;
                        if (!(l && t < a))
                            return !!i(n, o, n + h - 1, a) || void 0
                    }
                }
            }
            ) : l ? function(e, t, i) {
                var n, s = c.getLine(e), o = [], r = 0;
                for (u.lastIndex = 0; n = u.exec(s); ) {
                    var a = n[0].length
                      , r = n.index;
                    if (!a) {
                        if (r >= s.length)
                            break;
                        u.lastIndex = r += 1
                    }
                    if (n.index + a > t)
                        break;
                    o.push(n.index, a)
                }
                for (var l = o.length - 1; 0 <= l; l -= 2) {
                    var h = o[l - 1];
                    if (i(e, h, e, h + (a = o[l])))
                        return !0
                }
            }
            : function(e, t, i) {
                var n, s = c.getLine(e);
                for (u.lastIndex = t; n = u.exec(s); ) {
                    var o, r = n[0].length;
                    if (i(e, o = n.index, e, o + r))
                        return !0;
                    if (!r && (u.lastIndex = o += 1,
                    o >= s.length))
                        return !1
                }
            }
            ,
            {
                forEach: s
            }
        }
    }
    ).call(n.prototype),
    t.Search = n
}),
define("ace/keyboard/hash_handler", ["require", "exports", "module", "ace/lib/keys", "ace/lib/useragent"], function(e, t, i) {
    "use strict";
    function n(e, t) {
        this.platform = t || (o.isMac ? "mac" : "win"),
        this.commands = {},
        this.commandKeyBinding = {},
        this.addCommands(e),
        this.$singleCommand = !0
    }
    function s(e, t) {
        n.call(this, e, t),
        this.$singleCommand = !1
    }
    var a = e("../lib/keys")
      , o = e("../lib/useragent")
      , l = a.KEY_MODS;
    s.prototype = n.prototype,
    function() {
        function r(e) {
            return "object" == typeof e && e.bindKey && e.bindKey.position || (e.isDefault ? -100 : 0)
        }
        this.addCommand = function(e) {
            this.commands[e.name] && this.removeCommand(e),
            (this.commands[e.name] = e).bindKey && this._buildKeyHash(e)
        }
        ,
        this.removeCommand = function(e, t) {
            var i = e && ("string" == typeof e ? e : e.name);
            e = this.commands[i],
            t || delete this.commands[i];
            var n = this.commandKeyBinding;
            for (var s in n) {
                var o, r = n[s];
                r == e ? delete n[s] : !Array.isArray(r) || -1 != (o = r.indexOf(e)) && (r.splice(o, 1),
                1 == r.length && (n[s] = r[0]))
            }
        }
        ,
        this.bindKey = function(e, o, r) {
            if ("object" == typeof e && e && (null == r && (r = e.position),
            e = e[this.platform]),
            e)
                return "function" == typeof o ? this.addCommand({
                    exec: o,
                    bindKey: e,
                    name: o.name || e
                }) : void e.split("|").forEach(function(e) {
                    var t, n = "";
                    -1 != e.indexOf(" ") && (e = (t = e.split(/\s+/)).pop(),
                    t.forEach(function(e) {
                        var t = this.parseKeys(e)
                          , i = l[t.hashId] + t.key;
                        n += (n ? " " : "") + i,
                        this._addCommandToBinding(n, "chainKeys")
                    }, this),
                    n += " ");
                    var i = this.parseKeys(e)
                      , s = l[i.hashId] + i.key;
                    this._addCommandToBinding(n + s, o, r)
                }, this)
        }
        ,
        this._addCommandToBinding = function(e, t, i) {
            var n = this.commandKeyBinding;
            if (t)
                if (!n[e] || this.$singleCommand)
                    n[e] = t;
                else {
                    Array.isArray(n[e]) ? -1 != (o = n[e].indexOf(t)) && n[e].splice(o, 1) : n[e] = [n[e]],
                    "number" != typeof i && (i = r(t));
                    for (var s = n[e], o = 0; o < s.length; o++) {
                        if (i < r(s[o]))
                            break
                    }
                    s.splice(o, 0, t)
                }
            else
                delete n[e]
        }
        ,
        this.addCommands = function(i) {
            i && Object.keys(i).forEach(function(e) {
                var t = i[e];
                if (t) {
                    if ("string" == typeof t)
                        return this.bindKey(t, e);
                    "function" == typeof t && (t = {
                        exec: t
                    }),
                    "object" == typeof t && (t.name || (t.name = e),
                    this.addCommand(t))
                }
            }, this)
        }
        ,
        this.removeCommands = function(t) {
            Object.keys(t).forEach(function(e) {
                this.removeCommand(t[e])
            }, this)
        }
        ,
        this.bindKeys = function(t) {
            Object.keys(t).forEach(function(e) {
                this.bindKey(e, t[e])
            }, this)
        }
        ,
        this._buildKeyHash = function(e) {
            this.bindKey(e.bindKey, e)
        }
        ,
        this.parseKeys = function(e) {
            var t = e.toLowerCase().split(/[\-\+]([\-\+])?/).filter(function(e) {
                return e
            })
              , i = t.pop()
              , n = a[i];
            if (a.FUNCTION_KEYS[n])
                i = a.FUNCTION_KEYS[n].toLowerCase();
            else {
                if (!t.length)
                    return {
                        key: i,
                        hashId: -1
                    };
                if (1 == t.length && "shift" == t[0])
                    return {
                        key: i.toUpperCase(),
                        hashId: -1
                    }
            }
            for (var s = 0, o = t.length; o--; ) {
                var r = a.KEY_MODS[t[o]];
                if (null == r)
                    return "undefined" != typeof console && console.error("invalid modifier " + t[o] + " in " + e),
                    !1;
                s |= r
            }
            return {
                key: i,
                hashId: s
            }
        }
        ,
        this.findKeyCommand = function(e, t) {
            var i = l[e] + t;
            return this.commandKeyBinding[i]
        }
        ,
        this.handleKeyboard = function(e, t, i, n) {
            if (!(n < 0)) {
                var s = l[t] + i
                  , o = this.commandKeyBinding[s];
                return (e.$keyChain && (e.$keyChain += " " + s,
                o = this.commandKeyBinding[e.$keyChain] || o),
                !o || "chainKeys" != o && "chainKeys" != o[o.length - 1]) ? (e.$keyChain && (t && 4 != t || 1 != i.length ? (-1 == t || 0 < n) && (e.$keyChain = "") : e.$keyChain = e.$keyChain.slice(0, -s.length - 1)),
                {
                    command: o
                }) : (e.$keyChain = e.$keyChain || s,
                {
                    command: "null"
                })
            }
        }
        ,
        this.getStatusText = function(e, t) {
            return t.$keyChain || ""
        }
    }
    .call(n.prototype),
    t.HashHandler = n,
    t.MultiHashHandler = s
}),
define("ace/commands/command_manager", ["require", "exports", "module", "ace/lib/oop", "ace/keyboard/hash_handler", "ace/lib/event_emitter"], function(e, t, i) {
    "use strict";
    function n(e, t) {
        o.call(this, t, e),
        this.byName = this.commands,
        this.setDefaultHandler("exec", function(e) {
            return e.command.exec(e.editor, e.args || {})
        })
    }
    var s = e("../lib/oop")
      , o = e("../keyboard/hash_handler").MultiHashHandler
      , r = e("../lib/event_emitter").EventEmitter;
    s.inherits(n, o),
    function() {
        s.implement(this, r),
        this.exec = function(e, t, i) {
            if (Array.isArray(e)) {
                for (var n = e.length; n--; )
                    if (this.exec(e[n], t, i))
                        return !0;
                return !1
            }
            if ("string" == typeof e && (e = this.commands[e]),
            !e)
                return !1;
            if (t && t.$readOnly && !e.readOnly)
                return !1;
            if (0 != this.$checkCommandState && e.isAvailable && !e.isAvailable(t))
                return !1;
            var s = {
                editor: t,
                command: e,
                args: i
            };
            return s.returnValue = this._emit("exec", s),
            this._signal("afterExec", s),
            !1 !== s.returnValue
        }
        ,
        this.toggleRecording = function(e) {
            if (!this.$inReplay)
                return e && e._emit("changeStatus"),
                this.recording ? (this.macro.pop(),
                this.off("exec", this.$addCommandToMacro),
                this.macro.length || (this.macro = this.oldMacro),
                this.recording = !1) : (this.$addCommandToMacro || (this.$addCommandToMacro = function(e) {
                    this.macro.push([e.command, e.args])
                }
                .bind(this)),
                this.oldMacro = this.macro,
                this.macro = [],
                this.on("exec", this.$addCommandToMacro),
                this.recording = !0)
        }
        ,
        this.replay = function(t) {
            if (!this.$inReplay && this.macro) {
                if (this.recording)
                    return this.toggleRecording(t);
                try {
                    this.$inReplay = !0,
                    this.macro.forEach(function(e) {
                        "string" == typeof e ? this.exec(e, t) : this.exec(e[0], t, e[1])
                    }, this)
                } finally {
                    this.$inReplay = !1
                }
            }
        }
        ,
        this.trimMacro = function(e) {
            return e.map(function(e) {
                return "string" != typeof e[0] && (e[0] = e[0].name),
                e[1] || (e = e[0]),
                e
            })
        }
    }
    .call(n.prototype),
    t.CommandManager = n
}),
define("ace/commands/default_commands", ["require", "exports", "module", "ace/lib/lang", "ace/config", "ace/range"], function(e, t, i) {
    "use strict";
    function n(e, t) {
        return {
            win: e,
            mac: t
        }
    }
    var h = e("../lib/lang")
      , s = e("../config")
      , c = e("../range").Range;
    t.commands = [{
        name: "showSettingsMenu",
        bindKey: n("Ctrl-,", "Command-,"),
        exec: function(t) {
            s.loadModule("ace/ext/settings_menu", function(e) {
                e.init(t),
                t.showSettingsMenu()
            })
        },
        readOnly: !0
    }, {
        name: "goToNextError",
        bindKey: n("Alt-E", "F4"),
        exec: function(t) {
            s.loadModule("./ext/error_marker", function(e) {
                e.showErrorMarker(t, 1)
            })
        },
        scrollIntoView: "animate",
        readOnly: !0
    }, {
        name: "goToPreviousError",
        bindKey: n("Alt-Shift-E", "Shift-F4"),
        exec: function(t) {
            s.loadModule("./ext/error_marker", function(e) {
                e.showErrorMarker(t, -1)
            })
        },
        scrollIntoView: "animate",
        readOnly: !0
    }, {
        name: "selectall",
        description: "Select all",
        bindKey: n("Ctrl-A", "Command-A"),
        exec: function(e) {
            e.selectAll()
        },
        readOnly: !0
    }, {
        name: "centerselection",
        description: "Center selection",
        bindKey: n(null, "Ctrl-L"),
        exec: function(e) {
            e.centerSelection()
        },
        readOnly: !0
    }, {
        name: "gotoline",
        description: "Go to line...",
        bindKey: n("Ctrl-L", "Command-L"),
        exec: function(e, t) {
            "number" != typeof t || isNaN(t) || e.gotoLine(t),
            e.prompt({
                $type: "gotoLine"
            })
        },
        readOnly: !0
    }, {
        name: "fold",
        bindKey: n("Alt-L|Ctrl-F1", "Command-Alt-L|Command-F1"),
        exec: function(e) {
            e.session.toggleFold(!1)
        },
        multiSelectAction: "forEach",
        scrollIntoView: "center",
        readOnly: !0
    }, {
        name: "unfold",
        bindKey: n("Alt-Shift-L|Ctrl-Shift-F1", "Command-Alt-Shift-L|Command-Shift-F1"),
        exec: function(e) {
            e.session.toggleFold(!0)
        },
        multiSelectAction: "forEach",
        scrollIntoView: "center",
        readOnly: !0
    }, {
        name: "toggleFoldWidget",
        bindKey: n("F2", "F2"),
        exec: function(e) {
            e.session.toggleFoldWidget()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "center",
        readOnly: !0
    }, {
        name: "toggleParentFoldWidget",
        bindKey: n("Alt-F2", "Alt-F2"),
        exec: function(e) {
            e.session.toggleFoldWidget(!0)
        },
        multiSelectAction: "forEach",
        scrollIntoView: "center",
        readOnly: !0
    }, {
        name: "foldall",
        description: "Fold all",
        bindKey: n(null, "Ctrl-Command-Option-0"),
        exec: function(e) {
            e.session.foldAll()
        },
        scrollIntoView: "center",
        readOnly: !0
    }, {
        name: "foldAllComments",
        description: "Fold all comments",
        bindKey: n(null, "Ctrl-Command-Option-0"),
        exec: function(e) {
            e.session.foldAllComments()
        },
        scrollIntoView: "center",
        readOnly: !0
    }, {
        name: "foldOther",
        description: "Fold other",
        bindKey: n("Alt-0", "Command-Option-0"),
        exec: function(e) {
            e.session.foldAll(),
            e.session.unfold(e.selection.getAllRanges())
        },
        scrollIntoView: "center",
        readOnly: !0
    }, {
        name: "unfoldall",
        description: "Unfold all",
        bindKey: n("Alt-Shift-0", "Command-Option-Shift-0"),
        exec: function(e) {
            e.session.unfold()
        },
        scrollIntoView: "center",
        readOnly: !0
    }, {
        name: "findnext",
        description: "Find next",
        bindKey: n("Ctrl-K", "Command-G"),
        exec: function(e) {
            e.findNext()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "center",
        readOnly: !0
    }, {
        name: "findprevious",
        description: "Find previous",
        bindKey: n("Ctrl-Shift-K", "Command-Shift-G"),
        exec: function(e) {
            e.findPrevious()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "center",
        readOnly: !0
    }, {
        name: "selectOrFindNext",
        description: "Select or find next",
        bindKey: n("Alt-K", "Ctrl-G"),
        exec: function(e) {
            e.selection.isEmpty() ? e.selection.selectWord() : e.findNext()
        },
        readOnly: !0
    }, {
        name: "selectOrFindPrevious",
        description: "Select or find previous",
        bindKey: n("Alt-Shift-K", "Ctrl-Shift-G"),
        exec: function(e) {
            e.selection.isEmpty() ? e.selection.selectWord() : e.findPrevious()
        },
        readOnly: !0
    }, {
        name: "find",
        description: "Find",
        bindKey: n("Ctrl-F", "Command-F"),
        exec: function(t) {
            s.loadModule("ace/ext/searchbox", function(e) {
                e.Search(t)
            })
        },
        readOnly: !0
    }, {
        name: "overwrite",
        description: "Overwrite",
        bindKey: "Insert",
        exec: function(e) {
            e.toggleOverwrite()
        },
        readOnly: !0
    }, {
        name: "selecttostart",
        description: "Select to start",
        bindKey: n("Ctrl-Shift-Home", "Command-Shift-Home|Command-Shift-Up"),
        exec: function(e) {
            e.getSelection().selectFileStart()
        },
        multiSelectAction: "forEach",
        readOnly: !0,
        scrollIntoView: "animate",
        aceCommandGroup: "fileJump"
    }, {
        name: "gotostart",
        description: "Go to start",
        bindKey: n("Ctrl-Home", "Command-Home|Command-Up"),
        exec: function(e) {
            e.navigateFileStart()
        },
        multiSelectAction: "forEach",
        readOnly: !0,
        scrollIntoView: "animate",
        aceCommandGroup: "fileJump"
    }, {
        name: "selectup",
        description: "Select up",
        bindKey: n("Shift-Up", "Shift-Up|Ctrl-Shift-P"),
        exec: function(e) {
            e.getSelection().selectUp()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "golineup",
        description: "Go line up",
        bindKey: n("Up", "Up|Ctrl-P"),
        exec: function(e, t) {
            e.navigateUp(t.times)
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "selecttoend",
        description: "Select to end",
        bindKey: n("Ctrl-Shift-End", "Command-Shift-End|Command-Shift-Down"),
        exec: function(e) {
            e.getSelection().selectFileEnd()
        },
        multiSelectAction: "forEach",
        readOnly: !0,
        scrollIntoView: "animate",
        aceCommandGroup: "fileJump"
    }, {
        name: "gotoend",
        description: "Go to end",
        bindKey: n("Ctrl-End", "Command-End|Command-Down"),
        exec: function(e) {
            e.navigateFileEnd()
        },
        multiSelectAction: "forEach",
        readOnly: !0,
        scrollIntoView: "animate",
        aceCommandGroup: "fileJump"
    }, {
        name: "selectdown",
        description: "Select down",
        bindKey: n("Shift-Down", "Shift-Down|Ctrl-Shift-N"),
        exec: function(e) {
            e.getSelection().selectDown()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "golinedown",
        description: "Go line down",
        bindKey: n("Down", "Down|Ctrl-N"),
        exec: function(e, t) {
            e.navigateDown(t.times)
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "selectwordleft",
        description: "Select word left",
        bindKey: n("Ctrl-Shift-Left", "Option-Shift-Left"),
        exec: function(e) {
            e.getSelection().selectWordLeft()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "gotowordleft",
        description: "Go to word left",
        bindKey: n("Ctrl-Left", "Option-Left"),
        exec: function(e) {
            e.navigateWordLeft()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "selecttolinestart",
        description: "Select to line start",
        bindKey: n("Alt-Shift-Left", "Command-Shift-Left|Ctrl-Shift-A"),
        exec: function(e) {
            e.getSelection().selectLineStart()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "gotolinestart",
        description: "Go to line start",
        bindKey: n("Alt-Left|Home", "Command-Left|Home|Ctrl-A"),
        exec: function(e) {
            e.navigateLineStart()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "selectleft",
        description: "Select left",
        bindKey: n("Shift-Left", "Shift-Left|Ctrl-Shift-B"),
        exec: function(e) {
            e.getSelection().selectLeft()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "gotoleft",
        description: "Go to left",
        bindKey: n("Left", "Left|Ctrl-B"),
        exec: function(e, t) {
            e.navigateLeft(t.times)
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "selectwordright",
        description: "Select word right",
        bindKey: n("Ctrl-Shift-Right", "Option-Shift-Right"),
        exec: function(e) {
            e.getSelection().selectWordRight()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "gotowordright",
        description: "Go to word right",
        bindKey: n("Ctrl-Right", "Option-Right"),
        exec: function(e) {
            e.navigateWordRight()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "selecttolineend",
        description: "Select to line end",
        bindKey: n("Alt-Shift-Right", "Command-Shift-Right|Shift-End|Ctrl-Shift-E"),
        exec: function(e) {
            e.getSelection().selectLineEnd()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "gotolineend",
        description: "Go to line end",
        bindKey: n("Alt-Right|End", "Command-Right|End|Ctrl-E"),
        exec: function(e) {
            e.navigateLineEnd()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "selectright",
        description: "Select right",
        bindKey: n("Shift-Right", "Shift-Right"),
        exec: function(e) {
            e.getSelection().selectRight()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "gotoright",
        description: "Go to right",
        bindKey: n("Right", "Right|Ctrl-F"),
        exec: function(e, t) {
            e.navigateRight(t.times)
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "selectpagedown",
        description: "Select page down",
        bindKey: "Shift-PageDown",
        exec: function(e) {
            e.selectPageDown()
        },
        readOnly: !0
    }, {
        name: "pagedown",
        description: "Page down",
        bindKey: n(null, "Option-PageDown"),
        exec: function(e) {
            e.scrollPageDown()
        },
        readOnly: !0
    }, {
        name: "gotopagedown",
        description: "Go to page down",
        bindKey: n("PageDown", "PageDown|Ctrl-V"),
        exec: function(e) {
            e.gotoPageDown()
        },
        readOnly: !0
    }, {
        name: "selectpageup",
        description: "Select page up",
        bindKey: "Shift-PageUp",
        exec: function(e) {
            e.selectPageUp()
        },
        readOnly: !0
    }, {
        name: "pageup",
        description: "Page up",
        bindKey: n(null, "Option-PageUp"),
        exec: function(e) {
            e.scrollPageUp()
        },
        readOnly: !0
    }, {
        name: "gotopageup",
        description: "Go to page up",
        bindKey: "PageUp",
        exec: function(e) {
            e.gotoPageUp()
        },
        readOnly: !0
    }, {
        name: "scrollup",
        description: "Scroll up",
        bindKey: n("Ctrl-Up", null),
        exec: function(e) {
            e.renderer.scrollBy(0, -2 * e.renderer.layerConfig.lineHeight)
        },
        readOnly: !0
    }, {
        name: "scrolldown",
        description: "Scroll down",
        bindKey: n("Ctrl-Down", null),
        exec: function(e) {
            e.renderer.scrollBy(0, 2 * e.renderer.layerConfig.lineHeight)
        },
        readOnly: !0
    }, {
        name: "selectlinestart",
        description: "Select line start",
        bindKey: "Shift-Home",
        exec: function(e) {
            e.getSelection().selectLineStart()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "selectlineend",
        description: "Select line end",
        bindKey: "Shift-End",
        exec: function(e) {
            e.getSelection().selectLineEnd()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "togglerecording",
        description: "Toggle recording",
        bindKey: n("Ctrl-Alt-E", "Command-Option-E"),
        exec: function(e) {
            e.commands.toggleRecording(e)
        },
        readOnly: !0
    }, {
        name: "replaymacro",
        description: "Replay macro",
        bindKey: n("Ctrl-Shift-E", "Command-Shift-E"),
        exec: function(e) {
            e.commands.replay(e)
        },
        readOnly: !0
    }, {
        name: "jumptomatching",
        description: "Jump to matching",
        bindKey: n("Ctrl-\\|Ctrl-P", "Command-\\"),
        exec: function(e) {
            e.jumpToMatching()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "animate",
        readOnly: !0
    }, {
        name: "selecttomatching",
        description: "Select to matching",
        bindKey: n("Ctrl-Shift-\\|Ctrl-Shift-P", "Command-Shift-\\"),
        exec: function(e) {
            e.jumpToMatching(!0)
        },
        multiSelectAction: "forEach",
        scrollIntoView: "animate",
        readOnly: !0
    }, {
        name: "expandToMatching",
        description: "Expand to matching",
        bindKey: n("Ctrl-Shift-M", "Ctrl-Shift-M"),
        exec: function(e) {
            e.jumpToMatching(!0, !0)
        },
        multiSelectAction: "forEach",
        scrollIntoView: "animate",
        readOnly: !0
    }, {
        name: "passKeysToBrowser",
        description: "Pass keys to browser",
        bindKey: n(null, null),
        exec: function() {},
        passEvent: !0,
        readOnly: !0
    }, {
        name: "copy",
        description: "Copy",
        exec: function(e) {},
        readOnly: !0
    }, {
        name: "cut",
        description: "Cut",
        exec: function(e) {
            var t = e.$copyWithEmptySelection && e.selection.isEmpty() ? e.selection.getLineRange() : e.selection.getRange();
            e._emit("cut", t),
            t.isEmpty() || e.session.remove(t),
            e.clearSelection()
        },
        scrollIntoView: "cursor",
        multiSelectAction: "forEach"
    }, {
        name: "paste",
        description: "Paste",
        exec: function(e, t) {
            e.$handlePaste(t)
        },
        scrollIntoView: "cursor"
    }, {
        name: "removeline",
        description: "Remove line",
        bindKey: n("Ctrl-D", "Command-D"),
        exec: function(e) {
            e.removeLines()
        },
        scrollIntoView: "cursor",
        multiSelectAction: "forEachLine"
    }, {
        name: "duplicateSelection",
        description: "Duplicate selection",
        bindKey: n("Ctrl-Shift-D", "Command-Shift-D"),
        exec: function(e) {
            e.duplicateSelection()
        },
        scrollIntoView: "cursor",
        multiSelectAction: "forEach"
    }, {
        name: "sortlines",
        description: "Sort lines",
        bindKey: n("Ctrl-Alt-S", "Command-Alt-S"),
        exec: function(e) {
            e.sortLines()
        },
        scrollIntoView: "selection",
        multiSelectAction: "forEachLine"
    }, {
        name: "togglecomment",
        description: "Toggle comment",
        bindKey: n("Ctrl-/", "Command-/"),
        exec: function(e) {
            e.toggleCommentLines()
        },
        multiSelectAction: "forEachLine",
        scrollIntoView: "selectionPart"
    }, {
        name: "toggleBlockComment",
        description: "Toggle block comment",
        bindKey: n("Ctrl-Shift-/", "Command-Shift-/"),
        exec: function(e) {
            e.toggleBlockComment()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "selectionPart"
    }, {
        name: "modifyNumberUp",
        description: "Modify number up",
        bindKey: n("Ctrl-Shift-Up", "Alt-Shift-Up"),
        exec: function(e) {
            e.modifyNumber(1)
        },
        scrollIntoView: "cursor",
        multiSelectAction: "forEach"
    }, {
        name: "modifyNumberDown",
        description: "Modify number down",
        bindKey: n("Ctrl-Shift-Down", "Alt-Shift-Down"),
        exec: function(e) {
            e.modifyNumber(-1)
        },
        scrollIntoView: "cursor",
        multiSelectAction: "forEach"
    }, {
        name: "replace",
        description: "Replace",
        bindKey: n("Ctrl-H", "Command-Option-F"),
        exec: function(t) {
            s.loadModule("ace/ext/searchbox", function(e) {
                e.Search(t, !0)
            })
        }
    }, {
        name: "undo",
        description: "Undo",
        bindKey: n("Ctrl-Z", "Command-Z"),
        exec: function(e) {
            e.undo()
        }
    }, {
        name: "redo",
        description: "Redo",
        bindKey: n("Ctrl-Shift-Z|Ctrl-Y", "Command-Shift-Z|Command-Y"),
        exec: function(e) {
            e.redo()
        }
    }, {
        name: "copylinesup",
        description: "Copy lines up",
        bindKey: n("Alt-Shift-Up", "Command-Option-Up"),
        exec: function(e) {
            e.copyLinesUp()
        },
        scrollIntoView: "cursor"
    }, {
        name: "movelinesup",
        description: "Move lines up",
        bindKey: n("Alt-Up", "Option-Up"),
        exec: function(e) {
            e.moveLinesUp()
        },
        scrollIntoView: "cursor"
    }, {
        name: "copylinesdown",
        description: "Copy lines down",
        bindKey: n("Alt-Shift-Down", "Command-Option-Down"),
        exec: function(e) {
            e.copyLinesDown()
        },
        scrollIntoView: "cursor"
    }, {
        name: "movelinesdown",
        description: "Move lines down",
        bindKey: n("Alt-Down", "Option-Down"),
        exec: function(e) {
            e.moveLinesDown()
        },
        scrollIntoView: "cursor"
    }, {
        name: "del",
        description: "Delete",
        bindKey: n("Delete", "Delete|Ctrl-D|Shift-Delete"),
        exec: function(e) {
            e.remove("right")
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor"
    }, {
        name: "backspace",
        description: "Backspace",
        bindKey: n("Shift-Backspace|Backspace", "Ctrl-Backspace|Shift-Backspace|Backspace|Ctrl-H"),
        exec: function(e) {
            e.remove("left")
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor"
    }, {
        name: "cut_or_delete",
        description: "Cut or delete",
        bindKey: n("Shift-Delete", null),
        exec: function(e) {
            if (!e.selection.isEmpty())
                return !1;
            e.remove("left")
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor"
    }, {
        name: "removetolinestart",
        description: "Remove to line start",
        bindKey: n("Alt-Backspace", "Command-Backspace"),
        exec: function(e) {
            e.removeToLineStart()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor"
    }, {
        name: "removetolineend",
        description: "Remove to line end",
        bindKey: n("Alt-Delete", "Ctrl-K|Command-Delete"),
        exec: function(e) {
            e.removeToLineEnd()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor"
    }, {
        name: "removetolinestarthard",
        description: "Remove to line start hard",
        bindKey: n("Ctrl-Shift-Backspace", null),
        exec: function(e) {
            var t = e.selection.getRange();
            t.start.column = 0,
            e.session.remove(t)
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor"
    }, {
        name: "removetolineendhard",
        description: "Remove to line end hard",
        bindKey: n("Ctrl-Shift-Delete", null),
        exec: function(e) {
            var t = e.selection.getRange();
            t.end.column = Number.MAX_VALUE,
            e.session.remove(t)
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor"
    }, {
        name: "removewordleft",
        description: "Remove word left",
        bindKey: n("Ctrl-Backspace", "Alt-Backspace|Ctrl-Alt-Backspace"),
        exec: function(e) {
            e.removeWordLeft()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor"
    }, {
        name: "removewordright",
        description: "Remove word right",
        bindKey: n("Ctrl-Delete", "Alt-Delete"),
        exec: function(e) {
            e.removeWordRight()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor"
    }, {
        name: "outdent",
        description: "Outdent",
        bindKey: n("Shift-Tab", "Shift-Tab"),
        exec: function(e) {
            e.blockOutdent()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "selectionPart"
    }, {
        name: "indent",
        description: "Indent",
        bindKey: n("Tab", "Tab"),
        exec: function(e) {
            e.indent()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "selectionPart"
    }, {
        name: "blockoutdent",
        description: "Block outdent",
        bindKey: n("Ctrl-[", "Ctrl-["),
        exec: function(e) {
            e.blockOutdent()
        },
        multiSelectAction: "forEachLine",
        scrollIntoView: "selectionPart"
    }, {
        name: "blockindent",
        description: "Block indent",
        bindKey: n("Ctrl-]", "Ctrl-]"),
        exec: function(e) {
            e.blockIndent()
        },
        multiSelectAction: "forEachLine",
        scrollIntoView: "selectionPart"
    }, {
        name: "insertstring",
        description: "Insert string",
        exec: function(e, t) {
            e.insert(t)
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor"
    }, {
        name: "inserttext",
        description: "Insert text",
        exec: function(e, t) {
            e.insert(h.stringRepeat(t.text || "", t.times || 1))
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor"
    }, {
        name: "splitline",
        description: "Split line",
        bindKey: n(null, "Ctrl-O"),
        exec: function(e) {
            e.splitLine()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor"
    }, {
        name: "transposeletters",
        description: "Transpose letters",
        bindKey: n("Alt-Shift-X", "Ctrl-T"),
        exec: function(e) {
            e.transposeLetters()
        },
        multiSelectAction: function(e) {
            e.transposeSelections(1)
        },
        scrollIntoView: "cursor"
    }, {
        name: "touppercase",
        description: "To uppercase",
        bindKey: n("Ctrl-U", "Ctrl-U"),
        exec: function(e) {
            e.toUpperCase()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor"
    }, {
        name: "tolowercase",
        description: "To lowercase",
        bindKey: n("Ctrl-Shift-U", "Ctrl-Shift-U"),
        exec: function(e) {
            e.toLowerCase()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor"
    }, {
        name: "autoindent",
        description: "Auto Indent",
        bindKey: n(null, null),
        exec: function(e) {
            e.autoIndent()
        },
        multiSelectAction: "forEachLine",
        scrollIntoView: "animate"
    }, {
        name: "expandtoline",
        description: "Expand to line",
        bindKey: n("Ctrl-Shift-L", "Command-Shift-L"),
        exec: function(e) {
            var t = e.selection.getRange();
            t.start.column = t.end.column = 0,
            t.end.row++,
            e.selection.setRange(t, !1)
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "joinlines",
        description: "Join lines",
        bindKey: n(null, null),
        exec: function(e) {
            for (var t = e.selection.isBackwards(), i = t ? e.selection.getSelectionLead() : e.selection.getSelectionAnchor(), n = t ? e.selection.getSelectionAnchor() : e.selection.getSelectionLead(), s = e.session.doc.getLine(i.row).length, o = e.session.doc.getTextRange(e.selection.getRange()).replace(/\n\s*/, " ").length, r = e.session.doc.getLine(i.row), a = i.row + 1; a <= n.row + 1; a++) {
                var l = h.stringTrimLeft(h.stringTrimRight(e.session.doc.getLine(a)));
                0 !== l.length && (l = " " + l),
                r += l
            }
            n.row + 1 < e.session.doc.getLength() - 1 && (r += e.session.doc.getNewLineCharacter()),
            e.clearSelection(),
            e.session.doc.replace(new c(i.row,0,n.row + 2,0), r),
            0 < o ? (e.selection.moveCursorTo(i.row, i.column),
            e.selection.selectTo(i.row, i.column + o)) : (s = e.session.doc.getLine(i.row).length > s ? s + 1 : s,
            e.selection.moveCursorTo(i.row, s))
        },
        multiSelectAction: "forEach",
        readOnly: !0
    }, {
        name: "invertSelection",
        description: "Invert selection",
        bindKey: n(null, null),
        exec: function(e) {
            var t = e.session.doc.getLength() - 1
              , i = e.session.doc.getLine(t).length
              , n = e.selection.rangeList.ranges
              , s = [];
            n.length < 1 && (n = [e.selection.getRange()]);
            for (var o = 0; o < n.length; o++)
                o != n.length - 1 || n[o].end.row === t && n[o].end.column === i || s.push(new c(n[o].end.row,n[o].end.column,t,i)),
                0 === o ? 0 === n[o].start.row && 0 === n[o].start.column || s.push(new c(0,0,n[o].start.row,n[o].start.column)) : s.push(new c(n[o - 1].end.row,n[o - 1].end.column,n[o].start.row,n[o].start.column));
            e.exitMultiSelectMode(),
            e.clearSelection();
            for (o = 0; o < s.length; o++)
                e.selection.addRange(s[o], !1)
        },
        readOnly: !0,
        scrollIntoView: "none"
    }, {
        name: "addLineAfter",
        exec: function(e) {
            e.selection.clearSelection(),
            e.navigateLineEnd(),
            e.insert("\n")
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor"
    }, {
        name: "addLineBefore",
        exec: function(e) {
            e.selection.clearSelection();
            var t = e.getCursorPosition();
            e.selection.moveTo(t.row - 1, Number.MAX_VALUE),
            e.insert("\n"),
            0 === t.row && e.navigateUp()
        },
        multiSelectAction: "forEach",
        scrollIntoView: "cursor"
    }, {
        name: "openCommandPallete",
        description: "Open command pallete",
        bindKey: n("F1", "F1"),
        exec: function(e) {
            e.prompt({
                $type: "commands"
            })
        },
        readOnly: !0
    }, {
        name: "modeSelect",
        description: "Change language mode...",
        bindKey: n(null, null),
        exec: function(e) {
            e.prompt({
                $type: "modes"
            })
        },
        readOnly: !0
    }];
    for (var o = 1; o < 9; o++)
        t.commands.push({
            name: "foldToLevel" + o,
            description: "Fold To Level " + o,
            level: o,
            exec: function(e) {
                e.session.foldToLevel(this.level)
            },
            scrollIntoView: "center",
            readOnly: !0
        })
}),
define("ace/editor", ["require", "exports", "module", "ace/lib/fixoldbrowsers", "ace/lib/oop", "ace/lib/dom", "ace/lib/lang", "ace/lib/useragent", "ace/keyboard/textinput", "ace/mouse/mouse_handler", "ace/mouse/fold_handler", "ace/keyboard/keybinding", "ace/edit_session", "ace/search", "ace/range", "ace/lib/event_emitter", "ace/commands/command_manager", "ace/commands/default_commands", "ace/config", "ace/token_iterator", "ace/clipboard"], function(e, t, i) {
    "use strict";
    e("./lib/fixoldbrowsers");
    var o = e("./lib/oop")
      , n = e("./lib/dom")
      , p = e("./lib/lang")
      , s = e("./lib/useragent")
      , r = e("./keyboard/textinput").TextInput
      , a = e("./mouse/mouse_handler").MouseHandler
      , l = e("./mouse/fold_handler").FoldHandler
      , h = e("./keyboard/keybinding").KeyBinding
      , c = e("./edit_session").EditSession
      , u = e("./search").Search
      , w = e("./range").Range
      , d = e("./lib/event_emitter").EventEmitter
      , g = e("./commands/command_manager").CommandManager
      , f = e("./commands/default_commands").commands
      , m = e("./config")
      , v = e("./token_iterator").TokenIterator
      , $ = e("./clipboard")
      , b = function(e, t, i) {
        this.$toDestroy = [];
        var n = e.getContainerElement();
        this.container = n,
        this.renderer = e,
        this.id = "editor" + ++b.$uid,
        this.commands = new g(s.isMac ? "mac" : "win",f),
        "object" == typeof document && (this.textInput = new r(e.getTextAreaContainer(),this),
        this.renderer.textarea = this.textInput.getElement(),
        this.$mouseHandler = new a(this),
        new l(this)),
        this.keyBinding = new h(this),
        this.$search = (new u).set({
            wrap: !0
        }),
        this.$historyTracker = this.$historyTracker.bind(this),
        this.commands.on("exec", this.$historyTracker),
        this.$initOperationListeners(),
        this._$emitInputEvent = p.delayedCall(function() {
            this._signal("input", {}),
            this.session && this.session.bgTokenizer && this.session.bgTokenizer.scheduleStart()
        }
        .bind(this)),
        this.on("change", function(e, t) {
            t._$emitInputEvent.schedule(31)
        }),
        this.setSession(t || i && i.session || new c("")),
        m.resetOptions(this),
        i && this.setOptions(i),
        m._signal("editor", this)
    };
    b.$uid = 0,
    function() {
        o.implement(this, d),
        this.$initOperationListeners = function() {
            this.commands.on("exec", this.startOperation.bind(this), !0),
            this.commands.on("afterExec", this.endOperation.bind(this), !0),
            this.$opResetTimer = p.delayedCall(this.endOperation.bind(this, !0)),
            this.on("change", function() {
                this.curOp || (this.startOperation(),
                this.curOp.selectionBefore = this.$lastSel),
                this.curOp.docChanged = !0
            }
            .bind(this), !0),
            this.on("changeSelection", function() {
                this.curOp || (this.startOperation(),
                this.curOp.selectionBefore = this.$lastSel),
                this.curOp.selectionChanged = !0
            }
            .bind(this), !0)
        }
        ,
        this.curOp = null,
        this.prevOp = {},
        this.startOperation = function(e) {
            if (this.curOp) {
                if (!e || this.curOp.command)
                    return;
                this.prevOp = this.curOp
            }
            e || (this.previousCommand = null,
            e = {}),
            this.$opResetTimer.schedule(),
            this.curOp = this.session.curOp = {
                command: e.command || {},
                args: e.args,
                scrollTop: this.renderer.scrollTop
            },
            this.curOp.selectionBefore = this.selection.toJSON()
        }
        ,
        this.endOperation = function(e) {
            if (this.curOp && this.session) {
                if (e && !1 === e.returnValue || !this.session)
                    return this.curOp = null;
                if (1 == e && this.curOp.command && "mouse" == this.curOp.command.name)
                    return;
                if (this._signal("beforeEndOperation"),
                !this.curOp)
                    return;
                var t = this.curOp.command
                  , i = t && t.scrollIntoView;
                if (i) {
                    switch (i) {
                    case "center-animate":
                        i = "animate";
                    case "center":
                        this.renderer.scrollCursorIntoView(null, .5);
                        break;
                    case "animate":
                    case "cursor":
                        this.renderer.scrollCursorIntoView();
                        break;
                    case "selectionPart":
                        var n = this.selection.getRange()
                          , s = this.renderer.layerConfig;
                        (n.start.row >= s.lastRow || n.end.row <= s.firstRow) && this.renderer.scrollSelectionIntoView(this.selection.anchor, this.selection.lead)
                    }
                    "animate" == i && this.renderer.animateScrolling(this.curOp.scrollTop)
                }
                var o = this.selection.toJSON();
                this.curOp.selectionAfter = o,
                this.$lastSel = this.selection.toJSON(),
                this.session.getUndoManager().addSelection(o),
                this.prevOp = this.curOp,
                this.curOp = null
            }
        }
        ,
        this.$mergeableCommands = ["backspace", "del", "insertstring"],
        this.$historyTracker = function(e) {
            var t, i, n, s;
            this.$mergeUndoDeltas && (t = this.prevOp,
            i = this.$mergeableCommands,
            n = t.command && e.command.name == t.command.name,
            "insertstring" == e.command.name ? (s = e.args,
            void 0 === this.mergeNextCommand && (this.mergeNextCommand = !0),
            n = n && this.mergeNextCommand && (!/\s/.test(s) || /\s/.test(t.args)),
            this.mergeNextCommand = !0) : n = n && -1 !== i.indexOf(e.command.name),
            "always" != this.$mergeUndoDeltas && 2e3 < Date.now() - this.sequenceStartTime && (n = !1),
            n ? this.session.mergeUndoDeltas = !0 : -1 !== i.indexOf(e.command.name) && (this.sequenceStartTime = Date.now()))
        }
        ,
        this.setKeyboardHandler = function(t, i) {
            var n;
            t && "string" == typeof t && "ace" != t ? (this.$keybindingId = t,
            n = this,
            m.loadModule(["keybinding", t], function(e) {
                n.$keybindingId == t && n.keyBinding.setKeyboardHandler(e && e.handler),
                i && i()
            })) : (this.$keybindingId = null,
            this.keyBinding.setKeyboardHandler(t),
            i && i())
        }
        ,
        this.getKeyboardHandler = function() {
            return this.keyBinding.getKeyboardHandler()
        }
        ,
        this.setSession = function(e) {
            var t, i;
            this.session != e && (this.curOp && this.endOperation(),
            this.curOp = {},
            (t = this.session) && (this.session.off("change", this.$onDocumentChange),
            this.session.off("changeMode", this.$onChangeMode),
            this.session.off("tokenizerUpdate", this.$onTokenizerUpdate),
            this.session.off("changeTabSize", this.$onChangeTabSize),
            this.session.off("changeWrapLimit", this.$onChangeWrapLimit),
            this.session.off("changeWrapMode", this.$onChangeWrapMode),
            this.session.off("changeFold", this.$onChangeFold),
            this.session.off("changeFrontMarker", this.$onChangeFrontMarker),
            this.session.off("changeBackMarker", this.$onChangeBackMarker),
            this.session.off("changeBreakpoint", this.$onChangeBreakpoint),
            this.session.off("changeAnnotation", this.$onChangeAnnotation),
            this.session.off("changeOverwrite", this.$onCursorChange),
            this.session.off("changeScrollTop", this.$onScrollTopChange),
            this.session.off("changeScrollLeft", this.$onScrollLeftChange),
            (i = this.session.getSelection()).off("changeCursor", this.$onCursorChange),
            i.off("changeSelection", this.$onSelectionChange)),
            (this.session = e) ? (this.$onDocumentChange = this.onDocumentChange.bind(this),
            e.on("change", this.$onDocumentChange),
            this.renderer.setSession(e),
            this.$onChangeMode = this.onChangeMode.bind(this),
            e.on("changeMode", this.$onChangeMode),
            this.$onTokenizerUpdate = this.onTokenizerUpdate.bind(this),
            e.on("tokenizerUpdate", this.$onTokenizerUpdate),
            this.$onChangeTabSize = this.renderer.onChangeTabSize.bind(this.renderer),
            e.on("changeTabSize", this.$onChangeTabSize),
            this.$onChangeWrapLimit = this.onChangeWrapLimit.bind(this),
            e.on("changeWrapLimit", this.$onChangeWrapLimit),
            this.$onChangeWrapMode = this.onChangeWrapMode.bind(this),
            e.on("changeWrapMode", this.$onChangeWrapMode),
            this.$onChangeFold = this.onChangeFold.bind(this),
            e.on("changeFold", this.$onChangeFold),
            this.$onChangeFrontMarker = this.onChangeFrontMarker.bind(this),
            this.session.on("changeFrontMarker", this.$onChangeFrontMarker),
            this.$onChangeBackMarker = this.onChangeBackMarker.bind(this),
            this.session.on("changeBackMarker", this.$onChangeBackMarker),
            this.$onChangeBreakpoint = this.onChangeBreakpoint.bind(this),
            this.session.on("changeBreakpoint", this.$onChangeBreakpoint),
            this.$onChangeAnnotation = this.onChangeAnnotation.bind(this),
            this.session.on("changeAnnotation", this.$onChangeAnnotation),
            this.$onCursorChange = this.onCursorChange.bind(this),
            this.session.on("changeOverwrite", this.$onCursorChange),
            this.$onScrollTopChange = this.onScrollTopChange.bind(this),
            this.session.on("changeScrollTop", this.$onScrollTopChange),
            this.$onScrollLeftChange = this.onScrollLeftChange.bind(this),
            this.session.on("changeScrollLeft", this.$onScrollLeftChange),
            this.selection = e.getSelection(),
            this.selection.on("changeCursor", this.$onCursorChange),
            this.$onSelectionChange = this.onSelectionChange.bind(this),
            this.selection.on("changeSelection", this.$onSelectionChange),
            this.onChangeMode(),
            this.onCursorChange(),
            this.onScrollTopChange(),
            this.onScrollLeftChange(),
            this.onSelectionChange(),
            this.onChangeFrontMarker(),
            this.onChangeBackMarker(),
            this.onChangeBreakpoint(),
            this.onChangeAnnotation(),
            this.session.getUseWrapMode() && this.renderer.adjustWrapLimit(),
            this.renderer.updateFull()) : (this.selection = null,
            this.renderer.setSession(e)),
            this._signal("changeSession", {
                session: e,
                oldSession: t
            }),
            this.curOp = null,
            t && t._signal("changeEditor", {
                oldEditor: this
            }),
            e && e._signal("changeEditor", {
                editor: this
            }),
            e && e.bgTokenizer && e.bgTokenizer.scheduleStart())
        }
        ,
        this.getSession = function() {
            return this.session
        }
        ,
        this.setValue = function(e, t) {
            return this.session.doc.setValue(e),
            t ? 1 == t ? this.navigateFileEnd() : -1 == t && this.navigateFileStart() : this.selectAll(),
            e
        }
        ,
        this.getValue = function() {
            return this.session.getValue()
        }
        ,
        this.getSelection = function() {
            return this.selection
        }
        ,
        this.resize = function(e) {
            this.renderer.onResize(e)
        }
        ,
        this.setTheme = function(e, t) {
            this.renderer.setTheme(e, t)
        }
        ,
        this.getTheme = function() {
            return this.renderer.getTheme()
        }
        ,
        this.setStyle = function(e) {
            this.renderer.setStyle(e)
        }
        ,
        this.unsetStyle = function(e) {
            this.renderer.unsetStyle(e)
        }
        ,
        this.getFontSize = function() {
            return this.getOption("fontSize") || n.computedStyle(this.container).fontSize
        }
        ,
        this.setFontSize = function(e) {
            this.setOption("fontSize", e)
        }
        ,
        this.$highlightBrackets = function() {
            var n;
            this.$highlightPending || ((n = this).$highlightPending = !0,
            setTimeout(function() {
                n.$highlightPending = !1;
                var e, t, i = n.session;
                i && i.bgTokenizer && (i.$bracketHighlight && (i.$bracketHighlight.markerIds.forEach(function(e) {
                    i.removeMarker(e)
                }),
                i.$bracketHighlight = null),
                !(e = i.getMatchingBracketRanges(n.getCursorPosition())) && i.$mode.getMatching && (e = i.$mode.getMatching(n.session)),
                e && (t = "ace_bracket",
                Array.isArray(e) ? 1 == e.length && (t = "ace_error_bracket") : e = [e],
                2 == e.length && (0 == w.comparePoints(e[0].end, e[1].start) ? e = [w.fromPoints(e[0].start, e[1].end)] : 0 == w.comparePoints(e[0].start, e[1].end) && (e = [w.fromPoints(e[1].start, e[0].end)])),
                i.$bracketHighlight = {
                    ranges: e,
                    markerIds: e.map(function(e) {
                        return i.addMarker(e, t, "text")
                    })
                }))
            }, 50))
        }
        ,
        this.$highlightTags = function() {
            var m;
            this.$highlightTagPending || ((m = this).$highlightTagPending = !0,
            setTimeout(function() {
                m.$highlightTagPending = !1;
                var e = m.session;
                if (e && e.bgTokenizer) {
                    var t = m.getCursorPosition()
                      , i = new v(m.session,t.row,t.column)
                      , n = i.getCurrentToken();
                    if (!n || !/\b(?:tag-open|tag-name)/.test(n.type))
                        return e.removeMarker(e.$tagHighlight),
                        void (e.$tagHighlight = null);
                    if (-1 === n.type.indexOf("tag-open") || (n = i.stepForward())) {
                        var s = n.value
                          , o = n.value
                          , r = 0
                          , a = i.stepBackward();
                        if ("<" === a.value)
                            for (; a = n,
                            (n = i.stepForward()) && (-1 !== n.type.indexOf("tag-name") ? s === (o = n.value) && ("<" === a.value ? r++ : "</" === a.value && r--) : s === o && "/>" === n.value && r--),
                            n && 0 <= r; )
                                ;
                        else {
                            do {
                                if (n = a,
                                a = i.stepBackward(),
                                n)
                                    if (-1 !== n.type.indexOf("tag-name"))
                                        s === n.value && ("<" === a.value ? r++ : "</" === a.value && r--);
                                    else if ("/>" === n.value) {
                                        for (var l = 0, h = a; h; ) {
                                            if (-1 !== h.type.indexOf("tag-name") && h.value === s) {
                                                r--;
                                                break
                                            }
                                            if ("<" === h.value)
                                                break;
                                            h = i.stepBackward(),
                                            l++
                                        }
                                        for (var c = 0; c < l; c++)
                                            i.stepForward()
                                    }
                            } while (a && r <= 0);
                            i.stepForward()
                        }
                        if (!n)
                            return e.removeMarker(e.$tagHighlight),
                            void (e.$tagHighlight = null);
                        var u = i.getCurrentTokenRow()
                          , d = i.getCurrentTokenColumn()
                          , g = new w(u,d,u,d + n.value.length)
                          , f = e.$backMarkers[e.$tagHighlight];
                        e.$tagHighlight && null != f && 0 !== g.compareRange(f.range) && (e.removeMarker(e.$tagHighlight),
                        e.$tagHighlight = null),
                        e.$tagHighlight || (e.$tagHighlight = e.addMarker(g, "ace_bracket", "text"))
                    }
                }
            }, 50))
        }
        ,
        this.focus = function() {
            var e = this;
            setTimeout(function() {
                e.isFocused() || e.textInput.focus()
            }),
            this.textInput.focus()
        }
        ,
        this.isFocused = function() {
            return this.textInput.isFocused()
        }
        ,
        this.blur = function() {
            this.textInput.blur()
        }
        ,
        this.onFocus = function(e) {
            this.$isFocused || (this.$isFocused = !0,
            this.renderer.showCursor(),
            this.renderer.visualizeFocus(),
            this._emit("focus", e))
        }
        ,
        this.onBlur = function(e) {
            this.$isFocused && (this.$isFocused = !1,
            this.renderer.hideCursor(),
            this.renderer.visualizeBlur(),
            this._emit("blur", e))
        }
        ,
        this.$cursorChange = function() {
            this.renderer.updateCursor(),
            this.$highlightBrackets(),
            this.$highlightTags(),
            this.$updateHighlightActiveLine()
        }
        ,
        this.onDocumentChange = function(e) {
            var t = this.session.$useWrapMode
              , i = e.start.row == e.end.row ? e.end.row : 1 / 0;
            this.renderer.updateLines(e.start.row, i, t),
            this._signal("change", e),
            this.$cursorChange()
        }
        ,
        this.onTokenizerUpdate = function(e) {
            var t = e.data;
            this.renderer.updateLines(t.first, t.last)
        }
        ,
        this.onScrollTopChange = function() {
            this.renderer.scrollToY(this.session.getScrollTop())
        }
        ,
        this.onScrollLeftChange = function() {
            this.renderer.scrollToX(this.session.getScrollLeft())
        }
        ,
        this.onCursorChange = function() {
            this.$cursorChange(),
            this._signal("changeSelection")
        }
        ,
        this.$updateHighlightActiveLine = function() {
            var e, t, i = this.getSession();
            this.$highlightActiveLine && ("line" == this.$selectionStyle && this.selection.isMultiLine() || (e = this.getCursorPosition()),
            this.renderer.theme && this.renderer.theme.$selectionColorConflict && !this.selection.isEmpty() && (e = !1),
            !this.renderer.$maxLines || 1 !== this.session.getLength() || 1 < this.renderer.$minLines || (e = !1)),
            i.$highlightLineMarker && !e ? (i.removeMarker(i.$highlightLineMarker.id),
            i.$highlightLineMarker = null) : !i.$highlightLineMarker && e ? ((t = new w(e.row,e.column,e.row,1 / 0)).id = i.addMarker(t, "ace_active-line", "screenLine"),
            i.$highlightLineMarker = t) : e && (i.$highlightLineMarker.start.row = e.row,
            i.$highlightLineMarker.end.row = e.row,
            i.$highlightLineMarker.start.column = e.column,
            i._signal("changeBackMarker"))
        }
        ,
        this.onSelectionChange = function(e) {
            var t, i, n = this.session;
            n.$selectionMarker && n.removeMarker(n.$selectionMarker),
            n.$selectionMarker = null,
            this.selection.isEmpty() ? this.$updateHighlightActiveLine() : (t = this.selection.getRange(),
            i = this.getSelectionStyle(),
            n.$selectionMarker = n.addMarker(t, "ace_selection", i));
            var s = this.$highlightSelectedWord && this.$getSelectionHighLightRegexp();
            this.session.highlight(s),
            this._signal("changeSelection")
        }
        ,
        this.$getSelectionHighLightRegexp = function() {
            var e = this.session
              , t = this.getSelectionRange();
            if (!t.isEmpty() && !t.isMultiLine()) {
                var i = t.start.column
                  , n = t.end.column
                  , s = e.getLine(t.start.row)
                  , o = s.substring(i, n);
                if (!(5e3 < o.length) && /[\w\d]/.test(o)) {
                    var r = this.$search.$assembleRegExp({
                        wholeWord: !0,
                        caseSensitive: !0,
                        needle: o
                    })
                      , a = s.substring(i - 1, n + 1);
                    if (r.test(a))
                        return r
                }
            }
        }
        ,
        this.onChangeFrontMarker = function() {
            this.renderer.updateFrontMarkers()
        }
        ,
        this.onChangeBackMarker = function() {
            this.renderer.updateBackMarkers()
        }
        ,
        this.onChangeBreakpoint = function() {
            this.renderer.updateBreakpoints()
        }
        ,
        this.onChangeAnnotation = function() {
            this.renderer.setAnnotations(this.session.getAnnotations())
        }
        ,
        this.onChangeMode = function(e) {
            this.renderer.updateText(),
            this._emit("changeMode", e)
        }
        ,
        this.onChangeWrapLimit = function() {
            this.renderer.updateFull()
        }
        ,
        this.onChangeWrapMode = function() {
            this.renderer.onResize(!0)
        }
        ,
        this.onChangeFold = function() {
            this.$updateHighlightActiveLine(),
            this.renderer.updateFull()
        }
        ,
        this.getSelectedText = function() {
            return this.session.getTextRange(this.getSelectionRange())
        }
        ,
        this.getCopyText = function() {
            var e = this.getSelectedText()
              , t = this.session.doc.getNewLineCharacter()
              , i = !1;
            if (!e && this.$copyWithEmptySelection) {
                i = !0;
                for (var n = this.selection.getAllRanges(), s = 0; s < n.length; s++) {
                    var o = n[s];
                    s && n[s - 1].start.row == o.start.row || (e += this.session.getLine(o.start.row) + t)
                }
            }
            var r = {
                text: e
            };
            return this._signal("copy", r),
            $.lineMode = i ? r.text : "",
            r.text
        }
        ,
        this.onCopy = function() {
            this.commands.exec("copy", this)
        }
        ,
        this.onCut = function() {
            this.commands.exec("cut", this)
        }
        ,
        this.onPaste = function(e, t) {
            var i = {
                text: e,
                event: t
            };
            this.commands.exec("paste", this, i)
        }
        ,
        this.$handlePaste = function(e) {
            "string" == typeof e && (e = {
                text: e
            }),
            this._signal("paste", e);
            var t = e.text
              , i = t == $.lineMode
              , n = this.session;
            if (!this.inMultiSelectMode || this.inVirtualSelectionMode)
                i ? n.insert({
                    row: this.selection.lead.row,
                    column: 0
                }, t) : this.insert(t);
            else if (i)
                this.selection.rangeList.ranges.forEach(function(e) {
                    n.insert({
                        row: e.start.row,
                        column: 0
                    }, t)
                });
            else {
                var s = t.split(/\r\n|\r|\n/)
                  , o = this.selection.rangeList.ranges
                  , r = !(2 != s.length || s[0] && s[1]);
                if (s.length != o.length || r)
                    return this.commands.exec("insertstring", this, t);
                for (var a = o.length; a--; ) {
                    var l = o[a];
                    l.isEmpty() || n.remove(l),
                    n.insert(l.start, s[a])
                }
            }
        }
        ,
        this.execCommand = function(e, t) {
            return this.commands.exec(e, this, t)
        }
        ,
        this.insert = function(e, t) {
            var i, n, s, o = this.session, r = o.getMode(), a = this.getCursorPosition();
            !this.getBehavioursEnabled() || t || (i = r.transformAction(o.getState(a.row), "insertion", this, o, e)) && (e !== i.text && (this.inVirtualSelectionMode || (this.session.mergeUndoDeltas = !1,
            this.mergeNextCommand = !1)),
            e = i.text),
            "\t" == e && (e = this.session.getTabString()),
            this.selection.isEmpty() ? this.session.getOverwrite() && -1 == e.indexOf("\n") && ((n = new w.fromPoints(a,a)).end.column += e.length,
            this.session.remove(n)) : (n = this.getSelectionRange(),
            a = this.session.remove(n),
            this.clearSelection()),
            "\n" != e && "\r\n" != e || (u = o.getLine(a.row),
            a.column > u.search(/\S|$/) && (s = u.substr(a.column).search(/\S|$/),
            o.doc.removeInLine(a.row, a.column, a.column + s))),
            this.clearSelection();
            var l, h = a.column, c = o.getState(a.row), u = o.getLine(a.row), d = r.checkOutdent(c, u, e);
            o.insert(a, e),
            i && i.selection && (2 == i.selection.length ? this.selection.setSelectionRange(new w(a.row,h + i.selection[0],a.row,h + i.selection[1])) : this.selection.setSelectionRange(new w(a.row + i.selection[0],i.selection[1],a.row + i.selection[2],i.selection[3]))),
            this.$enableAutoIndent && (o.getDocument().isNewLine(e) && (l = r.getNextLineIndent(c, u.slice(0, a.column), o.getTabString()),
            o.insert({
                row: a.row + 1,
                column: 0
            }, l)),
            d && r.autoOutdent(c, o, a.row))
        }
        ,
        this.autoIndent = function() {
            var e, t, i, n = this.session, s = n.getMode();
            i = this.selection.isEmpty() ? (t = 0,
            n.doc.getLength() - 1) : (t = (e = this.getSelectionRange()).start.row,
            e.end.row);
            for (var o, r, a, l = "", h = "", c = "", u = n.getTabString(), d = t; d <= i; d++)
                0 < d && (l = n.getState(d - 1),
                h = n.getLine(d - 1),
                c = s.getNextLineIndent(l, h, u)),
                o = n.getLine(d),
                c !== (r = s.$getIndent(o)) && (0 < r.length && (a = new w(d,0,d,r.length),
                n.remove(a)),
                0 < c.length && n.insert({
                    row: d,
                    column: 0
                }, c)),
                s.autoOutdent(l, n, d)
        }
        ,
        this.onTextInput = function(e, t) {
            if (!t)
                return this.keyBinding.onTextInput(e);
            this.startOperation({
                command: {
                    name: "insertstring"
                }
            });
            var i = this.applyComposition.bind(this, e, t);
            this.selection.rangeCount ? this.forEachSelection(i) : i(),
            this.endOperation()
        }
        ,
        this.applyComposition = function(e, t) {
            var i;
            (t.extendLeft || t.extendRight) && ((i = this.selection.getRange()).start.column -= t.extendLeft,
            i.end.column += t.extendRight,
            i.start.column < 0 && (i.start.row--,
            i.start.column += this.session.getLine(i.start.row).length + 1),
            this.selection.setRange(i),
            e || i.isEmpty() || this.remove()),
            !e && this.selection.isEmpty() || this.insert(e, !0),
            (t.restoreStart || t.restoreEnd) && ((i = this.selection.getRange()).start.column -= t.restoreStart,
            i.end.column -= t.restoreEnd,
            this.selection.setRange(i))
        }
        ,
        this.onCommandKey = function(e, t, i) {
            return this.keyBinding.onCommandKey(e, t, i)
        }
        ,
        this.setOverwrite = function(e) {
            this.session.setOverwrite(e)
        }
        ,
        this.getOverwrite = function() {
            return this.session.getOverwrite()
        }
        ,
        this.toggleOverwrite = function() {
            this.session.toggleOverwrite()
        }
        ,
        this.setScrollSpeed = function(e) {
            this.setOption("scrollSpeed", e)
        }
        ,
        this.getScrollSpeed = function() {
            return this.getOption("scrollSpeed")
        }
        ,
        this.setDragDelay = function(e) {
            this.setOption("dragDelay", e)
        }
        ,
        this.getDragDelay = function() {
            return this.getOption("dragDelay")
        }
        ,
        this.setSelectionStyle = function(e) {
            this.setOption("selectionStyle", e)
        }
        ,
        this.getSelectionStyle = function() {
            return this.getOption("selectionStyle")
        }
        ,
        this.setHighlightActiveLine = function(e) {
            this.setOption("highlightActiveLine", e)
        }
        ,
        this.getHighlightActiveLine = function() {
            return this.getOption("highlightActiveLine")
        }
        ,
        this.setHighlightGutterLine = function(e) {
            this.setOption("highlightGutterLine", e)
        }
        ,
        this.getHighlightGutterLine = function() {
            return this.getOption("highlightGutterLine")
        }
        ,
        this.setHighlightSelectedWord = function(e) {
            this.setOption("highlightSelectedWord", e)
        }
        ,
        this.getHighlightSelectedWord = function() {
            return this.$highlightSelectedWord
        }
        ,
        this.setAnimatedScroll = function(e) {
            this.renderer.setAnimatedScroll(e)
        }
        ,
        this.getAnimatedScroll = function() {
            return this.renderer.getAnimatedScroll()
        }
        ,
        this.setShowInvisibles = function(e) {
            this.renderer.setShowInvisibles(e)
        }
        ,
        this.getShowInvisibles = function() {
            return this.renderer.getShowInvisibles()
        }
        ,
        this.setDisplayIndentGuides = function(e) {
            this.renderer.setDisplayIndentGuides(e)
        }
        ,
        this.getDisplayIndentGuides = function() {
            return this.renderer.getDisplayIndentGuides()
        }
        ,
        this.setShowPrintMargin = function(e) {
            this.renderer.setShowPrintMargin(e)
        }
        ,
        this.getShowPrintMargin = function() {
            return this.renderer.getShowPrintMargin()
        }
        ,
        this.setPrintMarginColumn = function(e) {
            this.renderer.setPrintMarginColumn(e)
        }
        ,
        this.getPrintMarginColumn = function() {
            return this.renderer.getPrintMarginColumn()
        }
        ,
        this.setReadOnly = function(e) {
            this.setOption("readOnly", e)
        }
        ,
        this.getReadOnly = function() {
            return this.getOption("readOnly")
        }
        ,
        this.setBehavioursEnabled = function(e) {
            this.setOption("behavioursEnabled", e)
        }
        ,
        this.getBehavioursEnabled = function() {
            return this.getOption("behavioursEnabled")
        }
        ,
        this.setWrapBehavioursEnabled = function(e) {
            this.setOption("wrapBehavioursEnabled", e)
        }
        ,
        this.getWrapBehavioursEnabled = function() {
            return this.getOption("wrapBehavioursEnabled")
        }
        ,
        this.setShowFoldWidgets = function(e) {
            this.setOption("showFoldWidgets", e)
        }
        ,
        this.getShowFoldWidgets = function() {
            return this.getOption("showFoldWidgets")
        }
        ,
        this.setFadeFoldWidgets = function(e) {
            this.setOption("fadeFoldWidgets", e)
        }
        ,
        this.getFadeFoldWidgets = function() {
            return this.getOption("fadeFoldWidgets")
        }
        ,
        this.remove = function(e) {
            this.selection.isEmpty() && ("left" == e ? this.selection.selectLeft() : this.selection.selectRight());
            var t, i, n, s, o, r = this.getSelectionRange();
            this.getBehavioursEnabled() && (i = (t = this.session).getState(r.start.row),
            n = t.getMode().transformAction(i, "deletion", this, t, r),
            0 !== r.end.column || "\n" == (s = t.getTextRange(r))[s.length - 1] && (o = t.getLine(r.end.row),
            /^\s+$/.test(o) && (r.end.column = o.length)),
            n && (r = n)),
            this.session.remove(r),
            this.clearSelection()
        }
        ,
        this.removeWordRight = function() {
            this.selection.isEmpty() && this.selection.selectWordRight(),
            this.session.remove(this.getSelectionRange()),
            this.clearSelection()
        }
        ,
        this.removeWordLeft = function() {
            this.selection.isEmpty() && this.selection.selectWordLeft(),
            this.session.remove(this.getSelectionRange()),
            this.clearSelection()
        }
        ,
        this.removeToLineStart = function() {
            this.selection.isEmpty() && this.selection.selectLineStart(),
            this.selection.isEmpty() && this.selection.selectLeft(),
            this.session.remove(this.getSelectionRange()),
            this.clearSelection()
        }
        ,
        this.removeToLineEnd = function() {
            this.selection.isEmpty() && this.selection.selectLineEnd();
            var e = this.getSelectionRange();
            e.start.column == e.end.column && e.start.row == e.end.row && (e.end.column = 0,
            e.end.row++),
            this.session.remove(e),
            this.clearSelection()
        }
        ,
        this.splitLine = function() {
            this.selection.isEmpty() || (this.session.remove(this.getSelectionRange()),
            this.clearSelection());
            var e = this.getCursorPosition();
            this.insert("\n"),
            this.moveCursorToPosition(e)
        }
        ,
        this.transposeLetters = function() {
            var e, t, i, n, s;
            !this.selection.isEmpty() || 0 !== (t = (e = this.getCursorPosition()).column) && (s = t < (i = this.session.getLine(e.row)).length ? (n = i.charAt(t) + i.charAt(t - 1),
            new w(e.row,t - 1,e.row,t + 1)) : (n = i.charAt(t - 1) + i.charAt(t - 2),
            new w(e.row,t - 2,e.row,t)),
            this.session.replace(s, n),
            this.session.selection.moveToPosition(s.end))
        }
        ,
        this.toLowerCase = function() {
            var e = this.getSelectionRange();
            this.selection.isEmpty() && this.selection.selectWord();
            var t = this.getSelectionRange()
              , i = this.session.getTextRange(t);
            this.session.replace(t, i.toLowerCase()),
            this.selection.setSelectionRange(e)
        }
        ,
        this.toUpperCase = function() {
            var e = this.getSelectionRange();
            this.selection.isEmpty() && this.selection.selectWord();
            var t = this.getSelectionRange()
              , i = this.session.getTextRange(t);
            this.session.replace(t, i.toUpperCase()),
            this.selection.setSelectionRange(e)
        }
        ,
        this.indent = function() {
            var e = this.session
              , t = this.getSelectionRange();
            if (!(t.start.row < t.end.row)) {
                if (t.start.column < t.end.column) {
                    var i = e.getTextRange(t);
                    if (!/^\s+$/.test(i)) {
                        h = this.$getSelectedRows();
                        return void e.indentRows(h.first, h.last, "\t")
                    }
                }
                var n = e.getLine(t.start.row)
                  , s = t.start
                  , o = e.getTabSize()
                  , r = e.documentToScreenColumn(s.row, s.column);
                if (this.session.getUseSoftTabs())
                    var a = o - r % o
                      , l = p.stringRepeat(" ", a);
                else {
                    for (a = r % o; " " == n[t.start.column - 1] && a; )
                        t.start.column--,
                        a--;
                    this.selection.setSelectionRange(t),
                    l = "\t"
                }
                return this.insert(l)
            }
            var h = this.$getSelectedRows();
            e.indentRows(h.first, h.last, "\t")
        }
        ,
        this.blockIndent = function() {
            var e = this.$getSelectedRows();
            this.session.indentRows(e.first, e.last, "\t")
        }
        ,
        this.blockOutdent = function() {
            var e = this.session.getSelection();
            this.session.outdentRows(e.getRange())
        }
        ,
        this.sortLines = function() {
            for (var e = this.$getSelectedRows(), t = this.session, i = [], n = e.first; n <= e.last; n++)
                i.push(t.getLine(n));
            i.sort(function(e, t) {
                return e.toLowerCase() < t.toLowerCase() ? -1 : e.toLowerCase() > t.toLowerCase() ? 1 : 0
            });
            for (var s = new w(0,0,0,0), n = e.first; n <= e.last; n++) {
                var o = t.getLine(n);
                s.start.row = n,
                s.end.row = n,
                s.end.column = o.length,
                t.replace(s, i[n - e.first])
            }
        }
        ,
        this.toggleCommentLines = function() {
            var e = this.session.getState(this.getCursorPosition().row)
              , t = this.$getSelectedRows();
            this.session.getMode().toggleCommentLines(e, this.session, t.first, t.last)
        }
        ,
        this.toggleBlockComment = function() {
            var e = this.getCursorPosition()
              , t = this.session.getState(e.row)
              , i = this.getSelectionRange();
            this.session.getMode().toggleBlockComment(t, this.session, i, e)
        }
        ,
        this.getNumberAt = function(e, t) {
            var i = /[\-]?[0-9]+(?:\.[0-9]+)?/g;
            i.lastIndex = 0;
            for (var n = this.session.getLine(e); i.lastIndex < t; ) {
                var s = i.exec(n);
                if (s.index <= t && s.index + s[0].length >= t)
                    return {
                        value: s[0],
                        start: s.index,
                        end: s.index + s[0].length
                    }
            }
            return null
        }
        ,
        this.modifyNumber = function(e) {
            var t, i, n, s, o, r, a = this.selection.getCursor().row, l = this.selection.getCursor().column, h = new w(a,l - 1,a,l), c = this.session.getTextRange(h);
            !isNaN(parseFloat(c)) && isFinite(c) ? (t = this.getNumberAt(a, l)) && (i = 0 <= t.value.indexOf(".") ? t.start + t.value.indexOf(".") + 1 : t.end,
            n = t.start + t.value.length - i,
            s = parseFloat(t.value),
            s *= Math.pow(10, n),
            i !== t.end && l < i ? e *= Math.pow(10, t.end - l - 1) : e *= Math.pow(10, t.end - l),
            s += e,
            o = (s /= Math.pow(10, n)).toFixed(n),
            r = new w(a,t.start,a,t.end),
            this.session.replace(r, o),
            this.moveCursorTo(a, Math.max(t.start + 1, l + o.length - t.value.length))) : this.toggleWord()
        }
        ,
        this.$toggleWordPairs = [["first", "last"], ["true", "false"], ["yes", "no"], ["width", "height"], ["top", "bottom"], ["right", "left"], ["on", "off"], ["x", "y"], ["get", "set"], ["max", "min"], ["horizontal", "vertical"], ["show", "hide"], ["add", "remove"], ["up", "down"], ["before", "after"], ["even", "odd"], ["in", "out"], ["inside", "outside"], ["next", "previous"], ["increase", "decrease"], ["attach", "detach"], ["&&", "||"], ["==", "!="]],
        this.toggleWord = function() {
            var i = this.selection.getCursor().row
              , e = this.selection.getCursor().column;
            this.selection.selectWord();
            var n = this.getSelectedText()
              , s = this.selection.getWordRange().start.column
              , t = n.replace(/([a-z]+|[A-Z]+)(?=[A-Z_]|$)/g, "$1 ").split(/\s/)
              , o = e - s - 1;
            o < 0 && (o = 0);
            var r = 0
              , a = 0
              , l = this;
            n.match(/[A-Za-z0-9_]+/) && t.forEach(function(e, t) {
                a = r + e.length,
                r <= o && o <= a && (n = e,
                l.selection.clearSelection(),
                l.moveCursorTo(i, r + s),
                l.selection.selectTo(i, a + s)),
                r = a
            });
            for (var h, c = this.$toggleWordPairs, u = 0; u < c.length; u++)
                for (var d = c[u], g = 0; g <= 1; g++) {
                    var f = +!g
                      , m = n.match(new RegExp("^\\s?_?(" + p.escapeRegExp(d[g]) + ")\\s?$","i"));
                    m && n.match(new RegExp("([_]|^|\\s)(" + p.escapeRegExp(m[1]) + ")($|\\s)","g")) && (h = n.replace(new RegExp(p.escapeRegExp(d[g]),"i"), function(e) {
                        var t = d[f];
                        return e.toUpperCase() == e ? t = t.toUpperCase() : e.charAt(0).toUpperCase() == e.charAt(0) && (t = t.substr(0, 0) + d[f].charAt(0).toUpperCase() + t.substr(1)),
                        t
                    }),
                    this.insert(h),
                    h = "")
                }
        }
        ,
        this.removeLines = function() {
            var e = this.$getSelectedRows();
            this.session.removeFullLines(e.first, e.last),
            this.clearSelection()
        }
        ,
        this.duplicateSelection = function() {
            var e, t, i, n = this.selection, s = this.session, o = n.getRange(), r = n.isBackwards();
            o.isEmpty() ? (e = o.start.row,
            s.duplicateLines(e, e)) : (t = r ? o.start : o.end,
            i = s.insert(t, s.getTextRange(o), !1),
            o.start = t,
            o.end = i,
            n.setSelectionRange(o, r))
        }
        ,
        this.moveLinesDown = function() {
            this.$moveLines(1, !1)
        }
        ,
        this.moveLinesUp = function() {
            this.$moveLines(-1, !1)
        }
        ,
        this.moveText = function(e, t, i) {
            return this.session.moveText(e, t, i)
        }
        ,
        this.copyLinesUp = function() {
            this.$moveLines(-1, !0)
        }
        ,
        this.copyLinesDown = function() {
            this.$moveLines(1, !0)
        }
        ,
        this.$moveLines = function(e, t) {
            var i = this.selection;
            if (!i.inMultiSelectMode || this.inVirtualSelectionMode) {
                var n = i.toOrientedRange()
                  , s = this.$getSelectedRows(n)
                  , o = this.session.$moveLines(s.first, s.last, t ? 0 : e);
                t && -1 == e && (o = 0),
                n.moveBy(o, 0),
                i.fromOrientedRange(n)
            } else {
                var r = i.rangeList.ranges;
                i.rangeList.detach(this.session),
                this.inVirtualSelectionMode = !0;
                for (var a = 0, l = 0, h = r.length, c = 0; c < h; c++) {
                    var u = c;
                    r[c].moveBy(a, 0);
                    for (var d = (s = this.$getSelectedRows(r[c])).first, g = s.last; ++c < h; ) {
                        l && r[c].moveBy(l, 0);
                        var f = this.$getSelectedRows(r[c]);
                        if (t && f.first != g)
                            break;
                        if (!t && f.first > g + 1)
                            break;
                        g = f.last
                    }
                    for (c--,
                    a = this.session.$moveLines(d, g, t ? 0 : e),
                    t && -1 == e && (u = c + 1); u <= c; )
                        r[u].moveBy(a, 0),
                        u++;
                    t || (a = 0),
                    l += a
                }
                i.fromOrientedRange(i.ranges[0]),
                i.rangeList.attach(this.session),
                this.inVirtualSelectionMode = !1
            }
        }
        ,
        this.$getSelectedRows = function(e) {
            return e = (e || this.getSelectionRange()).collapseRows(),
            {
                first: this.session.getRowFoldStart(e.start.row),
                last: this.session.getRowFoldEnd(e.end.row)
            }
        }
        ,
        this.onCompositionStart = function(e) {
            this.renderer.showComposition(e)
        }
        ,
        this.onCompositionUpdate = function(e) {
            this.renderer.setCompositionText(e)
        }
        ,
        this.onCompositionEnd = function() {
            this.renderer.hideComposition()
        }
        ,
        this.getFirstVisibleRow = function() {
            return this.renderer.getFirstVisibleRow()
        }
        ,
        this.getLastVisibleRow = function() {
            return this.renderer.getLastVisibleRow()
        }
        ,
        this.isRowVisible = function(e) {
            return e >= this.getFirstVisibleRow() && e <= this.getLastVisibleRow()
        }
        ,
        this.isRowFullyVisible = function(e) {
            return e >= this.renderer.getFirstFullyVisibleRow() && e <= this.renderer.getLastFullyVisibleRow()
        }
        ,
        this.$getVisibleRowCount = function() {
            return this.renderer.getScrollBottomRow() - this.renderer.getScrollTopRow() + 1
        }
        ,
        this.$moveByPage = function(e, t) {
            var i = this.renderer
              , n = this.renderer.layerConfig
              , s = e * Math.floor(n.height / n.lineHeight);
            !0 === t ? this.selection.$moveSelection(function() {
                this.moveCursorBy(s, 0)
            }) : !1 === t && (this.selection.moveCursorBy(s, 0),
            this.selection.clearSelection());
            var o = i.scrollTop;
            i.scrollBy(0, s * n.lineHeight),
            null != t && i.scrollCursorIntoView(null, .5),
            i.animateScrolling(o)
        }
        ,
        this.selectPageDown = function() {
            this.$moveByPage(1, !0)
        }
        ,
        this.selectPageUp = function() {
            this.$moveByPage(-1, !0)
        }
        ,
        this.gotoPageDown = function() {
            this.$moveByPage(1, !1)
        }
        ,
        this.gotoPageUp = function() {
            this.$moveByPage(-1, !1)
        }
        ,
        this.scrollPageDown = function() {
            this.$moveByPage(1)
        }
        ,
        this.scrollPageUp = function() {
            this.$moveByPage(-1)
        }
        ,
        this.scrollToRow = function(e) {
            this.renderer.scrollToRow(e)
        }
        ,
        this.scrollToLine = function(e, t, i, n) {
            this.renderer.scrollToLine(e, t, i, n)
        }
        ,
        this.centerSelection = function() {
            var e = this.getSelectionRange()
              , t = {
                row: Math.floor(e.start.row + (e.end.row - e.start.row) / 2),
                column: Math.floor(e.start.column + (e.end.column - e.start.column) / 2)
            };
            this.renderer.alignCursor(t, .5)
        }
        ,
        this.getCursorPosition = function() {
            return this.selection.getCursor()
        }
        ,
        this.getCursorPositionScreen = function() {
            return this.session.documentToScreenPosition(this.getCursorPosition())
        }
        ,
        this.getSelectionRange = function() {
            return this.selection.getRange()
        }
        ,
        this.selectAll = function() {
            this.selection.selectAll()
        }
        ,
        this.clearSelection = function() {
            this.selection.clearSelection()
        }
        ,
        this.moveCursorTo = function(e, t) {
            this.selection.moveCursorTo(e, t)
        }
        ,
        this.moveCursorToPosition = function(e) {
            this.selection.moveCursorToPosition(e)
        }
        ,
        this.jumpToMatching = function(e, t) {
            var i = this.getCursorPosition()
              , n = new v(this.session,i.row,i.column)
              , s = n.getCurrentToken()
              , o = s || n.stepForward();
            if (o) {
                var r, a, l, h = !1, c = {}, u = i.column - o.start, d = {
                    ")": "(",
                    "(": "(",
                    "]": "[",
                    "[": "[",
                    "{": "{",
                    "}": "{"
                };
                do {
                    if (o.value.match(/[{}()\[\]]/g)) {
                        for (; u < o.value.length && !h; u++)
                            if (d[o.value[u]])
                                switch (a = d[o.value[u]] + "." + o.type.replace("rparen", "lparen"),
                                isNaN(c[a]) && (c[a] = 0),
                                o.value[u]) {
                                case "(":
                                case "[":
                                case "{":
                                    c[a]++;
                                    break;
                                case ")":
                                case "]":
                                case "}":
                                    c[a]--,
                                    -1 === c[a] && (r = "bracket",
                                    h = !0)
                                }
                    } else
                        -1 !== o.type.indexOf("tag-name") && (isNaN(c[o.value]) && (c[o.value] = 0),
                        "<" === s.value ? c[o.value]++ : "</" === s.value && c[o.value]--,
                        -1 === c[o.value] && (r = "tag",
                        h = !0));
                    h || (s = o,
                    o = n.stepForward(),
                    u = 0)
                } while (o && !h);
                if (r) {
                    if ("bracket" === r)
                        (g = this.session.getBracketRange(i)) || (l = (g = new w(n.getCurrentTokenRow(),n.getCurrentTokenColumn() + u - 1,n.getCurrentTokenRow(),n.getCurrentTokenColumn() + u - 1)).start,
                        (t || l.row === i.row && Math.abs(l.column - i.column) < 2) && (g = this.session.getBracketRange(l)));
                    else if ("tag" === r) {
                        if (!o || -1 === o.type.indexOf("tag-name"))
                            return;
                        var g, f = o.value;
                        if (0 === (g = new w(n.getCurrentTokenRow(),n.getCurrentTokenColumn() - 2,n.getCurrentTokenRow(),n.getCurrentTokenColumn() - 2)).compare(i.row, i.column))
                            for (h = !1; o = s,
                            (s = n.stepBackward()) && (-1 !== s.type.indexOf("tag-close") && g.setEnd(n.getCurrentTokenRow(), n.getCurrentTokenColumn() + 1),
                            o.value === f && -1 !== o.type.indexOf("tag-name") && ("<" === s.value ? c[f]++ : "</" === s.value && c[f]--,
                            0 === c[f] && (h = !0))),
                            s && !h; )
                                ;
                        o && o.type.indexOf("tag-name") && ((l = g.start).row == i.row && Math.abs(l.column - i.column) < 2 && (l = g.end))
                    }
                    (l = g && g.cursor || l) && (e ? g && t ? this.selection.setRange(g) : g && g.isEqual(this.getSelectionRange()) ? this.clearSelection() : this.selection.selectTo(l.row, l.column) : this.selection.moveTo(l.row, l.column))
                }
            }
        }
        ,
        this.gotoLine = function(e, t, i) {
            this.selection.clearSelection(),
            this.session.unfold({
                row: e - 1,
                column: t || 0
            }),
            this.exitMultiSelectMode && this.exitMultiSelectMode(),
            this.moveCursorTo(e - 1, t || 0),
            this.isRowFullyVisible(e - 1) || this.scrollToLine(e - 1, !0, i)
        }
        ,
        this.navigateTo = function(e, t) {
            this.selection.moveTo(e, t)
        }
        ,
        this.navigateUp = function(e) {
            if (this.selection.isMultiLine() && !this.selection.isBackwards()) {
                var t = this.selection.anchor.getPosition();
                return this.moveCursorToPosition(t)
            }
            this.selection.clearSelection(),
            this.selection.moveCursorBy(-e || -1, 0)
        }
        ,
        this.navigateDown = function(e) {
            if (this.selection.isMultiLine() && this.selection.isBackwards()) {
                var t = this.selection.anchor.getPosition();
                return this.moveCursorToPosition(t)
            }
            this.selection.clearSelection(),
            this.selection.moveCursorBy(e || 1, 0)
        }
        ,
        this.navigateLeft = function(e) {
            if (this.selection.isEmpty())
                for (e = e || 1; e--; )
                    this.selection.moveCursorLeft();
            else {
                var t = this.getSelectionRange().start;
                this.moveCursorToPosition(t)
            }
            this.clearSelection()
        }
        ,
        this.navigateRight = function(e) {
            if (this.selection.isEmpty())
                for (e = e || 1; e--; )
                    this.selection.moveCursorRight();
            else {
                var t = this.getSelectionRange().end;
                this.moveCursorToPosition(t)
            }
            this.clearSelection()
        }
        ,
        this.navigateLineStart = function() {
            this.selection.moveCursorLineStart(),
            this.clearSelection()
        }
        ,
        this.navigateLineEnd = function() {
            this.selection.moveCursorLineEnd(),
            this.clearSelection()
        }
        ,
        this.navigateFileEnd = function() {
            this.selection.moveCursorFileEnd(),
            this.clearSelection()
        }
        ,
        this.navigateFileStart = function() {
            this.selection.moveCursorFileStart(),
            this.clearSelection()
        }
        ,
        this.navigateWordRight = function() {
            this.selection.moveCursorWordRight(),
            this.clearSelection()
        }
        ,
        this.navigateWordLeft = function() {
            this.selection.moveCursorWordLeft(),
            this.clearSelection()
        }
        ,
        this.replace = function(e, t) {
            t && this.$search.set(t);
            var i = this.$search.find(this.session)
              , n = 0;
            return i && (this.$tryReplace(i, e) && (n = 1),
            this.selection.setSelectionRange(i),
            this.renderer.scrollSelectionIntoView(i.start, i.end)),
            n
        }
        ,
        this.replaceAll = function(e, t) {
            t && this.$search.set(t);
            var i = this.$search.findAll(this.session)
              , n = 0;
            if (!i.length)
                return n;
            var s = this.getSelectionRange();
            this.selection.moveTo(0, 0);
            for (var o = i.length - 1; 0 <= o; --o)
                this.$tryReplace(i[o], e) && n++;
            return this.selection.setSelectionRange(s),
            n
        }
        ,
        this.$tryReplace = function(e, t) {
            var i = this.session.getTextRange(e);
            return null !== (t = this.$search.replace(i, t)) ? (e.end = this.session.replace(e, t),
            e) : null
        }
        ,
        this.getLastSearchOptions = function() {
            return this.$search.getOptions()
        }
        ,
        this.find = function(e, t, i) {
            t = t || {},
            "string" == typeof e || e instanceof RegExp ? t.needle = e : "object" == typeof e && o.mixin(t, e);
            var n = this.selection.getRange();
            null == t.needle && ((e = this.session.getTextRange(n) || this.$search.$options.needle) || (n = this.session.getWordRange(n.start.row, n.start.column),
            e = this.session.getTextRange(n)),
            this.$search.set({
                needle: e
            })),
            this.$search.set(t),
            t.start || this.$search.set({
                start: n
            });
            var s = this.$search.find(this.session);
            return t.preventScroll ? s : s ? (this.revealRange(s, i),
            s) : (t.backwards ? n.start = n.end : n.end = n.start,
            void this.selection.setRange(n))
        }
        ,
        this.findNext = function(e, t) {
            this.find({
                skipCurrent: !0,
                backwards: !1
            }, e, t)
        }
        ,
        this.findPrevious = function(e, t) {
            this.find(e, {
                skipCurrent: !0,
                backwards: !0
            }, t)
        }
        ,
        this.revealRange = function(e, t) {
            this.session.unfold(e),
            this.selection.setSelectionRange(e);
            var i = this.renderer.scrollTop;
            this.renderer.scrollSelectionIntoView(e.start, e.end, .5),
            !1 !== t && this.renderer.animateScrolling(i)
        }
        ,
        this.undo = function() {
            this.session.getUndoManager().undo(this.session),
            this.renderer.scrollCursorIntoView(null, .5)
        }
        ,
        this.redo = function() {
            this.session.getUndoManager().redo(this.session),
            this.renderer.scrollCursorIntoView(null, .5)
        }
        ,
        this.destroy = function() {
            this.$toDestroy && (this.$toDestroy.forEach(function(e) {
                e.destroy()
            }),
            this.$toDestroy = null),
            this.$mouseHandler && this.$mouseHandler.destroy(),
            this.renderer.destroy(),
            this._signal("destroy", this),
            this.session && this.session.destroy(),
            this._$emitInputEvent && this._$emitInputEvent.cancel(),
            this.removeAllListeners()
        }
        ,
        this.setAutoScrollEditorIntoView = function(e) {
            var s, o, r, a, t, i, n;
            e && (r = !1,
            (o = this).$scrollAnchor || (this.$scrollAnchor = document.createElement("div")),
            (a = this.$scrollAnchor).style.cssText = "position:absolute",
            this.container.insertBefore(a, this.container.firstChild),
            t = this.on("changeSelection", function() {
                r = !0
            }),
            i = this.renderer.on("beforeRender", function() {
                r && (s = o.renderer.container.getBoundingClientRect())
            }),
            n = this.renderer.on("afterRender", function() {
                var e, t, i, n;
                r && s && (o.isFocused() || o.searchBox && o.searchBox.isFocused()) && (t = (e = o.renderer).$cursorLayer.$pixelPos,
                i = e.layerConfig,
                n = t.top - i.offset,
                null != (r = 0 <= t.top && n + s.top < 0 || !(t.top < i.height && t.top + s.top + i.lineHeight > window.innerHeight) && null) && (a.style.top = n + "px",
                a.style.left = t.left + "px",
                a.style.height = i.lineHeight + "px",
                a.scrollIntoView(r)),
                r = s = null)
            }),
            this.setAutoScrollEditorIntoView = function(e) {
                e || (delete this.setAutoScrollEditorIntoView,
                this.off("changeSelection", t),
                this.renderer.off("afterRender", n),
                this.renderer.off("beforeRender", i))
            }
            )
        }
        ,
        this.$resetCursorStyle = function() {
            var e = this.$cursorStyle || "ace"
              , t = this.renderer.$cursorLayer;
            t && (t.setSmoothBlinking(/smooth/.test(e)),
            t.isBlinking = !this.$readOnly && "wide" != e,
            n.setCssClass(t.element, "ace_slim-cursors", /slim/.test(e)))
        }
        ,
        this.prompt = function(t, i, n) {
            var s = this;
            m.loadModule("./ext/prompt", function(e) {
                e.prompt(s, t, i, n)
            })
        }
    }
    .call(b.prototype),
    m.defineOptions(b.prototype, "editor", {
        selectionStyle: {
            set: function(e) {
                this.onSelectionChange(),
                this._signal("changeSelectionStyle", {
                    data: e
                })
            },
            initialValue: "line"
        },
        highlightActiveLine: {
            set: function() {
                this.$updateHighlightActiveLine()
            },
            initialValue: !0
        },
        highlightSelectedWord: {
            set: function(e) {
                this.$onSelectionChange()
            },
            initialValue: !0
        },
        readOnly: {
            set: function(e) {
                this.textInput.setReadOnly(e),
                this.$resetCursorStyle()
            },
            initialValue: !1
        },
        copyWithEmptySelection: {
            set: function(e) {
                this.textInput.setCopyWithEmptySelection(e)
            },
            initialValue: !1
        },
        cursorStyle: {
            set: function(e) {
                this.$resetCursorStyle()
            },
            values: ["ace", "slim", "smooth", "wide"],
            initialValue: "ace"
        },
        mergeUndoDeltas: {
            values: [!1, !0, "always"],
            initialValue: !0
        },
        behavioursEnabled: {
            initialValue: !0
        },
        wrapBehavioursEnabled: {
            initialValue: !0
        },
        enableAutoIndent: {
            initialValue: !0
        },
        autoScrollEditorIntoView: {
            set: function(e) {
                this.setAutoScrollEditorIntoView(e)
            }
        },
        keyboardHandler: {
            set: function(e) {
                this.setKeyboardHandler(e)
            },
            get: function() {
                return this.$keybindingId
            },
            handlesSet: !0
        },
        value: {
            set: function(e) {
                this.session.setValue(e)
            },
            get: function() {
                return this.getValue()
            },
            handlesSet: !0,
            hidden: !0
        },
        session: {
            set: function(e) {
                this.setSession(e)
            },
            get: function() {
                return this.session
            },
            handlesSet: !0,
            hidden: !0
        },
        showLineNumbers: {
            set: function(e) {
                this.renderer.$gutterLayer.setShowLineNumbers(e),
                this.renderer.$loop.schedule(this.renderer.CHANGE_GUTTER),
                e && this.$relativeLineNumbers ? y.attach(this) : y.detach(this)
            },
            initialValue: !0
        },
        relativeLineNumbers: {
            set: function(e) {
                this.$showLineNumbers && e ? y.attach(this) : y.detach(this)
            }
        },
        placeholder: {
            set: function(e) {
                this.$updatePlaceholder || (this.$updatePlaceholder = function() {
                    var e, t = this.session && (this.renderer.$composition || this.getValue());
                    t && this.renderer.placeholderNode ? (this.renderer.off("afterRender", this.$updatePlaceholder),
                    n.removeCssClass(this.container, "ace_hasPlaceholder"),
                    this.renderer.placeholderNode.remove(),
                    this.renderer.placeholderNode = null) : t || this.renderer.placeholderNode ? !t && this.renderer.placeholderNode && (this.renderer.placeholderNode.textContent = this.$placeholder || "") : (this.renderer.on("afterRender", this.$updatePlaceholder),
                    n.addCssClass(this.container, "ace_hasPlaceholder"),
                    (e = n.createElement("div")).className = "ace_placeholder",
                    e.textContent = this.$placeholder || "",
                    this.renderer.placeholderNode = e,
                    this.renderer.content.appendChild(this.renderer.placeholderNode))
                }
                .bind(this),
                this.on("input", this.$updatePlaceholder)),
                this.$updatePlaceholder()
            }
        },
        hScrollBarAlwaysVisible: "renderer",
        vScrollBarAlwaysVisible: "renderer",
        highlightGutterLine: "renderer",
        animatedScroll: "renderer",
        showInvisibles: "renderer",
        showPrintMargin: "renderer",
        printMarginColumn: "renderer",
        printMargin: "renderer",
        fadeFoldWidgets: "renderer",
        showFoldWidgets: "renderer",
        displayIndentGuides: "renderer",
        showGutter: "renderer",
        fontSize: "renderer",
        fontFamily: "renderer",
        maxLines: "renderer",
        minLines: "renderer",
        scrollPastEnd: "renderer",
        fixedWidthGutter: "renderer",
        theme: "renderer",
        hasCssTransforms: "renderer",
        maxPixelHeight: "renderer",
        useTextareaForIME: "renderer",
        scrollSpeed: "$mouseHandler",
        dragDelay: "$mouseHandler",
        dragEnabled: "$mouseHandler",
        focusTimeout: "$mouseHandler",
        tooltipFollowsMouse: "$mouseHandler",
        firstLineNumber: "session",
        overwrite: "session",
        newLineMode: "session",
        useWorker: "session",
        useSoftTabs: "session",
        navigateWithinSoftTabs: "session",
        tabSize: "session",
        wrap: "session",
        indentedSoftWrap: "session",
        foldStyle: "session",
        mode: "session"
    });
    var y = {
        getText: function(e, t) {
            return (Math.abs(e.selection.lead.row - t) || t + 1 + (t < 9 ? "·" : "")) + ""
        },
        getWidth: function(e, t, i) {
            return Math.max(t.toString().length, (i.lastRow + 1).toString().length, 2) * i.characterWidth
        },
        update: function(e, t) {
            t.renderer.$loop.schedule(t.renderer.CHANGE_GUTTER)
        },
        attach: function(e) {
            e.renderer.$gutterLayer.$renderer = this,
            e.on("changeSelection", this.update),
            this.update(null, e)
        },
        detach: function(e) {
            e.renderer.$gutterLayer.$renderer == this && (e.renderer.$gutterLayer.$renderer = null),
            e.off("changeSelection", this.update),
            this.update(null, e)
        }
    };
    t.Editor = b
}),
define("ace/undomanager", ["require", "exports", "module", "ace/range"], function(e, t, i) {
    "use strict";
    function a(e) {
        return {
            row: e.row,
            column: e.column
        }
    }
    function n(e) {
        if (e = e || this,
        Array.isArray(e))
            return e.map(n).join("\n");
        var t = "";
        return e.action ? (t = "insert" == e.action ? "+" : "-",
        t += "[" + e.lines + "]") : e.value && (t = Array.isArray(e.value) ? e.value.map(s).join("\n") : s(e.value)),
        e.start && (t += s(e)),
        (e.id || e.rev) && (t += "\t(" + (e.id || e.rev) + ")"),
        t
    }
    function s(e) {
        return e.start.row + ":" + e.start.column + "=>" + e.end.row + ":" + e.end.column
    }
    function o(e, t) {
        var i = "insert" == e.action
          , n = "insert" == t.action;
        if (i && n)
            if (0 <= m(t.start, e.end))
                h(t, e, -1);
            else {
                if (!(m(t.start, e.start) <= 0))
                    return;
                h(e, t, 1)
            }
        else if (i && !n)
            if (0 <= m(t.start, e.end))
                h(t, e, -1);
            else {
                if (!(m(t.end, e.start) <= 0))
                    return;
                h(e, t, -1)
            }
        else if (!i && n)
            if (0 <= m(t.start, e.start))
                h(t, e, 1);
            else {
                if (!(m(t.start, e.start) <= 0))
                    return;
                h(e, t, 1)
            }
        else if (!i && !n)
            if (0 <= m(t.start, e.start))
                h(t, e, 1);
            else {
                if (!(m(t.end, e.start) <= 0))
                    return;
                h(e, t, -1)
            }
        return 1
    }
    function r(e, t) {
        for (var i = e.length; i--; )
            for (var n = 0; n < t.length; n++)
                if (!o(e[i], t[n])) {
                    for (; i < e.length; ) {
                        for (; n--; )
                            o(t[n], e[i]);
                        n = t.length,
                        i++
                    }
                    return [e, t]
                }
        return e.selectionBefore = t.selectionBefore = e.selectionAfter = t.selectionAfter = null,
        [t, e]
    }
    function l(e, t) {
        var i, n, s = "insert" == e.action, o = "insert" == t.action;
        if (s && o)
            m(e.start, t.start) < 0 ? h(t, e, 1) : h(e, t, 1);
        else if (s && !o)
            0 <= m(e.start, t.end) ? h(e, t, -1) : (m(e.start, t.start) <= 0 || h(e, f.fromPoints(t.start, e.start), -1),
            h(t, e, 1));
        else if (!s && o)
            0 <= m(t.start, e.end) ? h(t, e, -1) : (m(t.start, e.start) <= 0 || h(t, f.fromPoints(e.start, t.start), -1),
            h(e, t, 1));
        else if (!s && !o)
            if (0 <= m(t.start, e.end))
                h(t, e, -1);
            else {
                if (!(m(t.end, e.start) <= 0))
                    return m(e.start, t.start) < 0 && (e = u(i = e, t.start)),
                    0 < m(e.end, t.end) && (n = u(e, t.end)),
                    c(t.end, e.start, e.end, -1),
                    n && !i && (e.lines = n.lines,
                    e.start = n.start,
                    e.end = n.end,
                    n = e),
                    [t, i, n].filter(Boolean);
                h(e, t, -1)
            }
        return [t, e]
    }
    function h(e, t, i) {
        c(e.start, t.start, t.end, i),
        c(e.end, t.start, t.end, i)
    }
    function c(e, t, i, n) {
        e.row == (1 == n ? t : i).row && (e.column += n * (i.column - t.column)),
        e.row += n * (i.row - t.row)
    }
    function u(e, t) {
        var i = e.lines
          , n = e.end;
        e.end = a(t);
        var s = e.end.row - e.start.row
          , o = i.splice(s, i.length)
          , r = s ? t.column : t.column - e.start.column;
        return i.push(o[0].substring(0, r)),
        o[0] = o[0].substr(r),
        {
            start: a(t),
            end: n,
            lines: o,
            action: e.action
        }
    }
    function d(e, t) {
        var i;
        t = {
            start: a((i = t).start),
            end: a(i.end),
            action: i.action,
            lines: i.lines.slice()
        };
        for (var n = e.length; n--; ) {
            for (var s = e[n], o = 0; o < s.length; o++) {
                var r = l(s[o], t);
                t = r[0],
                2 != r.length && (r[2] ? (s.splice(o + 1, 1, r[1], r[2]),
                o++) : r[1] || (s.splice(o, 1),
                o--))
            }
            s.length || e.splice(n, 1)
        }
        return e
    }
    function g() {
        this.$maxRev = 0,
        this.$fromUndo = !1,
        this.reset()
    }
    (function() {
        this.addSession = function(e) {
            this.$session = e
        }
        ,
        this.add = function(e, t, i) {
            this.$fromUndo || e != this.$lastDelta && (this.$keepRedoStack || (this.$redoStack.length = 0),
            !1 !== t && this.lastDeltas || (this.lastDeltas = [],
            this.$undoStack.push(this.lastDeltas),
            e.id = this.$rev = ++this.$maxRev),
            "remove" != e.action && "insert" != e.action || (this.$lastDelta = e),
            this.lastDeltas.push(e))
        }
        ,
        this.addSelection = function(e, t) {
            this.selections.push({
                value: e,
                rev: t || this.$rev
            })
        }
        ,
        this.startNewGroup = function() {
            return this.lastDeltas = null,
            this.$rev
        }
        ,
        this.markIgnored = function(e, t) {
            null == t && (t = this.$rev + 1);
            for (var i = this.$undoStack, n = i.length; n--; ) {
                var s = i[n][0];
                if (s.id <= e)
                    break;
                s.id < t && (s.ignore = !0)
            }
            this.lastDeltas = null
        }
        ,
        this.getSelection = function(e, t) {
            for (var i = this.selections, n = i.length; n--; ) {
                var s = i[n];
                if (s.rev < e)
                    return t && (s = i[n + 1]),
                    s
            }
        }
        ,
        this.getRevision = function() {
            return this.$rev
        }
        ,
        this.getDeltas = function(e, t) {
            null == t && (t = this.$rev + 1);
            for (var i = this.$undoStack, n = null, s = 0, o = i.length; o--; ) {
                var r = i[o][0];
                if (r.id < t && !n && (n = o + 1),
                r.id <= e) {
                    s = o + 1;
                    break
                }
            }
            return i.slice(s, n)
        }
        ,
        this.getChangedRanges = function(e, t) {
            null == t && (t = this.$rev + 1)
        }
        ,
        this.getChangedLines = function(e, t) {
            null == t && (t = this.$rev + 1)
        }
        ,
        this.undo = function(e, t) {
            this.lastDeltas = null;
            var i = this.$undoStack;
            if (function(e, t) {
                for (var i = t; i--; ) {
                    var n = e[i];
                    if (n && !n[0].ignore) {
                        for (; i < t - 1; ) {
                            var s = r(e[i], e[i + 1]);
                            e[i] = s[0],
                            e[i + 1] = s[1],
                            i++
                        }
                        return 1
                    }
                }
            }(i, i.length)) {
                e = e || this.$session,
                this.$redoStackBaseRev !== this.$rev && this.$redoStack.length && (this.$redoStack = []),
                this.$fromUndo = !0;
                var n = i.pop()
                  , s = null;
                return n && (s = e.undoChanges(n, t),
                this.$redoStack.push(n),
                this.$syncRev()),
                this.$fromUndo = !1,
                s
            }
        }
        ,
        this.redo = function(e, t) {
            var i;
            this.lastDeltas = null,
            e = e || this.$session,
            this.$fromUndo = !0,
            this.$redoStackBaseRev != this.$rev && (i = this.getDeltas(this.$redoStackBaseRev, this.$rev + 1),
            function(e, t) {
                for (var i = 0; i < t.length; i++)
                    for (var n = t[i], s = 0; s < n.length; s++)
                        d(e, n[s])
            }(this.$redoStack, i),
            this.$redoStackBaseRev = this.$rev,
            this.$redoStack.forEach(function(e) {
                e[0].id = ++this.$maxRev
            }, this));
            var n = this.$redoStack.pop()
              , s = null;
            return n && (s = e.redoChanges(n, t),
            this.$undoStack.push(n),
            this.$syncRev()),
            this.$fromUndo = !1,
            s
        }
        ,
        this.$syncRev = function() {
            var e = this.$undoStack
              , t = e[e.length - 1]
              , i = t && t[0].id || 0;
            this.$redoStackBaseRev = i,
            this.$rev = i
        }
        ,
        this.reset = function() {
            this.lastDeltas = null,
            this.$lastDelta = null,
            this.$undoStack = [],
            this.$redoStack = [],
            this.$rev = 0,
            this.mark = 0,
            this.$redoStackBaseRev = this.$rev,
            this.selections = []
        }
        ,
        this.canUndo = function() {
            return 0 < this.$undoStack.length
        }
        ,
        this.canRedo = function() {
            return 0 < this.$redoStack.length
        }
        ,
        this.bookmark = function(e) {
            null == e && (e = this.$rev),
            this.mark = e
        }
        ,
        this.isAtBookmark = function() {
            return this.$rev === this.mark
        }
        ,
        this.toJSON = function() {}
        ,
        this.fromJSON = function() {}
        ,
        this.hasUndo = this.canUndo,
        this.hasRedo = this.canRedo,
        this.isClean = this.isAtBookmark,
        this.markClean = this.bookmark,
        this.$prettyPrint = function(e) {
            return e ? n(e) : n(this.$undoStack) + "\n---\n" + n(this.$redoStack)
        }
    }
    ).call(g.prototype);
    var f = e("./range").Range
      , m = f.comparePoints;
    f.comparePoints;
    t.UndoManager = g
}),
define("ace/layer/lines", ["require", "exports", "module", "ace/lib/dom"], function(e, t, i) {
    "use strict";
    function n(e, t) {
        this.element = e,
        this.canvasHeight = t || 5e5,
        this.element.style.height = 2 * this.canvasHeight + "px",
        this.cells = [],
        this.cellCache = [],
        this.$offsetCoefficient = 0
    }
    var r = e("../lib/dom");
    (function() {
        this.moveContainer = function(e) {
            r.translate(this.element, 0, -(e.firstRowScreen * e.lineHeight % this.canvasHeight) - e.offset * this.$offsetCoefficient)
        }
        ,
        this.pageChanged = function(e, t) {
            return Math.floor(e.firstRowScreen * e.lineHeight / this.canvasHeight) !== Math.floor(t.firstRowScreen * t.lineHeight / this.canvasHeight)
        }
        ,
        this.computeLineTop = function(e, t, i) {
            var n = t.firstRowScreen * t.lineHeight
              , s = Math.floor(n / this.canvasHeight);
            return i.documentToScreenRow(e, 0) * t.lineHeight - s * this.canvasHeight
        }
        ,
        this.computeLineHeight = function(e, t, i) {
            return t.lineHeight * i.getRowLineCount(e)
        }
        ,
        this.getLength = function() {
            return this.cells.length
        }
        ,
        this.get = function(e) {
            return this.cells[e]
        }
        ,
        this.shift = function() {
            this.$cacheCell(this.cells.shift())
        }
        ,
        this.pop = function() {
            this.$cacheCell(this.cells.pop())
        }
        ,
        this.push = function(e) {
            if (Array.isArray(e)) {
                this.cells.push.apply(this.cells, e);
                for (var t = r.createFragment(this.element), i = 0; i < e.length; i++)
                    t.appendChild(e[i].element);
                this.element.appendChild(t)
            } else
                this.cells.push(e),
                this.element.appendChild(e.element)
        }
        ,
        this.unshift = function(e) {
            if (Array.isArray(e)) {
                this.cells.unshift.apply(this.cells, e);
                for (var t = r.createFragment(this.element), i = 0; i < e.length; i++)
                    t.appendChild(e[i].element);
                this.element.firstChild ? this.element.insertBefore(t, this.element.firstChild) : this.element.appendChild(t)
            } else
                this.cells.unshift(e),
                this.element.insertAdjacentElement("afterbegin", e.element)
        }
        ,
        this.last = function() {
            return this.cells.length ? this.cells[this.cells.length - 1] : null
        }
        ,
        this.$cacheCell = function(e) {
            e && (e.element.remove(),
            this.cellCache.push(e))
        }
        ,
        this.createCell = function(e, t, i, n) {
            var s, o = this.cellCache.pop();
            return o || (s = r.createElement("div"),
            n && n(s),
            this.element.appendChild(s),
            o = {
                element: s,
                text: "",
                row: e
            }),
            o.row = e,
            o
        }
    }
    ).call(n.prototype),
    t.Lines = n
}),
define("ace/layer/gutter", ["require", "exports", "module", "ace/lib/dom", "ace/lib/oop", "ace/lib/lang", "ace/lib/event_emitter", "ace/layer/lines"], function(e, t, i) {
    "use strict";
    function h(e) {
        var t = document.createTextNode("");
        e.appendChild(t);
        var i = v.createElement("span");
        return e.appendChild(i),
        e
    }
    function n(e) {
        this.element = v.createElement("div"),
        this.element.className = "ace_layer ace_gutter-layer",
        e.appendChild(this.element),
        this.setShowFoldWidgets(this.$showFoldWidgets),
        this.gutterWidth = 0,
        this.$annotations = [],
        this.$updateAnnotations = this.$updateAnnotations.bind(this),
        this.$lines = new r(this.element),
        this.$lines.$offsetCoefficient = 1
    }
    var v = e("../lib/dom")
      , s = e("../lib/oop")
      , a = e("../lib/lang")
      , o = e("../lib/event_emitter").EventEmitter
      , r = e("./lines").Lines;
    (function() {
        s.implement(this, o),
        this.setSession = function(e) {
            this.session && this.session.off("change", this.$updateAnnotations),
            (this.session = e) && e.on("change", this.$updateAnnotations)
        }
        ,
        this.addGutterDecoration = function(e, t) {
            window.console && console.warn && console.warn("deprecated use session.addGutterDecoration"),
            this.session.addGutterDecoration(e, t)
        }
        ,
        this.removeGutterDecoration = function(e, t) {
            window.console && console.warn && console.warn("deprecated use session.removeGutterDecoration"),
            this.session.removeGutterDecoration(e, t)
        }
        ,
        this.setAnnotations = function(e) {
            this.$annotations = [];
            for (var t = 0; t < e.length; t++) {
                var i = e[t]
                  , n = i.row
                  , s = (s = this.$annotations[n]) || (this.$annotations[n] = {
                    text: []
                })
                  , o = (o = i.text) ? a.escapeHTML(o) : i.html || "";
                -1 === s.text.indexOf(o) && s.text.push(o);
                var r = i.type;
                "error" == r ? s.className = " ace_error" : "warning" == r && " ace_error" != s.className ? s.className = " ace_warning" : "info" != r || s.className || (s.className = " ace_info")
            }
        }
        ,
        this.$updateAnnotations = function(e) {
            var t, i, n;
            this.$annotations.length && (t = e.start.row,
            0 != (i = e.end.row - t) && ("remove" == e.action ? this.$annotations.splice(t, 1 + i, null) : ((n = new Array(1 + i)).unshift(t, 1),
            this.$annotations.splice.apply(this.$annotations, n))))
        }
        ,
        this.update = function(e) {
            this.config = e;
            var t = this.session
              , i = e.firstRow
              , n = Math.min(e.lastRow + e.gutterOffset, t.getLength() - 1);
            this.oldLastRow = n,
            this.config = e,
            this.$lines.moveContainer(e),
            this.$updateCursorRow();
            for (var s = t.getNextFoldLine(i), o = s ? s.start.row : 1 / 0, r = null, a = -1, l = i; ; ) {
                if (o < l && (l = s.end.row + 1,
                o = (s = t.getNextFoldLine(l, s)) ? s.start.row : 1 / 0),
                n < l) {
                    for (; this.$lines.getLength() > a + 1; )
                        this.$lines.pop();
                    break
                }
                (r = this.$lines.get(++a)) ? r.row = l : (r = this.$lines.createCell(l, e, this.session, h),
                this.$lines.push(r)),
                this.$renderCell(r, e, s, l),
                l++
            }
            this._signal("afterRender"),
            this.$updateGutterWidth(e)
        }
        ,
        this.$updateGutterWidth = function(e) {
            var t = this.session
              , i = t.gutterRenderer || this.$renderer
              , n = t.$firstLineNumber
              , s = this.$lines.last() ? this.$lines.last().text : "";
            (this.$fixedWidth || t.$useWrapMode) && (s = t.getLength() + n - 1);
            var o = i ? i.getWidth(t, s, e) : s.toString().length * e.characterWidth
              , r = this.$padding || this.$computePadding();
            (o += r.left + r.right) === this.gutterWidth || isNaN(o) || (this.gutterWidth = o,
            this.element.parentNode.style.width = this.element.style.width = Math.ceil(this.gutterWidth) + "px",
            this._signal("changeGutterWidth", o))
        }
        ,
        this.$updateCursorRow = function() {
            var e;
            this.$highlightGutterLine && (e = this.session.selection.getCursor(),
            this.$cursorRow !== e.row && (this.$cursorRow = e.row))
        }
        ,
        this.updateLineHighlight = function() {
            if (this.$highlightGutterLine) {
                var e = this.session.selection.cursor.row;
                if (this.$cursorRow = e,
                !this.$cursorCell || this.$cursorCell.row != e) {
                    this.$cursorCell && (this.$cursorCell.element.className = this.$cursorCell.element.className.replace("ace_gutter-active-line ", ""));
                    var t = this.$lines.cells;
                    this.$cursorCell = null;
                    for (var i = 0; i < t.length; i++) {
                        var n = t[i];
                        if (n.row >= this.$cursorRow) {
                            if (n.row > this.$cursorRow) {
                                var s = this.session.getFoldLine(this.$cursorRow);
                                if (!(0 < i && s && s.start.row == t[i - 1].row))
                                    break;
                                n = t[i - 1]
                            }
                            n.element.className = "ace_gutter-active-line " + n.element.className,
                            this.$cursorCell = n;
                            break
                        }
                    }
                }
            }
        }
        ,
        this.scrollLines = function(e) {
            var t = this.config;
            if (this.config = e,
            this.$updateCursorRow(),
            this.$lines.pageChanged(t, e))
                return this.update(e);
            this.$lines.moveContainer(e);
            var i = Math.min(e.lastRow + e.gutterOffset, this.session.getLength() - 1)
              , n = this.oldLastRow;
            if (this.oldLastRow = i,
            !t || n < e.firstRow)
                return this.update(e);
            if (i < t.firstRow)
                return this.update(e);
            if (t.firstRow < e.firstRow)
                for (var s = this.session.getFoldedRowCount(t.firstRow, e.firstRow - 1); 0 < s; s--)
                    this.$lines.shift();
            if (i < n)
                for (s = this.session.getFoldedRowCount(i + 1, n); 0 < s; s--)
                    this.$lines.pop();
            e.firstRow < t.firstRow && this.$lines.unshift(this.$renderLines(e, e.firstRow, t.firstRow - 1)),
            n < i && this.$lines.push(this.$renderLines(e, n + 1, i)),
            this.updateLineHighlight(),
            this._signal("afterRender"),
            this.$updateGutterWidth(e)
        }
        ,
        this.$renderLines = function(e, t, i) {
            for (var n = [], s = t, o = this.session.getNextFoldLine(s), r = o ? o.start.row : 1 / 0; r < s && (s = o.end.row + 1,
            r = (o = this.session.getNextFoldLine(s, o)) ? o.start.row : 1 / 0),
            !(i < s); ) {
                var a = this.$lines.createCell(s, e, this.session, h);
                this.$renderCell(a, e, o, s),
                n.push(a),
                s++
            }
            return n
        }
        ,
        this.$renderCell = function(e, t, i, n) {
            var s, o, r = e.element, a = this.session, l = r.childNodes[0], h = r.childNodes[1], c = a.$firstLineNumber, u = a.$breakpoints, d = a.$decorations, g = a.gutterRenderer || this.$renderer, f = this.$showFoldWidgets && a.foldWidgets, m = i ? i.start.row : Number.MAX_VALUE, p = "ace_gutter-cell ";
            this.$highlightGutterLine && (n == this.$cursorRow || i && n < this.$cursorRow && m <= n && this.$cursorRow <= i.end.row) && (p += "ace_gutter-active-line ",
            this.$cursorCell != e && (this.$cursorCell && (this.$cursorCell.element.className = this.$cursorCell.element.className.replace("ace_gutter-active-line ", "")),
            this.$cursorCell = e)),
            u[n] && (p += u[n]),
            d[n] && (p += d[n]),
            this.$annotations[n] && (p += this.$annotations[n].className),
            r.className != p && (r.className = p),
            !f || null == (s = f[n]) && (s = f[n] = a.getFoldWidget(n)),
            s ? (p = "ace_fold-widget ace_" + s,
            "start" == s && n == m && n < i.end.row ? p += " ace_closed" : p += " ace_open",
            h.className != p && (h.className = p),
            o = t.lineHeight + "px",
            v.setStyle(h.style, "height", o),
            v.setStyle(h.style, "display", "inline-block")) : h && v.setStyle(h.style, "display", "none");
            var w = (g ? g.getText(a, n) : n + c).toString();
            return w !== l.data && (l.data = w),
            v.setStyle(e.element.style, "height", this.$lines.computeLineHeight(n, t, a) + "px"),
            v.setStyle(e.element.style, "top", this.$lines.computeLineTop(n, t, a) + "px"),
            e.text = w,
            e
        }
        ,
        this.$fixedWidth = !1,
        this.$highlightGutterLine = !0,
        this.$renderer = "",
        this.setHighlightGutterLine = function(e) {
            this.$highlightGutterLine = e
        }
        ,
        this.$showLineNumbers = !0,
        this.$renderer = "",
        this.setShowLineNumbers = function(e) {
            this.$renderer = !e && {
                getWidth: function() {
                    return 0
                },
                getText: function() {
                    return ""
                }
            }
        }
        ,
        this.getShowLineNumbers = function() {
            return this.$showLineNumbers
        }
        ,
        this.$showFoldWidgets = !0,
        this.setShowFoldWidgets = function(e) {
            e ? v.addCssClass(this.element, "ace_folding-enabled") : v.removeCssClass(this.element, "ace_folding-enabled"),
            this.$showFoldWidgets = e,
            this.$padding = null
        }
        ,
        this.getShowFoldWidgets = function() {
            return this.$showFoldWidgets
        }
        ,
        this.$computePadding = function() {
            if (!this.element.firstChild)
                return {
                    left: 0,
                    right: 0
                };
            var e = v.computedStyle(this.element.firstChild);
            return this.$padding = {},
            this.$padding.left = (parseInt(e.borderLeftWidth) || 0) + (parseInt(e.paddingLeft) || 0) + 1,
            this.$padding.right = (parseInt(e.borderRightWidth) || 0) + (parseInt(e.paddingRight) || 0),
            this.$padding
        }
        ,
        this.getRegion = function(e) {
            var t = this.$padding || this.$computePadding()
              , i = this.element.getBoundingClientRect();
            return e.x < t.left + i.left ? "markers" : this.$showFoldWidgets && e.x > i.right - t.right ? "foldWidgets" : void 0
        }
    }
    ).call(n.prototype),
    t.Gutter = n
}),
define("ace/layer/marker", ["require", "exports", "module", "ace/range", "ace/lib/dom"], function(e, t, i) {
    "use strict";
    function n(e) {
        this.element = s.createElement("div"),
        this.element.className = "ace_layer ace_marker-layer",
        e.appendChild(this.element)
    }
    var g = e("../range").Range
      , s = e("../lib/dom");
    (function() {
        this.$padding = 0,
        this.setPadding = function(e) {
            this.$padding = e
        }
        ,
        this.setSession = function(e) {
            this.session = e
        }
        ,
        this.setMarkers = function(e) {
            this.markers = e
        }
        ,
        this.elt = function(e, t) {
            var i = -1 != this.i && this.element.childNodes[this.i];
            i ? this.i++ : (i = document.createElement("div"),
            this.element.appendChild(i),
            this.i = -1),
            i.style.cssText = t,
            i.className = e
        }
        ,
        this.update = function(e) {
            if (e) {
                var t;
                for (var i in this.config = e,
                this.i = 0,
                this.markers) {
                    var n, s, o, r = this.markers[i];
                    r.range ? (o = r.range.clipRows(e.firstRow, e.lastRow)).isEmpty() || (o = o.toScreenRange(this.session),
                    r.renderer ? (n = this.$getTop(o.start.row, e),
                    s = this.$padding + o.start.column * e.characterWidth,
                    r.renderer(t, o, s, n, e)) : "fullLine" == r.type ? this.drawFullLineMarker(t, o, r.clazz, e) : "screenLine" == r.type ? this.drawScreenLineMarker(t, o, r.clazz, e) : o.isMultiLine() ? "text" == r.type ? this.drawTextMarker(t, o, r.clazz, e) : this.drawMultiLineMarker(t, o, r.clazz, e) : this.drawSingleLineMarker(t, o, r.clazz + " ace_start ace_br15", e)) : r.update(t, this, this.session, e)
                }
                if (-1 != this.i)
                    for (; this.i < this.element.childElementCount; )
                        this.element.removeChild(this.element.lastChild)
            }
        }
        ,
        this.$getTop = function(e, t) {
            return (e - t.firstRowScreen) * t.lineHeight
        }
        ,
        this.drawTextMarker = function(e, t, i, n, s) {
            for (var o = this.session, r = t.start.row, a = t.end.row, l = r, h = 0, c = 0, u = o.getScreenLastRowColumn(l), d = new g(l,t.start.column,l,c); l <= a; l++)
                d.start.row = d.end.row = l,
                d.start.column = l == r ? t.start.column : o.getRowWrapIndent(l),
                h = c,
                c = d.end.column = u,
                u = l + 1 < a ? o.getScreenLastRowColumn(l + 1) : l == a ? 0 : t.end.column,
                this.drawSingleLineMarker(e, d, i + (l == r ? " ace_start" : "") + " ace_br" + ((l == r || l == r + 1 && t.start.column ? 1 : 0) | (h < c ? 2 : 0) | (u < c ? 4 : 0) | (l == a ? 8 : 0)), n, l == a ? 0 : 1, s)
        }
        ,
        this.drawMultiLineMarker = function(e, t, i, n, s) {
            var o, r, a, l = this.$padding, h = n.lineHeight, c = this.$getTop(t.start.row, n), u = l + t.start.column * n.characterWidth;
            s = s || "",
            this.session.$bidiHandler.isBidiRow(t.start.row) ? ((o = t.clone()).end.row = o.start.row,
            o.end.column = this.session.getLine(o.start.row).length,
            this.drawBidiSingleLineMarker(e, o, i + " ace_br1 ace_start", n, null, s)) : this.elt(i + " ace_br1 ace_start", "height:" + h + "px;right:0;top:" + c + "px;left:" + u + "px;" + (s || "")),
            this.session.$bidiHandler.isBidiRow(t.end.row) ? ((o = t.clone()).start.row = o.end.row,
            o.start.column = 0,
            this.drawBidiSingleLineMarker(e, o, i + " ace_br12", n, null, s)) : (c = this.$getTop(t.end.row, n),
            r = t.end.column * n.characterWidth,
            this.elt(i + " ace_br12", "height:" + h + "px;width:" + r + "px;top:" + c + "px;left:" + l + "px;" + (s || ""))),
            (h = (t.end.row - t.start.row - 1) * n.lineHeight) <= 0 || (c = this.$getTop(t.start.row + 1, n),
            a = (t.start.column ? 1 : 0) | (t.end.column ? 0 : 8),
            this.elt(i + (a ? " ace_br" + a : ""), "height:" + h + "px;right:0;top:" + c + "px;left:" + l + "px;" + (s || "")))
        }
        ,
        this.drawSingleLineMarker = function(e, t, i, n, s, o) {
            if (this.session.$bidiHandler.isBidiRow(t.start.row))
                return this.drawBidiSingleLineMarker(e, t, i, n, s, o);
            var r = n.lineHeight
              , a = (t.end.column + (s || 0) - t.start.column) * n.characterWidth
              , l = this.$getTop(t.start.row, n)
              , h = this.$padding + t.start.column * n.characterWidth;
            this.elt(i, "height:" + r + "px;width:" + a + "px;top:" + l + "px;left:" + h + "px;" + (o || ""))
        }
        ,
        this.drawBidiSingleLineMarker = function(e, t, i, n, s, o) {
            var r = n.lineHeight
              , a = this.$getTop(t.start.row, n)
              , l = this.$padding;
            this.session.$bidiHandler.getSelections(t.start.column, t.end.column).forEach(function(e) {
                this.elt(i, "height:" + r + "px;width:" + e.width + (s || 0) + "px;top:" + a + "px;left:" + (l + e.left) + "px;" + (o || ""))
            }, this)
        }
        ,
        this.drawFullLineMarker = function(e, t, i, n, s) {
            var o = this.$getTop(t.start.row, n)
              , r = n.lineHeight;
            t.start.row != t.end.row && (r += this.$getTop(t.end.row, n) - o),
            this.elt(i, "height:" + r + "px;top:" + o + "px;left:0;right:0;" + (s || ""))
        }
        ,
        this.drawScreenLineMarker = function(e, t, i, n, s) {
            var o = this.$getTop(t.start.row, n)
              , r = n.lineHeight;
            this.elt(i, "height:" + r + "px;top:" + o + "px;left:0;right:0;" + (s || ""))
        }
    }
    ).call(n.prototype),
    t.Marker = n
}),
define("ace/layer/text", ["require", "exports", "module", "ace/lib/oop", "ace/lib/dom", "ace/lib/lang", "ace/layer/lines", "ace/lib/event_emitter"], function(e, t, i) {
    "use strict";
    function n(e) {
        this.dom = h,
        this.element = this.dom.createElement("div"),
        this.element.className = "ace_layer ace_text-layer",
        e.appendChild(this.element),
        this.$updateEolChar = this.$updateEolChar.bind(this),
        this.$lines = new o(this.element)
    }
    var s = e("../lib/oop")
      , h = e("../lib/dom")
      , v = e("../lib/lang")
      , o = e("./lines").Lines
      , r = e("../lib/event_emitter").EventEmitter;
    (function() {
        s.implement(this, r),
        this.EOF_CHAR = "¶",
        this.EOL_CHAR_LF = "¬",
        this.EOL_CHAR_CRLF = "¤",
        this.EOL_CHAR = this.EOL_CHAR_LF,
        this.TAB_CHAR = "—",
        this.SPACE_CHAR = "·",
        this.$padding = 0,
        this.MAX_LINE_LENGTH = 1e4,
        this.$updateEolChar = function() {
            var e = this.session.doc
              , t = "\n" == e.getNewLineCharacter() && "windows" != e.getNewLineMode() ? this.EOL_CHAR_LF : this.EOL_CHAR_CRLF;
            if (this.EOL_CHAR != t)
                return this.EOL_CHAR = t,
                !0
        }
        ,
        this.setPadding = function(e) {
            this.$padding = e,
            this.element.style.margin = "0 " + e + "px"
        }
        ,
        this.getLineHeight = function() {
            return this.$fontMetrics.$characterSize.height || 0
        }
        ,
        this.getCharacterWidth = function() {
            return this.$fontMetrics.$characterSize.width || 0
        }
        ,
        this.$setFontMetrics = function(e) {
            this.$fontMetrics = e,
            this.$fontMetrics.on("changeCharacterSize", function(e) {
                this._signal("changeCharacterSize", e)
            }
            .bind(this)),
            this.$pollSizeChanges()
        }
        ,
        this.checkForSizeChanges = function() {
            this.$fontMetrics.checkForSizeChanges()
        }
        ,
        this.$pollSizeChanges = function() {
            return this.$pollSizeChangesTimer = this.$fontMetrics.$pollSizeChanges()
        }
        ,
        this.setSession = function(e) {
            (this.session = e) && this.$computeTabString()
        }
        ,
        this.showInvisibles = !1,
        this.showSpaces = !1,
        this.showTabs = !1,
        this.showEOL = !1,
        this.setShowInvisibles = function(e) {
            return this.showInvisibles != e && ("string" == typeof (this.showInvisibles = e) ? (this.showSpaces = /tab/i.test(e),
            this.showTabs = /space/i.test(e),
            this.showEOL = /eol/i.test(e)) : this.showSpaces = this.showTabs = this.showEOL = e,
            this.$computeTabString(),
            !0)
        }
        ,
        this.displayIndentGuides = !0,
        this.setDisplayIndentGuides = function(e) {
            return this.displayIndentGuides != e && (this.displayIndentGuides = e,
            this.$computeTabString(),
            !0)
        }
        ,
        this.$tabStrings = [],
        this.onChangeTabSize = this.$computeTabString = function() {
            var e = this.session.getTabSize();
            this.tabSize = e;
            for (var t, i, n, s, o, r, a = this.$tabStrings = [0], l = 1; l < e + 1; l++) {
                this.showTabs ? ((r = this.dom.createElement("span")).className = "ace_invisible ace_invisible_tab",
                r.textContent = v.stringRepeat(this.TAB_CHAR, l),
                a.push(r)) : a.push(this.dom.createTextNode(v.stringRepeat(" ", l), this.element))
            }
            this.displayIndentGuides && (this.$indentGuideRe = /\s\S| \t|\t |\s$/,
            t = "ace_indent-guide",
            i = this.showSpaces ? " ace_invisible ace_invisible_space" : "",
            n = this.showSpaces ? v.stringRepeat(this.SPACE_CHAR, this.tabSize) : v.stringRepeat(" ", this.tabSize),
            s = this.showTabs ? " ace_invisible ace_invisible_tab" : "",
            o = this.showTabs ? v.stringRepeat(this.TAB_CHAR, this.tabSize) : n,
            (r = this.dom.createElement("span")).className = t + i,
            r.textContent = n,
            this.$tabStrings[" "] = r,
            (r = this.dom.createElement("span")).className = t + s,
            r.textContent = o,
            this.$tabStrings["\t"] = r)
        }
        ,
        this.updateLines = function(e, t, i) {
            if (this.config.lastRow != e.lastRow || this.config.firstRow != e.firstRow)
                return this.update(e);
            this.config = e;
            for (var n = Math.max(t, e.firstRow), s = Math.min(i, e.lastRow), o = this.element.childNodes, r = 0, a = e.firstRow; a < n; a++) {
                if (l = this.session.getFoldLine(a)) {
                    if (l.containsRow(n)) {
                        n = l.start.row;
                        break
                    }
                    a = l.end.row
                }
                r++
            }
            for (var l, h = !1, a = n, c = (l = this.session.getNextFoldLine(a)) ? l.start.row : 1 / 0; c < a && (a = l.end.row + 1,
            c = (l = this.session.getNextFoldLine(a, l)) ? l.start.row : 1 / 0),
            !(s < a); ) {
                var u, d = o[r++];
                d && (this.dom.removeChildren(d),
                this.$renderLine(d, a, a == c && l),
                h && (d.style.top = this.$lines.computeLineTop(a, e, this.session) + "px"),
                u = e.lineHeight * this.session.getRowLength(a) + "px",
                d.style.height != u && (h = !0,
                d.style.height = u)),
                a++
            }
            if (h)
                for (; r < this.$lines.cells.length; ) {
                    var g = this.$lines.cells[r++];
                    g.element.style.top = this.$lines.computeLineTop(g.row, e, this.session) + "px"
                }
        }
        ,
        this.scrollLines = function(e) {
            var t = this.config;
            if (this.config = e,
            this.$lines.pageChanged(t, e))
                return this.update(e);
            this.$lines.moveContainer(e);
            var i = e.lastRow
              , n = t ? t.lastRow : -1;
            if (!t || n < e.firstRow)
                return this.update(e);
            if (i < t.firstRow)
                return this.update(e);
            if (!t || t.lastRow < e.firstRow)
                return this.update(e);
            if (e.lastRow < t.firstRow)
                return this.update(e);
            if (t.firstRow < e.firstRow)
                for (var s = this.session.getFoldedRowCount(t.firstRow, e.firstRow - 1); 0 < s; s--)
                    this.$lines.shift();
            if (t.lastRow > e.lastRow)
                for (s = this.session.getFoldedRowCount(e.lastRow + 1, t.lastRow); 0 < s; s--)
                    this.$lines.pop();
            e.firstRow < t.firstRow && this.$lines.unshift(this.$renderLinesFragment(e, e.firstRow, t.firstRow - 1)),
            e.lastRow > t.lastRow && this.$lines.push(this.$renderLinesFragment(e, t.lastRow + 1, e.lastRow))
        }
        ,
        this.$renderLinesFragment = function(e, t, i) {
            for (var n = [], s = t, o = this.session.getNextFoldLine(s), r = o ? o.start.row : 1 / 0; r < s && (s = o.end.row + 1,
            r = (o = this.session.getNextFoldLine(s, o)) ? o.start.row : 1 / 0),
            !(i < s); ) {
                var a = this.$lines.createCell(s, e, this.session)
                  , l = a.element;
                this.dom.removeChildren(l),
                h.setStyle(l.style, "height", this.$lines.computeLineHeight(s, e, this.session) + "px"),
                h.setStyle(l.style, "top", this.$lines.computeLineTop(s, e, this.session) + "px"),
                this.$renderLine(l, s, s == r && o),
                this.$useLineGroups() ? l.className = "ace_line_group" : l.className = "ace_line",
                n.push(a),
                s++
            }
            return n
        }
        ,
        this.update = function(e) {
            this.$lines.moveContainer(e);
            for (var t = (this.config = e).firstRow, i = e.lastRow, n = this.$lines; n.getLength(); )
                n.pop();
            n.push(this.$renderLinesFragment(e, t, i))
        }
        ,
        this.$textToken = {
            text: !0,
            rparen: !0,
            lparen: !0
        },
        this.$renderToken = function(e, t, i, n) {
            for (var s, o, r = this, a = /(\t)|( +)|([\x00-\x1f\x80-\xa0\xad\u1680\u180E\u2000-\u200f\u2028\u2029\u202F\u205F\uFEFF\uFFF9-\uFFFC]+)|(\u3000)|([\u1100-\u115F\u11A3-\u11A7\u11FA-\u11FF\u2329-\u232A\u2E80-\u2E99\u2E9B-\u2EF3\u2F00-\u2FD5\u2FF0-\u2FFB\u3001-\u303E\u3041-\u3096\u3099-\u30FF\u3105-\u312D\u3131-\u318E\u3190-\u31BA\u31C0-\u31E3\u31F0-\u321E\u3220-\u3247\u3250-\u32FE\u3300-\u4DBF\u4E00-\uA48C\uA490-\uA4C6\uA960-\uA97C\uAC00-\uD7A3\uD7B0-\uD7C6\uD7CB-\uD7FB\uF900-\uFAFF\uFE10-\uFE19\uFE30-\uFE52\uFE54-\uFE66\uFE68-\uFE6B\uFF01-\uFF60\uFFE0-\uFFE6]|[\uD800-\uDBFF][\uDC00-\uDFFF])/g, l = this.dom.createFragment(this.element), h = 0; s = a.exec(n); ) {
                var c, u, d, g = s[1], f = s[2], m = s[3], p = s[4], w = s[5];
                !r.showSpaces && f || (c = h != s.index ? n.slice(h, s.index) : "",
                h = s.index + s[0].length,
                c && l.appendChild(this.dom.createTextNode(c, this.element)),
                g ? (u = r.session.getScreenTabSize(t + s.index),
                l.appendChild(r.$tabStrings[u].cloneNode(!0)),
                t += u - 1) : f ? r.showSpaces ? ((d = this.dom.createElement("span")).className = "ace_invisible ace_invisible_space",
                d.textContent = v.stringRepeat(r.SPACE_CHAR, f.length),
                l.appendChild(d)) : l.appendChild(this.com.createTextNode(f, this.element)) : m ? ((d = this.dom.createElement("span")).className = "ace_invisible ace_invisible_space ace_invalid",
                d.textContent = v.stringRepeat(r.SPACE_CHAR, m.length),
                l.appendChild(d)) : p ? (t += 1,
                (d = this.dom.createElement("span")).style.width = 2 * r.config.characterWidth + "px",
                d.className = r.showSpaces ? "ace_cjk ace_invisible ace_invisible_space" : "ace_cjk",
                d.textContent = r.showSpaces ? r.SPACE_CHAR : p,
                l.appendChild(d)) : w && (t += 1,
                (d = this.dom.createElement("span")).style.width = 2 * r.config.characterWidth + "px",
                d.className = "ace_cjk",
                d.textContent = w,
                l.appendChild(d)))
            }
            return l.appendChild(this.dom.createTextNode(h ? n.slice(h) : n, this.element)),
            this.$textToken[i.type] ? e.appendChild(l) : (o = "ace_" + i.type.replace(/\./g, " ace_"),
            d = this.dom.createElement("span"),
            "fold" == i.type && (d.style.width = i.value.length * this.config.characterWidth + "px"),
            d.className = o,
            d.appendChild(l),
            e.appendChild(d)),
            t + n.length
        }
        ,
        this.renderIndentGuide = function(e, t, i) {
            var n = t.search(this.$indentGuideRe);
            if (n <= 0 || i <= n)
                return t;
            if (" " == t[0]) {
                for (var s = (n -= n % this.tabSize) / this.tabSize, o = 0; o < s; o++)
                    e.appendChild(this.$tabStrings[" "].cloneNode(!0));
                return t.substr(n)
            }
            if ("\t" != t[0])
                return t;
            for (o = 0; o < n; o++)
                e.appendChild(this.$tabStrings["\t"].cloneNode(!0));
            return t.substr(n)
        }
        ,
        this.$createLineElement = function(e) {
            var t = this.dom.createElement("div");
            return t.className = "ace_line",
            t.style.height = this.config.lineHeight + "px",
            t
        }
        ,
        this.$renderWrappedLine = function(e, t, i) {
            var n = 0
              , s = 0
              , o = i[0]
              , r = 0
              , a = this.$createLineElement();
            e.appendChild(a);
            for (var l = 0; l < t.length; l++) {
                var h = t[l]
                  , c = h.value;
                if (0 == l && this.displayIndentGuides) {
                    if (n = c.length,
                    !(c = this.renderIndentGuide(a, c, o)))
                        continue;
                    n -= c.length
                }
                if (n + c.length < o)
                    r = this.$renderToken(a, r, h, c),
                    n += c.length;
                else {
                    for (; n + c.length >= o; )
                        r = this.$renderToken(a, r, h, c.substring(0, o - n)),
                        c = c.substring(o - n),
                        n = o,
                        a = this.$createLineElement(),
                        e.appendChild(a),
                        a.appendChild(this.dom.createTextNode(v.stringRepeat(" ", i.indent), this.element)),
                        r = 0,
                        o = i[++s] || Number.MAX_VALUE;
                    0 != c.length && (n += c.length,
                    r = this.$renderToken(a, r, h, c))
                }
            }
            i[i.length - 1] > this.MAX_LINE_LENGTH && this.$renderOverflowMessage(a, r, null, "", !0)
        }
        ,
        this.$renderSimpleLine = function(e, t) {
            var i = 0
              , n = t[0]
              , s = n.value;
            this.displayIndentGuides && (s = this.renderIndentGuide(e, s)),
            s && (i = this.$renderToken(e, i, n, s));
            for (var o = 1; o < t.length; o++) {
                if (i + (s = (n = t[o]).value).length > this.MAX_LINE_LENGTH)
                    return this.$renderOverflowMessage(e, i, n, s);
                i = this.$renderToken(e, i, n, s)
            }
        }
        ,
        this.$renderOverflowMessage = function(e, t, i, n, s) {
            i && this.$renderToken(e, t, i, n.slice(0, this.MAX_LINE_LENGTH - t));
            var o = this.dom.createElement("span");
            o.className = "ace_inline_button ace_keyword ace_toggle_wrap",
            o.textContent = s ? "<hide>" : "<click to see more...>",
            e.appendChild(o)
        }
        ,
        this.$renderLine = function(e, t, i) {
            var n;
            i || 0 == i || (i = this.session.getFoldLine(t));
            var s, o, r = e;
            (n = i ? this.$getFoldLineTokens(t, i) : this.session.getTokens(t)).length ? (s = this.session.getRowSplitData(t)) && s.length ? (this.$renderWrappedLine(e, n, s),
            r = e.lastChild) : (r = e,
            this.$useLineGroups() && (r = this.$createLineElement(),
            e.appendChild(r)),
            this.$renderSimpleLine(r, n)) : this.$useLineGroups() && (r = this.$createLineElement(),
            e.appendChild(r)),
            this.showEOL && r && (i && (t = i.end.row),
            (o = this.dom.createElement("span")).className = "ace_invisible ace_invisible_eol",
            o.textContent = t == this.session.getLength() - 1 ? this.EOF_CHAR : this.EOL_CHAR,
            r.appendChild(o))
        }
        ,
        this.$getFoldLineTokens = function(e, t) {
            var o = this.session
              , r = []
              , a = o.getTokens(e);
            return t.walk(function(e, t, i, n, s) {
                null != e ? r.push({
                    type: "fold",
                    value: e
                }) : (s && (a = o.getTokens(t)),
                a.length && function(e, t, i) {
                    for (var n, s = 0, o = 0; o + e[s].value.length < t; )
                        if (o += e[s].value.length,
                        ++s == e.length)
                            return;
                    for (o != t && ((n = e[s].value.substring(t - o)).length > i - t && (n = n.substring(0, i - t)),
                    r.push({
                        type: e[s].type,
                        value: n
                    }),
                    o = t + n.length,
                    s += 1); o < i && s < e.length; ) {
                        (n = e[s].value).length + o > i ? r.push({
                            type: e[s].type,
                            value: n.substring(0, i - o)
                        }) : r.push(e[s]),
                        o += n.length,
                        s += 1
                    }
                }(a, n, i))
            }, t.end.row, this.session.getLine(t.end.row).length),
            r
        }
        ,
        this.$useLineGroups = function() {
            return this.session.getUseWrapMode()
        }
        ,
        this.destroy = function() {}
    }
    ).call(n.prototype),
    t.Text = n
}),
define("ace/layer/cursor", ["require", "exports", "module", "ace/lib/dom"], function(e, t, i) {
    "use strict";
    function n(e) {
        this.element = h.createElement("div"),
        this.element.className = "ace_layer ace_cursor-layer",
        e.appendChild(this.element),
        this.isVisible = !1,
        this.isBlinking = !0,
        this.blinkInterval = 1e3,
        this.smoothBlinking = !1,
        this.cursors = [],
        this.cursor = this.addCursor(),
        h.addCssClass(this.element, "ace_hidden-cursors"),
        this.$updateCursors = this.$updateOpacity.bind(this)
    }
    var h = e("../lib/dom");
    (function() {
        this.$updateOpacity = function(e) {
            for (var t = this.cursors, i = t.length; i--; )
                h.setStyle(t[i].style, "opacity", e ? "" : "0")
        }
        ,
        this.$startCssAnimation = function() {
            for (var e = this.cursors, t = e.length; t--; )
                e[t].style.animationDuration = this.blinkInterval + "ms";
            setTimeout(function() {
                h.addCssClass(this.element, "ace_animate-blinking")
            }
            .bind(this))
        }
        ,
        this.$stopCssAnimation = function() {
            h.removeCssClass(this.element, "ace_animate-blinking")
        }
        ,
        this.$padding = 0,
        this.setPadding = function(e) {
            this.$padding = e
        }
        ,
        this.setSession = function(e) {
            this.session = e
        }
        ,
        this.setBlinking = function(e) {
            e != this.isBlinking && (this.isBlinking = e,
            this.restartTimer())
        }
        ,
        this.setBlinkInterval = function(e) {
            e != this.blinkInterval && (this.blinkInterval = e,
            this.restartTimer())
        }
        ,
        this.setSmoothBlinking = function(e) {
            e != this.smoothBlinking && (this.smoothBlinking = e,
            h.setCssClass(this.element, "ace_smooth-blinking", e),
            this.$updateCursors(!0),
            this.restartTimer())
        }
        ,
        this.addCursor = function() {
            var e = h.createElement("div");
            return e.className = "ace_cursor",
            this.element.appendChild(e),
            this.cursors.push(e),
            e
        }
        ,
        this.removeCursor = function() {
            if (1 < this.cursors.length) {
                var e = this.cursors.pop();
                return e.parentNode.removeChild(e),
                e
            }
        }
        ,
        this.hideCursor = function() {
            this.isVisible = !1,
            h.addCssClass(this.element, "ace_hidden-cursors"),
            this.restartTimer()
        }
        ,
        this.showCursor = function() {
            this.isVisible = !0,
            h.removeCssClass(this.element, "ace_hidden-cursors"),
            this.restartTimer()
        }
        ,
        this.restartTimer = function() {
            var e, t = this.$updateCursors;
            clearInterval(this.intervalId),
            clearTimeout(this.timeoutId),
            this.$stopCssAnimation(),
            this.smoothBlinking && h.removeCssClass(this.element, "ace_smooth-blinking"),
            t(!0),
            this.isBlinking && this.blinkInterval && this.isVisible ? (this.smoothBlinking && setTimeout(function() {
                h.addCssClass(this.element, "ace_smooth-blinking")
            }
            .bind(this)),
            h.HAS_CSS_ANIMATION ? this.$startCssAnimation() : (e = function() {
                this.timeoutId = setTimeout(function() {
                    t(!1)
                }, .6 * this.blinkInterval)
            }
            .bind(this),
            this.intervalId = setInterval(function() {
                t(!0),
                e()
            }, this.blinkInterval),
            e())) : this.$stopCssAnimation()
        }
        ,
        this.getPixelPosition = function(e, t) {
            if (!this.config || !this.session)
                return {
                    left: 0,
                    top: 0
                };
            e = e || this.session.selection.getCursor();
            var i = this.session.documentToScreenPosition(e);
            return {
                left: this.$padding + (this.session.$bidiHandler.isBidiRow(i.row, e.row) ? this.session.$bidiHandler.getPosLeft(i.column) : i.column * this.config.characterWidth),
                top: (i.row - (t ? this.config.firstRowScreen : 0)) * this.config.lineHeight
            }
        }
        ,
        this.isCursorInView = function(e, t) {
            return 0 <= e.top && e.top < t.maxHeight
        }
        ,
        this.update = function(e) {
            this.config = e;
            var t = this.session.$selectionMarkers
              , i = 0
              , n = 0;
            void 0 !== t && 0 !== t.length || (t = [{
                cursor: null
            }]);
            for (var i = 0, s = t.length; i < s; i++) {
                var o, r, a = this.getPixelPosition(t[i].cursor, !0);
                (a.top > e.height + e.offset || a.top < 0) && 1 < i || (r = (o = this.cursors[n++] || this.addCursor()).style,
                this.drawCursor ? this.drawCursor(o, a, e, t[i], this.session) : this.isCursorInView(a, e) ? (h.setStyle(r, "display", "block"),
                h.translate(o, a.left, a.top),
                h.setStyle(r, "width", Math.round(e.characterWidth) + "px"),
                h.setStyle(r, "height", e.lineHeight + "px")) : h.setStyle(r, "display", "none"))
            }
            for (; this.cursors.length > n; )
                this.removeCursor();
            var l = this.session.getOverwrite();
            this.$setOverwrite(l),
            this.$pixelPos = a,
            this.restartTimer()
        }
        ,
        this.drawCursor = null,
        this.$setOverwrite = function(e) {
            e != this.overwrite && ((this.overwrite = e) ? h.addCssClass(this.element, "ace_overwrite-cursors") : h.removeCssClass(this.element, "ace_overwrite-cursors"))
        }
        ,
        this.destroy = function() {
            clearInterval(this.intervalId),
            clearTimeout(this.timeoutId)
        }
    }
    ).call(n.prototype),
    t.Cursor = n
}),
define("ace/scrollbar", ["require", "exports", "module", "ace/lib/oop", "ace/lib/dom", "ace/lib/event", "ace/lib/event_emitter"], function(e, t, i) {
    "use strict";
    function n(e) {
        this.element = o.createElement("div"),
        this.element.className = "ace_scrollbar ace_scrollbar" + this.classSuffix,
        this.inner = o.createElement("div"),
        this.inner.className = "ace_scrollbar-inner",
        this.inner.textContent = " ",
        this.element.appendChild(this.inner),
        e.appendChild(this.element),
        this.setVisible(!1),
        this.skipEvent = !1,
        r.addListener(this.element, "scroll", this.onScroll.bind(this)),
        r.addListener(this.element, "mousedown", r.preventDefault)
    }
    var s = e("./lib/oop")
      , o = e("./lib/dom")
      , r = e("./lib/event")
      , a = e("./lib/event_emitter").EventEmitter;
    (function() {
        s.implement(this, a),
        this.setVisible = function(e) {
            this.element.style.display = e ? "" : "none",
            this.isVisible = e,
            this.coeff = 1
        }
    }
    ).call(n.prototype);
    function l(e, t) {
        n.call(this, e),
        this.scrollTop = 0,
        this.scrollHeight = 0,
        t.$scrollbarWidth = this.width = o.scrollbarWidth(e.ownerDocument),
        this.inner.style.width = this.element.style.width = (this.width || 15) + 5 + "px",
        this.$minWidth = 0
    }
    s.inherits(l, n),
    function() {
        this.classSuffix = "-v",
        this.onScroll = function() {
            var e;
            this.skipEvent || (this.scrollTop = this.element.scrollTop,
            1 != this.coeff && (e = this.element.clientHeight / this.scrollHeight,
            this.scrollTop = this.scrollTop * (1 - e) / (this.coeff - e)),
            this._emit("scroll", {
                data: this.scrollTop
            })),
            this.skipEvent = !1
        }
        ,
        this.getWidth = function() {
            return Math.max(this.isVisible ? this.width : 0, this.$minWidth || 0)
        }
        ,
        this.setHeight = function(e) {
            this.element.style.height = e + "px"
        }
        ,
        this.setInnerHeight = this.setScrollHeight = function(e) {
            32768 < (this.scrollHeight = e) ? (this.coeff = 32768 / e,
            e = 32768) : 1 != this.coeff && (this.coeff = 1),
            this.inner.style.height = e + "px"
        }
        ,
        this.setScrollTop = function(e) {
            this.scrollTop != e && (this.skipEvent = !0,
            this.scrollTop = e,
            this.element.scrollTop = e * this.coeff)
        }
    }
    .call(l.prototype);
    function h(e, t) {
        n.call(this, e),
        this.scrollLeft = 0,
        this.height = t.$scrollbarWidth,
        this.inner.style.height = this.element.style.height = (this.height || 15) + 5 + "px"
    }
    s.inherits(h, n),
    function() {
        this.classSuffix = "-h",
        this.onScroll = function() {
            this.skipEvent || (this.scrollLeft = this.element.scrollLeft,
            this._emit("scroll", {
                data: this.scrollLeft
            })),
            this.skipEvent = !1
        }
        ,
        this.getHeight = function() {
            return this.isVisible ? this.height : 0
        }
        ,
        this.setWidth = function(e) {
            this.element.style.width = e + "px"
        }
        ,
        this.setInnerWidth = function(e) {
            this.inner.style.width = e + "px"
        }
        ,
        this.setScrollWidth = function(e) {
            this.inner.style.width = e + "px"
        }
        ,
        this.setScrollLeft = function(e) {
            this.scrollLeft != e && (this.skipEvent = !0,
            this.scrollLeft = this.element.scrollLeft = e)
        }
    }
    .call(h.prototype),
    t.ScrollBar = l,
    t.ScrollBarV = l,
    t.ScrollBarH = h,
    t.VScrollBar = l,
    t.HScrollBar = h
}),
define("ace/renderloop", ["require", "exports", "module", "ace/lib/event"], function(e, t, i) {
    "use strict";
    function n(e, t) {
        this.onRender = e,
        this.pending = !1,
        this.changes = 0,
        this.$recursionLimit = 2,
        this.window = t || window;
        var i = this;
        this._flush = function(e) {
            i.pending = !1;
            var t = i.changes;
            if (t && (s.blockIdle(100),
            i.changes = 0,
            i.onRender(t)),
            i.changes) {
                if (i.$recursionLimit-- < 0)
                    return;
                i.schedule()
            } else
                i.$recursionLimit = 2
        }
    }
    var s = e("./lib/event");
    (function() {
        this.schedule = function(e) {
            this.changes = this.changes | e,
            this.changes && !this.pending && (s.nextFrame(this._flush),
            this.pending = !0)
        }
        ,
        this.clear = function(e) {
            var t = this.changes;
            return this.changes = 0,
            t
        }
    }
    ).call(n.prototype),
    t.RenderLoop = n
}),
define("ace/layer/font_metrics", ["require", "exports", "module", "ace/lib/oop", "ace/lib/dom", "ace/lib/lang", "ace/lib/event", "ace/lib/useragent", "ace/lib/event_emitter"], function(e, t, i) {
    var n = e("../lib/oop")
      , s = e("../lib/dom")
      , o = e("../lib/lang")
      , r = e("../lib/event")
      , a = e("../lib/useragent")
      , l = e("../lib/event_emitter").EventEmitter
      , h = "function" == typeof ResizeObserver
      , c = t.FontMetrics = function(e) {
        this.el = s.createElement("div"),
        this.$setMeasureNodeStyles(this.el.style, !0),
        this.$main = s.createElement("div"),
        this.$setMeasureNodeStyles(this.$main.style),
        this.$measureNode = s.createElement("div"),
        this.$setMeasureNodeStyles(this.$measureNode.style),
        this.el.appendChild(this.$main),
        this.el.appendChild(this.$measureNode),
        e.appendChild(this.el),
        this.$measureNode.textContent = o.stringRepeat("X", 256),
        this.$characterSize = {
            width: 0,
            height: 0
        },
        h ? this.$addObserver() : this.checkForSizeChanges()
    }
    ;
    (function() {
        n.implement(this, l),
        this.$characterSize = {
            width: 0,
            height: 0
        },
        this.$setMeasureNodeStyles = function(e, t) {
            e.width = e.height = "auto",
            e.left = e.top = "0px",
            e.visibility = "hidden",
            e.position = "absolute",
            e.whiteSpace = "pre",
            a.isIE < 8 ? e["font-family"] = "inherit" : e.font = "inherit",
            e.overflow = t ? "hidden" : "visible"
        }
        ,
        this.checkForSizeChanges = function(e) {
            var t;
            void 0 === e && (e = this.$measureSizes()),
            !e || this.$characterSize.width === e.width && this.$characterSize.height === e.height || (this.$measureNode.style.fontWeight = "bold",
            t = this.$measureSizes(),
            this.$measureNode.style.fontWeight = "",
            this.$characterSize = e,
            this.charSizes = Object.create(null),
            this.allowBoldFonts = t && t.width === e.width && t.height === e.height,
            this._emit("changeCharacterSize", {
                data: e
            }))
        }
        ,
        this.$addObserver = function() {
            var t = this;
            this.$observer = new window.ResizeObserver(function(e) {
                t.checkForSizeChanges()
            }
            ),
            this.$observer.observe(this.$measureNode)
        }
        ,
        this.$pollSizeChanges = function() {
            if (this.$pollSizeChangesTimer || this.$observer)
                return this.$pollSizeChangesTimer;
            var t = this;
            return this.$pollSizeChangesTimer = r.onIdle(function e() {
                t.checkForSizeChanges(),
                r.onIdle(e, 500)
            }, 500)
        }
        ,
        this.setPolling = function(e) {
            e ? this.$pollSizeChanges() : this.$pollSizeChangesTimer && (clearInterval(this.$pollSizeChangesTimer),
            this.$pollSizeChangesTimer = 0)
        }
        ,
        this.$measureSizes = function(e) {
            var t = {
                height: (e || this.$measureNode).clientHeight,
                width: (e || this.$measureNode).clientWidth / 256
            };
            return 0 === t.width || 0 === t.height ? null : t
        }
        ,
        this.$measureCharWidth = function(e) {
            return this.$main.textContent = o.stringRepeat(e, 256),
            this.$main.getBoundingClientRect().width / 256
        }
        ,
        this.getCharacterWidth = function(e) {
            var t = this.charSizes[e];
            return void 0 === t && (t = this.charSizes[e] = this.$measureCharWidth(e) / this.$characterSize.width),
            t
        }
        ,
        this.destroy = function() {
            clearInterval(this.$pollSizeChangesTimer),
            this.$observer && this.$observer.disconnect(),
            this.el && this.el.parentNode && this.el.parentNode.removeChild(this.el)
        }
        ,
        this.$getZoom = function e(t) {
            return t && t.parentElement ? (window.getComputedStyle(t).zoom || 1) * e(t.parentElement) : 1
        }
        ,
        this.$initTransformMeasureNodes = function() {
            function e(e, t) {
                return ["div", {
                    style: "position: absolute;top:" + e + "px;left:" + t + "px;"
                }]
            }
            this.els = s.buildDom([e(0, 0), e(200, 0), e(0, 200), e(200, 200)], this.el)
        }
        ,
        this.transformCoordinates = function(e, t) {
            function i(e, t, i) {
                var n = e[1] * t[0] - e[0] * t[1];
                return [(-t[1] * i[0] + t[0] * i[1]) / n, (e[1] * i[0] - e[0] * i[1]) / n]
            }
            function n(e, t) {
                return [e[0] - t[0], e[1] - t[1]]
            }
            function s(e, t) {
                return [e[0] + t[0], e[1] + t[1]]
            }
            function o(e, t) {
                return [e * t[0], e * t[1]]
            }
            function r(e) {
                var t = e.getBoundingClientRect();
                return [t.left, t.top]
            }
            e = e && o(1 / this.$getZoom(this.el), e),
            this.els || this.$initTransformMeasureNodes();
            var a = r(this.els[0])
              , l = r(this.els[1])
              , h = r(this.els[2])
              , c = r(this.els[3])
              , u = i(n(c, l), n(c, h), n(s(l, h), s(c, a)))
              , d = o(1 + u[0], n(l, a))
              , g = o(1 + u[1], n(h, a));
            if (t) {
                var f = u[0] * t[0] / 200 + u[1] * t[1] / 200 + 1
                  , m = s(o(t[0], d), o(t[1], g));
                return s(o(1 / f / 200, m), a)
            }
            var p = n(e, a)
              , w = i(n(d, o(u[0], p)), n(g, o(u[1], p)), p);
            return o(200, w)
        }
    }
    ).call(c.prototype)
}),
define("ace/virtual_renderer", ["require", "exports", "module", "ace/lib/oop", "ace/lib/dom", "ace/config", "ace/layer/gutter", "ace/layer/marker", "ace/layer/text", "ace/layer/cursor", "ace/scrollbar", "ace/scrollbar", "ace/renderloop", "ace/layer/font_metrics", "ace/lib/event_emitter", "ace/lib/useragent"], function(e, t, i) {
    "use strict";
    var n = e("./lib/oop")
      , c = e("./lib/dom")
      , o = e("./config")
      , s = e("./layer/gutter").Gutter
      , r = e("./layer/marker").Marker
      , a = e("./layer/text").Text
      , l = e("./layer/cursor").Cursor
      , h = e("./scrollbar").HScrollBar
      , u = e("./scrollbar").VScrollBar
      , d = e("./renderloop").RenderLoop
      , g = e("./layer/font_metrics").FontMetrics
      , f = e("./lib/event_emitter").EventEmitter
      , m = '.ace_br1 {border-top-left-radius    : 3px;}.ace_br2 {border-top-right-radius   : 3px;}.ace_br3 {border-top-left-radius    : 3px; border-top-right-radius:    3px;}.ace_br4 {border-bottom-right-radius: 3px;}.ace_br5 {border-top-left-radius    : 3px; border-bottom-right-radius: 3px;}.ace_br6 {border-top-right-radius   : 3px; border-bottom-right-radius: 3px;}.ace_br7 {border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px;}.ace_br8 {border-bottom-left-radius : 3px;}.ace_br9 {border-top-left-radius    : 3px; border-bottom-left-radius:  3px;}.ace_br10{border-top-right-radius   : 3px; border-bottom-left-radius:  3px;}.ace_br11{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-left-radius:  3px;}.ace_br12{border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br13{border-top-left-radius    : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br14{border-top-right-radius   : 3px; border-bottom-right-radius: 3px; border-bottom-left-radius:  3px;}.ace_br15{border-top-left-radius    : 3px; border-top-right-radius:    3px; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px;}.ace_editor {position: relative;overflow: hidden;padding: 0;font: 12px/normal \'Monaco\', \'Menlo\', \'Ubuntu Mono\', \'Consolas\', \'source-code-pro\', monospace;direction: ltr;text-align: left;-webkit-tap-highlight-color: rgba(0, 0, 0, 0);}.ace_scroller {position: absolute;overflow: hidden;top: 0;bottom: 0;background-color: inherit;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;cursor: text;}.ace_content {position: absolute;box-sizing: border-box;min-width: 100%;contain: style size layout;font-variant-ligatures: no-common-ligatures;}.ace_dragging .ace_scroller:before{position: absolute;top: 0;left: 0;right: 0;bottom: 0;content: \'\';background: rgba(250, 250, 250, 0.01);z-index: 1000;}.ace_dragging.ace_dark .ace_scroller:before{background: rgba(0, 0, 0, 0.01);}.ace_selecting, .ace_selecting * {cursor: text !important;}.ace_gutter {position: absolute;overflow : hidden;width: auto;top: 0;bottom: 0;left: 0;cursor: default;z-index: 4;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;contain: style size layout;}.ace_gutter-active-line {position: absolute;left: 0;right: 0;}.ace_scroller.ace_scroll-left {box-shadow: 17px 0 16px -16px rgba(0, 0, 0, 0.4) inset;}.ace_gutter-cell {position: absolute;top: 0;left: 0;right: 0;padding-left: 19px;padding-right: 6px;background-repeat: no-repeat;}.ace_gutter-cell.ace_error {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAABOFBMVEX/////////QRswFAb/Ui4wFAYwFAYwFAaWGAfDRymzOSH/PxswFAb/SiUwFAYwFAbUPRvjQiDllog5HhHdRybsTi3/Tyv9Tir+Syj/UC3////XurebMBIwFAb/RSHbPx/gUzfdwL3kzMivKBAwFAbbvbnhPx66NhowFAYwFAaZJg8wFAaxKBDZurf/RB6mMxb/SCMwFAYwFAbxQB3+RB4wFAb/Qhy4Oh+4QifbNRcwFAYwFAYwFAb/QRzdNhgwFAYwFAbav7v/Uy7oaE68MBK5LxLewr/r2NXewLswFAaxJw4wFAbkPRy2PyYwFAaxKhLm1tMwFAazPiQwFAaUGAb/QBrfOx3bvrv/VC/maE4wFAbRPBq6MRO8Qynew8Dp2tjfwb0wFAbx6eju5+by6uns4uH9/f36+vr/GkHjAAAAYnRSTlMAGt+64rnWu/bo8eAA4InH3+DwoN7j4eLi4xP99Nfg4+b+/u9B/eDs1MD1mO7+4PHg2MXa347g7vDizMLN4eG+Pv7i5evs/v79yu7S3/DV7/498Yv24eH+4ufQ3Ozu/v7+y13sRqwAAADLSURBVHjaZc/XDsFgGIBhtDrshlitmk2IrbHFqL2pvXf/+78DPokj7+Fz9qpU/9UXJIlhmPaTaQ6QPaz0mm+5gwkgovcV6GZzd5JtCQwgsxoHOvJO15kleRLAnMgHFIESUEPmawB9ngmelTtipwwfASilxOLyiV5UVUyVAfbG0cCPHig+GBkzAENHS0AstVF6bacZIOzgLmxsHbt2OecNgJC83JERmePUYq8ARGkJx6XtFsdddBQgZE2nPR6CICZhawjA4Fb/chv+399kfR+MMMDGOQAAAABJRU5ErkJggg==");background-repeat: no-repeat;background-position: 2px center;}.ace_gutter-cell.ace_warning {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAMAAAAoLQ9TAAAAmVBMVEX///8AAAD///8AAAAAAABPSzb/5sAAAAB/blH/73z/ulkAAAAAAAD85pkAAAAAAAACAgP/vGz/rkDerGbGrV7/pkQICAf////e0IsAAAD/oED/qTvhrnUAAAD/yHD/njcAAADuv2r/nz//oTj/p064oGf/zHAAAAA9Nir/tFIAAAD/tlTiuWf/tkIAAACynXEAAAAAAAAtIRW7zBpBAAAAM3RSTlMAABR1m7RXO8Ln31Z36zT+neXe5OzooRDfn+TZ4p3h2hTf4t3k3ucyrN1K5+Xaks52Sfs9CXgrAAAAjklEQVR42o3PbQ+CIBQFYEwboPhSYgoYunIqqLn6/z8uYdH8Vmdnu9vz4WwXgN/xTPRD2+sgOcZjsge/whXZgUaYYvT8QnuJaUrjrHUQreGczuEafQCO/SJTufTbroWsPgsllVhq3wJEk2jUSzX3CUEDJC84707djRc5MTAQxoLgupWRwW6UB5fS++NV8AbOZgnsC7BpEAAAAABJRU5ErkJggg==");background-position: 2px center;}.ace_gutter-cell.ace_info {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAAAAAA6mKC9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAAJ0Uk5TAAB2k804AAAAPklEQVQY02NgIB68QuO3tiLznjAwpKTgNyDbMegwisCHZUETUZV0ZqOquBpXj2rtnpSJT1AEnnRmL2OgGgAAIKkRQap2htgAAAAASUVORK5CYII=");background-position: 2px center;}.ace_dark .ace_gutter-cell.ace_info {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAJFBMVEUAAAChoaGAgIAqKiq+vr6tra1ZWVmUlJSbm5s8PDxubm56enrdgzg3AAAAAXRSTlMAQObYZgAAAClJREFUeNpjYMAPdsMYHegyJZFQBlsUlMFVCWUYKkAZMxZAGdxlDMQBAG+TBP4B6RyJAAAAAElFTkSuQmCC");}.ace_scrollbar {contain: strict;position: absolute;right: 0;bottom: 0;z-index: 6;}.ace_scrollbar-inner {position: absolute;cursor: text;left: 0;top: 0;}.ace_scrollbar-v{overflow-x: hidden;overflow-y: scroll;top: 0;}.ace_scrollbar-h {overflow-x: scroll;overflow-y: hidden;left: 0;}.ace_print-margin {position: absolute;height: 100%;}.ace_text-input {position: absolute;z-index: 0;width: 0.5em;height: 1em;opacity: 0;background: transparent;-moz-appearance: none;appearance: none;border: none;resize: none;outline: none;overflow: hidden;font: inherit;padding: 0 1px;margin: 0 -1px;contain: strict;-ms-user-select: text;-moz-user-select: text;-webkit-user-select: text;user-select: text;white-space: pre!important;}.ace_text-input.ace_composition {background: transparent;color: inherit;z-index: 1000;opacity: 1;}.ace_composition_placeholder { color: transparent }.ace_composition_marker { border-bottom: 1px solid;position: absolute;border-radius: 0;margin-top: 1px;}[ace_nocontext=true] {transform: none!important;filter: none!important;clip-path: none!important;mask : none!important;contain: none!important;perspective: none!important;mix-blend-mode: initial!important;z-index: auto;}.ace_layer {z-index: 1;position: absolute;overflow: hidden;word-wrap: normal;white-space: pre;height: 100%;width: 100%;box-sizing: border-box;pointer-events: none;}.ace_gutter-layer {position: relative;width: auto;text-align: right;pointer-events: auto;height: 1000000px;contain: style size layout;}.ace_text-layer {font: inherit !important;position: absolute;height: 1000000px;width: 1000000px;contain: style size layout;}.ace_text-layer > .ace_line, .ace_text-layer > .ace_line_group {contain: style size layout;position: absolute;top: 0;left: 0;right: 0;}.ace_hidpi .ace_text-layer,.ace_hidpi .ace_gutter-layer,.ace_hidpi .ace_content,.ace_hidpi .ace_gutter {contain: strict;will-change: transform;}.ace_hidpi .ace_text-layer > .ace_line, .ace_hidpi .ace_text-layer > .ace_line_group {contain: strict;}.ace_cjk {display: inline-block;text-align: center;}.ace_cursor-layer {z-index: 4;}.ace_cursor {z-index: 4;position: absolute;box-sizing: border-box;border-left: 2px solid;transform: translatez(0);}.ace_multiselect .ace_cursor {border-left-width: 1px;}.ace_slim-cursors .ace_cursor {border-left-width: 1px;}.ace_overwrite-cursors .ace_cursor {border-left-width: 0;border-bottom: 1px solid;}.ace_hidden-cursors .ace_cursor {opacity: 0.2;}.ace_hasPlaceholder .ace_hidden-cursors .ace_cursor {opacity: 0;}.ace_smooth-blinking .ace_cursor {transition: opacity 0.18s;}.ace_animate-blinking .ace_cursor {animation-duration: 1000ms;animation-timing-function: step-end;animation-name: blink-ace-animate;animation-iteration-count: infinite;}.ace_animate-blinking.ace_smooth-blinking .ace_cursor {animation-duration: 1000ms;animation-timing-function: ease-in-out;animation-name: blink-ace-animate-smooth;}@keyframes blink-ace-animate {from, to { opacity: 1; }60% { opacity: 0; }}@keyframes blink-ace-animate-smooth {from, to { opacity: 1; }45% { opacity: 1; }60% { opacity: 0; }85% { opacity: 0; }}.ace_marker-layer .ace_step, .ace_marker-layer .ace_stack {position: absolute;z-index: 3;}.ace_marker-layer .ace_selection {position: absolute;z-index: 5;}.ace_marker-layer .ace_bracket {position: absolute;z-index: 6;}.ace_marker-layer .ace_error_bracket {position: absolute;border-bottom: 1px solid #DE5555;border-radius: 0;}.ace_marker-layer .ace_active-line {position: absolute;z-index: 2;}.ace_marker-layer .ace_selected-word {position: absolute;z-index: 4;box-sizing: border-box;}.ace_line .ace_fold {box-sizing: border-box;display: inline-block;height: 11px;margin-top: -2px;vertical-align: middle;background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACJJREFUeNpi+P//fxgTAwPDBxDxD078RSX+YeEyDFMCIMAAI3INmXiwf2YAAAAASUVORK5CYII=");background-repeat: no-repeat, repeat-x;background-position: center center, top left;color: transparent;border: 1px solid black;border-radius: 2px;cursor: pointer;pointer-events: auto;}.ace_dark .ace_fold {}.ace_fold:hover{background-image:url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAJCAYAAADU6McMAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAJpJREFUeNpi/P//PwOlgAXGYGRklAVSokD8GmjwY1wasKljQpYACtpCFeADcHVQfQyMQAwzwAZI3wJKvCLkfKBaMSClBlR7BOQikCFGQEErIH0VqkabiGCAqwUadAzZJRxQr/0gwiXIal8zQQPnNVTgJ1TdawL0T5gBIP1MUJNhBv2HKoQHHjqNrA4WO4zY0glyNKLT2KIfIMAAQsdgGiXvgnYAAAAASUVORK5CYII="),url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAA3CAYAAADNNiA5AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAACBJREFUeNpi+P//fz4TAwPDZxDxD5X4i5fLMEwJgAADAEPVDbjNw87ZAAAAAElFTkSuQmCC");}.ace_tooltip {background-color: #FFF;background-image: linear-gradient(to bottom, transparent, rgba(0, 0, 0, 0.1));border: 1px solid gray;border-radius: 1px;box-shadow: 0 1px 2px rgba(0, 0, 0, 0.3);color: black;max-width: 100%;padding: 3px 4px;position: fixed;z-index: 999999;box-sizing: border-box;cursor: default;white-space: pre;word-wrap: break-word;line-height: normal;font-style: normal;font-weight: normal;letter-spacing: normal;pointer-events: none;}.ace_folding-enabled > .ace_gutter-cell {padding-right: 13px;}.ace_fold-widget {box-sizing: border-box;margin: 0 -12px 0 1px;display: none;width: 11px;vertical-align: top;background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42mWKsQ0AMAzC8ixLlrzQjzmBiEjp0A6WwBCSPgKAXoLkqSot7nN3yMwR7pZ32NzpKkVoDBUxKAAAAABJRU5ErkJggg==");background-repeat: no-repeat;background-position: center;border-radius: 3px;border: 1px solid transparent;cursor: pointer;}.ace_folding-enabled .ace_fold-widget {display: inline-block;   }.ace_fold-widget.ace_end {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAANElEQVR42m3HwQkAMAhD0YzsRchFKI7sAikeWkrxwScEB0nh5e7KTPWimZki4tYfVbX+MNl4pyZXejUO1QAAAABJRU5ErkJggg==");}.ace_fold-widget.ace_closed {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAGCAYAAAAG5SQMAAAAOUlEQVR42jXKwQkAMAgDwKwqKD4EwQ26sSOkVWjgIIHAzPiCgaqiqnJHZnKICBERHN194O5b9vbLuAVRL+l0YWnZAAAAAElFTkSuQmCCXA==");}.ace_fold-widget:hover {border: 1px solid rgba(0, 0, 0, 0.3);background-color: rgba(255, 255, 255, 0.2);box-shadow: 0 1px 1px rgba(255, 255, 255, 0.7);}.ace_fold-widget:active {border: 1px solid rgba(0, 0, 0, 0.4);background-color: rgba(0, 0, 0, 0.05);box-shadow: 0 1px 1px rgba(255, 255, 255, 0.8);}.ace_dark .ace_fold-widget {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHklEQVQIW2P4//8/AzoGEQ7oGCaLLAhWiSwB146BAQCSTPYocqT0AAAAAElFTkSuQmCC");}.ace_dark .ace_fold-widget.ace_end {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAH0lEQVQIW2P4//8/AxQ7wNjIAjDMgC4AxjCVKBirIAAF0kz2rlhxpAAAAABJRU5ErkJggg==");}.ace_dark .ace_fold-widget.ace_closed {background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAMAAAAFCAYAAACAcVaiAAAAHElEQVQIW2P4//+/AxAzgDADlOOAznHAKgPWAwARji8UIDTfQQAAAABJRU5ErkJggg==");}.ace_dark .ace_fold-widget:hover {box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);background-color: rgba(255, 255, 255, 0.1);}.ace_dark .ace_fold-widget:active {box-shadow: 0 1px 1px rgba(255, 255, 255, 0.2);}.ace_inline_button {border: 1px solid lightgray;display: inline-block;margin: -1px 8px;padding: 0 5px;pointer-events: auto;cursor: pointer;}.ace_inline_button:hover {border-color: gray;background: rgba(200,200,200,0.2);display: inline-block;pointer-events: auto;}.ace_fold-widget.ace_invalid {background-color: #FFB4B4;border-color: #DE5555;}.ace_fade-fold-widgets .ace_fold-widget {transition: opacity 0.4s ease 0.05s;opacity: 0;}.ace_fade-fold-widgets:hover .ace_fold-widget {transition: opacity 0.05s ease 0.05s;opacity:1;}.ace_underline {text-decoration: underline;}.ace_bold {font-weight: bold;}.ace_nobold .ace_bold {font-weight: normal;}.ace_italic {font-style: italic;}.ace_error-marker {background-color: rgba(255, 0, 0,0.2);position: absolute;z-index: 9;}.ace_highlight-marker {background-color: rgba(255, 255, 0,0.2);position: absolute;z-index: 8;}.ace_mobile-menu {position: absolute;line-height: 1.5;border-radius: 4px;-ms-user-select: none;-moz-user-select: none;-webkit-user-select: none;user-select: none;background: white;box-shadow: 1px 3px 2px grey;border: 1px solid #dcdcdc;color: black;}.ace_dark > .ace_mobile-menu {background: #333;color: #ccc;box-shadow: 1px 3px 2px grey;border: 1px solid #444;}.ace_mobile-button {padding: 2px;cursor: pointer;overflow: hidden;}.ace_mobile-button:hover {background-color: #eee;opacity:1;}.ace_mobile-button:active {background-color: #ddd;}.ace_placeholder {font-family: arial;transform: scale(0.9);transform-origin: left;white-space: pre;opacity: 0.7;margin: 0 10px;}'
      , p = e("./lib/useragent")
      , w = p.isIE;
    c.importCssString(m, "ace_editor.css");
    function v(e, t) {
        var i = this;
        this.container = e || c.createElement("div"),
        c.addCssClass(this.container, "ace_editor"),
        c.HI_DPI && c.addCssClass(this.container, "ace_hidpi"),
        this.setTheme(t),
        this.$gutter = c.createElement("div"),
        this.$gutter.className = "ace_gutter",
        this.container.appendChild(this.$gutter),
        this.$gutter.setAttribute("aria-hidden", !0),
        this.scroller = c.createElement("div"),
        this.scroller.className = "ace_scroller",
        this.container.appendChild(this.scroller),
        this.content = c.createElement("div"),
        this.content.className = "ace_content",
        this.scroller.appendChild(this.content),
        this.$gutterLayer = new s(this.$gutter),
        this.$gutterLayer.on("changeGutterWidth", this.onGutterResize.bind(this)),
        this.$markerBack = new r(this.content);
        var n = this.$textLayer = new a(this.content);
        this.canvas = n.element,
        this.$markerFront = new r(this.content),
        this.$cursorLayer = new l(this.content),
        this.$horizScroll = !1,
        this.$vScroll = !1,
        this.scrollBar = this.scrollBarV = new u(this.container,this),
        this.scrollBarH = new h(this.container,this),
        this.scrollBarV.on("scroll", function(e) {
            i.$scrollAnimation || i.session.setScrollTop(e.data - i.scrollMargin.top)
        }),
        this.scrollBarH.on("scroll", function(e) {
            i.$scrollAnimation || i.session.setScrollLeft(e.data - i.scrollMargin.left)
        }),
        this.scrollTop = 0,
        this.scrollLeft = 0,
        this.cursorPos = {
            row: 0,
            column: 0
        },
        this.$fontMetrics = new g(this.container),
        this.$textLayer.$setFontMetrics(this.$fontMetrics),
        this.$textLayer.on("changeCharacterSize", function(e) {
            i.updateCharacterSize(),
            i.onResize(!0, i.gutterWidth, i.$size.width, i.$size.height),
            i._signal("changeCharacterSize", e)
        }),
        this.$size = {
            width: 0,
            height: 0,
            scrollerHeight: 0,
            scrollerWidth: 0,
            $dirty: !0
        },
        this.layerConfig = {
            width: 1,
            padding: 0,
            firstRow: 0,
            firstRowScreen: 0,
            lastRow: 0,
            lineHeight: 0,
            characterWidth: 0,
            minHeight: 1,
            maxHeight: 1,
            offset: 0,
            height: 1,
            gutterOffset: 1
        },
        this.scrollMargin = {
            left: 0,
            right: 0,
            top: 0,
            bottom: 0,
            v: 0,
            h: 0
        },
        this.margin = {
            left: 0,
            right: 0,
            top: 0,
            bottom: 0,
            v: 0,
            h: 0
        },
        this.$keepTextAreaAtCursor = !p.isIOS,
        this.$loop = new d(this.$renderChanges.bind(this),this.container.ownerDocument.defaultView),
        this.$loop.schedule(this.CHANGE_FULL),
        this.updateCharacterSize(),
        this.setPadding(4),
        o.resetOptions(this),
        o._signal("renderer", this)
    }
    (function() {
        this.CHANGE_CURSOR = 1,
        this.CHANGE_MARKER = 2,
        this.CHANGE_GUTTER = 4,
        this.CHANGE_SCROLL = 8,
        this.CHANGE_LINES = 16,
        this.CHANGE_TEXT = 32,
        this.CHANGE_SIZE = 64,
        this.CHANGE_MARKER_BACK = 128,
        this.CHANGE_MARKER_FRONT = 256,
        this.CHANGE_FULL = 512,
        this.CHANGE_H_SCROLL = 1024,
        n.implement(this, f),
        this.updateCharacterSize = function() {
            this.$textLayer.allowBoldFonts != this.$allowBoldFonts && (this.$allowBoldFonts = this.$textLayer.allowBoldFonts,
            this.setStyle("ace_nobold", !this.$allowBoldFonts)),
            this.layerConfig.characterWidth = this.characterWidth = this.$textLayer.getCharacterWidth(),
            this.layerConfig.lineHeight = this.lineHeight = this.$textLayer.getLineHeight(),
            this.$updatePrintMargin(),
            c.setStyle(this.scroller.style, "line-height", this.lineHeight + "px")
        }
        ,
        this.setSession = function(e) {
            this.session && this.session.doc.off("changeNewLineMode", this.onChangeNewLineMode),
            (this.session = e) && this.scrollMargin.top && e.getScrollTop() <= 0 && e.setScrollTop(-this.scrollMargin.top),
            this.$cursorLayer.setSession(e),
            this.$markerBack.setSession(e),
            this.$markerFront.setSession(e),
            this.$gutterLayer.setSession(e),
            this.$textLayer.setSession(e),
            e && (this.$loop.schedule(this.CHANGE_FULL),
            this.session.$setFontMetrics(this.$fontMetrics),
            this.scrollBarH.scrollLeft = this.scrollBarV.scrollTop = null,
            this.onChangeNewLineMode = this.onChangeNewLineMode.bind(this),
            this.onChangeNewLineMode(),
            this.session.doc.on("changeNewLineMode", this.onChangeNewLineMode))
        }
        ,
        this.updateLines = function(e, t, i) {
            if (void 0 === t && (t = 1 / 0),
            this.$changedLines ? (this.$changedLines.firstRow > e && (this.$changedLines.firstRow = e),
            this.$changedLines.lastRow < t && (this.$changedLines.lastRow = t)) : this.$changedLines = {
                firstRow: e,
                lastRow: t
            },
            this.$changedLines.lastRow < this.layerConfig.firstRow) {
                if (!i)
                    return;
                this.$changedLines.lastRow = this.layerConfig.lastRow
            }
            this.$changedLines.firstRow > this.layerConfig.lastRow || this.$loop.schedule(this.CHANGE_LINES)
        }
        ,
        this.onChangeNewLineMode = function() {
            this.$loop.schedule(this.CHANGE_TEXT),
            this.$textLayer.$updateEolChar(),
            this.session.$bidiHandler.setEolChar(this.$textLayer.EOL_CHAR)
        }
        ,
        this.onChangeTabSize = function() {
            this.$loop.schedule(this.CHANGE_TEXT | this.CHANGE_MARKER),
            this.$textLayer.onChangeTabSize()
        }
        ,
        this.updateText = function() {
            this.$loop.schedule(this.CHANGE_TEXT)
        }
        ,
        this.updateFull = function(e) {
            e ? this.$renderChanges(this.CHANGE_FULL, !0) : this.$loop.schedule(this.CHANGE_FULL)
        }
        ,
        this.updateFontSize = function() {
            this.$textLayer.checkForSizeChanges()
        }
        ,
        this.$changes = 0,
        this.$updateSizeAsync = function() {
            this.$loop.pending ? this.$size.$dirty = !0 : this.onResize()
        }
        ,
        this.onResize = function(e, t, i, n) {
            if (!(2 < this.resizing)) {
                0 < this.resizing ? this.resizing++ : this.resizing = e ? 1 : 0;
                var s = this.container;
                n = n || (s.clientHeight || s.scrollHeight),
                i = i || (s.clientWidth || s.scrollWidth);
                var o = this.$updateCachedSize(e, t, i, n);
                if (!this.$size.scrollerHeight || !i && !n)
                    return this.resizing = 0;
                e && (this.$gutterLayer.$padding = null),
                e ? this.$renderChanges(o | this.$changes, !0) : this.$loop.schedule(o | this.$changes),
                this.resizing && (this.resizing = 0),
                this.scrollBarV.scrollLeft = this.scrollBarV.scrollTop = null
            }
        }
        ,
        this.$updateCachedSize = function(e, t, i, n) {
            n -= this.$extraHeight || 0;
            var s, o = 0, r = this.$size, a = {
                width: r.width,
                height: r.height,
                scrollerHeight: r.scrollerHeight,
                scrollerWidth: r.scrollerWidth
            };
            return n && (e || r.height != n) && (r.height = n,
            o |= this.CHANGE_SIZE,
            r.scrollerHeight = r.height,
            this.$horizScroll && (r.scrollerHeight -= this.scrollBarH.getHeight()),
            this.scrollBarV.element.style.bottom = this.scrollBarH.getHeight() + "px",
            o |= this.CHANGE_SCROLL),
            i && (e || r.width != i) && (o |= this.CHANGE_SIZE,
            r.width = i,
            null == t && (t = this.$showGutter ? this.$gutter.offsetWidth : 0),
            this.gutterWidth = t,
            c.setStyle(this.scrollBarH.element.style, "left", t + "px"),
            c.setStyle(this.scroller.style, "left", t + this.margin.left + "px"),
            r.scrollerWidth = Math.max(0, i - t - this.scrollBarV.getWidth() - this.margin.h),
            c.setStyle(this.$gutter.style, "left", this.margin.left + "px"),
            s = this.scrollBarV.getWidth() + "px",
            c.setStyle(this.scrollBarH.element.style, "right", s),
            c.setStyle(this.scroller.style, "right", s),
            c.setStyle(this.scroller.style, "bottom", this.scrollBarH.getHeight()),
            (this.session && this.session.getUseWrapMode() && this.adjustWrapLimit() || e) && (o |= this.CHANGE_FULL)),
            r.$dirty = !i || !n,
            o && this._signal("resize", a),
            o
        }
        ,
        this.onGutterResize = function(e) {
            var t = this.$showGutter ? e : 0;
            t != this.gutterWidth && (this.$changes |= this.$updateCachedSize(!0, t, this.$size.width, this.$size.height)),
            this.session.getUseWrapMode() && this.adjustWrapLimit() || this.$size.$dirty ? this.$loop.schedule(this.CHANGE_FULL) : this.$computeLayerConfig()
        }
        ,
        this.adjustWrapLimit = function() {
            var e = this.$size.scrollerWidth - 2 * this.$padding
              , t = Math.floor(e / this.characterWidth);
            return this.session.adjustWrapLimit(t, this.$showPrintMargin && this.$printMarginColumn)
        }
        ,
        this.setAnimatedScroll = function(e) {
            this.setOption("animatedScroll", e)
        }
        ,
        this.getAnimatedScroll = function() {
            return this.$animatedScroll
        }
        ,
        this.setShowInvisibles = function(e) {
            this.setOption("showInvisibles", e),
            this.session.$bidiHandler.setShowInvisibles(e)
        }
        ,
        this.getShowInvisibles = function() {
            return this.getOption("showInvisibles")
        }
        ,
        this.getDisplayIndentGuides = function() {
            return this.getOption("displayIndentGuides")
        }
        ,
        this.setDisplayIndentGuides = function(e) {
            this.setOption("displayIndentGuides", e)
        }
        ,
        this.setShowPrintMargin = function(e) {
            this.setOption("showPrintMargin", e)
        }
        ,
        this.getShowPrintMargin = function() {
            return this.getOption("showPrintMargin")
        }
        ,
        this.setPrintMarginColumn = function(e) {
            this.setOption("printMarginColumn", e)
        }
        ,
        this.getPrintMarginColumn = function() {
            return this.getOption("printMarginColumn")
        }
        ,
        this.getShowGutter = function() {
            return this.getOption("showGutter")
        }
        ,
        this.setShowGutter = function(e) {
            return this.setOption("showGutter", e)
        }
        ,
        this.getFadeFoldWidgets = function() {
            return this.getOption("fadeFoldWidgets")
        }
        ,
        this.setFadeFoldWidgets = function(e) {
            this.setOption("fadeFoldWidgets", e)
        }
        ,
        this.setHighlightGutterLine = function(e) {
            this.setOption("highlightGutterLine", e)
        }
        ,
        this.getHighlightGutterLine = function() {
            return this.getOption("highlightGutterLine")
        }
        ,
        this.$updatePrintMargin = function() {
            var e, t;
            (this.$showPrintMargin || this.$printMarginEl) && (this.$printMarginEl || ((e = c.createElement("div")).className = "ace_layer ace_print-margin-layer",
            this.$printMarginEl = c.createElement("div"),
            this.$printMarginEl.className = "ace_print-margin",
            e.appendChild(this.$printMarginEl),
            this.content.insertBefore(e, this.content.firstChild)),
            (t = this.$printMarginEl.style).left = Math.round(this.characterWidth * this.$printMarginColumn + this.$padding) + "px",
            t.visibility = this.$showPrintMargin ? "visible" : "hidden",
            this.session && -1 == this.session.$wrap && this.adjustWrapLimit())
        }
        ,
        this.getContainerElement = function() {
            return this.container
        }
        ,
        this.getMouseEventTarget = function() {
            return this.scroller
        }
        ,
        this.getTextAreaContainer = function() {
            return this.container
        }
        ,
        this.$moveTextAreaToCursor = function() {
            var e, t, i, n, s, o, r, a, l, h;
            this.$isMousePressed || (e = this.textarea.style,
            t = this.$composition,
            this.$keepTextAreaAtCursor || t ? (i = this.$cursorLayer.$pixelPos) && (t && t.markerRange && (i = this.$cursorLayer.getPixelPosition(t.markerRange.start, !0)),
            n = this.layerConfig,
            s = i.top,
            o = i.left,
            s -= n.offset,
            r = t && t.useTextareaForIME ? this.lineHeight : w ? 0 : 1,
            s < 0 || s > n.height - r ? c.translate(this.textarea, 0, 0) : (h = 1,
            a = this.$size.height - r,
            t ? t.useTextareaForIME ? (l = this.textarea.value,
            h = this.characterWidth * this.session.$getStringScreenWidth(l)[0]) : s += this.lineHeight + 2 : s += this.lineHeight,
            (o -= this.scrollLeft) > this.$size.scrollerWidth - h && (o = this.$size.scrollerWidth - h),
            o += this.gutterWidth + this.margin.left,
            c.setStyle(e, "height", r + "px"),
            c.setStyle(e, "width", h + "px"),
            c.translate(this.textarea, Math.min(o, this.$size.scrollerWidth - h), Math.min(s, a)))) : c.translate(this.textarea, -100, 0))
        }
        ,
        this.getFirstVisibleRow = function() {
            return this.layerConfig.firstRow
        }
        ,
        this.getFirstFullyVisibleRow = function() {
            return this.layerConfig.firstRow + (0 === this.layerConfig.offset ? 0 : 1)
        }
        ,
        this.getLastFullyVisibleRow = function() {
            var e = this.layerConfig
              , t = e.lastRow;
            return this.session.documentToScreenRow(t, 0) * e.lineHeight - this.session.getScrollTop() > e.height - e.lineHeight ? t - 1 : t
        }
        ,
        this.getLastVisibleRow = function() {
            return this.layerConfig.lastRow
        }
        ,
        this.$padding = null,
        this.setPadding = function(e) {
            this.$padding = e,
            this.$textLayer.setPadding(e),
            this.$cursorLayer.setPadding(e),
            this.$markerFront.setPadding(e),
            this.$markerBack.setPadding(e),
            this.$loop.schedule(this.CHANGE_FULL),
            this.$updatePrintMargin()
        }
        ,
        this.setScrollMargin = function(e, t, i, n) {
            var s = this.scrollMargin;
            s.top = 0 | e,
            s.bottom = 0 | t,
            s.right = 0 | n,
            s.left = 0 | i,
            s.v = s.top + s.bottom,
            s.h = s.left + s.right,
            s.top && this.scrollTop <= 0 && this.session && this.session.setScrollTop(-s.top),
            this.updateFull()
        }
        ,
        this.setMargin = function(e, t, i, n) {
            var s = this.margin;
            s.top = 0 | e,
            s.bottom = 0 | t,
            s.right = 0 | n,
            s.left = 0 | i,
            s.v = s.top + s.bottom,
            s.h = s.left + s.right,
            this.$updateCachedSize(!0, this.gutterWidth, this.$size.width, this.$size.height),
            this.updateFull()
        }
        ,
        this.getHScrollBarAlwaysVisible = function() {
            return this.$hScrollBarAlwaysVisible
        }
        ,
        this.setHScrollBarAlwaysVisible = function(e) {
            this.setOption("hScrollBarAlwaysVisible", e)
        }
        ,
        this.getVScrollBarAlwaysVisible = function() {
            return this.$vScrollBarAlwaysVisible
        }
        ,
        this.setVScrollBarAlwaysVisible = function(e) {
            this.setOption("vScrollBarAlwaysVisible", e)
        }
        ,
        this.$updateScrollBarV = function() {
            var e = this.layerConfig.maxHeight
              , t = this.$size.scrollerHeight;
            !this.$maxLines && this.$scrollPastEnd && (e -= (t - this.lineHeight) * this.$scrollPastEnd,
            this.scrollTop > e - t && (e = this.scrollTop + t,
            this.scrollBarV.scrollTop = null)),
            this.scrollBarV.setScrollHeight(e + this.scrollMargin.v),
            this.scrollBarV.setScrollTop(this.scrollTop + this.scrollMargin.top)
        }
        ,
        this.$updateScrollBarH = function() {
            this.scrollBarH.setScrollWidth(this.layerConfig.width + 2 * this.$padding + this.scrollMargin.h),
            this.scrollBarH.setScrollLeft(this.scrollLeft + this.scrollMargin.left)
        }
        ,
        this.$frozen = !1,
        this.freeze = function() {
            this.$frozen = !0
        }
        ,
        this.unfreeze = function() {
            this.$frozen = !1
        }
        ,
        this.$renderChanges = function(e, t) {
            if (this.$changes && (e |= this.$changes,
            this.$changes = 0),
            this.session && this.container.offsetWidth && !this.$frozen && (e || t)) {
                if (this.$size.$dirty)
                    return this.$changes |= e,
                    this.onResize(!0);
                this.lineHeight || this.$textLayer.checkForSizeChanges(),
                this._signal("beforeRender", e),
                this.session && this.session.$bidiHandler && this.session.$bidiHandler.updateCharacterWidths(this.$fontMetrics);
                var i, n, s, o = this.layerConfig;
                return (e & this.CHANGE_FULL || e & this.CHANGE_SIZE || e & this.CHANGE_TEXT || e & this.CHANGE_LINES || e & this.CHANGE_SCROLL || e & this.CHANGE_H_SCROLL) && (e |= this.$computeLayerConfig() | this.$loop.clear(),
                o.firstRow == this.layerConfig.firstRow || o.firstRowScreen != this.layerConfig.firstRowScreen || 0 < (i = this.scrollTop + (o.firstRow - this.layerConfig.firstRow) * this.lineHeight) && (this.scrollTop = i,
                e |= this.CHANGE_SCROLL,
                e |= this.$computeLayerConfig() | this.$loop.clear()),
                o = this.layerConfig,
                this.$updateScrollBarV(),
                e & this.CHANGE_H_SCROLL && this.$updateScrollBarH(),
                c.translate(this.content, -this.scrollLeft, -o.offset),
                n = o.width + 2 * this.$padding + "px",
                s = o.minHeight + "px",
                c.setStyle(this.content.style, "width", n),
                c.setStyle(this.content.style, "height", s)),
                e & this.CHANGE_H_SCROLL && (c.translate(this.content, -this.scrollLeft, -o.offset),
                this.scroller.className = this.scrollLeft <= 0 ? "ace_scroller" : "ace_scroller ace_scroll-left"),
                e & this.CHANGE_FULL ? (this.$changedLines = null,
                this.$textLayer.update(o),
                this.$showGutter && this.$gutterLayer.update(o),
                this.$markerBack.update(o),
                this.$markerFront.update(o),
                this.$cursorLayer.update(o),
                this.$moveTextAreaToCursor()) : e & this.CHANGE_SCROLL ? (this.$changedLines = null,
                e & this.CHANGE_TEXT || e & this.CHANGE_LINES ? this.$textLayer.update(o) : this.$textLayer.scrollLines(o),
                this.$showGutter && (e & this.CHANGE_GUTTER || e & this.CHANGE_LINES ? this.$gutterLayer.update(o) : this.$gutterLayer.scrollLines(o)),
                this.$markerBack.update(o),
                this.$markerFront.update(o),
                this.$cursorLayer.update(o),
                this.$moveTextAreaToCursor()) : (e & this.CHANGE_TEXT ? (this.$changedLines = null,
                this.$textLayer.update(o),
                this.$showGutter && this.$gutterLayer.update(o)) : e & this.CHANGE_LINES ? (this.$updateLines() || e & this.CHANGE_GUTTER && this.$showGutter) && this.$gutterLayer.update(o) : e & this.CHANGE_TEXT || e & this.CHANGE_GUTTER ? this.$showGutter && this.$gutterLayer.update(o) : e & this.CHANGE_CURSOR && this.$highlightGutterLine && this.$gutterLayer.updateLineHighlight(o),
                e & this.CHANGE_CURSOR && (this.$cursorLayer.update(o),
                this.$moveTextAreaToCursor()),
                e & (this.CHANGE_MARKER | this.CHANGE_MARKER_FRONT) && this.$markerFront.update(o),
                e & (this.CHANGE_MARKER | this.CHANGE_MARKER_BACK) && this.$markerBack.update(o)),
                void this._signal("afterRender", e)
            }
            this.$changes |= e
        }
        ,
        this.$autosize = function() {
            var e = this.session.getScreenLength() * this.lineHeight
              , t = this.$maxLines * this.lineHeight
              , i = Math.min(t, Math.max((this.$minLines || 1) * this.lineHeight, e)) + this.scrollMargin.v + (this.$extraHeight || 0);
            this.$horizScroll && (i += this.scrollBarH.getHeight()),
            this.$maxPixelHeight && i > this.$maxPixelHeight && (i = this.$maxPixelHeight);
            var n, s = !(i <= 2 * this.lineHeight) && t < e;
            i == this.desiredHeight && this.$size.height == this.desiredHeight && s == this.$vScroll || (s != this.$vScroll && (this.$vScroll = s,
            this.scrollBarV.setVisible(s)),
            n = this.container.clientWidth,
            this.container.style.height = i + "px",
            this.$updateCachedSize(!0, this.$gutterWidth, n, i),
            this.desiredHeight = i,
            this._signal("autosize"))
        }
        ,
        this.$computeLayerConfig = function() {
            var e = this.session
              , t = this.$size
              , i = t.height <= 2 * this.lineHeight
              , n = this.session.getScreenLength() * this.lineHeight
              , s = this.$getLongestLine()
              , o = !i && (this.$hScrollBarAlwaysVisible || t.scrollerWidth - s - 2 * this.$padding < 0)
              , r = this.$horizScroll !== o;
            r && (this.$horizScroll = o,
            this.scrollBarH.setVisible(o));
            var a = this.$vScroll;
            this.$maxLines && 1 < this.lineHeight && this.$autosize();
            var l = t.scrollerHeight + this.lineHeight
              , h = !this.$maxLines && this.$scrollPastEnd ? (t.scrollerHeight - this.lineHeight) * this.$scrollPastEnd : 0;
            n += h;
            var c = this.scrollMargin;
            this.session.setScrollTop(Math.max(-c.top, Math.min(this.scrollTop, n - t.scrollerHeight + c.bottom))),
            this.session.setScrollLeft(Math.max(-c.left, Math.min(this.scrollLeft, s + 2 * this.$padding - t.scrollerWidth + c.right)));
            var u = !i && (this.$vScrollBarAlwaysVisible || t.scrollerHeight - n + h < 0 || this.scrollTop > c.top)
              , d = a !== u;
            d && (this.$vScroll = u,
            this.scrollBarV.setVisible(u));
            var g, f, m = this.scrollTop % this.lineHeight, p = Math.ceil(l / this.lineHeight) - 1, w = ($ = Math.max(0, Math.round((this.scrollTop - m) / this.lineHeight))) + p, v = this.lineHeight, $ = e.screenToDocumentRow($, 0), b = e.getFoldLine($);
            b && ($ = b.start.row),
            g = e.documentToScreenRow($, 0),
            f = e.getRowLength($) * v,
            w = Math.min(e.screenToDocumentRow(w, 0), e.getLength() - 1),
            l = t.scrollerHeight + e.getRowLength(w) * v + f,
            m = this.scrollTop - g * v;
            var y = 0;
            return this.layerConfig.width == s && !r || (y = this.CHANGE_H_SCROLL),
            (r || d) && (y |= this.$updateCachedSize(!0, this.gutterWidth, t.width, t.height),
            this._signal("scrollbarVisibilityChanged"),
            d && (s = this.$getLongestLine())),
            this.layerConfig = {
                width: s,
                padding: this.$padding,
                firstRow: $,
                firstRowScreen: g,
                lastRow: w,
                lineHeight: v,
                characterWidth: this.characterWidth,
                minHeight: l,
                maxHeight: n,
                offset: m,
                gutterOffset: v ? Math.max(0, Math.ceil((m + t.height - t.scrollerHeight) / v)) : 0,
                height: this.$size.scrollerHeight
            },
            this.session.$bidiHandler && this.session.$bidiHandler.setContentWidth(s - this.$padding),
            y
        }
        ,
        this.$updateLines = function() {
            if (this.$changedLines) {
                var e = this.$changedLines.firstRow
                  , t = this.$changedLines.lastRow;
                this.$changedLines = null;
                var i = this.layerConfig;
                if (!(e > i.lastRow + 1 || t < i.firstRow))
                    return t === 1 / 0 ? (this.$showGutter && this.$gutterLayer.update(i),
                    void this.$textLayer.update(i)) : (this.$textLayer.updateLines(i, e, t),
                    !0)
            }
        }
        ,
        this.$getLongestLine = function() {
            var e = this.session.getScreenWidth();
            return this.showInvisibles && !this.session.$useWrapMode && (e += 1),
            this.$textLayer && e > this.$textLayer.MAX_LINE_LENGTH && (e = this.$textLayer.MAX_LINE_LENGTH + 30),
            Math.max(this.$size.scrollerWidth - 2 * this.$padding, Math.round(e * this.characterWidth))
        }
        ,
        this.updateFrontMarkers = function() {
            this.$markerFront.setMarkers(this.session.getMarkers(!0)),
            this.$loop.schedule(this.CHANGE_MARKER_FRONT)
        }
        ,
        this.updateBackMarkers = function() {
            this.$markerBack.setMarkers(this.session.getMarkers()),
            this.$loop.schedule(this.CHANGE_MARKER_BACK)
        }
        ,
        this.addGutterDecoration = function(e, t) {
            this.$gutterLayer.addGutterDecoration(e, t)
        }
        ,
        this.removeGutterDecoration = function(e, t) {
            this.$gutterLayer.removeGutterDecoration(e, t)
        }
        ,
        this.updateBreakpoints = function(e) {
            this.$loop.schedule(this.CHANGE_GUTTER)
        }
        ,
        this.setAnnotations = function(e) {
            this.$gutterLayer.setAnnotations(e),
            this.$loop.schedule(this.CHANGE_GUTTER)
        }
        ,
        this.updateCursor = function() {
            this.$loop.schedule(this.CHANGE_CURSOR)
        }
        ,
        this.hideCursor = function() {
            this.$cursorLayer.hideCursor()
        }
        ,
        this.showCursor = function() {
            this.$cursorLayer.showCursor()
        }
        ,
        this.scrollSelectionIntoView = function(e, t, i) {
            this.scrollCursorIntoView(e, i),
            this.scrollCursorIntoView(t, i)
        }
        ,
        this.scrollCursorIntoView = function(e, t, i) {
            var n, s, o, r, a, l, h;
            0 !== this.$size.scrollerHeight && (s = (n = this.$cursorLayer.getPixelPosition(e)).left,
            o = n.top,
            r = i && i.top || 0,
            a = i && i.bottom || 0,
            o < (l = this.$scrollAnimation ? this.session.getScrollTop() : this.scrollTop) + r ? (t && l + r > o + this.lineHeight && (o -= t * this.$size.scrollerHeight),
            0 === o && (o = -this.scrollMargin.top),
            this.session.setScrollTop(o)) : l + this.$size.scrollerHeight - a < o + this.lineHeight && (t && l + this.$size.scrollerHeight - a < o - this.lineHeight && (o += t * this.$size.scrollerHeight),
            this.session.setScrollTop(o + this.lineHeight + a - this.$size.scrollerHeight)),
            s < (h = this.scrollLeft) ? (s < this.$padding + 2 * this.layerConfig.characterWidth && (s = -this.scrollMargin.left),
            this.session.setScrollLeft(s)) : h + this.$size.scrollerWidth < s + this.characterWidth ? this.session.setScrollLeft(Math.round(s + this.characterWidth - this.$size.scrollerWidth)) : h <= this.$padding && s - h < this.characterWidth && this.session.setScrollLeft(0))
        }
        ,
        this.getScrollTop = function() {
            return this.session.getScrollTop()
        }
        ,
        this.getScrollLeft = function() {
            return this.session.getScrollLeft()
        }
        ,
        this.getScrollTopRow = function() {
            return this.scrollTop / this.lineHeight
        }
        ,
        this.getScrollBottomRow = function() {
            return Math.max(0, Math.floor((this.scrollTop + this.$size.scrollerHeight) / this.lineHeight) - 1)
        }
        ,
        this.scrollToRow = function(e) {
            this.session.setScrollTop(e * this.lineHeight)
        }
        ,
        this.alignCursor = function(e, t) {
            "number" == typeof e && (e = {
                row: e,
                column: 0
            });
            var i = this.$cursorLayer.getPixelPosition(e)
              , n = this.$size.scrollerHeight - this.lineHeight
              , s = i.top - n * (t || 0);
            return this.session.setScrollTop(s),
            s
        }
        ,
        this.STEPS = 8,
        this.$calcSteps = function(e, t) {
            for (var i, n, s = 0, o = this.STEPS, r = [], s = 0; s < o; ++s)
                r.push((i = s / this.STEPS,
                (t - (n = e)) * (Math.pow(i - 1, 3) + 1) + n));
            return r
        }
        ,
        this.scrollToLine = function(e, t, i, n) {
            var s = this.$cursorLayer.getPixelPosition({
                row: e,
                column: 0
            }).top;
            t && (s -= this.$size.scrollerHeight / 2);
            var o = this.scrollTop;
            this.session.setScrollTop(s),
            !1 !== i && this.animateScrolling(o, n)
        }
        ,
        this.animateScrolling = function(e, t) {
            var i = this.scrollTop;
            if (this.$animatedScroll) {
                var n = this;
                if (e != i) {
                    if (this.$scrollAnimation) {
                        var s = this.$scrollAnimation.steps;
                        if (s.length && (e = s[0]) == i)
                            return
                    }
                    var o = n.$calcSteps(e, i);
                    this.$scrollAnimation = {
                        from: e,
                        to: i,
                        steps: o
                    },
                    clearInterval(this.$timer),
                    n.session.setScrollTop(o.shift()),
                    n.session.$scrollTop = i,
                    this.$timer = setInterval(function() {
                        if (!n.session)
                            return clearInterval(n.$timer);
                        o.length ? (n.session.setScrollTop(o.shift()),
                        n.session.$scrollTop = i) : null != i ? (n.session.$scrollTop = -1,
                        n.session.setScrollTop(i),
                        i = null) : (n.$timer = clearInterval(n.$timer),
                        n.$scrollAnimation = null,
                        t && t())
                    }, 10)
                }
            }
        }
        ,
        this.scrollToY = function(e) {
            this.scrollTop !== e && (this.$loop.schedule(this.CHANGE_SCROLL),
            this.scrollTop = e)
        }
        ,
        this.scrollToX = function(e) {
            this.scrollLeft !== e && (this.scrollLeft = e),
            this.$loop.schedule(this.CHANGE_H_SCROLL)
        }
        ,
        this.scrollTo = function(e, t) {
            this.session.setScrollTop(t),
            this.session.setScrollLeft(t)
        }
        ,
        this.scrollBy = function(e, t) {
            t && this.session.setScrollTop(this.session.getScrollTop() + t),
            e && this.session.setScrollLeft(this.session.getScrollLeft() + e)
        }
        ,
        this.isScrollableBy = function(e, t) {
            return t < 0 && this.session.getScrollTop() >= 1 - this.scrollMargin.top || (0 < t && this.session.getScrollTop() + this.$size.scrollerHeight - this.layerConfig.maxHeight < -1 + this.scrollMargin.bottom || (e < 0 && this.session.getScrollLeft() >= 1 - this.scrollMargin.left || (0 < e && this.session.getScrollLeft() + this.$size.scrollerWidth - this.layerConfig.width < -1 + this.scrollMargin.right || void 0)))
        }
        ,
        this.pixelToScreenCoordinates = function(e, t) {
            var i, n;
            this.$hasCssTransforms ? (i = {
                top: 0,
                left: 0
            },
            e = (n = this.$fontMetrics.transformCoordinates([e, t]))[1] - this.gutterWidth - this.margin.left,
            t = n[0]) : i = this.scroller.getBoundingClientRect();
            var s = e + this.scrollLeft - i.left - this.$padding
              , o = s / this.characterWidth
              , r = Math.floor((t + this.scrollTop - i.top) / this.lineHeight)
              , a = this.$blockCursor ? Math.floor(o) : Math.round(o);
            return {
                row: r,
                column: a,
                side: 0 < o - a ? 1 : -1,
                offsetX: s
            }
        }
        ,
        this.screenToTextCoordinates = function(e, t) {
            var i, n;
            this.$hasCssTransforms ? (i = {
                top: 0,
                left: 0
            },
            e = (n = this.$fontMetrics.transformCoordinates([e, t]))[1] - this.gutterWidth - this.margin.left,
            t = n[0]) : i = this.scroller.getBoundingClientRect();
            var s = e + this.scrollLeft - i.left - this.$padding
              , o = s / this.characterWidth
              , r = this.$blockCursor ? Math.floor(o) : Math.round(o)
              , a = Math.floor((t + this.scrollTop - i.top) / this.lineHeight);
            return this.session.screenToDocumentPosition(a, Math.max(r, 0), s)
        }
        ,
        this.textToScreenCoordinates = function(e, t) {
            var i = this.scroller.getBoundingClientRect()
              , n = this.session.documentToScreenPosition(e, t)
              , s = this.$padding + (this.session.$bidiHandler.isBidiRow(n.row, e) ? this.session.$bidiHandler.getPosLeft(n.column) : Math.round(n.column * this.characterWidth))
              , o = n.row * this.lineHeight;
            return {
                pageX: i.left + s - this.scrollLeft,
                pageY: i.top + o - this.scrollTop
            }
        }
        ,
        this.visualizeFocus = function() {
            c.addCssClass(this.container, "ace_focus")
        }
        ,
        this.visualizeBlur = function() {
            c.removeCssClass(this.container, "ace_focus")
        }
        ,
        this.showComposition = function(e) {
            (this.$composition = e).cssText || (e.cssText = this.textarea.style.cssText),
            null == e.useTextareaForIME && (e.useTextareaForIME = this.$useTextareaForIME),
            this.$useTextareaForIME ? (c.addCssClass(this.textarea, "ace_composition"),
            this.textarea.style.cssText = "",
            this.$moveTextAreaToCursor(),
            this.$cursorLayer.element.style.display = "none") : e.markerId = this.session.addMarker(e.markerRange, "ace_composition_marker", "text")
        }
        ,
        this.setCompositionText = function(e) {
            var t = this.session.selection.cursor;
            this.addToken(e, "composition_placeholder", t.row, t.column),
            this.$moveTextAreaToCursor()
        }
        ,
        this.hideComposition = function() {
            var e;
            this.$composition && (this.$composition.markerId && this.session.removeMarker(this.$composition.markerId),
            c.removeCssClass(this.textarea, "ace_composition"),
            this.textarea.style.cssText = this.$composition.cssText,
            e = this.session.selection.cursor,
            this.removeExtraToken(e.row, e.column),
            this.$composition = null,
            this.$cursorLayer.element.style.display = "")
        }
        ,
        this.addToken = function(e, t, i, n) {
            var s = this.session;
            s.bgTokenizer.lines[i] = null;
            var o = {
                type: t,
                value: e
            }
              , r = s.getTokens(i);
            if (null == n)
                r.push(o);
            else
                for (var a = 0, l = 0; l < r.length; l++) {
                    var h = r[l];
                    if (n <= (a += h.value.length)) {
                        var c = h.value.length - (a - n)
                          , u = h.value.slice(0, c)
                          , d = h.value.slice(c);
                        r.splice(l, 1, {
                            type: h.type,
                            value: u
                        }, o, {
                            type: h.type,
                            value: d
                        });
                        break
                    }
                }
            this.updateLines(i, i)
        }
        ,
        this.removeExtraToken = function(e, t) {
            this.updateLines(e, e)
        }
        ,
        this.setTheme = function(i, n) {
            function e(e) {
                if (s.$themeId != i)
                    return n && n();
                if (!e || !e.cssClass)
                    throw new Error("couldn't load module " + i + " or it didn't call define");
                e.$id && (s.$themeId = e.$id),
                c.importCssString(e.cssText, e.cssClass, s.container),
                s.theme && c.removeCssClass(s.container, s.theme.cssClass);
                var t = "padding"in e ? e.padding : "padding"in (s.theme || {}) ? 4 : s.$padding;
                s.$padding && t != s.$padding && s.setPadding(t),
                s.$theme = e.cssClass,
                s.theme = e,
                c.addCssClass(s.container, e.cssClass),
                c.setCssClass(s.container, "ace_dark", e.isDark),
                s.$size && (s.$size.width = 0,
                s.$updateSizeAsync()),
                s._dispatchEvent("themeLoaded", {
                    theme: e
                }),
                n && n()
            }
            var t, s = this;
            this.$themeId = i,
            s._dispatchEvent("themeChange", {
                theme: i
            }),
            i && "string" != typeof i ? e(i) : (t = i || this.$options.theme.initialValue,
            o.loadModule(["theme", t], e))
        }
        ,
        this.getTheme = function() {
            return this.$themeId
        }
        ,
        this.setStyle = function(e, t) {
            c.setCssClass(this.container, e, !1 !== t)
        }
        ,
        this.unsetStyle = function(e) {
            c.removeCssClass(this.container, e)
        }
        ,
        this.setCursorStyle = function(e) {
            c.setStyle(this.scroller.style, "cursor", e)
        }
        ,
        this.setMouseCursor = function(e) {
            c.setStyle(this.scroller.style, "cursor", e)
        }
        ,
        this.attachToShadowRoot = function() {
            c.importCssString(m, "ace_editor.css", this.container)
        }
        ,
        this.destroy = function() {
            this.freeze(),
            this.$fontMetrics.destroy(),
            this.$cursorLayer.destroy(),
            this.removeAllListeners(),
            this.container.textContent = ""
        }
    }
    ).call(v.prototype),
    o.defineOptions(v.prototype, "renderer", {
        animatedScroll: {
            initialValue: !1
        },
        showInvisibles: {
            set: function(e) {
                this.$textLayer.setShowInvisibles(e) && this.$loop.schedule(this.CHANGE_TEXT)
            },
            initialValue: !1
        },
        showPrintMargin: {
            set: function() {
                this.$updatePrintMargin()
            },
            initialValue: !0
        },
        printMarginColumn: {
            set: function() {
                this.$updatePrintMargin()
            },
            initialValue: 80
        },
        printMargin: {
            set: function(e) {
                "number" == typeof e && (this.$printMarginColumn = e),
                this.$showPrintMargin = !!e,
                this.$updatePrintMargin()
            },
            get: function() {
                return this.$showPrintMargin && this.$printMarginColumn
            }
        },
        showGutter: {
            set: function(e) {
                this.$gutter.style.display = e ? "block" : "none",
                this.$loop.schedule(this.CHANGE_FULL),
                this.onGutterResize()
            },
            initialValue: !0
        },
        fadeFoldWidgets: {
            set: function(e) {
                c.setCssClass(this.$gutter, "ace_fade-fold-widgets", e)
            },
            initialValue: !1
        },
        showFoldWidgets: {
            set: function(e) {
                this.$gutterLayer.setShowFoldWidgets(e),
                this.$loop.schedule(this.CHANGE_GUTTER)
            },
            initialValue: !0
        },
        displayIndentGuides: {
            set: function(e) {
                this.$textLayer.setDisplayIndentGuides(e) && this.$loop.schedule(this.CHANGE_TEXT)
            },
            initialValue: !0
        },
        highlightGutterLine: {
            set: function(e) {
                this.$gutterLayer.setHighlightGutterLine(e),
                this.$loop.schedule(this.CHANGE_GUTTER)
            },
            initialValue: !0
        },
        hScrollBarAlwaysVisible: {
            set: function(e) {
                this.$hScrollBarAlwaysVisible && this.$horizScroll || this.$loop.schedule(this.CHANGE_SCROLL)
            },
            initialValue: !1
        },
        vScrollBarAlwaysVisible: {
            set: function(e) {
                this.$vScrollBarAlwaysVisible && this.$vScroll || this.$loop.schedule(this.CHANGE_SCROLL)
            },
            initialValue: !1
        },
        fontSize: {
            set: function(e) {
                "number" == typeof e && (e += "px"),
                this.container.style.fontSize = e,
                this.updateFontSize()
            },
            initialValue: 12
        },
        fontFamily: {
            set: function(e) {
                this.container.style.fontFamily = e,
                this.updateFontSize()
            }
        },
        maxLines: {
            set: function(e) {
                this.updateFull()
            }
        },
        minLines: {
            set: function(e) {
                this.$minLines < 562949953421311 || (this.$minLines = 0),
                this.updateFull()
            }
        },
        maxPixelHeight: {
            set: function(e) {
                this.updateFull()
            },
            initialValue: 0
        },
        scrollPastEnd: {
            set: function(e) {
                e = +e || 0,
                this.$scrollPastEnd != e && (this.$scrollPastEnd = e,
                this.$loop.schedule(this.CHANGE_SCROLL))
            },
            initialValue: 0,
            handlesSet: !0
        },
        fixedWidthGutter: {
            set: function(e) {
                this.$gutterLayer.$fixedWidth = !!e,
                this.$loop.schedule(this.CHANGE_GUTTER)
            }
        },
        theme: {
            set: function(e) {
                this.setTheme(e)
            },
            get: function() {
                return this.$themeId || this.theme
            },
            initialValue: "./theme/textmate",
            handlesSet: !0
        },
        hasCssTransforms: {},
        useTextareaForIME: {
            initialValue: !p.isMobile && !p.isIE
        }
    }),
    t.VirtualRenderer = v
}),
define("ace/worker/worker_client", ["require", "exports", "module", "ace/lib/oop", "ace/lib/net", "ace/lib/event_emitter", "ace/config"], function(a, e, t) {
    "use strict";
    function l(e) {
        if ("undefined" == typeof Worker)
            return {
                postMessage: function() {},
                terminate: function() {}
            };
        if (u.get("loadWorkerFromBlob")) {
            var t = function(e) {
                var t = "importScripts('" + n.qualifyURL(e) + "');";
                try {
                    return new Blob([t],{
                        type: "application/javascript"
                    })
                } catch (e) {
                    var i = new (window.BlobBuilder || window.WebKitBlobBuilder || window.MozBlobBuilder);
                    return i.append(t),
                    i.getBlob("application/javascript")
                }
            }(e)
              , i = (window.URL || window.webkitURL).createObjectURL(t);
            return new Worker(i)
        }
        return new Worker(e)
    }
    function h(e) {
        e.postMessage || (e = this.$createWorkerFromOldConfig.apply(this, arguments)),
        this.$worker = e,
        this.$sendDeltaQueue = this.$sendDeltaQueue.bind(this),
        this.changeListener = this.changeListener.bind(this),
        this.onMessage = this.onMessage.bind(this),
        this.callbackId = 1,
        this.callbacks = {},
        this.$worker.onmessage = this.onMessage
    }
    var i = a("../lib/oop")
      , n = a("../lib/net")
      , c = a("../lib/event_emitter").EventEmitter
      , u = a("../config");
    (function() {
        i.implement(this, c),
        this.$createWorkerFromOldConfig = function(e, t, i, n, s) {
            var o, r;
            return a.nameToUrl && !a.toUrl && (a.toUrl = a.nameToUrl),
            u.get("packaged") || !a.toUrl ? n = n || u.moduleUrl(t, "worker") : (o = this.$normalizePath,
            n = n || o(a.toUrl("ace/worker/worker.js", null, "_")),
            r = {},
            e.forEach(function(e) {
                r[e] = o(a.toUrl(e, null, "_").replace(/(\.js)?(\?.*)?$/, ""))
            })),
            this.$worker = l(n),
            s && this.send("importScripts", s),
            this.$worker.postMessage({
                init: !0,
                tlns: r,
                module: t,
                classname: i
            }),
            this.$worker
        }
        ,
        this.onMessage = function(e) {
            var t = e.data;
            switch (t.type) {
            case "event":
                this._signal(t.name, {
                    data: t.data
                });
                break;
            case "call":
                var i = this.callbacks[t.id];
                i && (i(t.data),
                delete this.callbacks[t.id]);
                break;
            case "error":
                this.reportError(t.data);
                break;
            case "log":
                window.console && console.log && console.log.apply(console, t.data)
            }
        }
        ,
        this.reportError = function(e) {
            window.console && console.error && console.error(e)
        }
        ,
        this.$normalizePath = function(e) {
            return n.qualifyURL(e)
        }
        ,
        this.terminate = function() {
            this._signal("terminate", {}),
            this.deltaQueue = null,
            this.$worker.terminate(),
            this.$worker = null,
            this.$doc && this.$doc.off("change", this.changeListener),
            this.$doc = null
        }
        ,
        this.send = function(e, t) {
            this.$worker.postMessage({
                command: e,
                args: t
            })
        }
        ,
        this.call = function(e, t, i) {
            var n;
            i && (n = this.callbackId++,
            this.callbacks[n] = i,
            t.push(n)),
            this.send(e, t)
        }
        ,
        this.emit = function(e, t) {
            try {
                t.data && t.data.err && (t.data.err = {
                    message: t.data.err.message,
                    stack: t.data.err.stack,
                    code: t.data.err.code
                }),
                this.$worker.postMessage({
                    event: e,
                    data: {
                        data: t.data
                    }
                })
            } catch (e) {
                console.error(e.stack)
            }
        }
        ,
        this.attachToDocument = function(e) {
            this.$doc && this.terminate(),
            this.$doc = e,
            this.call("setValue", [e.getValue()]),
            e.on("change", this.changeListener)
        }
        ,
        this.changeListener = function(e) {
            this.deltaQueue || (this.deltaQueue = [],
            setTimeout(this.$sendDeltaQueue, 0)),
            "insert" == e.action ? this.deltaQueue.push(e.start, e.lines) : this.deltaQueue.push(e.start, e.end)
        }
        ,
        this.$sendDeltaQueue = function() {
            var e = this.deltaQueue;
            e && (this.deltaQueue = null,
            50 < e.length && e.length > this.$doc.getLength() >> 1 ? this.call("setValue", [this.$doc.getValue()]) : this.emit("change", {
                data: e
            }))
        }
    }
    ).call(h.prototype);
    e.UIWorkerClient = function(e, t, i) {
        var n = null
          , s = !1
          , o = Object.create(c)
          , r = []
          , a = new h({
            messageBuffer: r,
            terminate: function() {},
            postMessage: function(e) {
                r.push(e),
                n && (s ? setTimeout(l) : l())
            }
        });
        a.setEmitSync = function(e) {
            s = e
        }
        ;
        var l = function() {
            var e = r.shift();
            e.command ? n[e.command].apply(n, e.args) : e.event && o._signal(e.event, e.data)
        };
        return o.postMessage = function(e) {
            a.onMessage({
                data: e
            })
        }
        ,
        o.callback = function(e, t) {
            this.postMessage({
                type: "call",
                id: t,
                data: e
            })
        }
        ,
        o.emit = function(e, t) {
            this.postMessage({
                type: "event",
                name: e,
                data: t
            })
        }
        ,
        u.loadModule(["worker", t], function(e) {
            for (n = new e[i](o); r.length; )
                l()
        }),
        a
    }
    ,
    e.WorkerClient = h,
    e.createWorker = l
}),
define("ace/placeholder", ["require", "exports", "module", "ace/range", "ace/lib/event_emitter", "ace/lib/oop"], function(e, t, i) {
    "use strict";
    function n(e, t, i, n, s, o) {
        var r = this;
        this.length = t,
        this.session = e,
        this.doc = e.getDocument(),
        this.mainClass = s,
        this.othersClass = o,
        this.$onUpdate = this.onUpdate.bind(this),
        this.doc.on("change", this.$onUpdate),
        this.$others = n,
        this.$onCursorChange = function() {
            setTimeout(function() {
                r.onCursorChange()
            })
        }
        ,
        this.$pos = i;
        var a = e.getUndoManager().$undoStack || e.getUndoManager().$undostack || {
            length: -1
        };
        this.$undoStackDepth = a.length,
        this.setup(),
        e.selection.on("changeCursor", this.$onCursorChange)
    }
    var l = e("./range").Range
      , s = e("./lib/event_emitter").EventEmitter
      , o = e("./lib/oop");
    (function() {
        o.implement(this, s),
        this.setup = function() {
            var i = this
              , n = this.doc
              , e = this.session;
            this.selectionBefore = e.selection.toJSON(),
            e.selection.inMultiSelectMode && e.selection.toSingleRange(),
            this.pos = n.createAnchor(this.$pos.row, this.$pos.column);
            var t = this.pos;
            t.$insertRight = !0,
            t.detach(),
            t.markerId = e.addMarker(new l(t.row,t.column,t.row,t.column + this.length), this.mainClass, null, !1),
            this.others = [],
            this.$others.forEach(function(e) {
                var t = n.createAnchor(e.row, e.column);
                t.$insertRight = !0,
                t.detach(),
                i.others.push(t)
            }),
            e.setUndoSelect(!1)
        }
        ,
        this.showOtherMarkers = function() {
            var t, i;
            this.othersActive || (t = this.session,
            (i = this).othersActive = !0,
            this.others.forEach(function(e) {
                e.markerId = t.addMarker(new l(e.row,e.column,e.row,e.column + i.length), i.othersClass, null, !1)
            }))
        }
        ,
        this.hideOtherMarkers = function() {
            if (this.othersActive) {
                this.othersActive = !1;
                for (var e = 0; e < this.others.length; e++)
                    this.session.removeMarker(this.others[e].markerId)
            }
        }
        ,
        this.onUpdate = function(e) {
            if (this.$updating)
                return this.updateAnchors(e);
            var t = e;
            if (t.start.row === t.end.row && t.start.row === this.pos.row) {
                this.$updating = !0;
                var i = "insert" === e.action ? t.end.column - t.start.column : t.start.column - t.end.column
                  , n = t.start.column >= this.pos.column && t.start.column <= this.pos.column + this.length + 1
                  , s = t.start.column - this.pos.column;
                if (this.updateAnchors(e),
                n && (this.length += i),
                n && !this.session.$fromUndo)
                    if ("insert" === e.action)
                        for (var o = this.others.length - 1; 0 <= o; o--) {
                            var r = {
                                row: (a = this.others[o]).row,
                                column: a.column + s
                            };
                            this.doc.insertMergedLines(r, e.lines)
                        }
                    else if ("remove" === e.action)
                        for (o = this.others.length - 1; 0 <= o; o--) {
                            var a, r = {
                                row: (a = this.others[o]).row,
                                column: a.column + s
                            };
                            this.doc.remove(new l(r.row,r.column,r.row,r.column - i))
                        }
                this.$updating = !1,
                this.updateMarkers()
            }
        }
        ,
        this.updateAnchors = function(e) {
            this.pos.onChange(e);
            for (var t = this.others.length; t--; )
                this.others[t].onChange(e);
            this.updateMarkers()
        }
        ,
        this.updateMarkers = function() {
            if (!this.$updating) {
                var i = this
                  , n = this.session
                  , e = function(e, t) {
                    n.removeMarker(e.markerId),
                    e.markerId = n.addMarker(new l(e.row,e.column,e.row,e.column + i.length), t, null, !1)
                };
                e(this.pos, this.mainClass);
                for (var t = this.others.length; t--; )
                    e(this.others[t], this.othersClass)
            }
        }
        ,
        this.onCursorChange = function(e) {
            var t;
            !this.$updating && this.session && ((t = this.session.selection.getCursor()).row === this.pos.row && t.column >= this.pos.column && t.column <= this.pos.column + this.length ? (this.showOtherMarkers(),
            this._emit("cursorEnter", e)) : (this.hideOtherMarkers(),
            this._emit("cursorLeave", e)))
        }
        ,
        this.detach = function() {
            this.session.removeMarker(this.pos && this.pos.markerId),
            this.hideOtherMarkers(),
            this.doc.off("change", this.$onUpdate),
            this.session.selection.off("changeCursor", this.$onCursorChange),
            this.session.setUndoSelect(!0),
            this.session = null
        }
        ,
        this.cancel = function() {
            if (-1 !== this.$undoStackDepth) {
                for (var e = this.session.getUndoManager(), t = (e.$undoStack || e.$undostack).length - this.$undoStackDepth, i = 0; i < t; i++)
                    e.undo(this.session, !0);
                this.selectionBefore && this.session.selection.fromJSON(this.selectionBefore)
            }
        }
    }
    ).call(n.prototype),
    t.PlaceHolder = n
}),
define("ace/mouse/multi_select_handler", ["require", "exports", "module", "ace/lib/event", "ace/lib/useragent"], function(e, t, i) {
    function A(e, t) {
        return e.row == t.row && e.column == t.column
    }
    var L = e("../lib/event")
      , R = e("../lib/useragent");
    t.onMouseDown = function(e) {
        var t = e.domEvent
          , i = t.altKey
          , n = t.shiftKey
          , s = t.ctrlKey
          , o = e.getAccelKey()
          , r = e.getButton();
        if (s && R.isMac && (r = t.button),
        e.editor.inMultiSelectMode && 2 == r)
            e.editor.textInput.onContextMenu(e.domEvent);
        else if (s || i || o) {
            if (0 === r) {
                var a, l, h = e.editor, c = h.selection, u = h.inMultiSelectMode, d = e.getDocumentPosition(), g = c.getCursor(), f = e.inSelection() || c.isEmpty() && A(d, g), m = e.x, p = e.y, w = h.session, v = h.renderer.pixelToScreenCoordinates(m, p), $ = v;
                if (h.$mouseHandler.$enableJumpToDef)
                    s && i || o && i ? a = n ? "block" : "add" : i && h.$blockSelectEnabled && (a = "block");
                else if (o && !i) {
                    if (a = "add",
                    !u && n)
                        return
                } else
                    i && h.$blockSelectEnabled && (a = "block");
                if (a && R.isMac && t.ctrlKey && h.$mouseHandler.cancelContextMenu(),
                "add" == a) {
                    if (!u && f)
                        return;
                    u || (l = c.toOrientedRange(),
                    h.addSelectionMarker(l));
                    var b = c.rangeList.rangeAtPoint(d);
                    h.inVirtualSelectionMode = !0,
                    n && (b = null,
                    l = c.ranges[0] || l,
                    h.removeSelectionMarker(l)),
                    h.once("mouseup", function() {
                        var e = c.toOrientedRange();
                        b && e.isEmpty() && A(b.cursor, e.cursor) ? c.substractPoint(e.cursor) : (n ? c.substractPoint(l.cursor) : l && (h.removeSelectionMarker(l),
                        c.addRange(l)),
                        c.addRange(e)),
                        h.inVirtualSelectionMode = !1
                    })
                } else if ("block" == a) {
                    e.stop(),
                    h.inVirtualSelectionMode = !0;
                    function y() {
                        var e = h.renderer.pixelToScreenCoordinates(m, p)
                          , t = w.screenToDocumentPosition(e.row, e.column, e.offsetX);
                        A($, e) && A(t, c.lead) || ($ = e,
                        h.selection.moveToPosition(t),
                        h.renderer.scrollCursorIntoView(),
                        h.removeSelectionMarkers(S),
                        S = c.rectangularRangeBlock($, v),
                        h.$mouseHandler.$clickSelection && 1 == S.length && S[0].isEmpty() && (S[0] = h.$mouseHandler.$clickSelection.clone()),
                        S.forEach(h.addSelectionMarker, h),
                        h.updateSelectionMarkers())
                    }
                    var C, S = [];
                    u && !o ? c.toSingleRange() : !u && o && (C = c.toOrientedRange(),
                    h.addSelectionMarker(C)),
                    n ? v = w.documentToScreenPosition(c.lead) : c.moveToPosition(d),
                    $ = {
                        row: -1,
                        column: -1
                    };
                    var x = y;
                    L.capture(h.container, function(e) {
                        m = e.clientX,
                        p = e.clientY
                    }, function(e) {
                        y(),
                        clearInterval(k),
                        h.removeSelectionMarkers(S),
                        S.length || (S = [c.toOrientedRange()]),
                        C && (h.removeSelectionMarker(C),
                        c.toSingleRange(C));
                        for (var t = 0; t < S.length; t++)
                            c.addRange(S[t]);
                        h.inVirtualSelectionMode = !1,
                        h.$mouseHandler.$clickSelection = null
                    });
                    var k = setInterval(function() {
                        x()
                    }, 20);
                    return e.preventDefault()
                }
            }
        } else
            0 === r && e.editor.inMultiSelectMode && e.editor.exitMultiSelectMode()
    }
}),
define("ace/commands/multi_select_commands", ["require", "exports", "module", "ace/keyboard/hash_handler"], function(e, t, i) {
    t.defaultCommands = [{
        name: "addCursorAbove",
        description: "Add cursor above",
        exec: function(e) {
            e.selectMoreLines(-1)
        },
        bindKey: {
            win: "Ctrl-Alt-Up",
            mac: "Ctrl-Alt-Up"
        },
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "addCursorBelow",
        description: "Add cursor below",
        exec: function(e) {
            e.selectMoreLines(1)
        },
        bindKey: {
            win: "Ctrl-Alt-Down",
            mac: "Ctrl-Alt-Down"
        },
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "addCursorAboveSkipCurrent",
        description: "Add cursor above (skip current)",
        exec: function(e) {
            e.selectMoreLines(-1, !0)
        },
        bindKey: {
            win: "Ctrl-Alt-Shift-Up",
            mac: "Ctrl-Alt-Shift-Up"
        },
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "addCursorBelowSkipCurrent",
        description: "Add cursor below (skip current)",
        exec: function(e) {
            e.selectMoreLines(1, !0)
        },
        bindKey: {
            win: "Ctrl-Alt-Shift-Down",
            mac: "Ctrl-Alt-Shift-Down"
        },
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "selectMoreBefore",
        description: "Select more before",
        exec: function(e) {
            e.selectMore(-1)
        },
        bindKey: {
            win: "Ctrl-Alt-Left",
            mac: "Ctrl-Alt-Left"
        },
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "selectMoreAfter",
        description: "Select more after",
        exec: function(e) {
            e.selectMore(1)
        },
        bindKey: {
            win: "Ctrl-Alt-Right",
            mac: "Ctrl-Alt-Right"
        },
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "selectNextBefore",
        description: "Select next before",
        exec: function(e) {
            e.selectMore(-1, !0)
        },
        bindKey: {
            win: "Ctrl-Alt-Shift-Left",
            mac: "Ctrl-Alt-Shift-Left"
        },
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "selectNextAfter",
        description: "Select next after",
        exec: function(e) {
            e.selectMore(1, !0)
        },
        bindKey: {
            win: "Ctrl-Alt-Shift-Right",
            mac: "Ctrl-Alt-Shift-Right"
        },
        scrollIntoView: "cursor",
        readOnly: !0
    }, {
        name: "toggleSplitSelectionIntoLines",
        description: "Split into lines",
        exec: function(e) {
            1 < e.multiSelect.rangeCount ? e.multiSelect.joinSelections() : e.multiSelect.splitIntoLines()
        },
        bindKey: {
            win: "Ctrl-Alt-L",
            mac: "Ctrl-Alt-L"
        },
        readOnly: !0
    }, {
        name: "splitSelectionIntoLines",
        description: "Split into lines",
        exec: function(e) {
            e.multiSelect.splitIntoLines()
        },
        readOnly: !0
    }, {
        name: "alignCursors",
        description: "Align cursors",
        exec: function(e) {
            e.alignCursors()
        },
        bindKey: {
            win: "Ctrl-Alt-A",
            mac: "Ctrl-Alt-A"
        },
        scrollIntoView: "cursor"
    }, {
        name: "findAll",
        description: "Find all",
        exec: function(e) {
            e.findAll()
        },
        bindKey: {
            win: "Ctrl-Alt-K",
            mac: "Ctrl-Alt-G"
        },
        scrollIntoView: "cursor",
        readOnly: !0
    }],
    t.multiSelectCommands = [{
        name: "singleSelection",
        description: "Single selection",
        bindKey: "esc",
        exec: function(e) {
            e.exitMultiSelectMode()
        },
        scrollIntoView: "cursor",
        readOnly: !0,
        isAvailable: function(e) {
            return e && e.inMultiSelectMode
        }
    }];
    var n = e("../keyboard/hash_handler").HashHandler;
    t.keyboardHandler = new n(t.multiSelectCommands)
}),
define("ace/multi_select", ["require", "exports", "module", "ace/range_list", "ace/range", "ace/selection", "ace/mouse/multi_select_handler", "ace/lib/event", "ace/lib/lang", "ace/commands/multi_select_commands", "ace/search", "ace/edit_session", "ace/editor", "ace/config"], function(e, t, i) {
    function n(e) {
        e.$multiselectOnSessionChange || (e.$onAddRange = e.$onAddRange.bind(e),
        e.$onRemoveRange = e.$onRemoveRange.bind(e),
        e.$onMultiSelect = e.$onMultiSelect.bind(e),
        e.$onSingleSelect = e.$onSingleSelect.bind(e),
        e.$multiselectOnSessionChange = t.onSessionChange.bind(e),
        e.$checkMultiselectChange = e.$checkMultiselectChange.bind(e),
        e.$multiselectOnSessionChange(e),
        e.on("changeSession", e.$multiselectOnSessionChange),
        e.on("mousedown", o),
        e.commands.addCommands(a.defaultCommands),
        function(i) {
            function n(e) {
                s && (i.renderer.setMouseCursor(""),
                s = !1)
            }
            if (!i.textInput)
                return;
            var e = i.textInput.getElement()
              , s = !1;
            r.addListener(e, "keydown", function(e) {
                var t = 18 == e.keyCode && !(e.ctrlKey || e.shiftKey || e.metaKey);
                i.$blockSelectEnabled && t ? s || (i.renderer.setMouseCursor("crosshair"),
                s = !0) : s && n()
            }, i),
            r.addListener(e, "keyup", n, i),
            r.addListener(e, "blur", n, i)
        }(e))
    }
    var s = e("./range_list").RangeList
      , b = e("./range").Range
      , m = e("./selection").Selection
      , o = e("./mouse/multi_select_handler").onMouseDown
      , r = e("./lib/event")
      , p = e("./lib/lang")
      , a = e("./commands/multi_select_commands");
    t.commands = a.defaultCommands.concat(a.multiSelectCommands);
    var c = new (e("./search").Search)
      , l = e("./edit_session").EditSession;
    (function() {
        this.getSelectionMarkers = function() {
            return this.$selectionMarkers
        }
    }
    ).call(l.prototype),
    function() {
        this.ranges = null,
        this.rangeList = null,
        this.addRange = function(e, t) {
            if (e) {
                if (!this.inMultiSelectMode && 0 === this.rangeCount) {
                    var i = this.toOrientedRange();
                    if (this.rangeList.add(i),
                    this.rangeList.add(e),
                    2 != this.rangeList.ranges.length)
                        return this.rangeList.removeAll(),
                        t || this.fromOrientedRange(e);
                    this.rangeList.removeAll(),
                    this.rangeList.add(i),
                    this.$onAddRange(i)
                }
                e.cursor || (e.cursor = e.end);
                var n = this.rangeList.add(e);
                return this.$onAddRange(e),
                n.length && this.$onRemoveRange(n),
                1 < this.rangeCount && !this.inMultiSelectMode && (this._signal("multiSelect"),
                this.inMultiSelectMode = !0,
                this.session.$undoSelect = !1,
                this.rangeList.attach(this.session)),
                t || this.fromOrientedRange(e)
            }
        }
        ,
        this.toSingleRange = function(e) {
            e = e || this.ranges[0];
            var t = this.rangeList.removeAll();
            t.length && this.$onRemoveRange(t),
            e && this.fromOrientedRange(e)
        }
        ,
        this.substractPoint = function(e) {
            var t = this.rangeList.substractPoint(e);
            if (t)
                return this.$onRemoveRange(t),
                t[0]
        }
        ,
        this.mergeOverlappingRanges = function() {
            var e = this.rangeList.merge();
            e.length && this.$onRemoveRange(e)
        }
        ,
        this.$onAddRange = function(e) {
            this.rangeCount = this.rangeList.ranges.length,
            this.ranges.unshift(e),
            this._signal("addRange", {
                range: e
            })
        }
        ,
        this.$onRemoveRange = function(e) {
            var t;
            this.rangeCount = this.rangeList.ranges.length,
            1 == this.rangeCount && this.inMultiSelectMode && (t = this.rangeList.ranges.pop(),
            e.push(t),
            this.rangeCount = 0);
            for (var i = e.length; i--; ) {
                var n = this.ranges.indexOf(e[i]);
                this.ranges.splice(n, 1)
            }
            this._signal("removeRange", {
                ranges: e
            }),
            0 === this.rangeCount && this.inMultiSelectMode && (this.inMultiSelectMode = !1,
            this._signal("singleSelect"),
            this.session.$undoSelect = !0,
            this.rangeList.detach(this.session)),
            (t = t || this.ranges[0]) && !t.isEqual(this.getRange()) && this.fromOrientedRange(t)
        }
        ,
        this.$initRangeList = function() {
            this.rangeList || (this.rangeList = new s,
            this.ranges = [],
            this.rangeCount = 0)
        }
        ,
        this.getAllRanges = function() {
            return this.rangeCount ? this.rangeList.ranges.concat() : [this.getRange()]
        }
        ,
        this.splitIntoLines = function() {
            for (var e = this.ranges.length ? this.ranges : [this.getRange()], t = [], i = 0; i < e.length; i++) {
                var n = e[i]
                  , s = n.start.row
                  , o = n.end.row;
                if (s === o)
                    t.push(n.clone());
                else {
                    for (t.push(new b(s,n.start.column,s,this.session.getLine(s).length)); ++s < o; )
                        t.push(this.getLineRange(s, !0));
                    t.push(new b(o,0,o,n.end.column))
                }
                0 != i || this.isBackwards() || (t = t.reverse())
            }
            this.toSingleRange();
            for (i = t.length; i--; )
                this.addRange(t[i])
        }
        ,
        this.joinSelections = function() {
            var e = this.rangeList.ranges
              , t = e[e.length - 1]
              , i = b.fromPoints(e[0].start, t.end);
            this.toSingleRange(),
            this.setSelectionRange(i, t.cursor == t.start)
        }
        ,
        this.toggleBlockSelection = function() {
            var e, t, i, n, s;
            1 < this.rangeCount ? (t = (e = this.rangeList.ranges)[e.length - 1],
            i = b.fromPoints(e[0].start, t.end),
            this.toSingleRange(),
            this.setSelectionRange(i, t.cursor == t.start)) : (n = this.session.documentToScreenPosition(this.cursor),
            s = this.session.documentToScreenPosition(this.anchor),
            this.rectangularRangeBlock(n, s).forEach(this.addRange, this))
        }
        ,
        this.rectangularRangeBlock = function(e, t, i) {
            var n, s, o, r, a = [], l = e.column < t.column;
            r = l ? (n = e.column,
            s = t.column,
            o = e.offsetX,
            t.offsetX) : (n = t.column,
            s = e.column,
            o = t.offsetX,
            e.offsetX);
            var h, c, u, d = e.row < t.row;
            c = d ? (h = e.row,
            t.row) : (h = t.row,
            e.row),
            n < 0 && (n = 0),
            h < 0 && (h = 0),
            h == c && (i = !0);
            for (var g, f, m = h; m <= c; m++) {
                var p = b.fromPoints(this.session.screenToDocumentPosition(m, n, o), this.session.screenToDocumentPosition(m, s, r));
                if (p.isEmpty()) {
                    if (u && (g = p.end,
                    f = u,
                    g.row == f.row && g.column == f.column))
                        break;
                    u = p.end
                }
                p.cursor = l ? p.start : p.end,
                a.push(p)
            }
            if (d && a.reverse(),
            !i) {
                for (var w = a.length - 1; a[w].isEmpty() && 0 < w; )
                    w--;
                if (0 < w)
                    for (var v = 0; a[v].isEmpty(); )
                        v++;
                for (var $ = w; v <= $; $--)
                    a[$].isEmpty() && a.splice($, 1)
            }
            return a
        }
    }
    .call(m.prototype);
    var h = e("./editor").Editor;
    (function() {
        this.updateSelectionMarkers = function() {
            this.renderer.updateCursor(),
            this.renderer.updateBackMarkers()
        }
        ,
        this.addSelectionMarker = function(e) {
            e.cursor || (e.cursor = e.end);
            var t = this.getSelectionStyle();
            return e.marker = this.session.addMarker(e, "ace_selection", t),
            this.session.$selectionMarkers.push(e),
            this.session.selectionMarkerCount = this.session.$selectionMarkers.length,
            e
        }
        ,
        this.removeSelectionMarker = function(e) {
            var t;
            e.marker && (this.session.removeMarker(e.marker),
            -1 != (t = this.session.$selectionMarkers.indexOf(e)) && this.session.$selectionMarkers.splice(t, 1),
            this.session.selectionMarkerCount = this.session.$selectionMarkers.length)
        }
        ,
        this.removeSelectionMarkers = function(e) {
            for (var t = this.session.$selectionMarkers, i = e.length; i--; ) {
                var n, s = e[i];
                s.marker && (this.session.removeMarker(s.marker),
                -1 != (n = t.indexOf(s)) && t.splice(n, 1))
            }
            this.session.selectionMarkerCount = t.length
        }
        ,
        this.$onAddRange = function(e) {
            this.addSelectionMarker(e.range),
            this.renderer.updateCursor(),
            this.renderer.updateBackMarkers()
        }
        ,
        this.$onRemoveRange = function(e) {
            this.removeSelectionMarkers(e.ranges),
            this.renderer.updateCursor(),
            this.renderer.updateBackMarkers()
        }
        ,
        this.$onMultiSelect = function(e) {
            this.inMultiSelectMode || (this.inMultiSelectMode = !0,
            this.setStyle("ace_multiselect"),
            this.keyBinding.addKeyboardHandler(a.keyboardHandler),
            this.commands.setDefaultHandler("exec", this.$onMultiSelectExec),
            this.renderer.updateCursor(),
            this.renderer.updateBackMarkers())
        }
        ,
        this.$onSingleSelect = function(e) {
            this.session.multiSelect.inVirtualMode || (this.inMultiSelectMode = !1,
            this.unsetStyle("ace_multiselect"),
            this.keyBinding.removeKeyboardHandler(a.keyboardHandler),
            this.commands.removeDefaultHandler("exec", this.$onMultiSelectExec),
            this.renderer.updateCursor(),
            this.renderer.updateBackMarkers(),
            this._emit("changeSelection"))
        }
        ,
        this.$onMultiSelectExec = function(e) {
            var t, i = e.command, n = e.editor;
            if (n.multiSelect)
                return i.multiSelectAction ? t = "forEach" == i.multiSelectAction ? n.forEachSelection(i, e.args) : "forEachLine" == i.multiSelectAction ? n.forEachSelection(i, e.args, !0) : "single" == i.multiSelectAction ? (n.exitMultiSelectMode(),
                i.exec(n, e.args || {})) : i.multiSelectAction(n, e.args || {}) : (t = i.exec(n, e.args || {}),
                n.multiSelect.addRange(n.multiSelect.toOrientedRange()),
                n.multiSelect.mergeOverlappingRanges()),
                t
        }
        ,
        this.forEachSelection = function(e, t, i) {
            if (!this.inVirtualSelectionMode) {
                var n, s = i && i.keepOrder, o = 1 == i || i && i.$byLines, r = this.session, a = this.selection, l = a.rangeList, h = (s ? a : l).ranges;
                if (!h.length)
                    return e.exec ? e.exec(this, t || {}) : e(this, t || {});
                var c = a._eventRegistry;
                a._eventRegistry = {};
                var u = new m(r);
                this.inVirtualSelectionMode = !0;
                for (var d = h.length; d--; ) {
                    if (o)
                        for (; 0 < d && h[d].start.row == h[d - 1].end.row; )
                            d--;
                    u.fromOrientedRange(h[d]),
                    u.index = d,
                    this.selection = r.selection = u;
                    var g = e.exec ? e.exec(this, t || {}) : e(this, t || {});
                    n || void 0 === g || (n = g),
                    u.toOrientedRange(h[d])
                }
                u.detach(),
                this.selection = r.selection = a,
                this.inVirtualSelectionMode = !1,
                a._eventRegistry = c,
                a.mergeOverlappingRanges(),
                a.ranges[0] && a.fromOrientedRange(a.ranges[0]);
                var f = this.renderer.$scrollAnimation;
                return this.onCursorChange(),
                this.onSelectionChange(),
                f && f.from == f.to && this.renderer.animateScrolling(f.from),
                n
            }
        }
        ,
        this.exitMultiSelectMode = function() {
            this.inMultiSelectMode && !this.inVirtualSelectionMode && this.multiSelect.toSingleRange()
        }
        ,
        this.getSelectedText = function() {
            var e = "";
            if (this.inMultiSelectMode && !this.inVirtualSelectionMode) {
                for (var t = this.multiSelect.rangeList.ranges, i = [], n = 0; n < t.length; n++)
                    i.push(this.session.getTextRange(t[n]));
                var s = this.session.getDocument().getNewLineCharacter();
                (e = i.join(s)).length == (i.length - 1) * s.length && (e = "")
            } else
                this.selection.isEmpty() || (e = this.session.getTextRange(this.getSelectionRange()));
            return e
        }
        ,
        this.$checkMultiselectChange = function(e, t) {
            if (this.inMultiSelectMode && !this.inVirtualSelectionMode) {
                var i = this.multiSelect.ranges[0];
                if (this.multiSelect.isEmpty() && t == this.multiSelect.anchor)
                    return;
                var n = t == this.multiSelect.anchor ? i.cursor == i.start ? i.end : i.start : i.cursor;
                n.row != t.row || this.session.$clipPositionToDocument(n.row, n.column).column != t.column ? this.multiSelect.toSingleRange(this.multiSelect.toOrientedRange()) : this.multiSelect.mergeOverlappingRanges()
            }
        }
        ,
        this.findAll = function(e, t, i) {
            var n;
            (t = t || {}).needle = e || t.needle,
            null == t.needle && (n = this.selection.isEmpty() ? this.selection.getWordRange() : this.selection.getRange(),
            t.needle = this.session.getTextRange(n)),
            this.$search.set(t);
            var s = this.$search.findAll(this.session);
            if (!s.length)
                return 0;
            var o = this.multiSelect;
            i || o.toSingleRange(s[0]);
            for (var r = s.length; r--; )
                o.addRange(s[r], !0);
            return n && o.rangeList.rangeAtPoint(n.start) && o.addRange(n, !0),
            s.length
        }
        ,
        this.selectMoreLines = function(e, t) {
            var i = this.selection.toOrientedRange()
              , n = i.cursor == i.end
              , s = this.session.documentToScreenPosition(i.cursor);
            this.selection.$desiredColumn && (s.column = this.selection.$desiredColumn);
            var o, r, a, l, h = this.session.screenToDocumentPosition(s.row + e, s.column);
            r = i.isEmpty() ? h : (o = this.session.documentToScreenPosition(n ? i.end : i.start),
            this.session.screenToDocumentPosition(o.row + e, o.column)),
            n ? (a = b.fromPoints(h, r)).cursor = a.start : (a = b.fromPoints(r, h)).cursor = a.end,
            a.desiredColumn = s.column,
            this.selection.inMultiSelectMode ? t && (l = i.cursor) : this.selection.addRange(i),
            this.selection.addRange(a),
            l && this.selection.substractPoint(l)
        }
        ,
        this.transposeSelections = function(e) {
            for (var t = this.session, i = t.multiSelect, n = i.ranges, s = n.length; s--; ) {
                (r = n[s]).isEmpty() && (a = t.getWordRange(r.start.row, r.start.column),
                r.start.row = a.start.row,
                r.start.column = a.start.column,
                r.end.row = a.end.row,
                r.end.column = a.end.column)
            }
            i.mergeOverlappingRanges();
            for (var o = [], s = n.length; s--; ) {
                var r = n[s];
                o.unshift(t.getTextRange(r))
            }
            e < 0 ? o.unshift(o.pop()) : o.push(o.shift());
            for (s = n.length; s--; ) {
                var a = (r = n[s]).clone();
                t.replace(r, o[s]),
                r.start.row = a.start.row,
                r.start.column = a.start.column
            }
            i.fromOrientedRange(i.ranges[0])
        }
        ,
        this.selectMore = function(e, t, i) {
            var n, s, o, r, a, l = this.session, h = l.multiSelect.toOrientedRange();
            h.isEmpty() && ((h = l.getWordRange(h.start.row, h.start.column)).cursor = -1 == e ? h.start : h.end,
            this.multiSelect.addRange(h),
            i) || (n = l.getTextRange(h),
            o = l,
            r = n,
            a = e,
            c.$options.wrap = !0,
            c.$options.needle = r,
            c.$options.backwards = -1 == a,
            (s = c.find(o)) && (s.cursor = -1 == e ? s.start : s.end,
            this.session.unfold(s),
            this.multiSelect.addRange(s),
            this.renderer.scrollCursorIntoView(null, .5)),
            t && this.multiSelect.substractPoint(h.cursor))
        }
        ,
        this.alignCursors = function() {
            var o = this.session
              , t = o.multiSelect
              , e = t.ranges
              , i = -1
              , n = e.filter(function(e) {
                if (e.cursor.row == i)
                    return !0;
                i = e.cursor.row
            });
            if (e.length && n.length != e.length - 1) {
                n.forEach(function(e) {
                    t.substractPoint(e.cursor)
                });
                var r = 0
                  , a = 1 / 0
                  , l = e.map(function(e) {
                    var t = e.cursor
                      , i = o.getLine(t.row).substr(t.column).search(/\S/g);
                    return -1 == i && (i = 0),
                    t.column > r && (r = t.column),
                    i < a && (a = i),
                    i
                });
                e.forEach(function(e, t) {
                    var i = e.cursor
                      , n = r - i.column
                      , s = l[t] - a;
                    s < n ? o.insert(i, p.stringRepeat(" ", n - s)) : o.remove(new b(i.row,i.column,i.row,i.column - n + s)),
                    e.start.column = e.end.column = r,
                    e.start.row = e.end.row = i.row,
                    e.cursor = e.end
                }),
                t.fromOrientedRange(e[0]),
                this.renderer.updateCursor(),
                this.renderer.updateBackMarkers()
            } else {
                var s = this.selection.getRange()
                  , h = s.start.row
                  , c = s.end.row
                  , u = h == c;
                if (u) {
                    for (var d, g = this.session.getLength(); d = this.session.getLine(c),
                    /[=:]/.test(d) && ++c < g; )
                        ;
                    for (; d = this.session.getLine(h),
                    /[=:]/.test(d) && 0 < --h; )
                        ;
                    h < 0 && (h = 0),
                    g <= c && (c = g - 1)
                }
                var f = this.session.removeFullLines(h, c)
                  , f = this.$reAlignText(f, u);
                this.session.insert({
                    row: h,
                    column: 0
                }, f.join("\n") + "\n"),
                u || (s.start.column = 0,
                s.end.column = f[f.length - 1].length),
                this.selection.setRange(s)
            }
        }
        ,
        this.$reAlignText = function(e, t) {
            function i(e) {
                return p.stringRepeat(" ", e)
            }
            function n(e) {
                return e[2] ? i(s) + e[2] + i(o - e[2].length + r) + e[4].replace(/^([=:])\s+/, "$1 ") : e[0]
            }
            var s, o, r, a = !0, l = !0;
            return e.map(function(e) {
                var t = e.match(/(\s*)(.*?)(\s*)([=:].*)/);
                return t ? (null == s ? (s = t[1].length,
                o = t[2].length,
                r = t[3].length) : (s + o + r != t[1].length + t[2].length + t[3].length && (l = !1),
                s != t[1].length && (a = !1),
                s > t[1].length && (s = t[1].length),
                o < t[2].length && (o = t[2].length),
                r > t[3].length && (r = t[3].length)),
                t) : [e]
            }).map(t ? n : a ? l ? function(e) {
                return e[2] ? i(s + o - e[2].length) + e[2] + i(r) + e[4].replace(/^([=:])\s+/, "$1 ") : e[0]
            }
            : n : function(e) {
                return e[2] ? i(s) + e[2] + i(r) + e[4].replace(/^([=:])\s+/, "$1 ") : e[0]
            }
            )
        }
    }
    ).call(h.prototype),
    t.onSessionChange = function(e) {
        var t = e.session;
        t && !t.multiSelect && (t.$selectionMarkers = [],
        t.selection.$initRangeList(),
        t.multiSelect = t.selection),
        this.multiSelect = t && t.multiSelect;
        var i = e.oldSession;
        i && (i.multiSelect.off("addRange", this.$onAddRange),
        i.multiSelect.off("removeRange", this.$onRemoveRange),
        i.multiSelect.off("multiSelect", this.$onMultiSelect),
        i.multiSelect.off("singleSelect", this.$onSingleSelect),
        i.multiSelect.lead.off("change", this.$checkMultiselectChange),
        i.multiSelect.anchor.off("change", this.$checkMultiselectChange)),
        t && (t.multiSelect.on("addRange", this.$onAddRange),
        t.multiSelect.on("removeRange", this.$onRemoveRange),
        t.multiSelect.on("multiSelect", this.$onMultiSelect),
        t.multiSelect.on("singleSelect", this.$onSingleSelect),
        t.multiSelect.lead.on("change", this.$checkMultiselectChange),
        t.multiSelect.anchor.on("change", this.$checkMultiselectChange)),
        t && this.inMultiSelectMode != t.selection.inMultiSelectMode && (t.selection.inMultiSelectMode ? this.$onMultiSelect() : this.$onSingleSelect())
    }
    ,
    t.MultiSelect = n,
    e("./config").defineOptions(h.prototype, "editor", {
        enableMultiselect: {
            set: function(e) {
                n(this),
                e ? (this.on("changeSession", this.$multiselectOnSessionChange),
                this.on("mousedown", o)) : (this.off("changeSession", this.$multiselectOnSessionChange),
                this.off("mousedown", o))
            },
            value: !0
        },
        enableBlockSelect: {
            set: function(e) {
                this.$blockSelectEnabled = e
            },
            value: !0
        }
    })
}),
define("ace/mode/folding/fold_mode", ["require", "exports", "module", "ace/range"], function(e, t, i) {
    "use strict";
    var g = e("../../range").Range
      , n = t.FoldMode = function() {}
    ;
    (function() {
        this.foldingStartMarker = null,
        this.foldingStopMarker = null,
        this.getFoldWidget = function(e, t, i) {
            var n = e.getLine(i);
            return this.foldingStartMarker.test(n) ? "start" : "markbeginend" == t && this.foldingStopMarker && this.foldingStopMarker.test(n) ? "end" : ""
        }
        ,
        this.getFoldWidgetRange = function(e, t, i) {
            return null
        }
        ,
        this.indentationBlock = function(e, t, i) {
            var n = /\S/
              , s = e.getLine(t)
              , o = s.search(n);
            if (-1 != o) {
                for (var r = i || s.length, a = e.getLength(), l = t, h = t; ++t < a; ) {
                    var c = e.getLine(t).search(n);
                    if (-1 != c) {
                        if (c <= o) {
                            var u = e.getTokenAt(t, 0);
                            if (!u || "string" !== u.type)
                                break
                        }
                        h = t
                    }
                }
                if (l < h) {
                    var d = e.getLine(h).length;
                    return new g(l,r,h,d)
                }
            }
        }
        ,
        this.openingBracketBlock = function(e, t, i, n, s) {
            var o = {
                row: i,
                column: n + 1
            }
              , r = e.$findClosingBracket(t, o, s);
            if (r) {
                var a = e.foldWidgets[r.row];
                return null == a && (a = e.getFoldWidget(r.row)),
                "start" == a && r.row > o.row && (r.row--,
                r.column = e.getLine(r.row).length),
                g.fromPoints(o, r)
            }
        }
        ,
        this.closingBracketBlock = function(e, t, i, n, s) {
            var o = {
                row: i,
                column: n
            }
              , r = e.$findOpeningBracket(t, o);
            if (r)
                return r.column++,
                o.column--,
                g.fromPoints(r, o)
        }
    }
    ).call(n.prototype)
}),
define("ace/theme/textmate", ["require", "exports", "module", "ace/lib/dom"], function(e, t, i) {
    "use strict";
    t.isDark = !1,
    t.cssClass = "ace-tm",
    t.cssText = '.ace-tm .ace_gutter {background: #f0f0f0;color: #333;}.ace-tm .ace_print-margin {width: 1px;background: #e8e8e8;}.ace-tm .ace_fold {background-color: #6B72E6;}.ace-tm {background-color: #FFFFFF;color: black;}.ace-tm .ace_cursor {color: black;}.ace-tm .ace_invisible {color: rgb(191, 191, 191);}.ace-tm .ace_storage,.ace-tm .ace_keyword {color: blue;}.ace-tm .ace_constant {color: rgb(197, 6, 11);}.ace-tm .ace_constant.ace_buildin {color: rgb(88, 72, 246);}.ace-tm .ace_constant.ace_language {color: rgb(88, 92, 246);}.ace-tm .ace_constant.ace_library {color: rgb(6, 150, 14);}.ace-tm .ace_invalid {background-color: rgba(255, 0, 0, 0.1);color: red;}.ace-tm .ace_support.ace_function {color: rgb(60, 76, 114);}.ace-tm .ace_support.ace_constant {color: rgb(6, 150, 14);}.ace-tm .ace_support.ace_type,.ace-tm .ace_support.ace_class {color: rgb(109, 121, 222);}.ace-tm .ace_keyword.ace_operator {color: rgb(104, 118, 135);}.ace-tm .ace_string {color: rgb(3, 106, 7);}.ace-tm .ace_comment {color: rgb(76, 136, 107);}.ace-tm .ace_comment.ace_doc {color: rgb(0, 102, 255);}.ace-tm .ace_comment.ace_doc.ace_tag {color: rgb(128, 159, 191);}.ace-tm .ace_constant.ace_numeric {color: rgb(0, 0, 205);}.ace-tm .ace_variable {color: rgb(49, 132, 149);}.ace-tm .ace_xml-pe {color: rgb(104, 104, 91);}.ace-tm .ace_entity.ace_name.ace_function {color: #0000A2;}.ace-tm .ace_heading {color: rgb(12, 7, 255);}.ace-tm .ace_list {color:rgb(185, 6, 144);}.ace-tm .ace_meta.ace_tag {color:rgb(0, 22, 142);}.ace-tm .ace_string.ace_regex {color: rgb(255, 0, 0)}.ace-tm .ace_marker-layer .ace_selection {background: rgb(181, 213, 255);}.ace-tm.ace_multiselect .ace_selection.ace_start {box-shadow: 0 0 3px 0px white;}.ace-tm .ace_marker-layer .ace_step {background: rgb(252, 255, 0);}.ace-tm .ace_marker-layer .ace_stack {background: rgb(164, 229, 101);}.ace-tm .ace_marker-layer .ace_bracket {margin: -1px 0 0 -1px;border: 1px solid rgb(192, 192, 192);}.ace-tm .ace_marker-layer .ace_active-line {background: rgba(0, 0, 0, 0.07);}.ace-tm .ace_gutter-active-line {background-color : #dcdcdc;}.ace-tm .ace_marker-layer .ace_selected-word {background: rgb(250, 250, 255);border: 1px solid rgb(200, 200, 250);}.ace-tm .ace_indent-guide {background: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAACCAYAAACZgbYnAAAAE0lEQVQImWP4////f4bLly//BwAmVgd1/w11/gAAAABJRU5ErkJggg==") right repeat-y;}',
    t.$id = "ace/theme/textmate",
    e("../lib/dom").importCssString(t.cssText, t.cssClass)
}),
define("ace/line_widgets", ["require", "exports", "module", "ace/lib/dom"], function(e, t, i) {
    "use strict";
    function n(e) {
        this.session = e,
        (this.session.widgetManager = this).session.getRowLength = this.getRowLength,
        this.session.$getWidgetScreenLength = this.$getWidgetScreenLength,
        this.updateOnChange = this.updateOnChange.bind(this),
        this.renderWidgets = this.renderWidgets.bind(this),
        this.measureWidgets = this.measureWidgets.bind(this),
        this.session._changedWidgets = [],
        this.$onChangeEditor = this.$onChangeEditor.bind(this),
        this.session.on("change", this.updateOnChange),
        this.session.on("changeFold", this.updateOnFold),
        this.session.on("changeEditor", this.$onChangeEditor)
    }
    var s = e("./lib/dom");
    (function() {
        this.getRowLength = function(e) {
            var t = this.lineWidgets && this.lineWidgets[e] && this.lineWidgets[e].rowCount || 0;
            return this.$useWrapMode && this.$wrapData[e] ? this.$wrapData[e].length + 1 + t : 1 + t
        }
        ,
        this.$getWidgetScreenLength = function() {
            var t = 0;
            return this.lineWidgets.forEach(function(e) {
                e && e.rowCount && !e.hidden && (t += e.rowCount)
            }),
            t
        }
        ,
        this.$onChangeEditor = function(e) {
            this.attach(e.editor)
        }
        ,
        this.attach = function(e) {
            e && e.widgetManager && e.widgetManager != this && e.widgetManager.detach(),
            this.editor != e && (this.detach(),
            (this.editor = e) && (e.widgetManager = this,
            e.renderer.on("beforeRender", this.measureWidgets),
            e.renderer.on("afterRender", this.renderWidgets)))
        }
        ,
        this.detach = function(e) {
            var t, i = this.editor;
            i && (this.editor = null,
            i.widgetManager = null,
            i.renderer.off("beforeRender", this.measureWidgets),
            i.renderer.off("afterRender", this.renderWidgets),
            (t = this.session.lineWidgets) && t.forEach(function(e) {
                e && e.el && e.el.parentNode && (e._inDocument = !1,
                e.el.parentNode.removeChild(e.el))
            }))
        }
        ,
        this.updateOnFold = function(e, t) {
            var i = t.lineWidgets;
            if (i && e.action) {
                for (var n = e.data, s = n.start.row, o = n.end.row, r = "add" == e.action, a = s + 1; a < o; a++)
                    i[a] && (i[a].hidden = r);
                i[o] && (r ? i[s] ? i[o].hidden = r : i[s] = i[o] : (i[s] == i[o] && (i[s] = void 0),
                i[o].hidden = r))
            }
        }
        ,
        this.updateOnChange = function(e) {
            var t, i, n, s, o = this.session.lineWidgets;
            o && (t = e.start.row,
            0 != (i = e.end.row - t) && ("remove" == e.action ? (n = o.splice(t + 1, i),
            !o[t] && n[n.length - 1] && (o[t] = n.pop()),
            n.forEach(function(e) {
                e && this.removeLineWidget(e)
            }, this)) : (s = new Array(i),
            o[t] && null != o[t].column && e.start.column > o[t].column && t++,
            s.unshift(t, 0),
            o.splice.apply(o, s)),
            this.$updateRows()))
        }
        ,
        this.$updateRows = function() {
            var i, e = this.session.lineWidgets;
            e && (i = !0,
            e.forEach(function(e, t) {
                if (e)
                    for (i = !1,
                    e.row = t; e.$oldWidget; )
                        e.$oldWidget.row = t,
                        e = e.$oldWidget
            }),
            i && (this.session.lineWidgets = null))
        }
        ,
        this.$registerLineWidget = function(e) {
            this.session.lineWidgets || (this.session.lineWidgets = new Array(this.session.getLength()));
            var t = this.session.lineWidgets[e.row];
            return t && ((e.$oldWidget = t).el && t.el.parentNode && (t.el.parentNode.removeChild(t.el),
            t._inDocument = !1)),
            this.session.lineWidgets[e.row] = e
        }
        ,
        this.addLineWidget = function(e) {
            if (this.$registerLineWidget(e),
            e.session = this.session,
            !this.editor)
                return e;
            var t = this.editor.renderer;
            e.html && !e.el && (e.el = s.createElement("div"),
            e.el.innerHTML = e.html),
            e.el && (s.addCssClass(e.el, "ace_lineWidgetContainer"),
            e.el.style.position = "absolute",
            e.el.style.zIndex = 5,
            t.container.appendChild(e.el),
            e._inDocument = !0,
            e.coverGutter || (e.el.style.zIndex = 3),
            null == e.pixelHeight && (e.pixelHeight = e.el.offsetHeight)),
            null == e.rowCount && (e.rowCount = e.pixelHeight / t.layerConfig.lineHeight);
            var i, n = this.session.getFoldAt(e.row, 0);
            return (e.$fold = n) && (i = this.session.lineWidgets,
            e.row != n.end.row || i[n.start.row] ? e.hidden = !0 : i[n.start.row] = e),
            this.session._emit("changeFold", {
                data: {
                    start: {
                        row: e.row
                    }
                }
            }),
            this.$updateRows(),
            this.renderWidgets(null, t),
            this.onWidgetChanged(e),
            e
        }
        ,
        this.removeLineWidget = function(e) {
            if (e._inDocument = !1,
            e.session = null,
            e.el && e.el.parentNode && e.el.parentNode.removeChild(e.el),
            e.editor && e.editor.destroy)
                try {
                    e.editor.destroy()
                } catch (e) {}
            if (this.session.lineWidgets) {
                var t = this.session.lineWidgets[e.row];
                if (t == e)
                    this.session.lineWidgets[e.row] = e.$oldWidget,
                    e.$oldWidget && this.onWidgetChanged(e.$oldWidget);
                else
                    for (; t; ) {
                        if (t.$oldWidget == e) {
                            t.$oldWidget = e.$oldWidget;
                            break
                        }
                        t = t.$oldWidget
                    }
            }
            this.session._emit("changeFold", {
                data: {
                    start: {
                        row: e.row
                    }
                }
            }),
            this.$updateRows()
        }
        ,
        this.getWidgetsAtRow = function(e) {
            for (var t = this.session.lineWidgets, i = t && t[e], n = []; i; )
                n.push(i),
                i = i.$oldWidget;
            return n
        }
        ,
        this.onWidgetChanged = function(e) {
            this.session._changedWidgets.push(e),
            this.editor && this.editor.renderer.updateFull()
        }
        ,
        this.measureWidgets = function(e, t) {
            var i = this.session._changedWidgets
              , n = t.layerConfig;
            if (i && i.length) {
                for (var s = 1 / 0, o = 0; o < i.length; o++) {
                    var r = i[o];
                    if (r && r.el && r.session == this.session) {
                        if (!r._inDocument) {
                            if (this.session.lineWidgets[r.row] != r)
                                continue;
                            r._inDocument = !0,
                            t.container.appendChild(r.el)
                        }
                        r.h = r.el.offsetHeight,
                        r.fixedWidth || (r.w = r.el.offsetWidth,
                        r.screenWidth = Math.ceil(r.w / n.characterWidth));
                        var a = r.h / n.lineHeight;
                        r.coverLine && ((a -= this.session.getRowLineCount(r.row)) < 0 && (a = 0)),
                        r.rowCount != a && (r.rowCount = a,
                        r.row < s && (s = r.row))
                    }
                }
                s != 1 / 0 && (this.session._emit("changeFold", {
                    data: {
                        start: {
                            row: s
                        }
                    }
                }),
                this.session.lineWidgetWidth = null),
                this.session._changedWidgets = []
            }
        }
        ,
        this.renderWidgets = function(e, t) {
            var i = t.layerConfig
              , n = this.session.lineWidgets;
            if (n) {
                for (var s = Math.min(this.firstRow, i.firstRow), o = Math.max(this.lastRow, i.lastRow, n.length); 0 < s && !n[s]; )
                    s--;
                this.firstRow = i.firstRow,
                this.lastRow = i.lastRow,
                t.$cursorLayer.config = i;
                for (var r = s; r <= o; r++) {
                    var a, l, h = n[r];
                    h && h.el && (h.hidden ? h.el.style.top = -100 - (h.pixelHeight || 0) + "px" : (h._inDocument || (h._inDocument = !0,
                    t.container.appendChild(h.el)),
                    a = t.$cursorLayer.getPixelPosition({
                        row: r,
                        column: 0
                    }, !0).top,
                    h.coverLine || (a += i.lineHeight * this.session.getRowLineCount(h.row)),
                    h.el.style.top = a - i.offset + "px",
                    l = h.coverGutter ? 0 : t.gutterWidth,
                    h.fixedWidth || (l -= t.scrollLeft),
                    h.el.style.left = l + "px",
                    h.fullWidth && h.screenWidth && (h.el.style.minWidth = i.width + 2 * i.padding + "px"),
                    h.fixedWidth ? h.el.style.right = t.scrollBar.getWidth() + "px" : h.el.style.right = ""))
                }
            }
        }
    }
    ).call(n.prototype),
    t.LineWidgets = n
}),
define("ace/ext/error_marker", ["require", "exports", "module", "ace/line_widgets", "ace/lib/dom", "ace/range"], function(e, t, i) {
    "use strict";
    function f(e, t, i) {
        var n = e.getAnnotations().sort(a.comparePoints);
        if (n.length) {
            var s = function(e, t, i) {
                for (var n = 0, s = e.length - 1; n <= s; ) {
                    var o = n + s >> 1
                      , r = i(t, e[o]);
                    if (0 < r)
                        n = 1 + o;
                    else {
                        if (!(r < 0))
                            return o;
                        s = o - 1
                    }
                }
                return -(n + 1)
            }(n, {
                row: t,
                column: -1
            }, a.comparePoints);
            s < 0 && (s = -s - 1),
            s >= n.length ? s = 0 < i ? 0 : n.length - 1 : 0 === s && i < 0 && (s = n.length - 1);
            var o = n[s];
            if (o && i) {
                if (o.row === t) {
                    for (; (o = n[s += i]) && o.row === t; )
                        ;
                    if (!o)
                        return n.slice()
                }
                var r = [];
                for (t = o.row; r[i < 0 ? "unshift" : "push"](o),
                (o = n[s += i]) && o.row == t; )
                    ;
                return r.length && r
            }
        }
    }
    var m = e("../line_widgets").LineWidgets
      , p = e("../lib/dom")
      , a = e("../range").Range;
    t.showErrorMarker = function(e, t) {
        var i = e.session;
        i.widgetManager || (i.widgetManager = new m(i),
        i.widgetManager.attach(e));
        var n = e.getCursorPosition()
          , s = n.row
          , o = i.widgetManager.getWidgetsAtRow(s).filter(function(e) {
            return "errorMarker" == e.type
        })[0];
        o ? o.destroy() : s -= t;
        var r, a = f(i, s, t);
        if (a) {
            var l = a[0];
            n.column = (l.pos && "number" != typeof l.column ? l.pos.sc : l.column) || 0,
            n.row = l.row,
            r = e.renderer.$gutterLayer.$annotations[n.row]
        } else {
            if (o)
                return;
            r = {
                text: ["Looks good!"],
                className: "ace_ok"
            }
        }
        e.session.unfold(n.row),
        e.selection.moveToPosition(n);
        var h = {
            row: n.row,
            fixedWidth: !0,
            coverGutter: !0,
            el: p.createElement("div"),
            type: "errorMarker"
        }
          , c = h.el.appendChild(p.createElement("div"))
          , u = h.el.appendChild(p.createElement("div"));
        u.className = "error_widget_arrow " + r.className;
        var d = e.renderer.$cursorLayer.getPixelPosition(n).left;
        u.style.left = d + e.renderer.gutterWidth - 5 + "px",
        h.el.className = "error_widget_wrapper",
        c.className = "error_widget " + r.className,
        c.innerHTML = r.text.join("<br>"),
        c.appendChild(p.createElement("div"));
        function g(e, t, i) {
            if (0 === t && ("esc" === i || "return" === i))
                return h.destroy(),
                {
                    command: "null"
                }
        }
        h.destroy = function() {
            e.$mouseHandler.isMousePressed || (e.keyBinding.removeKeyboardHandler(g),
            i.widgetManager.removeLineWidget(h),
            e.off("changeSelection", h.destroy),
            e.off("changeSession", h.destroy),
            e.off("mouseup", h.destroy),
            e.off("change", h.destroy))
        }
        ,
        e.keyBinding.addKeyboardHandler(g),
        e.on("changeSelection", h.destroy),
        e.on("changeSession", h.destroy),
        e.on("mouseup", h.destroy),
        e.on("change", h.destroy),
        e.session.widgetManager.addLineWidget(h),
        h.el.onmousedown = e.focus.bind(e),
        e.renderer.scrollCursorIntoView(null, .5, {
            bottom: h.el.offsetHeight
        })
    }
    ,
    p.importCssString("    .error_widget_wrapper {        background: inherit;        color: inherit;        border:none    }    .error_widget {        border-top: solid 2px;        border-bottom: solid 2px;        margin: 5px 0;        padding: 10px 40px;        white-space: pre-wrap;    }    .error_widget.ace_error, .error_widget_arrow.ace_error{        border-color: #ff5a5a    }    .error_widget.ace_warning, .error_widget_arrow.ace_warning{        border-color: #F1D817    }    .error_widget.ace_info, .error_widget_arrow.ace_info{        border-color: #5a5a5a    }    .error_widget.ace_ok, .error_widget_arrow.ace_ok{        border-color: #5aaa5a    }    .error_widget_arrow {        position: absolute;        border: solid 5px;        border-top-color: transparent!important;        border-right-color: transparent!important;        border-left-color: transparent!important;        top: -5px;    }", "")
}),
define("ace/ace", ["require", "exports", "module", "ace/lib/fixoldbrowsers", "ace/lib/dom", "ace/lib/event", "ace/range", "ace/editor", "ace/edit_session", "ace/undomanager", "ace/virtual_renderer", "ace/worker/worker_client", "ace/keyboard/hash_handler", "ace/placeholder", "ace/multi_select", "ace/mode/folding/fold_mode", "ace/theme/textmate", "ace/ext/error_marker", "ace/config"], function(e, l, t) {
    "use strict";
    e("./lib/fixoldbrowsers");
    var h = e("./lib/dom")
      , c = e("./lib/event")
      , i = e("./range").Range
      , u = e("./editor").Editor
      , n = e("./edit_session").EditSession
      , s = e("./undomanager").UndoManager
      , d = e("./virtual_renderer").VirtualRenderer;
    e("./worker/worker_client"),
    e("./keyboard/hash_handler"),
    e("./placeholder"),
    e("./multi_select"),
    e("./mode/folding/fold_mode"),
    e("./theme/textmate"),
    e("./ext/error_marker"),
    l.config = e("./config"),
    l.require = e,
    "function" == typeof define && (l.define = define),
    l.edit = function(e, t) {
        if ("string" == typeof e) {
            var i = e;
            if (!(e = document.getElementById(i)))
                throw new Error("ace.edit can't find div #" + i)
        }
        if (e && e.env && e.env.editor instanceof u)
            return e.env.editor;
        var n, s = "";
        e && /input|textarea/i.test(e.tagName) ? (s = (n = e).value,
        e = h.createElement("pre"),
        n.parentNode.replaceChild(e, n)) : e && (s = e.textContent,
        e.innerHTML = "");
        var o = l.createEditSession(s)
          , r = new u(new d(e),o,t)
          , a = {
            document: o,
            editor: r,
            onResize: r.resize.bind(r, null)
        };
        return n && (a.textarea = n),
        c.addListener(window, "resize", a.onResize),
        r.on("destroy", function() {
            c.removeListener(window, "resize", a.onResize),
            a.editor.container.env = null
        }),
        r.container.env = r.env = a,
        r
    }
    ,
    l.createEditSession = function(e, t) {
        var i = new n(e,t);
        return i.setUndoManager(new s),
        i
    }
    ,
    l.Range = i,
    l.Editor = u,
    l.EditSession = n,
    l.UndoManager = s,
    l.VirtualRenderer = d,
    l.version = l.config.version
}),
window.require(["ace/ace"], function(e) {
    for (var t in e && (e.config.init(!0),
    e.define = window.define),
    window.ace || (window.ace = e),
    e)
        e.hasOwnProperty(t) && (window.ace[t] = e[t]);
    window.ace.default = window.ace,
    "object" == typeof module && "object" == typeof exports && module && (module.exports = window.ace)
});
