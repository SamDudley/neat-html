all_tags: set[str] = {
    "html",
    "base",
    "head",
    "link",
    "meta",
    "style",
    "title",
    "body",
    "address",
    "article",
    "aside",
    "footer",
    "header",
    "h1",
    "h2",
    "h3",
    "h4",
    "h5",
    "h6",
    "hgroup",
    "main",
    "nav",
    "section",
    "blockquote",
    "dd",
    "div",
    "dl",
    "dt",
    "figcaption",
    "figure",
    "hr",
    "li",
    "menu",
    "ol",
    "p",
    "pre",
    "ul",
    "a",
    "abbr",
    "b",
    "bdi",
    "bdo",
    "br",
    "cite",
    "code",
    "data",
    "dfn",
    "em",
    "i",
    "kbd",
    "mark",
    "q",
    "rp",
    "rt",
    "ruby",
    "s",
    "samp",
    "small",
    "span",
    "strong",
    "sub",
    "sup",
    "time",
    "u",
    "var",
    "wbr",
    "area",
    "audio",
    "img",
    "map",
    "track",
    "video",
    "embed",
    "iframe",
    "object",
    "picture",
    "portal",
    "source",
    "svg",
    "canvas",
    "noscript",
    "script",
    "del",
    "ins",
    "caption",
    "col",
    "colgroup",
    "table",
    "tbody",
    "td",
    "tfoot",
    "th",
    "thead",
    "tr",
    "button",
    "datalist",
    "fieldset",
    "form",
    "input",
    "label",
    "legend",
    "meter",
    "optgroup",
    "option",
    "output",
    "progress",
    "select",
    "textarea",
    "details",
    "dialog",
    "summary",
    "slot",
    "template",
    "acronym",
    "big",
    "center",
    "dir",
    "font",
    "frame",
    "frameset",
    "image",
    "marquee",
    "menuitem",
    "nobr",
    "noembed",
    "noframes",
    "param",
    "plaintext",
    "rb",
    "rtc",
    "strike",
    "tt",
    "xmp",
}

self_closing_tags: set[str] = {
    "area",
    "base",
    "br",
    "col",
    "command",
    "embed",
    "hr",
    "img",
    "input",
    "keygen",
    "link",
    "menuitem",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}

# FIXME: Add the rest of the block tags.
block_tags: set[str] = {
    "html",
    "head",
    "body",
    "meta",
    "div",
    "p",
    "main",
    "form",
}

# FIXME: Add the rest of the inline tags.
inline_tags: set[str] = {
    "a",
    "abbr",
    "acronym",
    "b",
    "bdo",
    "big",
    "br",
    "button",
    "cite",
    "code",
    "dfn",
    "em",
    "i",
    "img",
    "input",
    "kbd",
    "label",
    "map",
    "object",
    "q",
    "samp",
    "script",
    "select",
    "small",
    "span",
    "strong",
    "sub",
    "sup",
    "textarea",
    "time",
    "tt",
    "var",
}
