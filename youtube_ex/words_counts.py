from collections import defaultdict

from pytube import YouTube, StreamQuery, CaptionQuery, Caption
from xml.etree import ElementTree


# FIX
# https://stackoverflow.com/questions/68780808/xml-to-srt-conversion-not-working-after-installing-pytube/74618309#74618309
# srt = caption.xml_caption_to_srt(xml_captions)
def get_yt_caption(yt: YouTube):
    caption: Caption = None
    for c in yt.captions:
        caption = yt.captions[c.code]
        break

    return caption


def get_counted_words(caption: Caption):
    xml_captions = caption.xml_captions

    root = ElementTree.fromstring(xml_captions)
    body = list(root.findall('body'))[0]

    lines = []
    for p in body.findall("p"):
        text = " ".join(p.itertext())
        if text != "\n":
            lines.append(text)

    words = [w for l in lines for w in l.split(" ")]
    sorted_words = defaultdict(int)
    for w in words:
        sorted_words[w.lower()] += 1

    counted_words = [(w, count) for w, count in sorted_words.items()]
    counted_words.sort(key=lambda t: t[1], reverse=True)
    return counted_words


def get_yt_counted_worlds(url: str):
    yt = YouTube(url)
    caption = get_yt_caption(yt)
    if caption:
        return get_counted_words(caption)


if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=sP5agpp4tJ4' # DUD
    counted_words = get_yt_counted_worlds(url)

    print("counted_words count: ", len(counted_words))

    for w, c in counted_words:
        print(f"{c} {w}")
        if c < 5:
            break
