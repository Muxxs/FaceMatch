#!/usr/bin/env python
#-*- coding: utf-8 -*-

from wordpress_xmlrpc import Client, WordPressPost, WordPressTerm
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_xmlrpc.methods import taxonomies
import csv
def blog_content(title,content,tage,category):
  passwd=""
  wp = Client('http://123.206.66.55/xmlrpc.php', 'admin', passwd)
  """
  发表博文
  """
  post = WordPressPost()
  post.title = title
  post.content = content
  post.post_status = 'publish'
  print tage
  post.terms_names = {
    'post_tag': tage,
    'category': category
  }
  wp.call(NewPost(post))
def new_tag(name):
  wp = Client('http://127.0.0.1/xmlrpc.php', 'root', '123456')
  tag = WordPressTerm()
  tag.taxonomy = 'tage'  # 这里为category的话插入的是category，为post_tag的话插入的是tag
  tag.name = name
  tag.id = wp.call(taxonomies.NewTerm(tag))
def new_category(name):
  wp = Client('http://127.0.0.1/xmlrpc.php', 'root', '123456')
  tag = WordPressTerm()
  tag.taxonomy = 'category'  # 这里为category的话插入的是category，为post_tag的话插入的是tag
  tag.name = name
  tag.id = wp.call(taxonomies.NewTerm(tag))
#print blog("Test","Hi python",["家庭"],'我的生活')
def blog(text):
  text="t:Test|c:Hi python|a:家庭|e:我的生活"
  text=text.split("|")
  i=[]
  for n in text:
    n=n.split(":")
    i.append(n[1])
  tage=[]
  tage.append(i[2])
  blog_content(i[0],i[1],tage,i[3])
blog("")
