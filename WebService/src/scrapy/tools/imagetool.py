# -*- coding:utf-8 -*-
import urllib.request


def _get_type(url):
    img_type = ''

    if url.endswith('.jpg'):
        img_type = 'jpg'
    elif url.endswith('.png'):
        img_type = 'png'

    return img_type


class ImageTool(object):

    @classmethod
    def download_item(cls, item):

        pass

    @classmethod
    def download(cls, img_urls, img_names):
        """
        下载一个或一组网络图片

        demo: download('http://www.xxx.xxx.xxx.jpg', 'my_image')
        or
            download(['http://www.xxx.xxx.xxx.jpg','http://www.xxx.xxx.xxx.jpg'],['my_image1','my_image2'])

        :param img_urls: 图片链接，或一组图片链接
        :param img_names:图片保存在本地的名称，或一组名称
        :return:None
        """
        if type(img_urls) == str and type(img_names) == str:
            cls.__download_img(img_urls, img_names)
        elif type(img_urls) == list and type(img_names) == list:
            for i in range(len(img_urls)):
                cls.__download_img(img_urls[i], img_names[i])

    @classmethod
    def __download_img(cls, img_url, img_name):
        """
        下载单个图片
        :param img_url:
        :param img_name:
        :return:
        """
        response = urllib.request.urlopen(img_url)
        cat_img = response.read()
        with open(img_name + "." + _get_type(img_url), 'wb') as f:
            f.write(cat_img)
            f.close()


def main():
    ImageTool.download('//img001.hc360.cn/k1/M05/53/76/wKhQwFehlyOEJXjnAAAAADKz4tI853.jpg..220x220a.jpg', 'hc/220_220')
    pass


if __name__ == '__main__':
    main()