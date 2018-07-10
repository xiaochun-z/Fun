import re
import os
import errno


class ChapterMaster:
    def __init__(self, fpath: str):
        self.__filename = fpath
        self.__path = os.path.dirname(os.path.abspath(fpath))
        # 章节的正则表达式，多数小说是“第1002章 咒怨”这类格式，如果小说不是这样的格式，同时实现多种正则表达式
        self.keywords = [r"^\s*[第地](\d+)章.+$", r"\s*[第地]([一两二三四五六七八九十百千万零\d]+)章.*$"]

        self.__navPointTemplate = """
    <navPoint id="navPoint-{0}" playOrder="{0}">
        <navLabel>
            <text>{1}</text>
        </navLabel>
        <content src="Text/{2}.xhtml"/>
    </navPoint>
        """

        self.__xhtmlTemplate = """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8"/>
<title>{0}</title>
</head>
<body>
{1}
</body>
</html>
        """

    def generateTOC(self, chapter: str, title: str) -> (str, str):
        """
        generate toc based on the template
        :param chapter: the chapter count
        :param title: the chapter title
        :return: filename + navPoint
        """
        c = chapter.zfill(5)
        filename = str.format("Section{0}", c)
        return filename, str.format(self.__navPointTemplate, c, title.rstrip(), filename)

    def parse(self) -> list:
        """
        parse the file with some pre-defined keywords.
        :rtype: list
        """
        print("parse file name " + self.__filename)
        lst = list()
        regexps = [re.compile(keyword, re.UNICODE) for keyword in self.keywords]
        try:
            with(open(self.__filename, 'r', encoding="utf-8")) as f:
                # 原本的小说的行数（第1行，第2行）
                cnt: int = 1
                # 章节数（第5章，第6章之类的）
                chaptercnt: int = 0
                while True:
                    line = f.readline()
                    if not line:
                        break
                    for regex in regexps:
                        if regex.match(line):
                            search = regex.search(line)

                            if len(lst) > 0:
                                # 太短的章节忽略掉
                                predicative = lst[-1][0]
                                if cnt > predicative + 10:
                                    chaptercnt += 1
                                    self.appendtolist(chaptercnt, cnt, line, lst, search)
                            else:
                                chaptercnt += 1
                                self.appendtolist(chaptercnt, cnt, line, lst, search)
                            break
                    cnt += 1
        except Exception as e:
            print(str(e))
        finally:
            print("end process")
        return lst

    def appendtolist(self, chaptercnt, cnt, line, lst, search):
        lst.append((cnt, chaptercnt, search.group(1), line))
        print(str.format("行数:{0}, 计算序号:{1}, 书中章节序号:{2}, 章节名称:{3}", cnt, chaptercnt,
                         search.group(1), line))

    @staticmethod
    def prepareTextDirectory(path: str):
        """
        create the directory if this directory does not exist
        :param path:
        :return:
        """
        try:
            os.makedirs(path)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    def split(self, it: list):
        """
        split the novel into different chapters.
        :param it: a list of chapters
        :return:
        """
        textpath = os.path.join(self.__path, "Text")
        self.prepareTextDirectory(textpath)
        toc = ''
        cnt = 1
        for i in range(0, len(it)):
            chapter = it[i]
            line2 = -1
            if i < len(it) - 1:
                nxt = it[i + 1]
                line2 = nxt[0] - 1
            chapternum = str(chapter[1])
            chaptertitle = chapter[3]

            t = self.generateTOC(chapternum, chaptertitle)
            toc += t[1]
            content = self.getChapterContent(chapter[0] - 1, line2, chapter[2])
            fn = os.path.join(self.__path, "Text\\" + t[0] + ".xhtml")
            print(str.format("{0}: 处理{1}", cnt, fn))
            self.writetofile(fn, content)
            cnt += 1

        tocfn = os.path.join(self.__path, "toc.txt")
        self.writetofile(tocfn, toc)

    @staticmethod
    def writetofile(path, content):

        with(open(path, "w", encoding="utf-8")) as f:
            f.write(content)

    def getChapterContent(self, line1: int, line2: int, title) -> str:

        with(open(self.__filename, 'r', encoding='utf-8')) as f:
            lines = f.readlines()
            title = lines[line1].rstrip()
            if line2 > 0:
                body = "".join(lines[line1 + 1:line2])
            else:
                body = "".join(lines[line1 + 1:])
            body = str.format("<h1>{0}</h1>\n", title) + self.convertToHTML(body)
            return str.format(self.__xhtmlTemplate, title, body)

    @staticmethod
    def convertToHTML(text: str) -> str:
        formatted = text.replace('\n', '</p><p>')
        formatted = formatted.replace("</p><p>", "<p>", 1)
        formatted = ChapterMaster.rreplace(formatted, "</p><p>", "</p>", 1)
        formatted = formatted.replace("<p></p>", "")
        return formatted.replace(" ", "")

    @staticmethod
    def rreplace(s, old, new, occurrence):
        li = s.rsplit(old, occurrence)
        return new.join(li)

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
            if chapter[2] is not int:
                break
            c = int(chapter[2])
            n = int(nxt[2])
            if n != c + 1:
                print(str.format("没有找到章节 {0} , 应该在 {1} 行以后", c + 1, chapter[0]))


if __name__ == "__main__":
    file = "武动乾坤.txt"
    cm = ChapterMaster(file)
    res = cm.parse()
    print(str.format("{0} results was extracted.", len(res)))
    cm.checking(res)
    cm.split(res)
