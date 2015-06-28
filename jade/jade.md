## Jade 是什么

Jade 是一个使用 Node.js 编写的、高性能 HTML 模板引擎。在使用 Node.js 开发 Web 应用时，经常和 Express 一起使用，能快速提高开发效率。如果读者以前使用过 Ruby On Rails 开发过 Web 应用，可能用过 [HAML](http://haml.info/)，Jade 基于 Node.js，就如 HAML 基于 Ruby On Rails。如果您以前没有使用过模板引擎，也没有关系，接下来我们看看为什么开发 Web 应用，需要使用模板引擎。

Web 最早被用来在少数科学家之间共享文档，文档以 HTML 格式编写，通过 HTTP 协议访问。早期的 Web 页面，都是简单的静态页面，所有人看到的都是同样的内容。随着 Web 的发展，这种纯静态页面已经不能满足人们的要求，于是服务器端根据情况的不同，生成不同的 HTML 文档。比如不同用户登录到豆瓣网，会看到各自收藏的电影、图书等。豆瓣网当然不会为每个用户都编写一个页面，而是使用同样的模板，根据不同用户的不同数据，通过服务器程序，为用户生成定制的页面。大家每日访问的各种网站，其工作方式基本如是：首先定义一套 HTML 模板，描述出页面的基本结构；然后从数据库中查询访问用户的数据，由服务器程序将数据和 HTML 模板组装起来，渲染出最终的 HTML 页面，返回给客户端，用户就看到了为他们定制的页面。

下面是一个使用 Jade 编写的简单模板，运行命令 `jade -P hello.jade` 生成相应的 HTML 文档 `hello.html`：

**代码列表-1 hello.jade**  

```
h1 Jade is amazing!
p Yes. It's really amazing!
``` 
**代码列表-2 hello.html** 

```
<h1> Jade is amzing! </h1>
<p> Yes. It's really amazing! </p>

```

## 安装

这里假设读者已经安装了 Node.js 和 npm，如果还没有安装，请自行搜索相关文档安装。安装完成后，在命令行里输入如下命令安装 Jade：

```
$ npm install jade --global
```

在命令里输入 `jade --version` 可验证是否安装成功。

## 语法

Jade 的语法非常简单，下面我们将逐个描述。在描述过程中，我们同时给出 Jade 代码和 HTML 代码，两相对比，相信读者可以快速掌握 Jade 的语法。

### 元素

Jade 直接使用对应的 HTML 元素名来声明，声明时无需像 HTML 那样繁琐，只需要元素名即可。元素之间的关系使用缩进来表示。

```
div
  p
```

对应的 HTML 片段为：

```
<div>
  <p></p>
<div>
```



## 命令行

## API


## 参考文档

1. [http://haml.info/](http://haml.info/)
2. [http://www.sitepoint.com/an-introduction-to-haml/](http://www.sitepoint.com/an-introduction-to-haml/)
3. [http://naltatis.github.io/jade-syntax-docs/](http://naltatis.github.io/jade-syntax-docs/)
4. [http://cssdeck.com/labs/learning-the-jade-templating-engine-syntax](http://cssdeck.com/labs/learning-the-jade-templating-engine-syntax)
5. [http://cssdeck.com/labs/jade-templating-tutorial-codecast-part-2](http://cssdeck.com/labs/jade-templating-tutorial-codecast-part-2)
6. [http://jade-lang.com/tutorial/](http://jade-lang.com/tutorial/)
7. [http://jade-lang.com](http://jade-lang.com)