from collections import deque
import re
import os
import errno


class ChapterMaster:
    def __init__(self, fpath: str):
        self.__filename = fpath
        self.__path = os.path.dirname(os.path.abspath(fpath))
        self.keywords = "^\s*[第地](\d+)章.+$"
        self.__navPointTemplate = """
    <navPoint id="navPoint-{0}" playOrder="{0}">
        <navLabel>
            <text>{1}</text>
        </navLabel>
        <content src="Text/{2}.xhtml"/>
    </navPoint>
        """

        self.__xhtmlTemplate = """
 <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>{0}</title>
</head>
<body>
<pre>
{1}
</pre>
</body>
</html>
        """

    def generateTOC(self, chapter: str, title: str) -> (str, str):
        """
        generate toc based on the template
        :param chapter:
        :param title:
        :return:
        """
        c = chapter.zfill(5)
        filename = str.format("Section{0}", c)
        return filename, str.format(self.__navPointTemplate, c, title.rstrip(), filename)

    def parse(self) -> list:
        """
        parse the file with some pre-defined keywords.
        :rtype: deque
        """
        print("parse file name " + self.__filename)
        lst = list()
        regex = re.compile(self.keywords, re.IGNORECASE)
        try:
            with(open(self.__filename, 'r', encoding="utf-8")) as f:
                cnt = 1
                while True:
                    line = f.readline()
                    if not line:
                        break
                    if regex.match(line):
                        search = regex.search(line)
                        print(str.format("行数:{0}, 章节序号:{1}, 名称:{2}", cnt, search.group(1), line))
                        lst.append((cnt, search.group(1), line))
                    cnt += 1
        except Exception as e:
            print(str(e))
        finally:
            print("end process")
            f.close()
        return lst

    def preparseTextDirectory(self, path: str):
        try:
            os.makedirs(path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    def split(self, it: list):
        textpath = os.path.join(self.__path, "Text")
        self.preparseTextDirectory(textpath)
        toc = ''
        cnt = 1
        for i in range(0, len(it) - 1):
            chapter = it[i]
            nxt = it[i + 1]
            t = self.generateTOC(chapter[1], chapter[2])
            toc += t[1]
            content = self.getChapterContent(chapter[0] - 1, nxt[0] - 1, chapter[2])
            fn = os.path.join(self.__path, "Text\\" + t[0] + ".xhtml")
            print(str.format("{0}: 处理{1}", cnt, fn))
            with(open(fn, "w", encoding='utf-8')) as f:
                f.write(content)
            cnt += 1

        tocfn = os.path.join(self.__path, "toc.txt")
        with(open(tocfn, "w", encoding="utf-8")) as f:
            f.write(toc)

    def getChapterContent(self, line1: int, line2: int, title) -> str:
        with(open(self.__filename, 'r', encoding='utf-8')) as f:
            return str.format(self.__xhtmlTemplate, title, "".join(f.readlines()[line1:line2]))

    @staticmethod
    def checking(result):
        """
        auto check the result after parsed the novel.
        :param result: the parsed result
        :return:
        """
        iterator = iter(result)
        for chapter in iterator:
            nxt = next(iterator, None)
            if not nxt:
                break
            c = int(chapter[1])
            n = int(nxt[1])
            if n != c + 1:
                print(str.format("没有找到章节 {0} , 应该在 {1} 行以后", c + 1, chapter[0]))


if __name__ == "__main__":
    file = "C:\\Downloads\\老衲要还俗.txt"
    cm = ChapterMaster(file)
    res = cm.parse()
    print(str.format("{0} results was extracted.", len(res)))
    cm.checking(res)
    cm.split(res)
