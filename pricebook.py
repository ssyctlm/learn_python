# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.Header import Header

result = {"name": [], "cover": [], "desc": [], "link": [], "price": []}


def get_page():
    return requests.get("http://t.cn/Rvm4xgc").text


def parse(html):
    soup = BeautifulSoup(html)
    table = soup.body.find_all("table")[8]

    name = table.find_all("tr")[1]

    result["name"].append(name.find_all("td")[0].b.string)
    result["name"].append(name.find_all("td")[2].b.string)

    desc = table.find_all("tr")[2]

    book_1 = desc.find_all("td")[0]
    result["cover"].append(book_1.a.img["src"])
    result["link"].append("http://www.amazon.cn" + book_1.a["href"])
    result["desc"].append(book_1.contents[1])
    result["price"].append(book_1.find_all("p")[1].b.span.string)

    book_2 = desc.find_all("td")[2]
    result["cover"].append(book_2.a.img["src"])
    result["link"].append("http://www.amazon.cn" + book_2.a["href"])
    result["desc"].append(book_2.contents[1])
    result["price"].append(book_2.find_all("p")[1].b.span.string)


mail_config = {
    "from": "maomaobug114222@163.com",
    "to": "maomaobug114222@163.com",
    "server": "smtp.163.com",
    "username": "maomaobug114222",
    "pwd": "mcsxmcj1314"
}


def send_mail(sbj, content, from_whom=mail_config['from'], to_whom=mail_config['to'], server=mail_config['server'],
              username=mail_config['username'], pwd=mail_config['pwd']):
    msg = MIMEText(content, "html", "utf-8")
    msg['Subject'] = Header(sbj, "utf-8")
    msg['From'] = from_whom
    msg['To'] = to_whom
    s = smtplib.SMTP(server)
    s.ehlo()
    s.starttls()
    s.login(username, pwd)
    s.sendmail(from_whom, to_whom, msg.as_string())


def build_html():
    return '<html><body>' \
            + '<h2>'+ result["name"][0] + '&nbsp; ' + result["price"][0] + '</h2>' \
            + '<a href="' + result["link"][0] + '">' \
            + '<img src="' + result["cover"][0] + '"></img>' \
            + '</a>' \
            + '<p>' + result["desc"][0] + '</p>' \
            + '<h2>'+ result["name"][1] + '&nbsp; ' + result["price"][1] + '</h2>' \
            + '<a href="' + result["link"][1] + '">' \
            + '<img src="' + result["cover"][1] + '"></img>' \
            + '</a>' \
            + '<p>' + result["desc"][1] + '</p>' \
            + '</body></html>'


if __name__ == "__main__":
    parse(get_page())
    html = build_html()
    sbj = "Kindle今日特价书"
    send_mail(sbj, html)